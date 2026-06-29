# Guía de estudio — Clase 4 (2026-06-25)
### Finanzas 2632 · Prof. Eduardo Heredia Contreras

> Otra clase densísima de **Unidad 2**. Tres bloques: (1) cierre del **balance general** (cuentas del activo
> circulante y del pasivo, con el par **clientes/deudores** y **proveedores/acreedores**); (2) el **IVA** a fondo
> (trasladado vs. acreditable, por pagar vs. a favor) y la **clasificación de impuestos**; (3) la **naturaleza de
> las cuentas** + ecuación contable, la **aportación de capital en una S.A.**, la **doble óptica contable↔financiera**
> del balance, las **cifras históricas vs. futuras**, y por fin el **arranque de los métodos de análisis**
> (razones **simples** vs. **estándar**). Dominio: ⬜ por estudiar.
>
> ⚠️ **Calidad de audio:** Voxtral primaria (esta vez **sin bucles**), Groq cruce, **Gemini** (comprensión de
> audio completo, corrió tras varios reintentos por saturación del API). Audio de campo lejano y ruidoso → tramos
> distorsionados; ver `disagreements.md`. **Las fórmulas de razones quedaron confirmadas por la pasada de Gemini.**

---

## ⭐ A. Las rondas de preguntas de hoy (memorízalas — resta participación)
El profe interrogó al azar (a "Charly"=Carlos, a Mike, a José). Tipos que repite:
1. ¿Cómo se **ordena el activo** y bajo qué criterio? → grado de **disponibilidad**. [00:43–00:47]
2. ¿Qué registras en **clientes** y en qué se diferencia de **deudores diversos**? [01:06–01:11]
3. ¿Qué va en **proveedores** vs. **acreedores diversos**? [01:12–01:13]
4. ¿De quién es el **IVA que cobras**? ¿Quién lo paga al final? [01:21–01:32]
5. Si el **IVA trasladado > acreditable**, ¿qué cuenta resulta? ¿y al revés? [01:27–01:31]
6. Nombra los **impuestos federales**; diferencia **directo vs. indirecto**. [01:14–01:17]
7. ¿De qué **naturaleza** son las cuentas de activo / de pasivo y capital? [01:34–01:39]
8. ¿Cuál es la **ecuación contable**? "A todo cargo corresponde un…" [01:36–01:40]
9. En una **S.A.**, ¿cómo se aporta el capital y a qué cuenta va? ¿de quién es ese dinero? [01:47–01:53]
10. ¿Con qué **cifras** empezamos el análisis y por qué? [01:55–02:06]
11. 🔁 **Nombra los métodos de análisis financiero**; ¿cómo se clasifican las **razones**? [02:13–02:19]

> 👉 **Anuncio para la próxima clase:** dará **dos empresas (escenario A y B)** con su *pura estructura* de
> estados financieros (sin cifras) y preguntará **cuál comprarías y por qué** ("si fueran parientes de Slim…").
> Empezamos en forma con **razones financieras** (fórmulas de liquidez). [02:43–02:48]

---

## B. Balance general — cuentas del activo y del pasivo (cierre) ⬜
[00:43–01:13]. Repaso del orden y detalle por cuenta:
- **Activo** ordenado por **grado de disponibilidad** (rapidez de volverse efectivo); **pasivo** por **grado de
  exigibilidad** (rapidez con que hay que pagarlo). Ambos lados con cuentas a **≤ 1 año** (corto) y **> 1 año** (largo).
- **Activo circulante** (orden): **caja → bancos → inversiones de inmediata realización → clientes → … → inventarios**.
  Los **inventarios van al final** porque todavía hay que venderlos para convertirlos en dinero ("como la D de
  perro, hasta abajo"). [00:48, 01:05]
- **Activo fijo:** lo inmovilizado (maquinaria, **un auto es activo fijo**, equipo). [00:45]
- **Activo diferido:** partidas que se **amortizan** — **gastos de instalación, gastos notariales, gastos de
  constitución**, gastos pagados por anticipado. [00:45–00:46]
- **Capital contable:** controla la **inversión y el patrimonio de los accionistas**. [00:46]

### El par CLIENTES vs. DEUDORES DIVERSOS ⭐ [01:06–01:11]
- **Clientes:** ventas **a crédito** que **sí son del giro** de tu empresa. (Vendes jeans a crédito → clientes.)
- **Deudores diversos:** ventas a crédito de algo que **NO es tu giro** (vendes tu **scooter**, tu carro, una
  laptop). "No me dedico a eso, fue adicional al giro" → deudores diversos, no clientes.
- Si la venta es **de contado**, no entra a ninguna de las dos (entra a caja/bancos).

### El par PROVEEDORES vs. ACREEDORES DIVERSOS ⭐ [01:12–01:13]
- **Proveedores:** a quien le compras **a crédito** la materia prima **de tu giro** (mezclilla, botones, hilo).
- **Acreedores diversos:** a quien le debes algo que **NO es de tu giro** (compraste una laptop, un teléfono).
> Regla mnemónica: **clientes/proveedores = del giro; deudores/acreedores diversos = fuera del giro.**

## C. IVA — Impuesto al Valor Agregado ⭐⭐ (núcleo nuevo de la clase) ⬜
[01:14–01:45]. Tasa general **16%**.
- **IVA trasladado (cobrado):** el IVA que **cobras** cuando vendes. **No es tuyo, es de Hacienda** — solo lo
  recaudas. Ejemplo: una laptop vale **$10,000**; con IVA la vendes en **$11,600** ($1,600 = IVA del 16%). [01:23–01:26]
- **IVA acreditable (pagado):** el IVA que **pagas** cuando compras. Tienes **derecho a acreditarlo** (restarlo).
- **Mecánica que pide Hacienda:** *"al IVA que cobras, réstale el IVA que pagas, y entrégame la diferencia"*
  (la chamba de calcularlo te la deja a ti). [01:25]
  - **IVA trasladado > IVA acreditable** → te sobra dinero de Hacienda → **IVA por pagar** = **pasivo**
    (obligación: se lo entregas a Hacienda). [01:27–01:31]
  - **IVA acreditable > IVA trasladado** → pagaste más IVA del que cobraste → **IVA a favor / acreditable** =
    **activo** (derecho: te lo devuelven, o lo **acreditas el mes siguiente**; al cierre hay **devolución
    automática** si presentas en tiempo). [01:31–01:36]
- **Quién paga el IVA al final:** el **consumidor final** — el último de la cadena, que ya **no tiene a quién
  trasladárselo**. Tú como empresa solo lo **separas y lo devuelves**, no lo pagas. [01:32, 01:40]
- **Financiamiento temporal:** entre que cobras el IVA y lo entregas, puedes "financiarte" con ese dinero…
  **pero no es tuyo**; quien se lo gasta y no lo devuelve cae en **multas, actualizaciones y recargos**. [01:32–01:33]
- **Control contable:** se llevan en cuentas de **mayor** — **IVA trasladado** vs. **IVA acreditable**. [01:26, 01:45]

## D. Clasificación de impuestos ⬜ [01:14–01:17]
- **Por ámbito:**
  - **Federales** (aplican en toda la república): **ISR** (Impuesto Sobre la Renta), **IVA**, **IEPS** (Impuesto
    Especial sobre Producción y Servicios).
  - **Locales** (estatales/municipales).
- **Por traslación:**
  - **Directos:** los paga **directamente** quien los causa, **no se trasladan**. Ej. **ISR** — grava la
    **renta/ingreso**; *"el que más gana, más paga"*; las **deducciones** bajan la base gravable.
  - **Indirectos:** se pueden **trasladar** al siguiente de la cadena. Ej. **IVA**, **IEPS**.

## E. Naturaleza de las cuentas + ecuación contable (partida doble) ⬜⭐ [01:34–01:40, 01:45]
- **Cuentas de ACTIVO → naturaleza DEUDORA:** **aumentan con cargos (débitos), disminuyen con abonos (créditos)**
  (salvo cuentas complementarias/especiales).
- **Cuentas de PASIVO y CAPITAL → naturaleza ACREEDORA:** **aumentan con abonos, disminuyen con cargos.**
- **Ecuación contable:** **ACTIVO = PASIVO + CAPITAL** (es una **igualdad** matemática; el balance "cuadra").
- **Partida doble:** *"a todo cargo corresponde un abono"*. Hay que **cuadrar** la operación. [01:37]
- **Ejemplo de registro — compro una computadora de $10,000 + IVA:** [01:37–01:39, 01:50–01:52]
  ```
  Cargo:  Equipo de cómputo .......... 10,000   (activo fijo, naturaleza deudora ↑)
  Cargo:  IVA acreditable ...........   1,600
  Abono:  Bancos ..................... 11,600   (activo, deudora; abono ↓ porque sale dinero)
  ```
  La computadora **costó 10,000**, no 11,600 (los 1,600 del IVA son acreditables). [01:38]

## F. Aportación de capital en una S.A. ⬜ [01:46–01:53]
- Repaso: **persona moral / S.A.** = **unión jurídica de 2+ personas** con **personalidad jurídica propia**,
  distinta a la de los socios. [01:47]
- El capital se aporta **en efectivo o en bienes distintos al numerario** (propiedad intelectual, infraestructura/
  oficinas, equipo). Ejemplo: tres socios forman una S.A. de **$1,000,000** (uno pone el "cerebro"/dinero, otro
  las instalaciones, otro parte efectivo + equipo). [01:48–01:50]
- Cada socio recibe **acciones** proporcionales a su aportación → se vuelve **accionista** (mayoritario o
  minoritario). [01:50, 01:65]
- La aportación **NO** va a deudores ni a acreedores: va a **capital contable → cuenta de CAPITAL SOCIAL**. [01:51–01:53]
- 🔑 **Idea fuerte:** una vez aportado, **el dinero ya no es tuyo, es de la empresa** (ente con personalidad
  propia). Por eso el **capital es una fuente de financiamiento INTERNA** y el **pasivo una fuente EXTERNA**. [01:51–01:53, 01:63]

## G. Doble óptica del balance — contable vs. financiera ⬜⭐ [01:41–01:45, 01:59–01:61]
"El mismo documento, dos veces impreso, visto con dos ópticas":
| | **Óptica CONTABLE** | **Óptica FINANCIERA** |
|---|---|---|
| **Activo** | bienes y derechos | **en qué se invirtió** (uso/aplicación de recursos) |
| **Pasivo** | deudas y obligaciones | **fuente de financiamiento EXTERNA** |
| **Capital** | inversión y patrimonio de accionistas | **fuente de financiamiento INTERNA** |
> El administrador (Pancho) reclama que *"no es lo mismo igualar pasivo con capital"*: en finanzas se **separan**
> porque representan **fuentes de financiamiento de distinto origen** (externo vs. interno). [01:45]

## H. Cifras históricas vs. futuras — línea de tiempo y fecha focal ⬜ [01:53–02:06]
- **Fecha focal = hoy**: divide la línea del tiempo en **pasado / presente / futuro**. [01:55]
- **Pasado → cifras HISTÓRICAS:** hechos **ya consumados**, **conocidos, definidos, realizados** (muchos ya
  pagados). Aquí no "pienso comprar": **ya compré**. [01:57–01:58]
- **Futuro → cifras FUTURAS:** **no se conocen aún**; se **estiman, presupuestan o proyectan**. [01:57, 01:85]
- **Qué se aplica a cada lado:**
  - A las **históricas** → **métodos de análisis financiero** (lo que veremos). La **auditoría** también revisa
    históricas, pero con otro fin (verificar el registro). [01:59–02:00]
  - Al **futuro** → **métodos de evaluación de proyectos** (Unidad 5; se ven a fondo en otra materia,
    *"Proyectos de inversión"*). [02:02–02:03]
- El programa marca como tema central el **análisis financiero** (de cifras históricas). [01:53, 02:13]

## I. Métodos de análisis financiero — arranque ⬜⭐ (lo anunciado) [02:13–02:48]
Lista (enunciativa, no limitativa): **razones, porcientos integrales, comparativos, aumentos y disminuciones,
punto de equilibrio, horizontales, verticales**. [02:07–02:15]

### Razones: dos grandes clasificaciones ⭐ [02:12–02:22]
- **Razones SIMPLES** → miden lo **endógeno (interno)**: lo que la empresa **controla, mide y puede modificar**
  con sus propios resultados (liquidez, solvencia, etc. de la propia empresa).
- **Razones ESTÁNDAR** → miden lo **exógeno (externo)**: comparan a la empresa contra su **sector, ramo, giro,
  competencia, mercado** (ej.: cómo está Nissan **frente a su industria**). Ejemplos: **la media** y otras
  medidas estadísticas. Se ven a fondo en **estadística** (curvas, distribución normal). [02:18–02:22, 02:33–02:40]

### Tipos de razones simples (enunciativas) [02:14–02:19, 02:34–02:43]
**liquidez · solvencia · apalancamiento · rotación (actividad) · cronológicas · rentabilidad**
(hay **híbridas/compuestas** = mezcla de dos, pero siguen siendo las mismas por naturaleza).
- **Liquidez:** capacidad de pago a **corto plazo**.
- **Solvencia:** capacidad de cubrir **todas** las obligaciones (incluye razón de **capital de trabajo**).
- **Cronológicas:** **plazo de cobro**, **plazo de pago**.

### Fórmulas que mencionó (✅ confirmadas con la pasada de Gemini) [02:35–02:48]
- **Prueba severa / prueba del ácido** = **(activo circulante − inventarios) / pasivo a corto plazo**.
  Es la liquidez **excluyendo inventarios**. [02:36, 02:47]
- **Prueba de liquidez** = **(efectivo en caja + efectivo en bancos + efectivo de realización) / pasivo a corto
  plazo**. [02:36]
- **Razón de capital de trabajo (RCT / "FCT")** = **activo circulante / pasivo a corto plazo**. [02:44]
- **Capital neto de trabajo (CNT / "CMT")** = **activo circulante − pasivo a corto plazo**. [02:45]
- **Margen de seguridad** = **capital de trabajo (CMT) / pasivo a corto plazo**. [02:44]
- **Razones de rotación:** de cuentas por cobrar (clientes), por pagar (proveedores), de inventarios.
  **Cronológicas:** **plazo medio de cobro**, **plazo medio de pago**. [02:35]
- Cada razón da un **índice** al que hay que darle **lectura/interpretación** (positiva o negativa) — esa es la
  "tarea". [02:37, 02:46]
- Mencionó "normas/boletines" (números tipo *128, 80, 50*): dijo que **no hace falta memorizar los números**,
  sino **entender de dónde salen las cifras y cómo se ocupan**. [02:38–02:39]
> El profe cerró anunciando: **"para mañana voy a preguntar el método de razones."** (confirmado por Gemini)

## J. Ejercicio anunciado: comparar dos empresas (A vs. B) ⬜ [02:43–02:48]
Dará **dos estructuras de estado financiero** sin cifras y preguntará **cuál comprarías**. Criterio de la
respuesta modelo (la dio Carlos/José): la mejor tiene **más activos, menos pasivos (deuda) y más capital**.
Meta del curso: con la **pura estructura** poder decir si la empresa está **sana, enferma o moribunda** e
incluso a qué se dedica.

---

## K. Cobertura vs. plan de estudios — actualizado tras Clase 4
| Unidad | Estado |
|---|---|
| 1. Introducción | 🟢 Cubierto. |
| **2. Análisis financiero integral** | 🟢🟡 **Casi completo el bloque de estructura**: balance (cuentas del activo/pasivo, clientes/deudores, proveedores/acreedores), **IVA** y clasificación de impuestos, **naturaleza de cuentas + ecuación contable**, aportación de capital S.A., doble óptica contable/financiera, cifras históricas vs. futuras, **arranque de métodos (razones simples vs. estándar)**. Falta: desarrollar cada razón con cifras, porcientos integrales, análisis horizontal. |
| 3. Planeación (WACC, CAPM) | ⬜ Solo nombrado. |
| 4. Flujo de efectivo | ⬜ Nombrado como básico. |
| **5. VPN / TIR / evaluación de proyectos** | 🟡 TIR explicada (C3); hoy se ubicó la evaluación de proyectos como herramienta para el **futuro** (otra materia). |

**Prioridad para Clase 5:** llevar **memorizadas** las fórmulas de **liquidez / prueba del ácido / CNT / RCT**,
el par **clientes-deudores / proveedores-acreedores**, la **mecánica del IVA** (trasladado/acreditable → por
pagar/a favor) y la **naturaleza de las cuentas + ecuación contable**; y llegar listo para el **ejercicio de las
dos empresas (A vs. B)**.
