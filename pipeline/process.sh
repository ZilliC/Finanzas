#!/usr/bin/env bash
# process.sh — one command per class. Drop a recording in Grabaciones/ and run:
#   ./pipeline/process.sh "Grabaciones/New Recording 12.qta" [YYYY-MM-DD]
#
# Produces out/<date>_finanzas/ with audio, both transcripts, disagreements,
# and leaves a marker so the Claude Code synthesis step (Stage 4-6) can run.
set -euo pipefail

REC="${1:?usage: process.sh <recording> [date]}"
DATE="${2:-$(date +%F)}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/out/${DATE}_finanzas"
VENV="$ROOT/.venv/bin/activate"

mkdir -p "$OUT"
# shellcheck disable=SC1090
source "$VENV"

echo "==> [1/4] Extract mono 16kHz audio"
ffmpeg -y -nostdin -loglevel error -i "$REC" -map 0:a:0 -ac 1 -ar 16000 -c:a pcm_s16le "$OUT/audio16k.wav"

echo "==> [2/4] Ear A: Whisper large-v3 (chunked)"
WORD_TS="${WORD_TS:-0}" python "$ROOT/pipeline/transcribe.py" "$OUT/audio16k.wav" "$OUT" 1200

echo "==> [3/4] Stage 3: flag low-confidence / hard-audio spots"
# Note: Qwen3-ASR-0.6B proved too weak as a 2nd ear (incomplete coverage, lower quality).
# We instead detect Whisper's own repetition loops, which mark the noisy/distant-audio moments.
python "$ROOT/pipeline/lowconf.py" "$OUT/transcript_whisperx.json" "$OUT/disagreements.md"

echo "==> [4/4] Condensed timestamped transcript for review/extraction"
python "$ROOT/pipeline/condense.py" "$OUT/transcript_whisperx.json" "$OUT/transcript_timed.txt"

echo "==> Mechanical stages done. Next: run the Claude Code synthesis on $OUT"
echo "    See pipeline/SYNTHESIS.md for the full per-class checklist. In short:"
echo "    1. study_guide.md   (concept inventory + coverage gap vs Finanzas.pdf)"
echo "    2. obligations.md   (homework/deadlines/rules, over-include, with quotes)"
echo "    3. MASTER_glosario.md          (new concepts + mark repeats)"
echo "    4. HISTORICO_preguntas_profesor.md  (prof questions by round, mark recurrentes)"
echo "    5. <date>/cuestionario.md      (predictive practice quiz for next class)"
echo "    6. MASTER_obligations.md + MASTER_concept_index.md (update cumulative)"
echo "    Deliver: Notion (class page + masters) + Google Calendar (confirmed deadlines)"
echo "    Optional diarization: see diarize.py usage in pipeline/SYNTHESIS.md"
