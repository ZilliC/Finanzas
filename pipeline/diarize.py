#!/usr/bin/env python3
"""Speaker diarization (Stage 3.5) — adds "who spoke when" to the transcript.

Runs pyannote on the 16kHz audio to get anonymous speaker turns (SPEAKER_00,
SPEAKER_01, ...), then assigns each Whisper segment to the speaker whose turns
overlap it most. Optionally remaps anonymous labels to real names via a JSON
map. Writes:
  - transcript_diarized.json : segments with a "speaker" field
  - transcript_diarized.txt  : human-readable "[hh:mm:ss] NAME: text"

Usage:
  python diarize.py <audio16k.wav> <whisper.json> <out_dir> [speakers.json]
Env:
  HF_TOKEN     required — Hugging Face token (gated pyannote models)
  NUM_SPEAKERS optional — exact number of speakers (e.g. 6) to improve accuracy
  PYANNOTE_MODEL optional — override model id (default community-1)
"""
import json
import os
import sys

MODEL = os.environ.get("PYANNOTE_MODEL", "pyannote/speaker-diarization-community-1")


def fmt(t: float) -> str:
    h, rem = divmod(int(t), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def diarize(audio: str):
    import torch
    from pyannote.audio import Pipeline

    token = os.environ.get("HF_TOKEN")
    if not token:
        sys.exit("ERROR: set HF_TOKEN (Hugging Face token) in the environment")
    pipe = Pipeline.from_pretrained(MODEL, token=token)
    if torch.backends.mps.is_available():
        pipe.to(torch.device("mps"))

    kwargs = {}
    n = os.environ.get("NUM_SPEAKERS")
    if n:
        kwargs["num_speakers"] = int(n)
    print(f"diarizing with {MODEL} {kwargs or '(auto speakers)'} ...", flush=True)
    out = pipe(audio, **kwargs)
    # community-1 returns a DiarizeOutput wrapper; use the overlap-free annotation
    ann = getattr(out, "exclusive_speaker_diarization", None)
    if ann is None:
        ann = getattr(out, "speaker_diarization", out)
    # list of (start, end, speaker_label)
    turns = [(seg.start, seg.end, spk) for seg, _, spk in ann.itertracks(yield_label=True)]
    print(f"  {len(turns)} turns, {len(set(t[2] for t in turns))} speakers", flush=True)
    return turns


def assign(segments, turns):
    """For each Whisper segment, pick the speaker with max temporal overlap."""
    for seg in segments:
        s, e = float(seg["start"]), float(seg["end"])
        best, best_ov = None, 0.0
        for ts, te, spk in turns:
            ov = min(e, te) - max(s, ts)
            if ov > best_ov:
                best_ov, best = ov, spk
        seg["speaker"] = best or "UNKNOWN"
    return segments


def main():
    audio, whisper_json, out_dir = sys.argv[1:4]
    spk_map = {}
    if len(sys.argv) > 4 and os.path.exists(sys.argv[4]):
        spk_map = json.load(open(sys.argv[4]))

    segments = json.load(open(whisper_json))["segments"]
    turns = diarize(audio)
    segments = assign(segments, turns)

    def name(label):
        return spk_map.get(label, label)

    base = os.path.join(out_dir, "transcript_diarized")
    with open(base + ".json", "w") as f:
        json.dump({"segments": segments}, f, ensure_ascii=False, indent=1)

    # Collapse consecutive same-speaker segments for readability
    with open(base + ".txt", "w") as f:
        cur_spk, buf, start = None, [], None
        def flush():
            if buf:
                f.write(f"[{fmt(start)}] {name(cur_spk)}: {' '.join(buf).strip()}\n")
        for seg in segments:
            if seg["speaker"] != cur_spk:
                flush()
                cur_spk, buf, start = seg["speaker"], [], seg["start"]
            buf.append(seg["text"].strip())
        flush()

    speakers = sorted(set(s["speaker"] for s in segments))
    print(f"WROTE {base}.json/.txt — speakers found: {speakers}", flush=True)
    if not spk_map:
        print("  TIP: create speakers.json mapping labels to names, e.g.")
        print('       {"SPEAKER_00": "Prof. Heredia", "SPEAKER_01": "Carlos"}')


if __name__ == "__main__":
    main()
