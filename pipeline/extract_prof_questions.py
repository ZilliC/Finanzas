#!/usr/bin/env python3
"""Volcado de preguntas-candidatas del profesor para curar el histórico.

Lee un transcript (diarizado o no) y saca los segmentos que parecen preguntas, agrupados en "rondas"
(cortes por silencios > GAP segundos). Filtra los bucles de Whisper (segmentos con baja proporción de
tokens únicos). NO decide cuáles son de conocimiento vs retóricas — eso lo cura Claude en la síntesis.

Uso:
  python extract_prof_questions.py <transcript.json> [speaker_label]
    transcript.json : transcript_diarized.json (con campo "speaker") o transcript_whisperx.json
    speaker_label   : si se da (p.ej. SPEAKER_02), filtra solo ese hablante (el profe)
Env:
  GAP   segundos de silencio que separan rondas (default 360 = 6 min)
"""
import json
import os
import sys


def fmt(t: float) -> str:
    m, s = divmod(int(t), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    src = sys.argv[1]
    spk = sys.argv[2] if len(sys.argv) > 2 else None
    gap = float(os.environ.get("GAP", "360"))

    segs = json.load(open(src))["segments"]
    qs = []
    for s in segs:
        if spk and s.get("speaker") != spk:
            continue
        t = s["text"].strip()
        if "?" not in t and "¿" not in t:
            continue
        toks = t.split()
        if len(toks) < 4:
            continue
        if len(set(toks)) / len(toks) < 0.55:   # bucle de Whisper
            continue
        qs.append((float(s["start"]), t))

    print(f"# {len(qs)} preguntas-candidatas"
          f"{f' de {spk}' if spk else ''} — cura a mano (quita retóricas)\n")
    last, rnd = None, 0
    for st, t in qs:
        if last is None or st - last > gap:
            rnd += 1
            print(f"\n## Ronda {rnd} (~{fmt(st)})")
        print(f"- [{fmt(st)}] {t}")
        last = st


if __name__ == "__main__":
    main()
