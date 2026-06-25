#!/usr/bin/env python3
"""Chunked Whisper transcription (Ear A) — robust for long lectures.

Each chunk is transcribed in a FRESH mlx_whisper subprocess so a Metal GPU
hang in one chunk can't kill the whole run and the GPU context resets between
chunks. Per-chunk JSON is cached on disk, so a re-run resumes where it stopped.
Finally merges all chunks with time offsets into transcript_whisperx.{json,txt,srt}.

Usage: python transcribe.py <audio16k.wav> <out_dir> [chunk_seconds]
Env:   WORD_TS=1 to enable word-level timestamps (~2x slower; only for diarization)
"""
import json
import os
import subprocess
import sys

MODEL = "mlx-community/whisper-large-v3-mlx"
WORD_TS = os.environ.get("WORD_TS", "0") == "1"
MAX_RETRIES = 3


def fmt_ts(t: float) -> str:
    h, rem = divmod(int(t), 3600)
    m, s = divmod(rem, 60)
    ms = int((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def audio_duration(path: str) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


WORKER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_whisper_worker.py")


def transcribe_chunk(piece_wav: str, chunk_dir: str, name: str) -> dict:
    """Run the Whisper worker in a fresh process; return parsed json. Retries on GPU hang.

    The worker uses the Python API for temperature fallback + initial_prompt (passed via
    the INIT_PROMPT env var set by the caller)."""
    json_path = os.path.join(chunk_dir, name + ".json")
    if os.path.exists(json_path):
        with open(json_path) as f:
            return json.load(f)
    cmd = [sys.executable, WORKER, piece_wav, json_path]
    for attempt in range(1, MAX_RETRIES + 1):
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0 and os.path.exists(json_path):
            with open(json_path) as f:
                return json.load(f)
        print(f"    retry {attempt}/{MAX_RETRIES} for {name} (rc={r.returncode}): "
              f"{r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'no stderr'}", flush=True)
    raise RuntimeError(f"chunk {name} failed after {MAX_RETRIES} attempts")


def main():
    audio = sys.argv[1]
    out_dir = sys.argv[2]
    chunk = int(sys.argv[3]) if len(sys.argv) > 3 else 600  # 10 min
    chunk_dir = os.path.join(out_dir, "_chunks")
    os.makedirs(chunk_dir, exist_ok=True)

    dur = audio_duration(audio)
    n_chunks = int(dur // chunk) + (1 if dur % chunk else 0)
    print(f"duration={dur:.1f}s chunks={n_chunks} chunk_len={chunk}s word_ts={WORD_TS}", flush=True)

    all_segments, full_text = [], []
    for i in range(n_chunks):
        offset = i * chunk
        name = f"piece_{i:03d}"
        piece = os.path.join(chunk_dir, name + ".wav")
        if not os.path.exists(os.path.join(chunk_dir, name + ".json")):
            subprocess.run(
                ["ffmpeg", "-y", "-nostdin", "-loglevel", "error",
                 "-ss", str(offset), "-t", str(chunk), "-i", audio,
                 "-ac", "1", "-ar", "16000", piece],
                check=True,
            )
        print(f"[chunk {i+1}/{n_chunks}] offset={offset}s", flush=True)
        res = transcribe_chunk(piece, chunk_dir, name)
        for seg in res.get("segments", []):
            seg["start"] = float(seg["start"]) + offset
            seg["end"] = float(seg["end"]) + offset
            for w in seg.get("words", []) or []:
                if "start" in w:
                    w["start"] += offset
                if "end" in w:
                    w["end"] += offset
            all_segments.append(seg)
        full_text.append(res.get("text", "").strip())
        if os.path.exists(piece):
            os.remove(piece)  # keep json, drop wav to save space
        print(f"[chunk {i+1}/{n_chunks}] done ({len(res.get('segments', []))} segments)", flush=True)

    base = os.path.join(out_dir, "transcript_whisperx")
    with open(base + ".json", "w") as f:
        json.dump({"segments": all_segments, "text": " ".join(full_text)}, f, ensure_ascii=False, indent=1)
    with open(base + ".txt", "w") as f:
        for seg in all_segments:
            f.write(seg["text"].strip() + "\n")
    with open(base + ".srt", "w") as f:
        for idx, seg in enumerate(all_segments, 1):
            f.write(f"{idx}\n{fmt_ts(seg['start'])} --> {fmt_ts(seg['end'])}\n{seg['text'].strip()}\n\n")
    print(f"WROTE {base}.json/.txt/.srt  segments={len(all_segments)}", flush=True)


if __name__ == "__main__":
    main()
