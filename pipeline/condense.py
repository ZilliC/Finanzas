#!/usr/bin/env python3
"""Condense Whisper segments into ~30s timestamped blocks for human review / extraction.

Usage: python condense.py <whisper.json> <out.txt> [block_seconds]
"""
import json
import sys


def main():
    src, out = sys.argv[1:3]
    block = float(sys.argv[3]) if len(sys.argv) > 3 else 30.0
    segs = json.load(open(src))["segments"]
    lines, cur_start, cur_text, cur_end = [], None, [], 0.0

    def flush():
        if cur_text:
            h, rem = divmod(int(cur_start), 3600)
            m, s = divmod(rem, 60)
            lines.append("[%02d:%02d:%02d] %s" % (h, m, s, " ".join(cur_text).strip()))

    for seg in segs:
        if cur_start is None:
            cur_start = seg["start"]
        cur_text.append(seg["text"].strip())
        cur_end = seg["end"]
        if cur_end - cur_start >= block:
            flush()
            cur_start, cur_text = None, []
    flush()
    open(out, "w").write("\n".join(lines))
    print(f"WROTE {out} — {len(lines)} blocks", flush=True)


if __name__ == "__main__":
    main()
