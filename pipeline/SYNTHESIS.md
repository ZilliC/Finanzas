# Síntesis por clase — flujo que ejecuta Claude Code

> Esto es lo que hace **Claude Code** (sin API, con la suscripción de Carlos) *después* de que `process.sh`
> termina las etapas mecánicas. Requiere comprensión, por eso no son scripts. Orden por clase:

## Cómo se transcribe (cloud, sin modelo local)
`./pipeline/process_cloud.sh <grabación> [fecha]` corre los 3 modelos cloud:
- **Voxtral** (`MISTRAL_API_KEY`) = Oído A primario, con **diarización** (segmentos traen `speaker`).
- **Groq whisper-large-v3** (`GROQ_API_KEY`) = Oído B → `disagreements.md` (Voxtral vs Groq).
- **Gemini 2.5** (`GEMINI_API_KEY`) = pasada de comprensión de TODO el audio → `transcript_gemini.md`.
El primario se copia a `transcript_whisperx.json` (lo que leen condense/synthesis). El local
(`process.sh` + mlx-whisper) queda como respaldo offline si algún día no hay red/keys.

## Insumos
- `out/<fecha>/transcript_timed.txt` — transcript condensado con timestamps (insumo principal).
- `out/<fecha>/transcript_gemini.md` — **comprensión global** de la clase (temario, conceptos, preguntas).
  Úsalo para contrastar/rellenar lo que el ASR troceado distorsione (no como verdad literal de WER).
- `out/<fecha>/transcript_voxtral.json` — trae `speaker` por segmento (diarización Voxtral, ya no hace falta
  `diarize.py`/pyannote).
- `out/<fecha>/disagreements.md` — tramos donde Voxtral y Groq difieren = audio dudoso (no fiarse).
- Referencia: `2632_Finanzas_Apunte.pdf` (apunte primario), `Finanzas.pdf` (temario/cobertura),
  `pipeline/course_config.json` (mapa de unidades + hotwords).

## Entregables (en este orden)
1. **`out/<fecha>/study_guide.md`** — inventario exhaustivo de conceptos de la clase + gap de cobertura vs.
   temario. (Formato ya establecido.)
2. **`out/<fecha>/obligations.md`** — tareas, reglas, fechas límite; sobre-incluir, con citas + timestamp.
3. **`out/MASTER_glosario.md`** — agregar **conceptos nuevos** (definición en palabras del profe, unidad,
   clase de origen). A los conceptos ya presentes, **anexar la clase** y marcar 🔁 si reaparecen. No duplicar.
4. **`out/HISTORICO_preguntas_profesor.md`** — añadir sección `## Clase N` con las preguntas del profe por
   **rondas**. Curar: quitar retóricas, dejar solo preguntas de **conocimiento**. Marcar 🔁 las repetidas y
   actualizar la sección `⭐ Recurrentes`. Acelerador: `python pipeline/extract_prof_questions.py
   out/<fecha>/transcript_diarized.json SPEAKER_xx` (o el whisperx sin label) vuelca candidatas a curar.
5. **`out/<fecha>/cuestionario.md`** — quiz de práctica **predictivo** para preparar la clase siguiente.
   Insumos: histórico (⭐ recurrentes), `study_guide.md` de la clase, `obligations.md` (lo que el profe
   anunció que preguntará). Preguntas abiertas estilo profe + clave colapsable. No inventar temas.
6. **`out/MASTER_obligations.md`** + **`out/MASTER_concept_index.md`** — actualizar acumulados (cobertura,
   estados de dominio, pendientes por confirmar).

## Entrega (delivery)
- **Notion** (MCP `notion-*`): página de la clase con study_guide + cuestionario; páginas maestras para
  glosario, histórico y obligaciones.
- **Google Calendar** (MCP `create_event`): un evento por cada **fecha límite confirmada** en `obligations.md`
  (mientras estén "por confirmar", no crear nada).

## Diarización (opcional)
`diarize.py` (pyannote) NO está en `process.sh`. Correrla solo cuando el audio lo amerite:
```
HF_TOKEN=$HF_TOKEN NUM_SPEAKERS=<n> python pipeline/diarize.py \
  out/<fecha>/audio16k.wav out/<fecha>/transcript_whisperx.json out/<fecha>/ out/<fecha>/speakers.json
```
Requiere `HF_TOKEN` en `~/.zshrc` + licencias pyannote aceptadas. `speakers.json` mapea `SPEAKER_xx`→nombres.
