#!/usr/bin/env python3
"""Stage 3 — flag where the two transcripts (Ear A Whisper vs Ear B Qwen3-ASR) diverge.

Buckets both transcripts into fixed windows, concatenates text per window,
scores similarity, and writes windows below threshold to disagreements.md
with timestamps so the user can listen back to exactly the hard-to-hear spots.

Usage: python disagreements.py <whisper.json> <qwen.json> <out.md> [window_s] [threshold]
"""
import json
import re
import sys
from difflib import SequenceMatcher


def load_segments(path):
    """Return list of (start, end, text). Accepts mlx-whisper / mlx-audio json."""
    with open(path) as f:
        data = json.load(f)
    segs = data.get("segments") or data.get("chunks") or []
    out = []
    for s in segs:
        start = s.get("start", s.get("timestamp", [0])[0] if isinstance(s.get("timestamp"), list) else 0)
        end = s.get("end", s.get("timestamp", [0, 0])[1] if isinstance(s.get("timestamp"), list) else start)
        text = s.get("text", "")
        out.append((float(start or 0), float(end or 0), text))
    return out


def norm(t):
    t = t.lower()
    t = re.sub(r"[^\wáéíóúñü ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def bucket(segs, window):
    buckets = {}
    for start, _end, text in segs:
        w = int(start // window)
        buckets.setdefault(w, []).append(text)
    return {w: norm(" ".join(v)) for w, v in buckets.items()}


def hhmmss(sec):
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    whisper_json, qwen_json, out_md = sys.argv[1:4]
    window = int(sys.argv[4]) if len(sys.argv) > 4 else 30
    threshold = float(sys.argv[5]) if len(sys.argv) > 5 else 0.55

    a = bucket(load_segments(whisper_json), window)
    b = bucket(load_segments(qwen_json), window)
    windows = sorted(set(a) | set(b))

    flagged = []
    for w in windows:
        ta, tb = a.get(w, ""), b.get(w, "")
        if not ta and not tb:
            continue
        ratio = SequenceMatcher(None, ta, tb).ratio()
        if ratio < threshold:
            flagged.append((w * window, ratio, ta, tb))

    with open(out_md, "w") as f:
        f.write("# Discrepancias entre transcripciones (escuchar de nuevo)\n\n")
        f.write(f"Ventana={window}s · umbral similitud<{threshold} · {len(flagged)} de {len(windows)} ventanas marcadas.\n\n")
        f.write("Cada bloque es un punto donde Whisper y Qwen-ASR no coinciden — probablemente audio difícil. "
                "Salta al timestamp en `audio16k.wav` para confirmar qué dijo el profesor.\n\n")
        for start, ratio, ta, tb in flagged:
            f.write(f"## ⏱ {hhmmss(start)}  (similitud {ratio:.2f})\n")
            f.write(f"- **Whisper:** {ta or '(silencio)'}\n")
            f.write(f"- **Qwen-ASR:** {tb or '(silencio)'}\n\n")
    print(f"WROTE {out_md} — {len(flagged)}/{len(windows)} windows flagged", flush=True)


if __name__ == "__main__":
    main()
