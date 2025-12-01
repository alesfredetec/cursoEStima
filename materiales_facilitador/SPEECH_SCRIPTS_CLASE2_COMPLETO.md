# Speech Scripts - CLASE 2 COMPLETA: Métodos de Estimación

**Versión:** 2.0 - Formato Remoto
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Tono:** Amigable, relajado, conversacional
**Duración total:** 3 horas (180 minutos)

---

## 🎯 Estructura de Clase 2

**PARTE 1:** Métodos Clásicos (PERT, CPM) - 50 minutos
**BREAK:** 15 minutos
**PARTE 2:** Métodos Ágiles (Planning Poker, Velocity) - 80 minutos
**PARTE 3:** Comparación y Síntesis - 15 minutos
**Cierre:** 5 minutos

---

## Slide 1: Portada (2 min)

"Bienvenidos de vuelta a la Clase 2: **Métodos de Estimación**.

[PAUSA - sonreír]

En Clase 1 vimos EL PROBLEMA. El diagnóstico. Por qué las estimaciones tradicionales fallan sistemáticamente.

Hoy vemos LAS HERRAMIENTAS.

[ÉNFASIS]

Vamos a ver 3 enfoques diferentes:

1. **PERT / CPM**: Los clásicos. Años 50-60. Militar, NASA, construcción.
2. **Ágil**: Story Points, Planning Poker. Años 2000. Software, equipos auto-organizados.
3. **CCPM**: Preview para Clase 3. El cambio de paradigma.

[PAUSA]

¿El objetivo de hoy?

Que al final de esta clase puedan elegir la herramienta **APROPIADA** para su contexto.

No hay 'mejor método'. Hay 'método apropiado para este proyecto'.

[TRANSICIÓN]

Empecemos con los clásicos. Vamos a 1958..."

---

## Slide 2: Agenda (3 min)

"OK, el plan de hoy.

[LEER agenda relajadamente]

**Primera mitad (50 min):**

**PERT**: Program Evaluation and Review Technique.
Cómo estimar con 3 puntos (Optimista, Más Probable, Pesimista).
La matemática detrás. Por qué funciona... y por qué NO basta.

**CPM**: Critical Path Method.
Cómo identificar la Ruta Crítica.
Por qué optimizar la ruta crítica acorta el proyecto.
Y... spoiler... por qué CPM ignora algo crítico: los **recursos**.

**Break de 15 minutos.**

**Segunda mitad (95 min):**

**Estimación Ágil**:
- Story Points: complejidad relativa, no horas absolutas.
- Escala Fibonacci: 1, 2, 3, 5, 8, 13...
- T-Shirt Sizing: XS, S, M, L, XL.

**Planning Poker**:
Aquí viene lo jugoso. Vamos a narrar un caso COMPLETO paso a paso.
Van a ver cómo el proceso expone suposiciones ocultas y genera alineación.

**Velocidad y Forecasting**:
Cómo medir la capacidad del equipo empíricamente.
Cómo responder '¿cuándo estará listo?' sin mentir.

**Cierre (20 min):**

Tabla comparativa: ¿Cuándo usar PERT? ¿Cuándo Ágil? ¿Cuándo CCPM?

[ÉNFASIS]

Esta clase tiene MUCHO contenido. Les pido paciencia. Al final va a cerrar.

¿Listos? Vamos a 1958, plena Guerra Fría..."

---

## Slide 3: Introducción a PERT (8 min)

"PERT. **Program Evaluation and Review Technique**.

[CONTEXTO histórico - tono narrativo]

1958, plena Guerra Fría. La Marina de EEUU necesita desarrollar misiles balísticos Polaris para submarinos nucleares.

Problema: el proyecto tiene **3,300 contratistas**, 250 tareas principales, dependencias complejas.

Pregunta: ¿Cuánto va a tardar?

[PAUSA]

Método tradicional (Gantt, single estimate): 'Tarea X toma 30 días'.

Pero... ¿y si hay retrasos? ¿y si hay imprevistos? En un proyecto con 3,300 partes móviles, las probabilidades de que TODO salga según plan son... cero.

[ÉNFASIS]

Necesitaban un método que **capturara la incertidumbre** explícitamente.

Ahí nace PERT.

[EXPLICAR concepto]

La idea central de PERT:

**NO estimar con un número. Estimar con TRES números.**

[LEER los 3 puntos]

1. **Optimista:** ¿Qué pasa si TODO sale perfecto?
2. **Más Probable:** ¿Qué esperamos realistamente?
3. **Pesimista:** ¿Qué pasa si Murphy ataca?

[PAUSA]

Y luego usan matemática para calcular una estimación ponderada.

**Resultado:** Proyecto Polaris se completó **2 años ANTES** de lo originalmente estimado.

PERT se acreditó como factor crítico del éxito.

[CONEXIÓN con Clase 1]

¿Recuerdan el Cono de Incertidumbre?

En fase de Concepto: ±400%.

PERT es una forma de **CAPTURAR** esa variabilidad explícitamente.

No das un número falso. Das un **RANGO** que refleja la incertidumbre real.

[ANALOGÍA]

Pregunta: '¿Cuánto tarda llegar del aeropuerto a tu casa?'

Respuesta puntual: '30 minutos.'

Respuesta PERT:
- Optimista (3am, cero tráfico): 20 min
- Más probable: 30 min
- Pesimista (hora pico, accidente): 60 min

¿Cuál es más honesta? La respuesta PERT.

[TRANSICIÓN]

Veamos la matemática..."

---

## Slide 4: Fórmula PERT (10 min)

"OK, la fórmula.

[LEER fórmula en pantalla]

**μ = (O + 4M + P) / 6**

Donde:
- O = Optimista
- M = Más Probable (Most Likely)
- P = Pesimista

[PAUSA - dejar que miren]

Pregunta obvia: ¿Por qué multiplicar M por 4?

¿Por qué dividir entre 6?

¿De dónde sale esto?

[EXPLICAR]

Esto viene de la **distribución Beta**.

En estadística, cuando tenés incertidumbre asimétrica (no es una campana perfecta), la distribución Beta modela bien el comportamiento.

La fórmula **μ = (O + 4M + P) / 6** es una aproximación de la **media** de esa distribución.

[PAUSA]

Traducción: el número 'M' (Más Probable) tiene 4 veces más peso que los extremos.

Tiene sentido: los extremos (best case / worst case) son menos probables. El centro es donde caemos usualmente.

[EJEMPLO numérico]

Tarea: Implementar módulo de autenticación.

**Estimaciones del equipo:**
- Optimista (O): 3 días (todo va perfecto, API lista, sin bugs)
- Más Probable (M): 7 días (normal, algún bug, testing)
- Pesimista (P): 15 días (API incompleta, bugs severos, refactor)

[CALCULAR]

**μ = (3 + 4×7 + 15) / 6**
**μ = (3 + 28 + 15) / 6**
**μ = 46 / 6**
**μ ≈ 7.7 días**

[INTERPRETAR]

La estimación PERT dice: **8 días** (redondeado).

Pero ojo: NO es una promesa. Es la **esperanza matemática**.

[PAUSA]

Pregunta: '¿Hay 50% de probabilidad de terminar en 8 días?'

Respuesta: **NO**.

La distribución Beta es asimétrica. Típicamente hay ~35-40% de chance de terminar en la esperanza.

Más chance de pasarse que de terminarse antes.

[VER GRÁFICO en slide - curva Beta]

La distribución se 've así: pico en 7, pero cola larga hacia la derecha (15 días).

[ÉNFASIS]

Por eso PERT también calcula **varianza**:

**σ² = [(P - O) / 6]²**

Varianza mide 'qué tan dispersa' está la estimación.

En nuestro caso:
- σ² = [(15 - 3) / 6]² = [12/6]² = 2² = 4
- σ = 2 días (desviación estándar)

[INTERPRETAR varianza]

Estimación: **8 días ± 2 días**

Rango razonable: 6-10 días.

[PAUSA]

Esto es MUCHO más honesto que decir 'toma 8 días' sin contexto.

[TRANSICIÓN]

Ahora, ¿cómo usamos esto en un proyecto con MUCHAS tareas?"

---

## Slide 5: PERT en Proyectos Complejos (8 min)

"Un proyecto real no es UNA tarea. Son 50, 100, 200 tareas.

¿Cómo aplicamos PERT ahí?

[EXPLICAR proceso]

**Paso 1:** Cada tarea se estima con 3 puntos (O-M-P).

**Paso 2:** Calcular μ y σ² para cada tarea.

**Paso 3:** Sumar esperanzas (μ) para obtener duración total del proyecto.

**Paso 4:** Sumar varianzas (σ²) para obtener incertidumbre total.

[PAUSA - ÉNFASIS en Paso 4]

Esto es crítico: **las varianzas se SUMAN**.

No se promedian. Se SUMAN.

¿Por qué importa?

[EJEMPLO]

Proyecto con 10 tareas:
- Cada tarea: μ = 5 días, σ = 1 día
- Duración total: 10 × 5 = **50 días**
- Varianza total: 10 × 1² = 10
- Desviación estándar total: √10 ≈ **3.2 días**

[PAUSA]

Rango del proyecto: **50 ± 3.2 días** → 47-53 días (razonable).

[AHORA el problema]

Proyecto con 100 tareas:
- Cada tarea: μ = 5 días, σ = 1 día
- Duración total: 100 × 5 = **500 días**
- Varianza total: 100 × 1² = 100
- Desviación estándar total: √100 = **10 días**

Rango: **500 ± 10 días** → 490-510 días.

[PAUSA - tono reflexivo]

Esperen... 100 tareas, cada una con ±1 día de incertidumbre...

...y el proyecto TOTAL solo tiene ±10 días de incertidumbre?

Eso suena... optimista.

[PROBLEMA DE PERT]

En la práctica, las tareas NO son independientes.

Si una tarea se retrasa, a menudo arrastra a otras:
- Dependencias técnicas
- Recursos compartidos
- Conocimiento oculto que se descubre tarde

**PERT asume independencia. Eso es falso en proyectos reales.**

[CONEXIÓN con Clase 1]

¿Recuerdan los estudios de Microsoft y MIT?

Los proyectos con padding distribuido (cada tarea con 'colchón') terminaban PEOR.

Parkinson y Student Syndrome comían el padding.

[ÉNFASIS]

PERT mejora la **estimación individual**, pero NO previene la **dinámica psicológica**.

[TRANSICIÓN]

Y ahí entra CPM..."

---

## Slide 6: CPM - Critical Path Method (12 min)

"CPM: **Critical Path Method**.

Hermano de PERT. Desarrollado casi al mismo tiempo (1957) por DuPont.

[PREGUNTA retórica]

Si tengo 100 tareas en mi proyecto, ¿todas son igual de importantes?

[Esperar respuestas mentales]

Respuesta: **NO**.

Algunas tareas están en la **Ruta Crítica**.

[DEFINICIÓN]

**Ruta Crítica:** Secuencia de tareas que determina la duración MÍNIMA del proyecto.

Si una tarea en la ruta crítica se retrasa 1 día → el proyecto se retrasa 1 día.

Si una tarea FUERA de la ruta crítica se retrasa 1 día → puede no afectar (tiene 'holgura').

[ANALOGÍA]

Imaginen que van a preparar una cena de 3 platos:

**Tareas:**
1. Cocinar arroz: 20 min
2. Hacer ensalada: 10 min
3. Cocinar carne: 30 min
4. Hacer postre: 15 min

¿Cuánto tarda la cena completa?

[PAUSA]

Si hacen TODO secuencial: 20 + 10 + 30 + 15 = **75 minutos**.

Pero pueden **paralelizar**:
- Mientras se cocina el arroz (20 min), hacen la ensalada (10 min)
- Mientras se cocina la carne (30 min), hacen el postre (15 min)

Timeline real:
- Minuto 0-20: Arroz (+ Ensalada en paralelo)
- Minuto 20-50: Carne (+ Postre en paralelo)

**Total: 50 minutos** (no 75).

[IDENTIFICAR ruta crítica]

**Ruta Crítica:** Arroz (20) → Carne (30) = **50 min**

Ensalada y Postre tienen **holgura** (pueden retrasarse sin afectar).

[PAUSA]

**Implicación:** Si querés acortar la cena, optimizá la carne o el arroz.

NO pierdas tiempo optimizando la ensalada (no está en ruta crítica).

[APLICAR a software]

Proyecto de desarrollo:

**Tareas:**
- A: Diseño de DB (5 días)
- B: Backend API (10 días) - depende de A
- C: Frontend (8 días) - depende de B
- D: Testing (3 días) - depende de C
- E: Documentación (4 días) - puede empezar después de A

[DIBUJAR mentalmente]

A (5) → B (10) → C (8) → D (3) = **26 días** (Ruta Crítica)

E (4) puede empezar después de A, termina en día 9.

**Duración proyecto: 26 días** (no 30 si hicieras todo secuencial).

[ÉNFASIS]

CPM dice: **Optimizá B y C** (están en ruta crítica).

Si B baja de 10 a 8 días → proyecto baja a 24 días.

Si E baja de 4 a 2 días → proyecto sigue en 26 días (E no está en ruta crítica).

[PAUSA - El problema de CPM]

CPM asume que podés **paralelizar** A, B, C, D, E sin problema.

Pero... ¿qué pasa si:
- B y E necesitan al MISMO desarrollador?
- C y D necesitan el MISMO entorno de testing?

Ahí CPM **falla**. Porque ignora **recursos**.

[PREVIEW Clase 3]

En Clase 3 veremos **Critical CHAIN** (no Critical Path).

La diferencia: Critical Chain incluye **recursos**.

Eso cambia todo.

[TRANSICIÓN]

Antes del break, veamos cómo PERT y CPM se combinan..."

---

## Slide 7: Combinando PERT y CPM (10 min)

"En la práctica, PERT y CPM se usan juntos.

[PROCESO combinado]

**Paso 1:** Identificar todas las tareas y dependencias (grafo de red).

**Paso 2:** Estimar cada tarea con PERT (O-M-P → μ y σ²).

**Paso 3:** Calcular Ruta Crítica (CPM).

**Paso 4:** Sumar μ de tareas en ruta crítica → Duración esperada del proyecto.

**Paso 5:** Sumar σ² de tareas en ruta crítica → Varianza del proyecto.

[EJEMPLO completo]

Proyecto con 6 tareas:

| Tarea | Predecesoras | O | M | P | μ | σ² |
|-------|--------------|---|---|---|---|----|
| A | - | 2 | 3 | 5 | 3.2 | 0.25 |
| B | A | 4 | 6 | 10 | 6.3 | 1.0 |
| C | A | 3 | 4 | 6 | 4.2 | 0.25 |
| D | B | 5 | 7 | 11 | 7.3 | 1.0 |
| E | C | 2 | 3 | 5 | 3.2 | 0.25 |
| F | D, E | 3 | 4 | 6 | 4.2 | 0.25 |

[IDENTIFICAR rutas]

**Ruta 1:** A → B → D → F = 3.2 + 6.3 + 7.3 + 4.2 = **21 días**
**Ruta 2:** A → C → E → F = 3.2 + 4.2 + 3.2 + 4.2 = **14.8 días**

**Ruta Crítica:** Ruta 1 (21 días).

[CALCULAR incertidumbre]

Varianza de Ruta Crítica: 0.25 + 1.0 + 1.0 + 0.25 = **2.5**
Desviación estándar: √2.5 ≈ **1.6 días**

**Resultado:**

Duración esperada: **21 ± 1.6 días** (68% de confianza)
Rango amplio (95% confianza): **21 ± 3.2 días** → 18-24 días

[INTERPRETAR para stakeholder]

"El proyecto tomará aproximadamente **21 días**.

Hay 68% de probabilidad de que esté entre 19-23 días.

Hay 95% de probabilidad de que esté entre 18-24 días.

Si necesitamos compromiso firme, recomendamos planificar para **24 días** (incluye 2σ de buffer)."

[PAUSA - ÉNFASIS]

Esto es **honestidad** vs falsa precisión.

Mejor decir '21 ± 3 días' que '21 días exactos'.

[BENEFICIOS de PERT/CPM]

✅ Captura incertidumbre explícitamente (PERT 3 puntos)
✅ Identifica dónde concentrar esfuerzo (CPM ruta crítica)
✅ Cuantifica riesgo (varianza agregada)
✅ Funciona bien para proyectos con fases claras

[LIMITACIONES]

❌ Asume independencia de tareas (raramente cierto)
❌ Ignora recursos (CPM asume paralelismo infinito)
❌ NO previene Parkinson / Student Syndrome
❌ Estimaciones iniciales siguen siendo basadas en 'adivinar'

[TRANSICIÓN]

OK, eso es PERT/CPM. Los clásicos.

Break de 15 minutos.

Cuando volvamos: **Métodos Ágiles**."

---

## ☕ BREAK - 15 MINUTOS

**Instrucciones para el facilitador:**

Antes del break, decir:

"OK, 15 minutos de break.

Cuando volvamos: **Estimación Ágil**.

Vamos a ver por qué Agile dice 'NO estimen en horas, estimen en Story Points'.

Y vamos a hacer un caso COMPLETO de Planning Poker.

Van a ver cómo el proceso expone suposiciones ocultas y genera alineación.

Es el equivalente del momento 'aha!' del Malvavisco Challenge, pero para software.

Nos vemos en 15."

---

## 🎯 POST-BREAK: Estimación Ágil (80 minutos)

---

## Slide 8: Introducción a Estimación Ágil (8 min)

"Bienvenidos de vuelta.

[PAUSA]

Primera mitad: PERT y CPM. Métodos de los años 50-60. Militares, NASA, construcción.

Segunda mitad: **Estimación Ágil**. Años 2000. Software, equipos auto-organizados.

[ÉNFASIS]

El cambio de paradigma:

**PERT/CPM dicen:** 'Estimá en horas o días (tiempo absoluto).'

**Ágil dice:** 'Estimá en Story Points (complejidad relativa).'

[PAUSA - pregunta retórica]

¿Por qué?

[EXPLICAR]

**Problema de estimar en horas:**

Pregunta: '¿Cuántas horas toma implementar login básico?'

Respuestas:
- Dev Junior: 16 horas (nunca lo hizo)
- Dev Senior: 4 horas (lo hizo 20 veces)
- Dev que no sabe React: 12 horas (conoce backend, no frontend)

¿Quién tiene razón?

[PAUSA]

**Todos tienen razón**. Para su nivel de experiencia.

Estimar en horas **mezcla** dos cosas:
1. Complejidad de la tarea
2. Velocidad del ejecutor

[ANALOGÍA]

Pregunta: '¿Cuánto tardás en correr 5 km?'

- Atleta: 18 minutos
- Persona promedio: 35 minutos
- Sedentario: 50 minutos

La **distancia** (5 km) es fija.
El **tiempo** depende de quién corre.

[APLICAR a software]

**Story Points separan complejidad de velocidad:**

- **Complejidad (Story Points):** 'Login básico es 3 puntos' (relativo a baseline)
- **Velocidad (Velocity):** 'Este equipo hace 25 puntos por sprint' (empírico)

[BENEFICIOS]

✅ **Estabilidad:** Complejidad de 'login' no cambia si cambia el equipo.
✅ **No culpa:** No decimos 'tardaste 8 horas cuando estimaste 4'. Decimos 'el equipo hizo 20 puntos este sprint, históricamente hace 25'.
✅ **Colaboración:** Equipo estima junto (no PM solo).
✅ **Honestidad:** Reconoce que NO sabemos exacto.

[PREGUNTA obvia]

'OK, pero al final el stakeholder quiere **FECHA**. ¿Cómo convertís Story Points a calendario?'

[RESPUESTA]

Con **Velocidad**.

Después de 3-5 sprints, medís cuántos puntos el equipo completa por sprint.

Eso te da forecast empírico.

[EJEMPLO]

- Backlog: 120 Story Points
- Velocidad del equipo: 25 puntos/sprint
- Forecast: 120/25 ≈ 5 sprints
- Si sprints son 2 semanas → **10 semanas**

[ÉNFASIS]

Basado en **datos reales**, no adivinanzas.

[TRANSICIÓN]

Veamos los Story Points en detalle..."

---

## Slide 9: Story Points y Escala Fibonacci (12 min)

"Story Points. Unidad de **complejidad relativa**.

[EXPLICAR concepto]

No son horas. No son días. Son **puntos comparativos**.

[ANALOGÍA]

Imaginen que tienen que estimar cuánto tarda hacer 3 comidas:

- Comida A: Huevos revueltos
- Comida B: Pasta con salsa
- Comida C: Paella valenciana completa

[PREGUNTA]

'¿Cuántos minutos tarda cada una?'

Difícil. Depende de quién cocina.

[MEJOR PREGUNTA]

'Si Huevos Revueltos es 1 punto (baseline), ¿cuántos puntos son Pasta y Paella?'

Respuestas intuitivas:
- Huevos: **1**
- Pasta: **3** (3 veces más compleja)
- Paella: **13** (mucho más compleja, muchos ingredientes, timing crítico)

[PAUSA]

Eso es Story Points. **Relativo**, no absoluto.

[ESCALA FIBONACCI]

En Ágil se usa la secuencia de Fibonacci:

**0, 1, 2, 3, 5, 8, 13, 21, 34, ...**

¿Por qué esta secuencia tan rara?

[EXPLICAR]

**Razón 1: Incertidumbre crece no-linealmente.**

Diferencia entre 3 y 4 horas: precisa, medible.
Diferencia entre 13 y 14 días: irrelevante, ambos son 'largo y riesgoso'.

Fibonacci **agrupa** estimaciones en buckets: 1, 2, 3, 5, 8, 13.

No hay 4. No hay 6. No hay 7.

Eso **previene falsa precisión**.

**Razón 2: Fibonacci fuerza discusión.**

Si alguien dice 'esta tarea es 4' y no existe 4, tiene que elegir: ¿3 o 5?

Eso genera debate → suposiciones salen a la luz.

**Razón 3: Refleja Cono de Incertidumbre.**

- Tarea 1-2 pts: muy bien entendida (±25%)
- Tarea 8-13 pts: poca claridad (±100%+)
- Tarea 21+ pts: épica, hay que dividir

[ESCALA completa]

**0:** Trivial (cambiar un texto, arreglar typo)
**1:** Muy simple (agregar campo a form, test unitario)
**2:** Simple (endpoint CRUD básico)
**3:** Baseline (feature simple end-to-end) ← ELEGIR ESTO COMO REFERENCIA
**5:** Moderadamente complejo (feature con lógica de negocio)
**8:** Complejo (integración con sistema externo, refactor)
**13:** Muy complejo (módulo completo, alta incertidumbre)
**21:** Épica (dividir en historias más chicas)
**?:** No sé (necesito investigar primero)
**∞:** Demasiado grande (imposible estimar, dividir)

[ÉNFASIS - Baseline]

**Clave: el equipo debe elegir una historia 'estándar' de 3 puntos.**

Todas las demás estimaciones son **relativas a esa baseline**.

Ejemplo:
- Baseline: 'CRUD completo con validaciones' = 3 pts
- Historia nueva: '¿Es más simple, igual, o más complejo que el CRUD?'

[PAUSA]

Si todos usan la MISMA baseline, las estimaciones se alinean.

[EVITAR]

❌ NO convertir puntos a horas ('1 pt = 2 horas')
❌ NO comparar velocidades entre equipos ('Equipo A hace 40 pts, B hace 25')
❌ NO cambiar baseline mid-proyecto (genera inconsistencia)

[TRANSICIÓN]

Ahora, ¿cómo el equipo decide cuántos puntos asignar?

Ahí entra **Planning Poker**."

---

## Slide 10: T-Shirt Sizing (10 min)

"Antes de Planning Poker, una variante más simple: **T-Shirt Sizing**.

[CONCEPTO]

En vez de números (1, 2, 3, 5...), usás tallas de remera:

**XS, S, M, L, XL, XXL**

[POR QUÉ]

T-Shirt Sizing es más **intuitivo** para equipos nuevos o stakeholders no-técnicos.

'Esta feature es L (grande)' es más fácil de entender que 'esta feature es 13 puntos'.

[CUÁNDO USAR]

**Situación 1: Estimación burda de backlog grande**

Tenés 100 historias en backlog.

NO necesitás precisión. Necesitás orden de magnitud.

Proceso:
- Stakeholders o PM asignan: XS, S, M, L, XL
- Historias L y XL se dividen después
- Historias XS, S, M se refinan cuando estén cerca

**Situación 2: Introducir Ágil a organización tradicional**

Cliente acostumbrado a horas/días.

Story Points suenan abstractos.

T-Shirt es puente:
- 'Esta feature es M (mediana), como el módulo de reportes que hicimos'
- Cliente entiende comparación, aunque no entienda 'puntos'

**Situación 3: Discovery / Inception**

Primeras sesiones con cliente.

NO sabemos suficiente para estimar con Fibonacci.

T-Shirt permite clasificar sin falsa precisión.

[MAPEO aproximado]

| T-Shirt | Fibonacci | Descripción |
|---------|-----------|-------------|
| XS | 1 | Trivial |
| S | 2-3 | Simple |
| M | 5 | Moderada |
| L | 8-13 | Grande |
| XL | 21+ | Épica |
| XXL | ∞ | Demasiado grande, dividir |

[PROCESO]

**Paso 1:** Elegir historia 'M' como baseline (igual que Fibonacci 3).

**Paso 2:** Para cada historia, comparar: '¿Es más chica (S), igual (M), o más grande (L) que baseline?'

**Paso 3:** Historias L y XL se marcan para dividir.

[EJEMPLO práctico]

Backlog de e-commerce:

| Historia | T-Shirt | Razón |
|----------|---------|-------|
| Agregar botón 'favoritos' | XS | Cambio UI simple |
| Registro de usuario | S | Form + validaciones + email |
| Checkout | L | Muchos pasos, integraciones |
| Recomendaciones con ML | XXL | Épica, dividir |
| Dashboard admin | L | Muchas pantallas |

[LUEGO refinar]

Las top 15 historias (las que entrarán pronto en sprint) se re-estiman con Fibonacci.

Proceso:
- S → 2 o 3 pts
- M → 5 pts
- L → 8 o 13 pts (o dividir en 2 M)

[EJEMPLO de refinamiento]

**Historia:** 'Checkout' (L)

**Al refinar:**
- Paso 1: Ingresar dirección → 3 pts
- Paso 2: Elegir método de pago → 5 pts
- Paso 3: Revisar orden → 2 pts
- Paso 4: Confirmar y email → 3 pts

Total: 13 pts (coincide con L).

O dividís en 2 historias: Pasos 1-2 (8 pts) y Pasos 3-4 (5 pts).

[VENTAJAS de T-Shirt]

✅ Rápido (sprint de 50 historias en 30 min)
✅ Intuitivo (todos entienden tallas)
✅ Previene parálisis por análisis

[DESVENTAJAS]

❌ Menos preciso que Fibonacci
❌ NO sirve para Sprint Planning (necesitás números para calcular capacidad)
❌ Puede ser ambiguo ('¿Esto es M grande o L chico?')

[COMBINACIÓN típica]

**Paso 1:** Toda el backlog con T-Shirt Sizing (burdo, rápido)

**Paso 2:** Historias top 15 con Planning Poker (Fibonacci, preciso)

**Paso 3:** En Sprint Planning, las top 15 historias se estiman con Fibonacci

**Resultado:**
- Backlog organizado por tamaño
- Top historias con puntos precisos
- Historias lejanas con estimación burda (está OK, se refinarán después)

[CONECTAR con Refinamiento Progresivo]

Esto conecta con un concepto que veremos después: **Refinamiento Progresivo**.

NO necesitas estimar TODO el backlog con precisión.
Solo lo que vas a trabajar PRONTO.

El resto puede ser T-Shirt o incluso 'Epic - grande' sin más detalle.

[TRANSICIÓN]

OK, ahora que sabemos la TEORÍA (puntos, Fibonacci, T-Shirt)...

¿Cómo el EQUIPO decide cuántos puntos asignar?

Ahí entra **Planning Poker**."

---

## Slide 11: Planning Poker - Marco Teórico (12 min)

"Bienvenidos de vuelta.

Ahora: **Planning Poker**.

[PAUSA]

Primero: ¿QUÉ es?

Planning Poker es una técnica **colaborativa** de estimación donde:

1. Todo el equipo participa
2. Cada persona vota simultáneamente
3. Se revelan extremos
4. Se debate hasta consenso

[VER ELEMENTOS en slide]

**Elementos:**

**Cartas Fibonacci:**
- Cada participante tiene mazo con: 1, 2, 3, 5, 8, 13, 21, ?, ∞
- Votan en secreto (sin influenciarse)
- Revelan simultáneamente

**Roles:**
- **Product Owner:** Lee historia, responde preguntas de negocio
- **Dev Team:** Estiman, debaten técnica
- **Scrum Master:** Facilita, cronometra, busca consenso
- **Todos votan** (excepto PO en algunos equipos)

**Proceso (5 pasos):**

1. **Leer historia**
   - PO lee User Story en voz alta
   - Criterios de aceptación
   - Contexto necesario

2. **Aclarar dudas**
   - Equipo pregunta
   - PO responde
   - Arquitecto aporta contexto técnico

3. **Votar en silencio**
   - Cada uno elige carta
   - Boca abajo (sin ver otros)
   - Todos revelan simultáneamente

4. **Discutir extremos**
   - Persona con voto MÁS BAJO explica
   - Persona con voto MÁS ALTO explica
   - (NO promedian, NO negocian aún)

5. **Re-votar hasta consenso**
   - Segunda ronda de votación
   - Usualmente converge
   - A veces 3ra ronda
   - Consenso = todos ±1 punto (5-8 OK, 3-13 NO)

[ÉNFASIS - LA CLAVE]

**El VALOR de Planning Poker NO está en el número final.**

El valor está en el PASO 4: **Discutir extremos**.

[PAUSA]

¿Por qué alguien dijo 2 y otro dijo 13?

Porque tienen **suposiciones diferentes**:

- Uno asumió API lista, otro asumió escribirla
- Uno pensó 'happy path', otro pensó casos edge
- Uno olvidó testing, otro lo incluyó

**Cuando explican sus votos, las suposiciones salen a la luz.**

[CONECTAR con Clase 1]

¿Recuerdan el Marshmallow Challenge?

MBAs fallaban porque planeaban 17 minutos SIN probar.
Todas sus suposiciones eran incorrectas.

Niños iteraban rápido. Feedback constante.

Planning Poker es **iteración de suposiciones**:
- Primera votación: suposiciones ocultas
- Discusión: suposiciones explícitas
- Segunda votación: suposiciones alineadas

[BENEFICIOS]

**1. Captura conocimiento distribuido:**
   - Tester ve bugs que dev no ve
   - Dev ve complejidad técnica que PO no ve
   - Arquitecto ve acoplamiento

**2. Genera alineación:**
   - Todos entienden la historia igual
   - Mismo nivel de detalle mental
   - Menos sorpresas después

**3. Previene estimaciones anchor:**
   - Si PM dice '8 horas', todos dicen 8
   - Votación secreta evita influencia

**4. Es rápido:**
   - Una historia típica: 3-5 minutos
   - Sprint Planning de 15 historias: 60-90 min
   - Incluye alineación + estimación

[PREPARAR CASO]

Ahora vamos a ver un CASO REAL.

Voy a narrar paso a paso una sesión de Planning Poker.

Van a ver cómo el proceso expone suposiciones.

Mientras lo cuento, PIENSEN ustedes cuántos puntos asignarían.

Al final comparamos."

---

## Slide 12: Caso de Estudio - Backlog de Autenticación (10 min)

"Aquí está nuestro caso: **Sistema de Autenticación**.

[LEER TABLA en pantalla]

Tenemos 5 Historias de Usuario (HU):

**HU-1: Login básico** - Ya estimado: **2 puntos**
**HU-2: Registro de usuarios** - Ya estimado: **3 puntos** ← BASELINE
**HU-3: Password reset** - **SIN ESTIMAR ← Este lo haremos**
**HU-4: OAuth Google** - Sin estimar
**HU-5: Two-Factor Auth (2FA)** - Sin estimar

[CONTEXTO]

El equipo ya completó HU-1 y HU-2 en sprint anterior.

Ahora en Sprint Planning están estimando las siguientes.

**HU-2 es el BASELINE:**

'Registro de usuarios' (form con nombre, email, password, confirmar password, validaciones, endpoint POST /register, hash de password, email confirmación) = **3 puntos**.

[ÉNFASIS]

Todos los miembros del equipo conocen HU-2 a fondo.
Lo completaron hace 5 días.
Tomó ~8 horas reales de trabajo (pero NO decimos 3pts = 8hs).

Es el **punto de comparación** para el resto.

[PAUSA]

Ahora van a estimar **HU-3: Password Reset**.

[LEER HU-3 completa]

**Como** usuario registrado que olvidó su contraseña,
**Quiero** poder resetearla mediante email,
**Para** recuperar acceso a mi cuenta.

**Criterios de Aceptación:**

1. Link 'Olvidé mi contraseña' en página de login
2. Form para ingresar email
3. Sistema envía email con token único temporal
4. Token expira en 1 hora
5. Email contiene link a página de reset
6. Usuario ingresa nueva contraseña (2 veces)
7. Password se actualiza y token se invalida
8. Usuario puede loguearse con nueva password

[PAUSA - Dejar que procesen]

Antes de ver la estimación del equipo...

**Pregunta para ustedes:**

**¿Cuántos puntos asignarían?**

[DAR 30 SEGUNDOS - pedir que escriban en chat o piensen]

Opciones: 1, 2, 3, 5, 8, 13...

Recuerden: HU-2 (Registro) = 3 puntos.

¿Password Reset es más simple, igual, o más complejo que Registro?

[RECOGER RESPUESTAS en chat si es posible]

[Leer algunas respuestas en voz alta]

'Juan dice 5'
'María dice 3'
'Pedro dice 8'

[RISA]

Perfecto. Exactamente lo que pasó en el equipo.

Vamos a ver qué pasó en su sesión de Planning Poker."

---

## Slide 13: Demostración - Historia HU-3 (Password Reset) (15 min)

"OK, momento de la verdad.

El equipo vota por HU-3.

Scrum Master dice: 'Todos listos? 3, 2, 1, revelar!'

[PAUSA DRAMÁTICA]

Los votos:

- **Ana (Dev Backend):** 2
- **Carlos (Dev Frontend):** 3
- **María (Tester QA):** 5
- **Pedro (Dev Fullstack):** 13
- **Laura (Arquitecta):** 8

[VER GRÁFICO en slide con las cartas]

[REACCIÓN]

ENORME dispersión: **2 a 13**.

Diferencia de **6.5x** entre extremos.

[PAUSA]

Scrum Master: 'OK, tenemos que hablar. Ana, empecemos contigo. ¿Por qué 2?'

---

**Ana (Dev Backend - votó 2):**

'Bueno, es bastante directo.

Yo lo comparo con HU-2 (Registro), que fue 3 puntos.

Password Reset es MÁS SIMPLE porque:

1. **Ya tenemos infraestructura de email** (la usamos para confirmación en HU-2)
2. **Ya sabemos hash passwords** (hicimos en HU-1 y HU-2)
3. **El form es más simple** (solo email, después solo 2 campos de password)
4. **No hay validaciones complejas** (solo email válido y password match)

Entonces, menos complejo que HU-2 (3 pts) → le pongo **2 puntos**.'

[PAUSA]

**Scrum Master:** 'OK, gracias Ana. Pedro, ahora vos. ¿Por qué 13?'

---

**Pedro (Dev Fullstack - votó 13):**

[Suspira]

'Yo veo MUCHA complejidad que Ana no mencionó.

**1. Seguridad:**

El token tiene que ser:
- Criptográficamente seguro (no un simple random())
- Único (check en DB que no existe)
- Temporal (expira en 1 hora)
- Invalidado después de uso (no reusable)

Eso es una **tabla nueva** en DB: `password_reset_tokens`.

**2. Email:**

Ana dice 'ya tenemos email'. Sí, para CONFIRMACIÓN (un template simple).

Pero reset password es diferente:
- Necesitamos OTRO template
- Con link que incluye token
- Link a página que NO existe aún (form de reset)

**3. Página nueva de reset:**

No es modificar login, es página NUEVA:
- Route /reset-password/:token
- Validar token (existe? expiró? ya se usó?)
- Form con UX específica
- Manejo de errores (token inválido, expirado, etc.)

**4. Testing:**

María (tester) votó 5, así que ella también ve complejidad.

Hay que testear:
- Happy path
- Token expirado (¿cómo simulo paso de 1 hora?)
- Token ya usado
- Token inexistente
- Email inexistente
- Passwords que no matchean

**5. Edge cases:**

- ¿Qué pasa si pido reset 5 veces? ¿5 emails con 5 tokens?
- ¿O invalido el anterior?
- ¿Hay rate limiting? (prevenir abuse)
- ¿Logging de intentos de reset? (auditoría de seguridad)

[ÉNFASIS]

Por todo eso, le pongo **13 puntos**.

De hecho, casi le pongo '?' porque hay incertidumbre en seguridad.'

[PAUSA LARGA]

---

**Scrum Master:** 'Guau. OK. Ana, ¿qué pensás de lo que dijo Pedro?'

---

**Ana:** 'Uh... tenés razón en varias cosas.

Yo asumí que:
- Tabla de tokens ya existía (no sé por qué asumí eso)
- Template de email era trivial (pero el link con token sí complica)
- Página de reset la podíamos hacer en login route (pero tenés razón, necesita route separada)

No pensé en rate limiting ni en abuse.

Ni en logging.

[PAUSA]

Cambio mi voto. No es 2, es más bien... ¿5? ¿Tal vez 8?'

---

**Scrum Master:** 'OK. María (tester), vos votaste 5. ¿Por qué?'

---

**María (Tester QA - votó 5):**

'Yo pensé en testing.

HU-2 (Registro) fue 3 puntos, y el testing fue ~20% del esfuerzo.

Password Reset tiene MÁS casos edge:
- Expiración
- Tokens inválidos
- Rate limiting (si lo hacemos)

Pero tampoco es 13. Es más complejo que Registro (3), pero no 4 veces más.

Le puse **5**: moderadamente más complejo.'

---

**Scrum Master:** 'Laura (arquitecta), vos votaste 8. ¿Tu perspectiva?'

---

**Laura (Arquitecta - votó 8):**

'Yo agregué la perspectiva de diseño.

Pedro tiene razón en complejidad técnica.
Ana tiene razón en que tenemos piezas.

**Mi análisis:**

**Complejidad TÉCNICA:** Alta (token, seguridad, tabla nueva) → 8-13
**Complejidad de NEGOCIO:** Baja (flujo claro, bien definido) → 3
**Riesgo de CAMBIOS:** Bajo (Password reset es standard, no va a cambiar) → 2

Promedio mental: **8 puntos**.

Pero además...

[PAUSA]

Creo que deberíamos dividir esta historia.

**Split en 2:**

**HU-3a: Password Reset - Happy Path** (5 pts)
- Token generation
- Email con link
- Form de reset
- Actualizar password
- Testing básico

**HU-3b: Password Reset - Seguridad Hardening** (3 pts)
- Rate limiting
- Token expiration enforcement
- Logging/auditoría
- Abuse prevention
- Testing edge cases

**Total: 8 pts, pero dividido para entregar valor incremental.'**

---

**Scrum Master:** 'Interesante. Carlos (frontend), vos votaste 3. ¿Cómo llegaste a ese número?'

---

**Carlos (Dev Frontend - votó 3):**

'Yo solo pensé en el frontend.

Form de email + Form de nueva password = 2 componentes React simples.
Igual de complejo que form de Registro (HU-2).

Por eso 3.

[PAUSA]

Pero escuchando a Pedro y Laura... claramente me faltó ver backend y seguridad.

Cambio a 5 o 8.'

---

**Scrum Master:** 'OK, resumen:

**Votos originales:**
- Ana: 2 → cambió a 5-8
- Carlos: 3 → cambió a 5-8
- María: 5 → mantiene
- Laura: 8 → propone split
- Pedro: 13 → considera bajar

**Opción 1:** Estimamos 8 pts y hacemos completo.
**Opción 2:** Split en 5 pts + 3 pts (propuesta de Laura).

¿Qué prefiere el equipo?'

[PAUSA]

**Product Owner interviene:**

'Me gusta el split. Prefiero tener Password Reset básico funcionando en este sprint, y hardening en el siguiente si hay tiempo.'

**Equipo acuerda:**

**HU-3a: 5 puntos (Sprint actual)**
**HU-3b: 3 puntos (Backlog, para después)**

[FIN DE LA HISTORIA]

---

**Debrief para la clase:**

'¿Qué acabamos de ver?

[PAUSA - Esperar respuestas]

**1. Extremos revelaron suposiciones:**
   - Ana asumió infraestructura lista → voto bajo
   - Pedro vio complejidad oculta → voto alto
   - Discusión expuso AMBAS perspectivas

**2. Conocimiento distribuido se capturó:**
   - Backend (Ana): infraestructura de email
   - Fullstack (Pedro): seguridad, edge cases
   - Tester (María): complejidad de testing
   - Arquitecta (Laura): propuesta de split
   - Frontend (Carlos): subestimó backend

**3. Resultado NO fue promedio:**
   - (2+3+5+13+8)/5 = 6.2 → ¿6 pts?
   - NO. Decidieron **split** en 5+3
   - Más inteligente que promedio ciego

**4. Historia mejoró:**
   - Antes: 'Password Reset' (vaga)
   - Después: 2 historias con alcances claros
   - Entregable incremental

**5. Alineación:**
   - Todos ahora entienden la complejidad
   - Menos sorpresas en implementación
   - Expectativas realistas

[CONECTAR con Clase 1]

Esto ES el Malvavisco Challenge en versión software.

Los niños probaban el malvavisco ANTES de construir.
Planning Poker 'prueba' las suposiciones ANTES de codear.

Evita el colapso de la torre de espaguetis.'"

---

## Slide 14: Velocidad - Concepto y Cálculo (10 min)

"Ahora tenemos historias estimadas en Story Points.

Pero el stakeholder pregunta: **'¿Cuándo estará listo?'**

Story Points NO responden eso directamente.

Ahí entra **Velocidad**.

[DEFINICIÓN]

**Velocidad:**
Cantidad de Story Points que el equipo completa por sprint.

[ÉNFASIS]

Velocidad es **EMPÍRICA**, no estimada:

- NO adivinamos '¿Cuántos puntos haremos?'
- MEDIMOS '¿Cuántos puntos HICIMOS?'
- Después de 3-5 sprints, se ESTABILIZA
- Usamos promedio para forecast

[EJEMPLO]

**Equipo Alfa - Sprints de 2 semanas:**

| Sprint | Puntos Comprometidos | Puntos Completados |
|--------|----------------------|--------------------|
| 1 | 25 | 18 |
| 2 | 20 | 20 |
| 3 | 25 | 22 |
| 4 | 25 | 26 |
| 5 | 28 | 27 |

**Velocidad promedio:** (18+20+22+26+27) / 5 = **22.6 ≈ 23 pts/sprint**

[VER GRÁFICO en slide - Velocidad estabilizándose]

**Sprint 1:** Caos (equipo formándose, estimaciones mal calibradas) → 18 pts

**Sprints 2-3:** Ajuste (mejoran estimaciones) → 20-22 pts

**Sprints 4-5:** Estable (ya conocen su capacidad) → 26-27 pts

**A partir de Sprint 6:** Usar ~25 pts como capacidad esperada.

[FACTORES que afectan Velocidad]

**Aumentan velocidad:**
- ✅ Equipo se conoce mejor
- ✅ Menos dependencias externas
- ✅ Tecnología familiar
- ✅ Backlog bien refinado
- ✅ Menos interrupciones

**Disminuyen velocidad:**
- ❌ Miembro del equipo sale (vacaciones, renuncia)
- ❌ Tecnología nueva
- ❌ Deuda técnica acumulada
- ❌ Interrupciones (producción, reuniones)
- ❌ Cambios de alcance mid-sprint

[ÉNFASIS CRÍTICO]

**Velocidad es POR EQUIPO, no universal:**

- Equipo A: 25 pts/sprint
- Equipo B: 40 pts/sprint

¿Equipo B es 'mejor'? **NO.**

Story Points son RELATIVOS a cada equipo:
- Equipo A tal vez es más conservador estimando
- Equipo B tal vez usa baseline diferente

**NO se pueden comparar velocidades entre equipos.**

[CÁLCULO en detalle]

**¿Qué contar?**

✅ **Contar:** Historias 100% completadas (Done según DoD)
❌ **NO contar:** Historias 90% completadas
❌ **NO contar:** Tareas técnicas no estimadas
❌ **NO contar:** Bugs (algunos equipos sí, otros no - definir política)

**Ejemplo:**

Sprint 5:
- HU-12: 5 pts → ✅ Done
- HU-13: 8 pts → ✅ Done
- HU-14: 13 pts → ❌ 80% completa (NO cuenta)
- HU-15: 3 pts → ✅ Done
- Bug fix: ❌ Sin puntos (no cuenta)

**Velocidad Sprint 5:** 5 + 8 + 3 = **16 pts**

[PAUSA]

¿Por qué HU-14 NO cuenta aunque está 80% hecha?

Porque Ágil valora **software funcionando**.

80% NO es funcionando. Es 0% de valor entregado.

Esto evita 'gaming' del sistema:
- NO dividir historia al final para 'contar puntos'
- Incentiva terminar pocas cosas bien vs muchas cosas a medias

[TRANSICIÓN]

OK, tenemos Velocidad.

¿Cómo la usamos para forecasting?"

---

## Slide 15: Forecasting con Velocidad (7 min)

"Ahora sí, respondemos la pregunta del stakeholder:

**'¿Cuándo estará listo?'**

[FÓRMULA simple]

**Forecast = Total Story Points / Velocidad**

**Ejemplo:**

Backlog del Feature X:
- 15 historias estimadas
- Total: **120 Story Points**

Velocidad del equipo:
- Promedio últimos 5 sprints: **25 pts/sprint**

**Forecast:**

120 pts / 25 pts/sprint = **4.8 sprints ≈ 5 sprints**

Si sprints son 2 semanas → **10 semanas**

[VER GRÁFICO en slide - Timeline con velocidad]

**Sprint 6:** 25 pts → Quedan 95
**Sprint 7:** 25 pts → Quedan 70
**Sprint 8:** 25 pts → Quedan 45
**Sprint 9:** 25 pts → Quedan 20
**Sprint 10:** 20 pts → ✅ Done

[PERO... incertidumbre]

¿Recuerdan el Cono de Incertidumbre (Clase 1)?

Forecast NO es fecha exacta. Es RANGO.

**Velocidad tiene variación:**

Equipo Alfa:
- Sprint 1: 18 pts
- Sprint 2: 20 pts
- Sprint 3: 22 pts
- Sprint 4: 26 pts
- Sprint 5: 27 pts

**Promedio:** 22.6 pts
**Desviación estándar:** ±3.5 pts
**Rango:** 19-26 pts

[FORECAST CON RANGO]

Total: 120 pts

**Escenario Optimista (velocidad alta: 26 pts/sprint):**
120 / 26 = 4.6 sprints ≈ **5 sprints (10 semanas)**

**Escenario Esperado (velocidad promedio: 23 pts/sprint):**
120 / 23 = 5.2 sprints ≈ **5-6 sprints (10-12 semanas)**

**Escenario Pesimista (velocidad baja: 19 pts/sprint):**
120 / 19 = 6.3 sprints ≈ **6-7 sprints (12-14 semanas)**

[ÉNFASIS]

**Comunicación honesta al stakeholder:**

❌ **MAL:** 'Estará listo en 10 semanas.'

✅ **BIEN:** 'Basado en velocidad histórica, estimamos 10-12 semanas, con rango de 8-14 semanas.'

[PAUSA]

Esto es HONESTIDAD vs falsa precisión.

¿Recuerdan PERT (inicio de clase)?

- Optimista (O): 8 semanas
- Más probable (M): 11 semanas
- Pesimista (P): 14 semanas
- Esperanza: (8 + 4×11 + 14) / 6 ≈ **11 semanas**

Forecast con Velocidad es similar:
- Basado en DATOS REALES (no adivinar)
- Con RANGO de incertidumbre (no número falso)

[TRANSICIÓN]

OK, vimos Planning Poker + Velocidad.

Cerremos con comparación y síntesis..."

---

## Slide 16: Cuadro Comparativo - PERT vs Ágil vs CCPM (8 min)

"Momento de síntesis.

Vimos 3 enfoques hoy:

1. **PERT / CPM** (clásicos, años 50-60)
2. **Ágil** (Scrum, Planning Poker, años 2000)
3. **CCPM** (lo veremos Clase 3, pero preview ahora)

[VER TABLA COMPARATIVA en slide]

Voy a leer fila por fila:

---

**Fila: Unidad de estimación**

- **PERT:** Horas o días (tiempo absoluto)
- **Ágil:** Story Points (complejidad relativa)
- **CCPM:** Días/horas pero con buffers agregados

---

**Fila: Quién estima**

- **PERT:** PM o especialista (individual)
- **Ágil:** Equipo completo (colaborativo)
- **CCPM:** Equipo + PM (híbrido)

---

**Fila: Técnica**

- **PERT:** 3 puntos (O-M-P), fórmula estadística
- **Ágil:** Planning Poker, Fibonacci, consenso
- **CCPM:** 50% de estimación + buffers agregados

---

**Fila: Gestión de incertidumbre**

- **PERT:** Varianza distribuida en cada tarea
- **Ágil:** Velocidad empírica + refinamiento progresivo
- **CCPM:** Buffers centralizados (proyecto, feeding, resource)

---

**Fila: Adaptación a cambios**

- **PERT:** Baja (plan fijo, re-planificar costoso)
- **Ágil:** Alta (re-priorización cada sprint)
- **CCPM:** Media (plan fijo pero buffers absorben variación)

---

**Fila: Cuándo usar**

**PERT:**
- Proyecto con fases claramente definidas
- Poca incertidumbre técnica
- Regulatorio (construcción, farmacéutica)

**Ágil:**
- Alta incertidumbre de requisitos
- Necesidad de feedback temprano
- Equipos auto-organizados
- Software con iteraciones cortas

**CCPM:**
- Múltiples proyectos paralelos
- Recursos compartidos entre proyectos
- Cuellos de botella críticos
- Necesidad de entregar MÁS RÁPIDO (acortar timelines)

---

[PAUSA]

**Pregunta clave:**

**'¿Cuál es MEJOR?'**

[Esperar respuestas]

**Respuesta: DEPENDE del contexto.**

No hay 'bala de plata'.

[PREVIEW Clase 3]

**En Clase 3 veremos:**

**CCPM (Critical Chain Project Management)**

La idea central:

**NO gestionar incertidumbre tarea por tarea.**

**Gestionar incertidumbre CENTRALIZADAMENTE con buffers agregados.**

[ANTICIPAR]

**Clase 3 responderá:**

1. ¿Cómo identificar Cadena Crítica (≠ Ruta Crítica)?
2. ¿Cómo dimensionar buffers (proyecto, feeding, resource)?
3. ¿Cómo monitorear con Fever Chart?
4. ¿Cómo gestionar cartera de múltiples proyectos?

[TRANSICIÓN]

Clase 2 casi completa.

Síntesis final..."

---

## Slide 17: Síntesis de Clase 2 (5 min)

"OK, sinteticemos Clase 2.

**¿Qué vimos?**

---

**PARTE 1: Métodos Clásicos (50 min)**

**PERT:**
- 3 puntos (O-M-P)
- μ = (O + 4M + P) / 6
- Reconoce incertidumbre con varianza
- Problema: varianzas se suman, proyectos se alargan

**CPM:**
- Ruta Crítica: secuencia más larga
- Tareas en ruta crítica NO tienen holgura
- Optimizar ruta crítica acorta proyecto
- Problema: ignora recursos (asume infinitos)

---

**PARTE 2: Estimación Ágil (80 min)**

**Story Points:**
- Unidad relativa de complejidad (NO horas)
- Fibonacci: 1, 2, 3, 5, 8, 13, 21
- T-Shirt Sizing: XS, S, M, L, XL

**Planning Poker:**
- Técnica colaborativa
- Todos votan simultáneamente
- Extremos explican → suposiciones salen a la luz
- Convergen a consenso

**Velocidad:**
- Puntos completados por sprint
- Empírica (medida, no estimada)
- Se estabiliza después de 3-5 sprints
- Forecast = Total pts / Velocidad

---

**Mensajes Clave de Clase 2:**

**1. NO existe 'la mejor técnica'**
- Contexto determina método apropiado

**2. Colaboración > Individual**
- Planning Poker captura conocimiento distribuido
- Extremos revelan suposiciones

**3. Empírico > Teórico**
- Velocidad basada en datos reales
- Forecast se ajusta con feedback

**4. Honestidad > Precisión falsa**
- Rangos de incertidumbre explícitos
- Story Points reconocen que NO sabemos exacto

---

**Conexión con Clase 1:**

**Clase 1 diagnosticó el problema:**
- Estimaciones fallan sistemáticamente
- Cono de Incertidumbre: ±400% al inicio
- Factores psicológicos (Parkinson, Estudiante)
- Malvavisco Challenge: probar suposiciones temprano

**Clase 2 presentó herramientas:**
- PERT: reconocer incertidumbre con 3 puntos
- Ágil: iteración corta + feedback empírico
- Planning Poker: exponer suposiciones ANTES de construir

---

**Setup para Clase 3:**

**Pregunta pendiente:**

'¿Y si el problema NO es estimar mejor...
...sino GESTIONAR la incertidumbre?'

**CCPM (Critical Chain) propone:**

1. **Aceptar** que estimaciones individuales son malas
2. **Quitar** colchones individuales (previene Parkinson)
3. **Agregar** buffers centralizados (protege entrega)
4. **Monitorear** consumo de buffer (Fever Chart)

**Resultado:**
- Timelines 20-30% más cortos
- Sin agregar recursos
- Mayor % de proyectos on-time

[ÉNFASIS]

Clase 3 es el **cambio de paradigma**:

De 'estimar cada tarea perfectamente'
A 'proteger el proyecto como sistema'

---

**Nos vemos en Clase 3."**

---

## Slide 18: Cierre y Preview Clase 3 (3 min)

"Excelente trabajo hoy.

**Clase 2 completada.**

---

**Recap:**

✅ Vimos 3 enfoques de estimación
✅ Profundizamos en Planning Poker (el core)
✅ Entendimos Velocidad y Forecasting
✅ Comparamos métodos según contexto

---

**Próxima clase (Clase 3):**

**Título:** Cadena Crítica y Gestión de Buffers

**Contenido:**

1. **Teoría de Restricciones (TOC):** Base conceptual
2. **Cadena Crítica vs Ruta Crítica:** Diferencias clave
3. **Tipos de Buffers:** Proyecto, Feeding, Resource
4. **Caso A-B-C-D:** Walkthrough completo (el momento 'aha!')
5. **Fever Chart:** Monitoreo visual
6. **Cartera de Proyectos:** Gestión multi-proyecto

**Duración:** 3 horas

**Formato:** Remoto / Teórico con caso detallado

---

**Por qué NO perderse Clase 3:**

**CCPM es el método que MENOS gente conoce...**
**...pero el que MÁS impacto tiene en timelines reales.**

Verán:
- Cómo 4 tareas de 10 días c/u NO toman 40 días
- Cómo quitar 'colchones' individuales ACELERA proyectos
- Cómo buffer al final PROTEGE mejor que buffers distribuidos

**Es contra-intuitivo.**

Y por eso funciona.

---

**¡Nos vemos en Clase 3!**

**Preguntas finales antes de cerrar?"**

---

## 🎯 FIN DE SPEECH SCRIPTS - CLASE 2 COMPLETA

---

**Total Clase 2:** 18 slides + break
**Duración:** 180 minutos (3 horas)
**Estructura:**
- Portada y Agenda: 5 min
- PERT/CPM: 50 min
- Break: 15 min
- Ágil/Planning Poker: 80 min
- Comparación y Cierre: 30 min

---

**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 2.0 - Formato Remoto
**Fecha:** Enero 2025
