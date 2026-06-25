#!/usr/bin/env bash
# process_cloud.sh — cloud-only pipeline (no local Whisper). One command per class:
#   ./pipeline/process_cloud.sh "Grabaciones/24JunioFinanzas.m4a" [YYYY-MM-DD]
#
# Ears: Voxtral (primary, diarized) + Groq Whisper (cross-check) + Gemini (comprehension).
# Each stage is skipped if its API key is missing, so you can run with whatever keys you have.
# Keys (in ~/.zshrc): MISTRAL_API_KEY, GROQ_API_KEY, GEMINI_API_KEY (or GOOGLE_API_KEY).
set -euo pipefail

REC="${1:?usage: process_cloud.sh <recording> [date]}"
DATE="${2:-$(date +%F)}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/out/${DATE}_finanzas"
mkdir -p "$OUT"
# shellcheck disable=SC1090
source "$ROOT/.venv/bin/activate"
P="$ROOT/pipeline"

echo "==> [1] Extract mono 16kHz audio"
ffmpeg -y -nostdin -loglevel error -i "$REC" -map 0:a:0 -ac 1 -ar 16000 -c:a pcm_s16le "$OUT/audio16k.wav"

PRIMARY=""
if [ -n "${MISTRAL_API_KEY:-}" ]; then
  echo "==> [2] Ear A: Voxtral (primary + diarization)"
  python "$P/cloud_transcribe.py" "$OUT/audio16k.wav" "$OUT" voxtral
  PRIMARY="$OUT/transcript_voxtral.json"
else
  echo "==> [2] SKIP Voxtral (no MISTRAL_API_KEY)"
fi

if [ -n "${GROQ_API_KEY:-}" ]; then
  echo "==> [3] Ear B: Groq Whisper large-v3 (cross-check)"
  python "$P/cloud_transcribe.py" "$OUT/audio16k.wav" "$OUT" groq
  [ -z "$PRIMARY" ] && PRIMARY="$OUT/transcript_groq.json"
else
  echo "==> [3] SKIP Groq (no GROQ_API_KEY)"
fi

if [ -z "$PRIMARY" ]; then
  echo "ERROR: no transcript produced (need MISTRAL_API_KEY and/or GROQ_API_KEY)"; exit 1
fi

# Canonical transcript that downstream (condense, diarize, synthesis) reads.
cp "$PRIMARY" "$OUT/transcript_whisperx.json"
echo "==> primary transcript = $(basename "$PRIMARY") -> transcript_whisperx.json"

if [ -f "$OUT/transcript_voxtral.json" ] && [ -f "$OUT/transcript_groq.json" ]; then
  echo "==> [4] Disagreements: Voxtral vs Groq"
  python "$P/disagreements.py" "$OUT/transcript_voxtral.json" "$OUT/transcript_groq.json" "$OUT/disagreements.md"
else
  echo "==> [4] Single ear: flag Whisper-style loops instead"
  python "$P/lowconf.py" "$OUT/transcript_whisperx.json" "$OUT/disagreements.md"
fi

echo "==> [5] Condensed timestamped transcript"
python "$P/condense.py" "$OUT/transcript_whisperx.json" "$OUT/transcript_timed.txt"

if [ -n "${GEMINI_API_KEY:-}${GOOGLE_API_KEY:-}" ]; then
  echo "==> [6] Gemini comprehension pass (whole audio)"
  python "$P/gemini_pass.py" "$OUT/audio16k.wav" "$OUT" || echo "    (gemini pass failed, continuing)"
else
  echo "==> [6] SKIP Gemini (no GEMINI_API_KEY/GOOGLE_API_KEY)"
fi

echo "==> Cloud stages done on $OUT. Next: Claude Code synthesis (see pipeline/SYNTHESIS.md)."
echo "    Inputs now also include transcript_gemini.md (comprehension) and a Voxtral-diarized transcript."
