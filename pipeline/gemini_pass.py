#!/usr/bin/env python3
"""Gemini comprehension pass — hears the RAW AUDIO in large chunks.

Sending a whole 3h lecture in one generateContent call hangs/times out; feeding only text
loses Gemini's main advantage (catching ASR errors by actually listening). Compromise:
split the audio into large chunks (default 30 min), send each as audio to gemini-2.5-flash
with its absolute start time, cache each chunk's result (resumable), and stitch them into one
transcript_gemini.md. Each chunk is big enough to keep topic-level context.

Usage:  python gemini_pass.py <audio16k.wav> <out_dir>
Env:    GEMINI_API_KEY (or GOOGLE_API_KEY) ; GEMINI_MODEL (default gemini-2.5-flash)
        GEMINI_CHUNK_SECONDS (default 1800 = 30 min)
"""
import os
import subprocess
import sys
import time

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
CHUNK = int(os.environ.get("GEMINI_CHUNK_SECONDS", "1800"))
MAX_RETRIES = int(os.environ.get("GEMINI_MAX_RETRIES", "8"))
RETRY_SECONDS = int(os.environ.get("GEMINI_RETRY_SECONDS", "120"))

PROMPT = """Eres un asistente que estudia una grabación de clase universitaria de Finanzas (español de México).
Este audio es un BLOQUE de la clase que empieza en el minuto absoluto {start_hhmm} (las marcas de tiempo que
des deben ser RELATIVAS al inicio de este bloque). Escúchalo y devuelve en español, en Markdown, sin inventar
nada que no se diga:

### Temas tratados (en orden, con [mm:ss] relativo)
### Conceptos y definiciones (en palabras del profesor)
### Preguntas que hizo el profesor (solo de conocimiento, no retóricas)
### Tareas, fechas y reglas mencionadas
### Tramos confusos / audio difícil ([mm:ss] relativo)
Si alguna sección no aplica en este bloque, omítela.
"""


def hhmm(sec):
    h, m = divmod(int(sec) // 60, 60)
    return f"{h:02d}:{m:02d}"


def audio_duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def with_retries(fn, label):
    """Transient 503s ('high demand') and DNS/network blips are common on gemini-2.5-flash;
    retry with a flat backoff instead of failing the whole multi-hour run over one blip."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return fn()
        except Exception as e:
            if attempt == MAX_RETRIES:
                raise
            print(f"[{label}] attempt {attempt}/{MAX_RETRIES} failed ({e!r}); "
                  f"retrying in {RETRY_SECONDS}s", flush=True)
            time.sleep(RETRY_SECONDS)


def main():
    audio, out_dir = sys.argv[1:3]
    from google import genai

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("ERROR: set GEMINI_API_KEY (or GOOGLE_API_KEY)")
    client = genai.Client(api_key=api_key)

    chunk_dir = os.path.join(out_dir, "_gemini_chunks")
    os.makedirs(chunk_dir, exist_ok=True)
    dur = audio_duration(audio)
    n = int(dur // CHUNK) + (1 if dur % CHUNK else 0)
    print(f"gemini audio-chunked: duration={dur:.0f}s chunks={n} chunk_len={CHUNK}s model={MODEL}", flush=True)

    sections = []
    for i in range(n):
        offset = i * CHUNK
        cache = os.path.join(chunk_dir, f"block_{i:03d}.md")
        header = f"## Bloque {i+1}/{n} — [{hhmm(offset)}–{hhmm(min(offset+CHUNK, dur))}]"
        if os.path.exists(cache):
            sections.append(header + "\n" + open(cache).read())
            print(f"[block {i+1}/{n}] cached", flush=True)
            continue
        mp3 = os.path.join(chunk_dir, f"block_{i:03d}.mp3")
        subprocess.run(["ffmpeg", "-y", "-nostdin", "-loglevel", "error",
                        "-ss", str(offset), "-t", str(CHUNK), "-i", audio,
                        "-ac", "1", "-ar", "16000", "-b:a", "64k", mp3], check=True)
        print(f"[block {i+1}/{n}] uploading + asking {MODEL}…", flush=True)
        f = with_retries(lambda: client.files.upload(file=mp3), f"block {i+1}/{n} upload")
        while getattr(f, "state", None) and str(f.state).endswith("PROCESSING"):
            time.sleep(3)
            f = client.files.get(name=f.name)
        prompt = PROMPT.format(start_hhmm=hhmm(offset))
        resp = with_retries(
            lambda: client.models.generate_content(model=MODEL, contents=[f, prompt]),
            f"block {i+1}/{n} generate",
        )
        text = resp.text or "(sin respuesta)"
        open(cache, "w").write(text)
        sections.append(header + "\n" + text)
        try:
            client.files.delete(name=f.name)
        except Exception:
            pass
        os.remove(mp3)
        print(f"[block {i+1}/{n}] done", flush=True)

    out = os.path.join(out_dir, "transcript_gemini.md")
    with open(out, "w") as fp:
        fp.write(f"# Pasada de comprensión (Gemini {MODEL}, audio en bloques de {CHUNK//60} min)\n\n")
        fp.write("\n\n".join(sections))
    print(f"WROTE {out} — {n} bloques", flush=True)


if __name__ == "__main__":
    main()
