# Guía de estudio — Clase 3 (2026-06-24)
### Finanzas 2632 · Prof. Eduardo Heredia Contreras

> Clase densísima de contenido real (Unidad 2). Eje: **estados financieros** (cuáles son, cómo se relacionan)
> y la **estructura del estado de costo de producción y de lo vendido**, más el arranque del **balance general**.
> Validado con 3 transcripciones (Groq=primaria por audio malo, Voxtral, Gemini-audio). Dominio: ⬜ por estudiar.
>
> ⚠️ **Calidad de audio:** Voxtral colapsó en bucles (~926); se usó **Groq** como primaria. Aun así hay tramos
> ruidosos — ver `disagreements.md`. Notas marcadas «(confirmar)» donde los 3 oídos no coincidieron.

---

## ⭐ A. La ronda de preguntas de hoy (el profe interrogó a "Charly"=Carlos y a otros)
Memoriza estas; son del tipo que repite y resta participación:
1. **Menciona ≥6 métodos de análisis financiero** → respondiste *razones, vertical y horizontal* (válido). [00:27]
2. **Menciona 10 tipos de financiamiento/créditos** → *hipotecarios, revolventes…* (faltó completar). [00:30]
3. **≥3 diferencias entre banca de primer piso y de segundo piso.** [00:32]
4. **¿Cómo se calcula el punto de equilibrio?** (lo dejó pendiente). [00:35]
5. **¿Qué es la TIR?** (otra vez — recurrente 🔁). [00:36]
6. **Nombra los estados financieros básicos** y **≥6 secundarios.** [00:39–01:05]
7. **La cuenta de "gastos financieros": naturaleza y en qué momento se presenta.** [00:40]

> 👉 Anunció: **"Mañana te pregunto… vamos a comenzar con los métodos."** El **primer método** de análisis
> que verán es por **reducción a porcientos / razones** (nombre exacto a confirmar — audio difícil [02:57]).

## B. TIR — Tasa Interna de Retorno (Unidad 5, se adelantó) ⬜
[00:15–00:18]:
- Es la **tasa de descuento capaz de igualar el valor presente de los flujos esperados con el valor presente
  de los desembolsos** (es decir, la que hace **VPN = 0**).
- Se calcula por **ensayo y error** (prueba y error): **no existe una fórmula única**; se prueban tasas hasta
  que el resultado da cero. Con suerte en 5–10 intentos.
- Idea clave: **"mover el dinero en el tiempo"** y buscar la tasa que iguala a cero.
- Característica: a **más decimales**, más te acercas al resultado exacto; la tasa es **inversamente
  proporcional** (a los flujos/al valor — confirmar el matiz). "Hasta los contadores lloran" con la fórmula.

## C. Valor del dinero en el tiempo → inflación ⬜
[00:37–00:38]: el dinero **cambia de valor con el simple transcurso del tiempo**. A ese fenómeno (lo que un
mismo dinero puede comprar hoy vs. en el futuro) se le asocia la **inflación**. Es la razón por la que en
finanzas hay que "mover el dinero en el tiempo".

## D. Contabilidad → Estados financieros (repaso de Clase 2, ampliado) ⬜
[00:58–01:00]: las **operaciones económico-financieras** (todo lo que se maneja con dinero) **se deben
registrar** → ese registro es la **contabilidad** (técnica de registro) → su **resultado** son los **estados
financieros**. El **SAT** obliga a registrar: sin registro no compruebas y "pagas". *(En finanzas usamos el
resultado, no hacemos contabilidad.)*

## E. Clasificación de los estados financieros ⬜ (clave de la clase)
[01:00–01:05]:
### Básicos (4) — los más importantes
1. **Balance General** = *Estado de Posición Financiera* = *Estado de Situación Financiera* (mismos nombres).
2. **Estado de Resultados** (hoy con apellido **"Integral"**; antes "de Pérdidas y Ganancias").
3. **Estado de Flujo de Efectivo** = *Estado de Situación Financiera con base en efectivo*.
4. **Estado de Variaciones en las Cuentas de Capital** = *Estado de Capital Contable*.
> 🔑 "Es la misma gata nada más que revolcada" — un mismo documento con varios nombres.

### Secundarios (apoyan/detallan a los básicos; hay muchos)
- Estado de **costo de producción y costo de producción de lo vendido**
- **Reexpresados** · **Consolidados** · **Comparativos** · **Presupuestados** · **Proforma** · **Analíticos**
- ⚠️ La relación básico↔secundario **va en ambos sentidos**: un secundario puede alimentar a un básico
  (costo de producción → estado de resultados) y un secundario (consolidado) puede agrupar varios básicos.
  Son "secundarios" porque **no todas las empresas están obligadas** a generarlos.

## F. Estado de Costo de Producción y de lo Vendido — ESTRUCTURA ⬜⭐ (el corazón de la clase)
[01:16–02:30, ejemplo Bimbo]. Apréndela en orden — la va a preguntar:

```
        Inventario inicial de materia prima
      + Compras netas            (= compras totales − devoluciones − rebajas − descuentos − bonificaciones s/compras)
      = Materia prima disponible
      − Inventario final de materia prima
      = Materia prima utilizada
      + Mano de obra directa
      = COSTO PRIMO
      + Gastos indirectos de producción (GIF)
      = COSTO INCURRIDO
      + Inventario inicial de producción en proceso
      − Inventario final de producción en proceso
      = Costo de producción TERMINADA
      + Inventario inicial de artículos terminados
      − Inventario final de artículos terminados
      = COSTO DE PRODUCCIÓN DE LO VENDIDO  (costo de ventas)
      ÷ número de unidades producidas
      = COSTO DE VENTA UNITARIO
```
- **Compras netas** = compras totales − (devoluciones + rebajas + descuentos + bonificaciones sobre compras).
  El ejemplo de los **600 sacos de harina** (control de calidad rechaza 40 rotos → devolución; sacos de 49.5 kg
  → rebaja; pago adelantado → descuento; perder el tiempo → bonificación) ilustra cada concepto.
- **3 elementos del costo:** materia prima, **mano de obra directa**, **gastos indirectos de producción**.

## G. Conceptos contables de apoyo ⬜
- **Ejercicio contable** = periodo contable de **un año**. *Ejercicio fiscal/año calendario* = 1 ene–31 dic. [01:40]
- **Periodos contables:** mensual, bimestral, trimestral, cuatrimestral, semestral. Cada uno tiene **saldo
  inicial** (día 1) y **saldo final** (último día); el **saldo final de un periodo = saldo inicial del siguiente**. [01:43]
- **Recta numérica / línea de tiempo** *(el profe la llama "la rana/ranita" — mistranscrito)*: se usa para
  representar la magnitud del movimiento (el ejercicio) en el tiempo. [01:40]
- **Inventario / almacén** = **cuenta de balance, naturaleza deudora**; controla las mercancías. [01:42]
- **Mano de obra directa** = nómina **solo** del personal directamente involucrado en producción (obreros).
  Secretarias, vendedores, limpieza, administración → **NO** son MOD, son gastos. Por eso las plantas están
  separadas de las oficinas. [02:07–02:09]
- **Comercializadora** (1 inventario; compra y vende igual: Walmart, Oxxo, Soriana) vs **Transformadora**
  (mín. **3 inventarios**: MP, producción en proceso, artículos terminados → **6** con inicial+final; produce/
  transforma: Bimbo, Samsung, Apple, Nissan). [02:16–02:26]

## H. Estado de Resultados — estructura ⬜
[01:11–01:12, 05:30 Gemini]:
```
  Ventas brutas (totales)
− descuentos, devoluciones, rebajas y bonificaciones sobre ventas
= Ventas netas
− Costo de ventas
= Resultado de operación (utilidad bruta)
− Gastos (…)
= Utilidad o pérdida
```
> Relación entre documentos: **costo de producción → da el costo de ventas → Estado de Resultados → da la
> utilidad → Balance General** (sin la utilidad, el balance no cuadra). [01:12–01:13]

## I. Estados consolidados y reexpresados ⬜
- **Consolidados:** grupos con varias empresas/plantas/**CEDIS** (centros de distribución)/puntos de venta →
  el corporativo no quiere 50 estados sueltos, pide **el consolidado** (resultado de todo el grupo). [02:09–02:13]
- **Reexpresados:** ajustan cifras por **inflación** para reflejar la realidad del dinero. **No todas** las
  empresas reexpresan — solo las grandes/**dictaminadas** (Bimbo, Ford, VW, Nissan, P&G, La Costeña). Mención
  de **just-in-time** (Japón, industria pesquera) y deflación en Japón. [02:32–02:35]

## J. Balance General — estructura (arranque del análisis) ⬜
[02:47–02:56]. Mismo documento visto **contable** vs **financieramente** (para analizar no necesitas ser contador):
- **Activo** = bienes y derechos · **Pasivo** = deudas y obligaciones · **Capital contable**.
- **Activo:** circulante, fijo, diferido. **Pasivo:** corto plazo, largo plazo.
- **Activo circulante** = cuentas convertibles en efectivo en **≤ 1 año**, ordenadas por **grado de
  disponibilidad** (rapidez de volverse efectivo): **caja → bancos → inversiones de inmediata realización →
  clientes → … → inventarios** (la última).
- **Pasivo** se ordena por **grado de exigibilidad** (≤ 1 año = corto plazo).
- **Capital contable / cuentas de capital:** **capital social** (de acta constitutiva, **acciones**,
  **accionistas**, títulos de crédito), **reserva legal** (**art. 20 LGSM**), **utilidades/pérdidas**. [01:08–01:11]

### Cuentas del activo circulante (detalle) ⬜
- **Caja:** efectivo inmediato (abres el cajón y ahí está).
- **Bancos:** cuenta de cheques. **Cheque = orden incondicional de pago** (al portador o nominativo).
  Disponibilidad *mediata* (mandas por el dinero y te lo traen). [02:51–02:53]
- **Inversiones de inmediata realización:** pagaré a plazo (p. ej. **28 días**) con rendimiento; o **CETES**
  (Certificados de la Tesorería de la Federación, a **tasa de descuento**) — puedes "reventarlos" antes del
  plazo y tener tu dinero en horas, sacrificando intereses → conservas **disponibilidad**. [02:53–02:56]

---

## K. Cobertura vs. plan de estudios — actualizado tras Clase 3
| Unidad | Estado |
|---|---|
| 1. Introducción | 🟢 Cubierto. |
| **2. Análisis financiero integral** | 🟢🟡 **Gran avance**: clasificación de estados financieros (básicos/secundarios), estructura del estado de costo de producción y de lo vendido, estado de resultados, arranque del balance general (activo circulante por disponibilidad). Falta: análisis vertical/horizontal (empieza mañana), razones completas. |
| 3. Planeación (WACC, CAPM) | ⬜ Solo nombrado en el repaso del temario. |
| 4. Flujo de efectivo (método directo) | ⬜ Nombrado como estado básico. |
| **5. VPN / TIR** | 🟡 **TIR explicada a fondo** (ensayo y error, VPN=0). Falta VPN formal. |

**Prioridad para Clase 4:** dominar la **estructura del estado de costo de producción** (memorizada), los **4
básicos + 6 secundarios**, el **balance general** (activo circulante por grado de disponibilidad), y llegar
listo para **el primer método de análisis financiero** (porcientos/razones) que el profe empezará mañana.
