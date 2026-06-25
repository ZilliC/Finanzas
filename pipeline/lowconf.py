#!/usr/bin/env python3
"""Stage 3 (revised) — flag low-confidence / hard-audio spots from Whisper itself.

A weak second ASR (Qwen3-ASR-0.6B) proved unreliable for cross-checking, so instead
we detect Whisper's own failure mode: repetition loops and degenerate segments that
occur on noisy/distant audio. These are exactly the "listen again" moments. No second
model needed.

Heuristics per segment:
  - token repetition ratio (few unique words / many total) -> looping
  - a single short token repeated many times ("no no no", "otro otro")
  - very long segment with tiny vocabulary

Usage: python lowconf.py <whisper.json> <out.md>
"""
import json
import re
import sys
from collections import Counter


def hhmmss(sec):
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    whisper_json, out_md = sys.argv[1:3]
    d = json.load(open(whisper_json))
    flagged = []
    for seg in d["segments"]:
        text = seg.get("text", "").strip()
        words = re.findall(r"\w+", text.lower())
        if len(words) < 6:
            continue
        counts = Counter(words)
        uniq_ratio = len(counts) / len(words)
        top_word, top_n = counts.most_common(1)[0]
        # looping if low unique ratio OR one word dominates
        if uniq_ratio < 0.45 or top_n / len(words) > 0.4:
            flagged.append((seg["start"], seg["end"], uniq_ratio, top_word, top_n, text))

    with open(out_md, "w") as f:
        f.write("# Tramos de audio difícil / baja confianza (reescuchar)\n\n")
        f.write(f"{len(flagged)} tramos donde Whisper entró en bucle de repetición — típico de audio lejano/ruidoso. "
                "Salta al timestamp en `audio16k.wav` para confirmar qué se dijo realmente.\n\n")
        for start, end, ur, tw, tn, text in flagged:
            preview = (text[:240] + "…") if len(text) > 240 else text
            f.write(f"## ⏱ {hhmmss(start)}–{hhmmss(end)}  (palabra «{tw}» ×{tn}, diversidad {ur:.2f})\n")
            f.write(f"{preview}\n\n")
    print(f"WROTE {out_md} — {len(flagged)} low-confidence spots", flush=True)


if __name__ == "__main__":
    main()
