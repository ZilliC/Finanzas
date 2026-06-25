#!/usr/bin/env python3
"""Single-chunk Whisper worker (fresh process per chunk).

Uses the mlx-whisper Python API so we get temperature fallback (which the CLI's
single --temperature can't do) — this is what actually breaks the repetition
loops on noisy/distant audio. Also passes an initial_prompt to bias domain
vocabulary and proper nouns.

Usage: python _whisper_worker.py <piece.wav> <out.json>
Env:   INIT_PROMPT, WORD_TS=1
"""
import json
import os
import sys

import mlx_whisper

MODEL = "mlx-community/whisper-large-v3-mlx"

wav, out_json = sys.argv[1], sys.argv[2]
prompt = os.environ.get("INIT_PROMPT", "").strip() or None
word_ts = os.environ.get("WORD_TS", "0") == "1"

res = mlx_whisper.transcribe(
    wav,
    path_or_hf_repo=MODEL,
    language="es",
    temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0),  # fallback retries on degenerate output
    initial_prompt=prompt,
    condition_on_previous_text=False,
    compression_ratio_threshold=2.2,   # drop high-repetition (loop) segments
    logprob_threshold=-1.0,
    no_speech_threshold=0.6,
    hallucination_silence_threshold=2.0,
    word_timestamps=word_ts,
)
json.dump(res, open(out_json, "w"), ensure_ascii=False)
print(f"OK {out_json} ({len(res.get('segments', []))} segments)", flush=True)
