#!/usr/bin/env python3
"""Cloud transcription (replaces local mlx-whisper) — Voxtral or Groq.

Splits the 16kHz wav into compressed mp3 chunks (so each stays under provider size
limits), transcribes each chunk via the chosen cloud provider, caches per-chunk json
on disk (resumable), and merges with time offsets into the whisperx-compatible
`transcript_<provider>.json` / `.txt`:  {"segments":[{start,end,text,(speaker)}], "text": "..."}

Providers:
  voxtral : Mistral voxtral-mini-latest — best WER + diarization + context_bias (hotwords).
            Needs MISTRAL_API_KEY.
  groq    : Groq whisper-large-v3 (verbose_json, segment timestamps). Free tier 25MB/file.
            Needs GROQ_API_KEY.

Usage:  python cloud_transcribe.py <audio16k.wav> <out_dir> <voxtral|groq> [chunk_seconds]
Env:    MISTRAL_API_KEY / GROQ_API_KEY ; CONFIG=pipeline/course_config.json (for hotwords)
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.environ.get("CONFIG", os.path.join(HERE, "course_config.json"))
MAX_RETRIES = 4


def hotwords():
    """Voxtral context_bias requires single tokens (pattern ^[^,\\s]+$), so split the
    comma-separated hotwords into individual words, drop short/common ones, dedupe."""
    STOP = {"de", "la", "el", "los", "las", "y", "del", "en", "al", "un", "una"}
    try:
        cfg = json.load(open(CONFIG))
        seen, out = set(), []
        for phrase in cfg.get("asr_hotwords", "").split(","):
            for w in phrase.split():
                w = w.strip()
                lw = w.lower()
                if len(w) < 3 or lw in STOP or lw in seen:
                    continue
                seen.add(lw)
                out.append(w)
        return out[:100]  # context_bias caps at ~100 entries
    except Exception:
        return []


def audio_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def make_chunk_mp3(audio, offset, length, dest):
    subprocess.run(
        ["ffmpeg", "-y", "-nostdin", "-loglevel", "error",
         "-ss", str(offset), "-t", str(length), "-i", audio,
         "-ac", "1", "-ar", "16000", "-b:a", "64k", dest], check=True)


# ---- providers: each returns list of {start,end,text,(speaker)} for one chunk ----

def transcribe_voxtral(mp3_path):
    from mistralai.client import Mistral
    client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
    with open(mp3_path, "rb") as f:
        resp = client.audio.transcriptions.complete(
            model="voxtral-mini-latest",
            file={"content": f, "file_name": os.path.basename(mp3_path)},
            language="es",
            diarize=True,
            context_bias=hotwords() or None,
            timestamp_granularities=["segment"],
        )
    data = resp.model_dump() if hasattr(resp, "model_dump") else resp
    segs = []
    for s in (data.get("segments") or []):
        segs.append({
            "start": float(s.get("start", 0) or 0),
            "end": float(s.get("end", 0) or 0),
            "text": (s.get("text") or "").strip(),
            "speaker": s.get("speaker") or s.get("speaker_id"),
        })
    if not segs and data.get("text"):           # no segments returned → one blob
        segs = [{"start": 0.0, "end": 0.0, "text": data["text"].strip(), "speaker": None}]
    return segs


def transcribe_groq(mp3_path):
    from groq import Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    with open(mp3_path, "rb") as f:
        resp = client.audio.transcriptions.create(
            file=(os.path.basename(mp3_path), f.read()),
            model="whisper-large-v3",
            language="es",
            response_format="verbose_json",
            timestamp_granularities=["segment"],
        )
    data = resp.model_dump() if hasattr(resp, "model_dump") else resp
    return [{"start": float(s["start"]), "end": float(s["end"]),
             "text": s["text"].strip(), "speaker": None}
            for s in (data.get("segments") or [])]


PROVIDERS = {"voxtral": transcribe_voxtral, "groq": transcribe_groq}


def main():
    audio, out_dir, provider = sys.argv[1:4]
    chunk = int(sys.argv[4]) if len(sys.argv) > 4 else 900  # 15 min
    fn = PROVIDERS[provider]
    chunk_dir = os.path.join(out_dir, f"_chunks_{provider}")
    os.makedirs(chunk_dir, exist_ok=True)

    dur = audio_duration(audio)
    n = int(dur // chunk) + (1 if dur % chunk else 0)
    print(f"provider={provider} duration={dur:.1f}s chunks={n} chunk_len={chunk}s", flush=True)

    all_segs, full_text = [], []
    for i in range(n):
        offset = i * chunk
        cache = os.path.join(chunk_dir, f"piece_{i:03d}.json")
        if os.path.exists(cache):
            segs = json.load(open(cache))
        else:
            mp3 = os.path.join(chunk_dir, f"piece_{i:03d}.mp3")
            make_chunk_mp3(audio, offset, chunk, mp3)
            print(f"[chunk {i+1}/{n}] offset={offset}s transcribing…", flush=True)
            segs = None
            for attempt in range(1, MAX_RETRIES + 1):
                try:
                    segs = fn(mp3)
                    break
                except Exception as e:
                    print(f"    retry {attempt}/{MAX_RETRIES}: {e}", flush=True)
            if segs is None:
                raise RuntimeError(f"chunk {i} failed after {MAX_RETRIES} attempts")
            json.dump(segs, open(cache, "w"), ensure_ascii=False)
            os.remove(mp3)
        for s in segs:
            s = dict(s)
            s["start"] += offset
            s["end"] += offset
            all_segs.append(s)
            full_text.append(s["text"])
        print(f"[chunk {i+1}/{n}] done ({len(segs)} segments)", flush=True)

    base = os.path.join(out_dir, f"transcript_{provider}")
    json.dump({"segments": all_segs, "text": " ".join(full_text)},
              open(base + ".json", "w"), ensure_ascii=False, indent=1)
    with open(base + ".txt", "w") as f:
        for s in all_segs:
            f.write(s["text"] + "\n")
    print(f"WROTE {base}.json/.txt segments={len(all_segs)}", flush=True)


if __name__ == "__main__":
    main()
