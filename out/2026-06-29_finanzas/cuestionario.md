# Cuestionario de práctica — preparación para la Clase 7 (martes 30-jun)
### Finanzas 2632 · generado tras Clase 6 (2026-06-29)

> Predictivo. El profe **avisó textualmente** que mañana **empieza preguntando el SISTEMA FINANCIERO MEXICANO y
> lo va a preguntar DOS VECES** [02:50:58]. Además dejó tarea de **construir la base de datos de reexpresión** y
> sigue con **razones de rotación/cronológicas**. Responde de viva voz; clave colapsable al final.

## 🎯🎯 Prioridad MÁXIMA — lo que dijo que preguntará mañana (×2)
1. **¿Cuál es la estructura del sistema financiero mexicano?** (autoridades/reguladores, intermediarios, organismos de protección). ⭐⭐
2. **Nombra ≥6 organismos del sistema financiero mexicano y di qué hace cada uno.** ⭐⭐
3. ¿Quién es la **máxima autoridad** del sistema financiero? ¿Qué papel juega **Banxico**? ¿y la **CNBV**?
4. ¿Qué organismo **protege al usuario** de servicios financieros? ¿y a los **ahorradores** si quiebra un banco?
5. Diferencia entre **banca de primer piso** y **de segundo piso** (ya la había preguntado en C3). ⭐

## 🎯 Prioridad ALTA — inflación y reexpresión
6. ¿Qué es la **inflación**? (la **pérdida** del poder adquisitivo del dinero). ⭐
7. ¿Con qué se **mide** la inflación? ¿quién publica el **INPC** y cuándo? (INEGI/Banxico, primeros 10 días; diezmilésimos)
8. ⭐ **¿Cuál es la diferencia entre el factor de actualización y el factor de ajuste?** Da las dos fórmulas.
9. Si el INPC reciente es 145.527 y el antiguo 108.850, ¿cuánto vale el **factor de actualización**? ¿qué significa? *(≈1.33)*
10. ⭐ ¿Qué dice el **Boletín B-10**? ¿Qué se reexpresa: **partidas monetarias o no monetarias**? Da 2 ejemplos de cada una.
11. ¿El **billete** se reexpresa? ¿y las **acciones/inversiones**? ¿por qué no?

## 🎯 Prioridad ALTA — razones de rotación y cronológicas
12. ⭐ **Fórmula** de la **rotación de cuentas por cobrar a clientes**. ¿En qué se lee? (veces/ciclos/vueltas)
13. ¿Por qué se usan **ventas netas a crédito** y no las totales? ¿Cómo saco las ventas netas?
14. **Fórmula** de la **rotación de cuentas por pagar a proveedores** (con **compras netas a crédito**).
15. ¿Cómo se saca el **promedio** de la cuenta? ¿Qué cambia si la cuenta **"juega con el sistema financiero"** (banco) vs. si no?
16. ⭐ **Plazo medio de cobro** y **plazo medio de pago**: fórmula, **año comercial = 360**, y resultados (60 y 45 días).
17. ⭐ Si **cobro a 60 días** pero **pago a 45**, ¿mi empresa está **bien o mal** y **por qué**? ¿Qué sería lo sano?

## 🎯 Prioridad MEDIA — Estado de Resultados y repaso
18. Integra el **Estado de Resultados**: de ventas totales hasta utilidad/pérdida de operación.
19. ¿En qué documento está el **resultado** de la empresa? (no en el balance). ¿Qué es una **cuenta de mayor** y una **subcuenta**?
20. ¿Qué significa **1.80 de "colchón"**? (margen de seguridad)
21. **Solvencia vs. liquidez**; lectura de una razón **sin nombrarla** (sigue siendo su patrón estrella).

## 🎯 Listas del diagnóstico (las sigue preguntando al azar) 🔁
22. **≥6 organismos del sistema financiero mexicano** ← *ahora es el tema central, domínala.*
23. **6–8 métodos de análisis financiero.**
24. **≥6 estados financieros secundarios.**
25. **10 tipos de crédito.**

## 💻 Tarea práctica (no es pregunta, es entrega/revisión)
- Arma el **Excel/sistema de reexpresión**: input = cifra base; el sistema busca el INPC en una tabla, calcula el
  **factor de actualización** y devuelve en automático la **cifra actualizada**.

---

<details>
<summary>✅ Clave de respuestas</summary>

1. **Estructura:** (a) **Autoridades/reguladores** (SHCP, Banxico, CNBV, CNSF, CONSAR); (b) **intermediarios
   financieros** (bancos/banca múltiple, casas de bolsa, aseguradoras, afores, sofomes…); (c) **organismos de
   protección** (CONDUSEF, IPAB). Todo encabezado por la **SHCP**.
2/3/4. **SHCP** = rectora de la política financiera/fiscal. **Banxico** = banco central; emite moneda, controla
   inflación y regula el sistema de pagos. **CNBV** = supervisa bancos y casas de bolsa. **CNSF** = seguros y
   fianzas. **CONSAR** = afores (ahorro para el retiro). **CONDUSEF** = **protege al usuario** de servicios
   financieros. **IPAB** = **protege al ahorrador** (seguro de depósitos si quiebra un banco). **BMV** = Bolsa
   Mexicana de Valores (mercado).
5. **Primer piso** = atiende directo al público (bancos comerciales). **Segundo piso** = presta a través de
   otros bancos, no al público directo (banca de desarrollo: Nafin, Bancomext, Banobras).
6. **Inflación = la pérdida del poder adquisitivo del dinero** (no "reducción": pérdida). El billete vale igual
   nominalmente pero compra menos.
7. Se mide con el **INPC** (fórmula de **Laspeyres** + ponderadores del **INEGI**); se publica en los **primeros
   10 días** de cada mes; la ley pide **diezmilésimos** (4 decimales).
8. **Factor de actualización = INPC reciente / INPC antiguo** → da la **cifra actualizada** (incluye la
   inflación). **Factor de ajuste = (INPC reciente / INPC antiguo) − 1** → da **solo la inflación** (el incremento).
9. 145.527 / 108.850 ≈ **1.33** → mi bien hoy "vale" 1.33 veces lo que valía; un $1,000 pasa a ≈$1,336.
10. **B-10** (NIF) ordena reexpresar por inflación; se reexpresan las **partidas no monetarias** (coche,
    escritorio, activo fijo, inventario/mercancía). Las **monetarias** (dinero/billete, inversiones, acciones)
    **no** (valor nominal circulante).
11. **No.** El billete y lo que se refleja en dinero (acciones/inversiones) ya están en valor nominal corriente;
    solo cambian de valor real los **bienes** (no monetarios).
12. **Rotación CxC = ventas netas a crédito / promedio de cuentas por cobrar a clientes**; en **veces/ciclos/
    vueltas/alternancias**. Ej. 6 = "cobro 6 veces mis CxC al año".
13. Porque la cuenta de clientes nace de ventas **a crédito** (las de contado ya entraron a caja/bancos). Ventas
    netas = ventas totales − descuentos − rebajas − devoluciones − bonificaciones; luego tomo solo las **a crédito**.
14. **Rotación CxP = compras netas a crédito / promedio de cuentas por pagar a proveedores**. Ej. 8 = "pago 8
    veces al año".
15. Promedio de cuenta que **NO** juega con el sistema financiero (clientes/proveedores) = **(saldo inicial +
    saldo final)/2**. Cuenta que **SÍ** juega (bancos) = **saldo promedio diario** (Σ saldos diarios ÷ nº de días).
16. **PMC = días del periodo / rotación CxC**; con **año comercial 360**: 360/6 = **60 días**. **PMP = 360 /
    rotación CxP** = 360/8 = **45 días**. (Son las "razones de confirmación" de la rotación.)
17. **Mal:** cobro cada **60** días pero pago cada **45** → estoy **pagando antes de cobrar** ⇒ me falta efectivo
    para nómina/impuestos. Lo **sano** es **cobrar antes de lo que pago** (PMC < PMP).
18. Ventas totales − (descuentos + rebajas + devoluciones + bonificaciones) = **Ventas netas** − Costo de ventas
    = **Resultado bruto** − Gastos de operación (administración + venta) = **Utilidad/pérdida de operación**.
19. En el **Estado de Resultados** (no en el balance). **Cuenta de mayor** = cuenta global; **subcuentas** la
    detallan y su suma da el saldo de la cuenta de mayor; las **contracuentas** restan.
20. **Margen de Seguridad = 1.80** → "pago toda mi deuda y aún me sobra el equivalente a $1.80 (180%)".
21. **Solvencia** = capacidad de pago (todo lo que tengo vs. lo que debo); **liquidez** = disponibilidad
    inmediata de efectivo. Regla: al interpretar **no nombrar la razón**, solo decir qué significa el resultado.
22. SHCP · Banxico · CNBV · CONDUSEF · CNSF · CONSAR · IPAB · BMV.
23. Vertical: porcientos integrales, razones simples, razones estándar · Horizontal: aumentos y disminuciones,
    tendencias, estados comparativos · + punto de equilibrio, flujo de efectivo.
24. Costo de producción · costo de producción y ventas · analítico de ventas · analítico de gastos · conciliación
    bancaria · antigüedad de saldos · origen y aplicación de recursos.
25. Hipotecario · personal · prendario · refaccionario · avío · quirografario · simple · cuenta corriente ·
    arrendamiento financiero · factoraje · automotriz · tarjeta · comercial.

</details>
