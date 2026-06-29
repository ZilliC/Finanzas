# Guía de estudio — Clase 6 (2026-06-29, lunes)
### Finanzas 2632 · Prof. Eduardo Heredia Contreras

> Clase larga (2h51m) y con **giro de tema**. Lo que la Clase 5 dejó pendiente (rotación, cronológicas) SÍ se
> vio, pero el profe metió un bloque grande y nuevo: **inflación → reexpresión de estados financieros** (lo que
> conecta con los "estados financieros reexpresados" que ya había nombrado), y **abrió formalmente el tema del
> SISTEMA FINANCIERO MEXICANO** como lo que hay que estudiar para mañana. Cinco ejes:
> (1) cierre de repaso (costo/inventarios + interpretación "1.80 de colchón"); (2) **inflación**: qué es, INPC,
> fórmula de Laspeyres; (3) **reexpresión**: factor de actualización vs. factor de ajuste, Boletín B-10,
> partidas monetarias vs. no monetarias; (4) **razones de rotación y cronológicas** con cifras (rotación de
> CxC y CxP, plazo medio de cobro y de pago); (5) repaso del **Estado de Resultados**. Dominio global: ⬜ por estudiar.
>
> ⚠️ **Calidad de audio:** Voxtral primaria (**sin bucles**: top repeat "¿Por qué?" ×13), Groq cruce, **Gemini**
> comprensión de audio completo (limpio, 6 bloques). Audio de campo lejano → muchos tramos dudosos en
> `disagreements.md` (176/343 ventanas). Timestamps **absolutos** [HH:MM:SS] del `transcript_timed.txt`.
> 🎙️ Hubo una **2ª grabación de 18s** (`Clase06b`) = el cierre, donde el profe aclara qué del sistema financiero estudiar.

---

## ⭐ A. Lo que dijo que estudiemos / tarea para mañana (Clase 7, martes 30-jun)
1. **EL SISTEMA FINANCIERO MEXICANO** — es la tarea estrella. *"Para mañana voy a empezar a preguntar el
   sistema financiero… mañana es por preguntar **dos veces**."* [02:50:58]. En el cierre (Clase06b) aclara qué
   estudiar: **"de entrada la estructura… todo lo que abarca el sistema financiero mexicano"** → su **estructura
   y sus organismos**. **Siglas:** **SHCP** (Secretaría de Hacienda y Crédito Público) · **Banxico** (Banco de
   México) · **CNBV** (Comisión Nacional Bancaria y de Valores) · **CNSF** (Comisión Nacional de Seguros y
   Fianzas) · **CONSAR** (Comisión Nacional del Sistema de Ahorro para el Retiro) · **CONDUSEF** (Comisión
   Nacional para la Protección y Defensa de los Usuarios de Servicios Financieros) · **IPAB** (Instituto para la
   Protección al Ahorro Bancario) · **BMV** (Bolsa Mexicana de Valores). El profe lamentó que les
   *quitaran* este tema del programa y lo va a ver igual porque "ustedes ya viven dentro del sistema financiero". [00:44:43–00:45:18]
2. **TAREA DE PROGRAMACIÓN (informáticos): construir la base de datos de reexpresión.** *"Necesito que tú, en
   tu sistema, me generes una base de datos para que cuando yo le inserte la cifra base, el algoritmo… busque el
   índice, lo jale… haga esta ecuación y a mí me aparezca en automático la cifra [actualizada]."* [01:39:41,
   01:38:38] → un Excel/sistema que, dada una cifra base, consulte la tabla del INPC y devuelva la cifra
   actualizada con el **factor de actualización**.
3. **Seguir dominando las razones** (las de hoy: rotación de CxC/CxP, plazo medio de cobro/pago) — ya las
   "encomendó" antes y volverá a preguntarlas. [01:57:26]
4. **Bibliografía:** revisar en el programa de estudio los textos de **Finanzas Corporativas de Ross** y de
   **Weston** (Westerfield/Copeland). [00:45:55]

---

## ⭐ B. Las rondas de preguntas de hoy (memorízalas — resta participación)
Clase otra vez socrática (interrogó a Carlos/"Charly", Mike/"Maik", Maite). Las de conocimiento:
1. ¿Qué significa **1.80 de colchón**? (margen de seguridad: paga todo lo que debe y le sobra $1.80) [≈00:25–00:28 / G-B1]
2. ¿Qué es la **inflación**? ¿qué les han enseñado? [00:43–00:45 / G-B2 05:45]
3. ¿Quién calcula el **INPC** y cuándo se publica? (INEGI/Banxico, primeros 10 días del mes) [G-B3 05:00–05:16]
4. ¿Cuál es la diferencia entre el **factor de actualización** y el **factor de ajuste**? [01:22:07, 01:22:45]
5. ¿Qué dice el **Boletín B-10**? ¿qué se reexpresa, partidas monetarias o no monetarias? [01:35:54–01:37:33]
6. ¿Cuál sería una **partida no monetaria**? ¿y una monetaria? (¿el billete se reexpresa? ¿las acciones?) [01:36:29–01:37:33]
7. ¿Cómo se leen las **razones de rotación**? (en veces, ciclos, vueltas o alternancias) [01:57:26]
8. ¿Cuál es la **fórmula de la rotación de cuentas por cobrar a clientes**? [01:59:09]
9. ¿De dónde saco las **ventas**? ¿por qué ventas **netas a crédito** y no totales? [02:23:00 / G-B5 25:41]
10. ¿Cómo se saca el **promedio** de una cuenta? ¿depende de si "juega o no con el sistema financiero"? [02:28:07–02:29:21]
11. ¿Cómo calculo el **plazo medio de cobro**? ¿y el de pago? [02:34:57, 02:48:39]
12. Comparando PMC (60 días) y PMP (45 días), **¿la empresa está bien o mal y por qué?** [G-B6 14:28]

---

## C. Conceptos nuevos de hoy (definición en palabras del profe)

### 1) Inflación y poder adquisitivo
- **Inflación** = *"la pérdida —no reducción, la **pérdida**— del poder adquisitivo del dinero"*. El billete
  sigue valiendo nominalmente lo mismo, pero compra menos. México vive en una **economía altamente
  inflacionaria** (incluso "espiral inflacionaria"). [00:43–00:45 / G-B2 05:54, G-B3 13:40]
- **Poder adquisitivo** = la capacidad de compra del dinero; se pierde cuando el dinero está "durmiendo"
  (inmovilizado) o con el simple transcurso del tiempo. [G-B2 02:19]
- **Por qué importa en finanzas:** "si no lo tomo en cuenta, mi cliente está perdiendo dinero". Hay que
  **actualizar** activos fijos y bienes para que reflejen su valor real. [G-B3 17:23]
- Relacionados (mencionados): **renta fija vs. renta variable**, **interés simple vs. compuesto** (el compuesto
  se capitaliza → más alto), **"a mayor riesgo, mayor rendimiento"**, **canasta básica**. [G-B2]

### 2) INPC — Índice Nacional de Precios al Consumidor
- Es el instrumento con que **se calcula la inflación**. Se construye con la **fórmula de Laspeyres** y
  **ponderadores** que calcula el **INEGI**; se **publica en los primeros 10 días de cada mes** (el de junio
  sale en julio). La ley exige tomarlo **hasta diezmilésimos** (4 decimales). [01:20:43 / G-B3, G-B4 00:48]

### 3) Reexpresión de estados financieros (⭐ el bloque grande y nuevo)
- **Reexpresar** = actualizar cifras por inflación. Lo manda el **Boletín B-10** de las **NIF** (Normas de
  Información Financiera); marca dos métodos, se usó el de **cambios en el nivel general de precios**. [01:35:54]
- **Factor de actualización** = `INPC más reciente / INPC más antiguo`. Da la **cifra actualizada** (el nuevo
  valor *incluyendo* la inflación). Ej.: 145.527 / 108.850 = **1.33**; ó 1.10/1.0 = 1.10 → un bien de $1,000
  hoy "vale" $1,100. [01:22:07, 01:26:43, 01:27:21, 01:33:32]
- **Factor de ajuste** = `(INPC más reciente / INPC más antiguo) − 1`. Da **la pura inflación** (solo el
  incremento). Ej.: 1.10 − 1 = 0.10 → 10%. **Diferencia clave:** actualización = cifra nueva completa; ajuste =
  nada más el efecto inflacionario. [01:22:07, 01:28:24]
- **Partidas monetarias** (el dinero/billete, inversiones y acciones que se reflejan en dinero) → **NO se
  reexpresan** (su valor nominal es circulante). **Partidas no monetarias** (un coche, un escritorio, un activo
  fijo, mercancía/inventario) → **SÍ se reexpresan** porque cambió su valor. [01:36:29–01:37:33]

### 4) Sistema financiero, dinero y macro (introducción)
- **Agregados monetarios (M1, M2, M3…)**: se analizan en macroeconomía para ver "cómo está el país"; valúan no
  solo el dinero en circulación sino el **documentado** (cheques). El **Banco de México** regula la **emisión y
  circulación** del dinero (hay parámetros que le impiden emitir sin límite). [G-B4 11:40, 12:35]
- **Cuentas que "juegan / no juegan con el sistema financiero mexicano"** (clave para promedios, ver abajo).

### 5) Razones de ROTACIÓN (se leen en veces / ciclos / vueltas / alternancias)
- **Rotación de cuentas por cobrar a clientes** = `ventas netas a crédito / promedio de cuentas por cobrar a
  clientes`. Resultado 6 → *"mi empresa convierte en efectivo (cobra) **6 veces** sus cuentas por cobrar en el
  año"*. Ojo: **ventas netas A CRÉDITO** (no totales: las totales incluyen el contado). Ventas netas = ventas
  totales − descuentos − rebajas − devoluciones − bonificaciones (ej. 1,000,000 − 40,000 = 960,000). [01:59:09, 02:23:00]
- **Rotación de cuentas por pagar a proveedores** = `compras netas a crédito / promedio de cuentas por pagar a
  proveedores`. Resultado 8 → *"pago 8 veces a mis proveedores en el año"*. [02:42:41, 02:48:01]
- **Cómo sacar el "promedio" de la cuenta** (regla del profe):
  - Cuentas que **NO** juegan con el sistema financiero (clientes, proveedores: "Pepito, Lupita…") →
    `(saldo inicial + saldo final) / 2`.
  - Cuentas que **SÍ** juegan con el sistema financiero (bancos) → **saldo promedio diario** (suma de los saldos
    de todos los días del mes ÷ número de días). [02:28:07–02:29:21]

### 6) Razones CRONOLÓGICAS (se leen en días) — "razones de confirmación"
- **Plazo medio de cobro (PMC)** = `número de días del periodo / razón de rotación de CxC`. Con **año comercial =
  360 días** (mes comercial = 30 × 12): 360 / 6 = **60 días** → "cobro cada 60 días". [02:34:57, 02:36:33, 02:37:53]
- **Plazo medio de pago (PMP)** = `número de días del periodo / razón de rotación de CxP`: 360 / 8 = **45 días**
  → "pago a proveedores cada 45 días". [02:48:39]
- **Lectura conjunta (lo que evalúa):** **cobro a 60 días pero pago a 45** → pago a mis proveedores ANTES de
  cobrarle a mis clientes ⇒ problema de **flujo de efectivo** ("¿con qué pago la nómina y los impuestos?").
  Una empresa sana querría **cobrar antes de lo que paga** (PMC < PMP). [G-B6 04:33–05:10, 14:28]

### 7) Estado de Resultados (repaso de estructura)
`Ventas totales − (descuentos + rebajas + devoluciones + bonificaciones sobre venta) = Ventas netas
− Costo de ventas = Resultado bruto (utilidad o pérdida bruta) − Gastos de operación (administración + venta)
= Utilidad o pérdida de operación …` Cada cuenta de mayor tiene **subcuentas** (la suma de subcuentas = saldo
de la cuenta de mayor); hay **contracuentas**. El resultado **NO** se encuentra en el balance, sino en el
**Estado de Resultados**. [G-B5 00:43–05:51]

---

## D. Cobertura vs. temario (Finanzas.pdf)
| Subtema del plan | Hoy | Nota |
|---|---|---|
| 2.1 Razones (rotación, cronológicas) | 🟢 con cifras | Rotación CxC/CxP + PMC/PMP desarrollados con ejemplo numérico. |
| 2.2 Estados financieros (Resultados, reexpresados) | 🟢🟡 | Estructura del Edo. de Resultados + reexpresión (B-10, factores). |
| 2.3 Métodos de análisis | 🟡 | Rotación/cronológicas son métodos verticales (razones simples). |
| **Sistema financiero mexicano** | 🆕 abierto | **NO está en el temario oficial** (se los quitaron); el profe lo agrega y lo evaluará. Tarea para mañana. |
| Inflación / INPC / valor del dinero | 🆕 a fondo | Transversal; sustenta reexpresión y evaluación de proyectos. |

## E. Pendientes / gaps que siguen sin verse con cifras
- **Razones de rentabilidad** y **apalancamiento** (nombradas, aún no desarrolladas con cifras).
- **Porcientos integrales** (método vertical) — aún no se ve; la Clase 5 lo anunciaba.
- **Análisis horizontal** (aumentos y disminuciones, tendencias, estados comparativos).
- **Punto de equilibrio contable** (Unidad 3).

## F. Audio dudoso a verificar (no fiarse de la cifra literal)
- Valores numéricos del INPC del ejemplo (145.527 / 108.850 → 1.33) salieron del ASR: la **mecánica** es
  correcta, pero verifica los índices exactos contra tu pizarrón/apuntes.
- Varios tramos de campo lejano con voz baja del profe en el bloque del Estado de Resultados (G-B5 lista muchos).
