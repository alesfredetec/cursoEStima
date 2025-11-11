# Material de Estudio - Clase 2: Métodos de Estimación

**Curso:** Estimación de Proyectos
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Duración:** 3 horas
**Versión:** 2.0 - Formato Remoto - Enero 2025

---

## 📋 Índice

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
3. [PERT: Estimación de 3 Puntos](#pert-estimación-de-3-puntos)
4. [CPM: Método del Camino Crítico](#cpm-método-del-camino-crítico)
5. [Estimación Ágil](#estimación-ágil)
6. [Planning Poker](#planning-poker)
7. [Velocidad y Forecasting](#velocidad-y-forecasting)
8. [Refinamiento Progresivo](#refinamiento-progresivo)
9. [Cuadro Comparativo de Métodos](#cuadro-comparativo-de-métodos)
10. [Ejercicios Prácticos](#ejercicios-prácticos)
11. [Preguntas de Autoevaluación](#preguntas-de-autoevaluación)

---

## 📝 Resumen Ejecutivo

### ¿De qué trata esta clase?

La Clase 2 presenta **herramientas y técnicas** para mejorar la estimación en proyectos.

**Pregunta central:** ¿Cómo estimamos mejor?

**Respuesta:** Usando el método apropiado según el contexto:

- **PERT:** Para proyectos con fases claramente definidas (reconoce incertidumbre con 3 puntos)
- **CPM:** Para identificar la ruta crítica (secuencia más larga de tareas)
- **Ágil:** Para proyectos con alta incertidumbre de requisitos (iteración + feedback empírico)

### Mensaje principal

**NO existe "el mejor método".**

El **contexto** determina qué método usar:
- Proyectos predecibles → PERT/CPM
- Proyectos con requisitos emergentes → Ágil
- Múltiples proyectos con recursos compartidos → CCPM (Clase 3)

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, serás capaz de:

✅ Calcular estimaciones con PERT usando 3 puntos (Optimista, Más Probable, Pesimista)
✅ Identificar la Ruta Crítica en un proyecto usando CPM
✅ Diferenciar Story Points de horas, y explicar por qué puntos son más confiables
✅ Facilitar una sesión de Planning Poker completa
✅ Calcular Velocidad de un equipo ágil
✅ Hacer forecasting basado en velocidad empírica
✅ Aplicar Refinamiento Progresivo para evitar over-planning
✅ Seleccionar el método apropiado según contexto del proyecto

---

## 📐 PERT: Estimación de 3 Puntos

### Origen e Historia

**PERT = Program Evaluation and Review Technique**

**Creado:** 1958
**Por:** US Navy para proyecto Polaris (submarinos con misiles balísticos)
**Contexto:** Proyecto con 3,000 contratistas, altísima incertidumbre

**Problema que resolvía:**
- Métodos tradicionales daban estimaciones puntuales (ej: "6 meses")
- Realidad: alta variabilidad (podía ser 3 meses o 12 meses)
- Necesitaban método que reconociera la incertidumbre explícitamente

### Concepto Central

**PERT reconoce que NO podemos estimar con precisión.**

En lugar de "adivinar un número", usamos **RANGO con 3 puntos:**

1. **Optimista (O):** Escenario donde TODO sale perfecto (~1% probabilidad)
2. **Más probable (M):** Expectativa realista (moda de la distribución)
3. **Pesimista (P):** Murphy ataca, todo sale mal (~99% probabilidad)

### Fórmulas PERT

#### **Estimación Esperada (Media):**

```
μ = (O + 4M + P) / 6
```

**¿Por qué 4M?**
- Porque el valor más probable (M) es MÁS informativo
- Peso 4:1:1 refleja distribución Beta
- M tiene 4x más influencia que O o P

#### **Desviación Estándar:**

```
σ = (P - O) / 6
```

**¿Por qué (P-O)/6?**
- Rango completo (P-O) contiene ~6 desviaciones estándar
- En distribución normal: 99.7% de datos está dentro de ±3σ

#### **Varianza:**

```
σ² = [(P - O) / 6]²
```

**Importante para agregación:** Las varianzas se SUMAN, las desviaciones NO.

### Ejemplo Práctico

**Tarea:** Implementar autenticación con OAuth

**3 Puntos:**
- **Optimista (O):** 3 días (todo funciona a la primera, API bien documentada, sin bugs)
- **Más Probable (M):** 5 días (expectativa realista)
- **Pesimista (P):** 10 días (API con problemas, documentación pobre, bugs de integración)

**Cálculos:**

```
Estimación Esperada:
μ = (3 + 4×5 + 10) / 6
μ = (3 + 20 + 10) / 6
μ = 33 / 6
μ = 5.5 días

Desviación Estándar:
σ = (10 - 3) / 6
σ = 7 / 6
σ = 1.17 días

Varianza:
σ² = 1.17²
σ² = 1.36 días²
```

**Interpretación:**
- Estimación central: **5.5 días**
- Rango de confianza 68%: 5.5 ± 1.17 = **4.3 a 6.7 días**
- Rango de confianza 95%: 5.5 ± 2×1.17 = **3.2 a 7.8 días**

### Agregación de Tareas

**Proyecto con 3 tareas secuenciales:**

| Tarea | O | M | P | μ | σ | σ² |
|-------|---|---|---|---|---|----|
| A | 2 | 3 | 5 | 3.2 | 0.5 | 0.25 |
| B | 4 | 6 | 10 | 6.3 | 1.0 | 1.00 |
| C | 1 | 2 | 4 | 2.2 | 0.5 | 0.25 |

**Agregación:**

```
μ_total = μ_A + μ_B + μ_C
μ_total = 3.2 + 6.3 + 2.2
μ_total = 11.7 días

σ²_total = σ²_A + σ²_B + σ²_C
σ²_total = 0.25 + 1.00 + 0.25
σ²_total = 1.5

σ_total = √1.5
σ_total = 1.22 días
```

**Resultado:**
- Proyecto: **11.7 ± 1.22 días**
- Rango 68%: **10.5 a 13 días**
- Rango 95%: **9.3 a 14.1 días**

### Ventajas y Limitaciones de PERT

#### **✅ Ventajas:**

1. **Reconoce incertidumbre explícitamente** (no finge precisión falsa)
2. **Base estadística sólida** (distribución Beta)
3. **Fácil de explicar** a stakeholders (3 escenarios)
4. **Útil para risk management** (σ indica volatilidad)

#### **❌ Limitaciones:**

1. **Estimaciones iniciales siguen siendo subjetivas** (basura entra, basura sale)
2. **Asume independencia de tareas** (si A falla, puede afectar B)
3. **Varianzas se suman** → proyectos largos tienen MUCHA incertidumbre
4. **No considera recursos limitados** (asume disponibilidad infinita)

---

## 🛤️ CPM: Método del Camino Crítico

### Origen e Historia

**CPM = Critical Path Method**

**Creado:** 1957
**Por:** DuPont y Remington Rand
**Contexto:** Construcción y mantenimiento de plantas químicas

**Diferencia con PERT:**
- PERT: para proyectos con alta incertidumbre (R&D, desarrollo)
- CPM: para proyectos más predecibles (construcción, manufactura)

### Conceptos Clave

#### **1. Ruta Crítica**

**Definición:**
Secuencia de tareas **dependientes** más larga del proyecto.

**Características:**
- Determina la duración MÍNIMA del proyecto
- Tareas en ruta crítica tienen holgura = 0 (no pueden retrasarse)
- Optimizar ruta crítica acorta el proyecto

#### **2. Holgura (Slack/Float)**

**Definición:**
Tiempo que una tarea puede retrasarse sin afectar la fecha de entrega.

**Fórmula:**
```
Holgura = Late Start - Early Start
```

**Tipos:**
- **Holgura = 0:** Tarea crítica (parte de ruta crítica)
- **Holgura > 0:** Tarea no crítica (tiene margen)

### Ejemplo Práctico: Migración de Base de Datos

**Proyecto:** Migrar de MySQL a PostgreSQL

**Tareas:**

| ID | Tarea | Depende de | Duración |
|----|-------|------------|----------|
| A | Análisis de esquema actual | - | 3 días |
| B | Diseño de nuevo esquema | A | 5 días |
| C | Instalación de PostgreSQL | A | 2 días |
| D | Scripts de migración | B | 4 días |
| E | Testing en ambiente dev | C, D | 3 días |
| F | Migración a producción | E | 2 días |

**Diagrama de Red:**

```
         ┌─── B (5d) ─── D (4d) ───┐
        │                          │
A (3d) ─┤                          ├─ E (3d) ─ F (2d)
        │                          │
         └─── C (2d) ──────────────┘
```

**Identificar Rutas:**

**Ruta 1:** A → B → D → E → F
- Duración: 3 + 5 + 4 + 3 + 2 = **17 días**

**Ruta 2:** A → C → E → F
- Duración: 3 + 2 + 3 + 2 = **10 días**

**Ruta Crítica:** Ruta 1 (A-B-D-E-F) = **17 días**

**Holguras:**

- Tarea C:
  - Early Start: día 3 (después de A)
  - Late Start: día 8 (antes de E que empieza día 11)
  - **Holgura: 8 - 3 = 5 días**

### Optimización de la Ruta Crítica

**Estrategias:**

1. **Fast-Tracking (Paralelización):**
   - Hacer tareas en paralelo que normalmente serían secuenciales
   - **Ejemplo:** Empezar D (scripts) antes de que B (diseño) termine al 100%
   - **Riesgo:** Mayor probabilidad de retrabajo

2. **Crashing (Agregar Recursos):**
   - Asignar más gente/recursos a tareas críticas
   - **Ejemplo:** 2 personas en tarea D en vez de 1
   - **Limitación:** Ley de Brooks ("9 mujeres no hacen un bebé en 1 mes")

3. **Reducir Alcance:**
   - Cortar features no esenciales de ruta crítica
   - **Ejemplo:** Migrar solo tablas críticas primero (MVP)

### Limitaciones Críticas de CPM

**⚠️ Problema Principal: CPM ignora RECURSOS**

**Ejemplo del problema:**

```
Proyecto según CPM:

Ruta A: Tarea X (5d) → Tarea Y (3d) = 8 días
Ruta B: Tarea Z (10d) = 10 días

CPM dice: Ruta Crítica = B (10 días)
          Duración del proyecto = 10 días

PERO... si Ana hace X, Y, y Z (recurso único):

Realidad: X (5d) → Y (3d) → Z (10d) = 18 días
          Duración real = 18 días (¡80% más!)
```

**Solución:** CCPM (Critical Chain Project Management) - Clase 3

---

## 🏃 Estimación Ágil

### Cambio de Paradigma

**De Horas/Días → Story Points (Puntos Relativos)**

#### **¿Por qué NO horas?**

**Problemas con estimar en horas:**

1. **Dependen de quién hace la tarea:**
   - Junior: 16 horas
   - Senior: 4 horas
   - **Misma tarea, 4x diferencia**

2. **Varían según contexto:**
   - Día tranquilo: 6 horas
   - Día con interrupciones: 12 horas
   - **Misma tarea, 2x diferencia**

3. **Generan compromiso prematuro:**
   - Cliente escucha "8 horas" → "Es 1 día entonces"
   - Si toma 12 horas → "Fallaste"
   - **Presión artificial**

4. **Fingen precisión:**
   - "8 horas" suena exacto
   - Realidad: puede ser 4-16 horas
   - **Falsa certeza**

#### **¿Por qué Story Points?**

**Story Points = Unidad abstracta de complejidad/esfuerzo**

**Ventajas:**

1. **Relativos, no absolutos:**
   - "Esta tarea es el doble de compleja que aquella"
   - No importa quién la haga

2. **Más estables en el tiempo:**
   - Complejidad de "implementar login" no cambia
   - Horas pueden variar por persona/contexto

3. **Fomentan conversación:**
   - No hay "respuesta correcta"
   - El equipo debe discutir y consensuar

4. **Protegen de compromiso prematuro:**
   - "5 puntos" no se convierte directamente a días
   - Cliente pregunta "¿Y eso cuánto es?"
   - Respuesta: "Según nuestra velocidad, ~1 sprint con ±20% variación"

### Escala de Fibonacci

**¿Por qué 1, 2, 3, 5, 8, 13, 21... y no 1, 2, 3, 4, 5, 6...?**

**Razón 1: Refleja incertidumbre creciente**

```
Tareas pequeñas (1-3 pts):
- Puedo distinguir claramente entre ellas
- 1 pt: Cambiar texto en UI (minutos)
- 2 pts: Agregar validación simple (1-2 horas)
- 3 pts: Endpoint CRUD completo (3-4 horas)

Tareas grandes (13-21 pts):
- Mucha incertidumbre, difícil distinguir
- 13 pts: Sistema completo pequeño
- 21 pts: Sistema completo pequeño + integración compleja
- Diferencia es borrosa
```

**Razón 2: Fuerza honestidad**

No puedes decir "15 puntos". Tienes que elegir:
- ¿Es un 13? (grande pero manejable)
- ¿O es un 21? (épica que deberíamos dividir)

**Escala completa:**

| Puntos | Interpretación | Ejemplos |
|--------|----------------|----------|
| **0** | Trivial | Ya está hecho, o es cambio de configuración |
| **1** | Muy simple | Cambiar texto, corregir typo |
| **2** | Simple | Agregar campo con validación |
| **3** | Pequeño completo | Endpoint CRUD, componente React simple |
| **5** | Moderado | Feature con múltiples componentes |
| **8** | Grande | Sistema pequeño, refactoring significativo |
| **13** | Muy grande | Deberíamos dividir (a menos que sea spike) |
| **21** | Épica | NO es historia, es contenedor de historias |
| **?** | Incertidumbre | No sabemos ni por dónde empezar (hacer spike) |
| **∞** | Imposible | "Reescribir todo de cero" (rechazar) |

### T-Shirt Sizing

**Alternativa más simple para grooming inicial:**

| Talla | Equivalente en Puntos | Uso |
|-------|----------------------|-----|
| **XS** | 1 punto | Backlog distante |
| **S** | 2-3 puntos | Grooming rápido |
| **M** | 5 puntos (baseline) | Referencia |
| **L** | 8 puntos | Considerar dividir |
| **XL** | 13+ puntos | DEBE dividirse |

**Cuándo usar:**
- Backlog grooming inicial (50+ historias por clasificar)
- Roadmap de alto nivel
- Equipo nuevo en Ágil

**Cuándo NO usar:**
- Sprint Planning formal (usar Fibonacci)
- Cuando necesitas velocidad numérica

---

## 🃏 Planning Poker

### Concepto

**Planning Poker = Técnica colaborativa de estimación**

**Creado por:** Mike Cohn, James Grenning (popularizado en 2002)

**Objetivo principal:** NO es el número final, es **exponer suposiciones ocultas**

### Proceso Completo (5 Pasos)

#### **Paso 1: Leer Historia**

Product Owner lee User Story en voz alta:

```
Como [rol]
Quiero [funcionalidad]
Para [beneficio]

Criterios de Aceptación:
1. ...
2. ...
3. ...
```

#### **Paso 2: Aclarar Dudas**

Equipo pregunta, PO responde:
- "¿Incluye validaciones?"
- "¿Qué pasa si el email ya existe?"
- "¿Tiene que funcionar offline?"

**⚠️ Importante:** PO responde preguntas de NEGOCIO, no técnicas.

#### **Paso 3: Votar en Silencio**

Cada miembro:
1. Elige carta (1, 2, 3, 5, 8, 13, 21, ?)
2. La pone boca abajo
3. Todos revelan **simultáneamente**

**¿Por qué simultáneo?**
- Evitar "anchoring bias" (influencia del primero que habla)
- Capturar perspectiva genuina de cada uno

#### **Paso 4: Discutir Extremos** ⭐ **PASO MÁS IMPORTANTE**

**Voto más BAJO explica:**
- "Yo puse 2 porque asumí que la API ya está hecha"

**Voto más ALTO explica:**
- "Yo puse 13 porque asumí que hay que escribir la API desde cero"

**⚡ Momento "Aha!":**
- Las suposiciones ocultas salen a la luz
- Equipo descubre que no todos entienden la historia igual
- Se clarifican ambigüedades

#### **Paso 5: Re-votar Hasta Consenso**

Después de discusión, segunda ronda de votación.

**Usualmente converge:**
- Antes: 2, 5, 5, 13
- Después: 5, 5, 8, 8

**Consenso = todos ±1 punto**

Si no converge después de 2-3 rondas:
- Marcar historia con '?' (hacer spike)
- O splitear historia

### Caso de Estudio: HU-3 Password Reset

**Historia:**
```
Como usuario que olvidó su contraseña,
Quiero poder resetearla mediante email,
Para recuperar acceso a mi cuenta.

Criterios:
1. Link "Olvidé mi contraseña" en login
2. Form para ingresar email
3. Sistema envía email con token temporal
4. Token expira en 1 hora
5. Usuario ingresa nueva contraseña
6. Password se actualiza
```

**Baseline:** HU-2 (Registro de usuarios) = 3 puntos

**Primera votación:**

| Persona | Voto | Rol |
|---------|------|-----|
| Ana | 2 | Dev Backend |
| Carlos | 3 | Dev Frontend |
| María | 5 | Tester |
| Pedro | 13 | Dev Fullstack |
| Laura | 8 | Arquitecta |

**Dispersión:** 2 a 13 (6.5x diferencia)

**Discusión:**

**Ana (2):** "Es más simple que Registro. Ya tenemos infraestructura de email."

**Pedro (13):** "Veo mucha complejidad oculta:
- Tabla nueva (password_reset_tokens)
- Seguridad (token criptográfico, expiración)
- Página nueva (/reset-password/:token)
- Edge cases (token ya usado, expirado, rate limiting)
- Testing complejo"

**Revelación:** Ana asumió que tabla de tokens existía. Pedro vio toda la complejidad real.

**Propuesta de Laura (Arquitecta):** Split en 2 historias:
- HU-3a: Password Reset - Happy Path (5 pts)
- HU-3b: Password Reset - Hardening (3 pts)

**Equipo acuerda:** Split, hacer 3a primero.

### Lecciones del Caso

1. **Extremos revelaron suposiciones** (Ana vs Pedro)
2. **Conocimiento distribuido se capturó** (tester vio casos edge)
3. **NO se promedió** ((2+3+5+13+8)/5 = 6.2 ≈ 6) → Habrían perdido información
4. **Historia mejoró** (split en 2 historias más claras)
5. **Alineación** (todos entienden complejidad ahora)

### Tips para Planning Poker Efectivo

#### **✅ Hacer:**

1. **Establecer baseline clara** (historia de 3 pts que todos conocen)
2. **Votar simultáneamente** (evitar anchoring)
3. **Siempre discutir extremos** (no promediar sin debate)
4. **Timeboxear** (máx 10 min por historia)
5. **Incluir TODO el equipo** (devs, testers, UX, DevOps)

#### **❌ Evitar:**

1. **Volver a convertir a horas** ("5 pts = 1 día") - Destruye el concepto
2. **Permitir que senior domine** - Todos votan igual
3. **Promediar sin discutir** - Pierdes el valor de la técnica
4. **Estimar sin criterios de aceptación** - Ambigüedad infinita
5. **Manipular estimación para que "quepa en sprint"** - Mentirse a uno mismo

---

## 📈 Velocidad y Forecasting

### Concepto de Velocidad

**Velocidad = Story Points completados por sprint**

**Características:**

- ✅ **Empírica** (medida, no estimada)
- ✅ **Por equipo** (no universal, no comparar equipos)
- ✅ **Se estabiliza** después de 3-5 sprints
- ✅ **Permite forecasting**

### Cálculo de Velocidad

**¿Qué contar?**

✅ **SÍ contar:**
- Historias 100% completadas (Done según Definition of Done)

❌ **NO contar:**
- Historias 90% completadas (0% de valor entregado)
- Tareas técnicas sin estimar
- Bugs (depende de política del equipo)

**Ejemplo:**

**Sprint 5:**
- HU-12: 5 pts → ✅ Done
- HU-13: 8 pts → ✅ Done
- HU-14: 13 pts → ❌ 80% completa (NO cuenta)
- HU-15: 3 pts → ✅ Done

**Velocidad Sprint 5:** 5 + 8 + 3 = **16 pts**

### Ejemplo Completo

**Equipo Alfa - Sprints de 2 semanas:**

| Sprint | Comprometidos | Completados | Velocidad |
|--------|---------------|-------------|-----------|
| 1 | 25 | 18 | 18 |
| 2 | 20 | 20 | 20 |
| 3 | 25 | 22 | 22 |
| 4 | 25 | 26 | 26 |
| 5 | 28 | 27 | 27 |

**Velocidad promedio:** (18+20+22+26+27) / 5 = **22.6 ≈ 23 pts/sprint**

### Forecasting con Velocidad

**Backlog del Feature X:**
- 15 historias estimadas
- Total: **120 Story Points**

**Velocidad del equipo:** 23 pts/sprint

**Forecast:**

```
Sprints necesarios = 120 pts / 23 pts/sprint
                   = 5.2 sprints
                   ≈ 5-6 sprints
```

Si sprints son 2 semanas → **10-12 semanas**

### Forecast con Rango de Incertidumbre

**Velocidad histórica:**
- Promedio: 23 pts
- Desviación estándar: ±3 pts
- Rango: 20-26 pts

**Escenarios:**

```
Optimista (velocidad alta: 26 pts/sprint):
120 / 26 = 4.6 sprints ≈ 5 sprints (10 semanas)

Esperado (velocidad promedio: 23 pts/sprint):
120 / 23 = 5.2 sprints ≈ 5-6 sprints (10-12 semanas)

Pesimista (velocidad baja: 20 pts/sprint):
120 / 20 = 6 sprints ≈ 6-7 sprints (12-14 semanas)
```

**Comunicación honesta al stakeholder:**

❌ **Mal:** "Estará listo en 10 semanas."

✅ **Bien:** "Basado en velocidad histórica, estimamos 10-12 semanas, con rango posible de 8-14 semanas."

---

## 🔄 Refinamiento Progresivo

### Concepto

**NO estimar todo el backlog con precisión desde el inicio.**

Solo estimar con detalle lo que vas a trabajar PRONTO.

### Niveles de Detalle

| Horizonte | Nivel de Detalle | Método |
|-----------|------------------|--------|
| **Próximo sprint** | Muy detallado | Planning Poker, Fibonacci, criterios claros |
| **Próximos 2-3 sprints** | Moderado | T-Shirt Sizing, criterios básicos |
| **3-6 meses** | Burdo | Épicas sin dividir, "Grande/Mediana/Pequeña" |
| **6+ meses** | Muy burdo | Ideas, no estimaciones |

### Ejemplo: Backlog de 100 Historias

**Sprint Actual (Sprint 10):**
- 6 historias en progreso (estimadas con Fibonacci)

**Próximos 2 sprints:**
- 20 historias refinadas (Fibonacci detallado)
- Criterios de aceptación completos
- **Tiempo invertido:** 60-90 min de backlog grooming

**Próximos 3-6 meses:**
- 30 historias con T-Shirt Sizing (S/M/L)
- Criterios básicos

**Backlog lejano:**
- 44 épicas sin dividir
- "Grande", "Mediana", "Pequeña"

**Total forecast:**
- Próximos 2 sprints: 50 pts (detallado)
- Resto: ~500 pts (burdo) → ~20 sprints
- **Suficiente para roadmap SIN desperdiciar esfuerzo**

### Ventajas

1. **Evita over-planning** (no estimar cosas que cambiarán)
2. **Ahorra tiempo** (solo detalle donde importa)
3. **Permite adaptación** (requisitos evolucionan)
4. **Reduce desperdicio** (trabajo de estimación tirado)

---

## 📊 Cuadro Comparativo de Métodos

| Característica | PERT | Ágil (Scrum) | CCPM |
|----------------|------|--------------|------|
| **Unidad** | Horas/días | Story Points | Días con 50% prob |
| **Contexto ideal** | Fases claras, baja incertidumbre | Alta incertidumbre requisitos | Recursos limitados |
| **Gestión incertidumbre** | Varianza distribuida | Velocidad empírica | Buffers agregados |
| **Adaptación** | Baja | Alta | Media |
| **Fortalezas** | Base estadística | Feedback continuo | Considera recursos |
| **Debilidades** | Ignora recursos | Difícil en proyectos grandes | Cambio cultural |

**Cuándo usar cada uno:**

**PERT:**
- Proyecto con fases claramente definidas
- Industria regulada (construcción, farmacéutica)
- Requisitos estables

**Ágil:**
- Alta incertidumbre de requisitos
- Entregas incrementales posibles
- Cliente disponible para feedback

**CCPM:**
- Múltiples proyectos con recursos compartidos
- Necesidad de acortar timeline sin agregar gente
- Cuellos de botella críticos

---

## 🎮 Ejercicios Prácticos

### Ejercicio 1: Calcular PERT

**Proyecto:** Backend API con 3 endpoints

| Tarea | O | M | P |
|-------|---|---|---|
| Endpoint Users | 1 | 2 | 4 |
| Endpoint Products | 2 | 3 | 6 |
| Endpoint Orders | 3 | 5 | 9 |

**Calcular:**

1. Estimación esperada (μ) de cada tarea
2. Desviación estándar (σ) de cada tarea
3. Varianza (σ²) de cada tarea
4. Duración total del proyecto
5. Desviación estándar total
6. Rango de confianza 95%

<details>
<summary>Ver Solución</summary>

**Tarea 1: Users**
- μ = (1 + 4×2 + 4) / 6 = 13/6 = 2.17 días
- σ = (4-1) / 6 = 0.5 días
- σ² = 0.25

**Tarea 2: Products**
- μ = (2 + 4×3 + 6) / 6 = 20/6 = 3.33 días
- σ = (6-2) / 6 = 0.67 días
- σ² = 0.44

**Tarea 3: Orders**
- μ = (3 + 4×5 + 9) / 6 = 32/6 = 5.33 días
- σ = (9-3) / 6 = 1 día
- σ² = 1

**Total:**
- μ_total = 2.17 + 3.33 + 5.33 = **10.83 días**
- σ²_total = 0.25 + 0.44 + 1 = 1.69
- σ_total = √1.69 = **1.3 días**
- Rango 95%: 10.83 ± 2×1.3 = **8.2 a 13.4 días**
</details>

### Ejercicio 2: Identificar Ruta Crítica

**Proyecto:** Deploy de aplicación

| Tarea | Depende de | Duración |
|-------|------------|----------|
| A: Build | - | 5 días |
| B: Test unitario | A | 3 días |
| C: Test integración | A | 4 días |
| D: Preparar servidor | - | 2 días |
| E: Deploy | B, C, D | 1 día |

**Preguntas:**

1. Dibuja el diagrama de red
2. Identifica todas las rutas
3. Calcula duración de cada ruta
4. ¿Cuál es la ruta crítica?
5. ¿Cuál es la holgura de Tarea D?

<details>
<summary>Ver Solución</summary>

**Rutas:**
- Ruta 1: A → B → E = 5+3+1 = 9 días
- Ruta 2: A → C → E = 5+4+1 = 10 días ⭐ **Crítica**
- Ruta 3: D → E = 2+1 = 3 días

**Ruta Crítica:** A-C-E (10 días)

**Holgura de D:**
- Early Start: día 0
- Late Start: día 8 (antes de E que empieza día 9)
- Holgura: 8 - 0 = **8 días**
</details>

### Ejercicio 3: Calcular Velocidad y Forecast

**Datos de Equipo Beta:**

| Sprint | Story Points Completados |
|--------|-------------------------|
| 1 | 15 |
| 2 | 18 |
| 3 | 20 |
| 4 | 22 |
| 5 | 25 |

**Backlog pendiente:** 180 Story Points

**Calcular:**

1. Velocidad promedio
2. Desviación estándar de velocidad
3. Forecast (número de sprints)
4. Rango optimista y pesimista

<details>
<summary>Ver Solución</summary>

1. **Velocidad promedio:** (15+18+20+22+25)/5 = **20 pts/sprint**

2. **Desviación estándar:**
   - Varianza = [(15-20)² + (18-20)² + (20-20)² + (22-20)² + (25-20)²] / 5
   - Varianza = [25 + 4 + 0 + 4 + 25] / 5 = 11.6
   - σ = √11.6 = **3.4 pts**

3. **Forecast:** 180 / 20 = **9 sprints**

4. **Rangos:**
   - Optimista (20+3.4 = 23.4): 180/23.4 = 7.7 ≈ **8 sprints**
   - Pesimista (20-3.4 = 16.6): 180/16.6 = 10.8 ≈ **11 sprints**
   - **Rango: 8-11 sprints** (16-22 semanas si sprints de 2 sem)
</details>

---

## 🧪 Preguntas de Autoevaluación

### Nivel 1: Recordar

1. ¿Qué significa PERT?
   <details><summary>Respuesta</summary>Program Evaluation and Review Technique</details>

2. ¿Cuál es la fórmula de estimación esperada en PERT?
   <details><summary>Respuesta</summary>μ = (O + 4M + P) / 6</details>

3. ¿Qué es la Ruta Crítica?
   <details><summary>Respuesta</summary>Secuencia de tareas dependientes más larga del proyecto</details>

4. ¿Por qué usamos Fibonacci en Story Points?
   <details><summary>Respuesta</summary>Refleja incertidumbre creciente (difícil distinguir entre tareas grandes) y fuerza honestidad (no hay "15 puntos")</details>

### Nivel 2: Comprender/Aplicar

5. ¿Cuál es el paso MÁS IMPORTANTE de Planning Poker y por qué?
   <details><summary>Respuesta</summary>Paso 4: Discutir extremos. Porque ahí se exponen suposiciones ocultas. El valor NO está en el número final, está en la conversación.</details>

6. ¿Por qué NO contamos historias 90% completadas en velocidad?
   <details><summary>Respuesta</summary>Porque Ágil valora software funcionando. 90% = 0% de valor entregado. Evita "gaming" del sistema.</details>

7. Tres tareas PERT: A (μ=5, σ=1), B (μ=3, σ=0.5), C (μ=7, σ=1.5). ¿Duración total y σ total?
   <details><summary>Respuesta</summary>
   μ_total = 5+3+7 = 15 días
   σ²_total = 1² + 0.5² + 1.5² = 1 + 0.25 + 2.25 = 3.5
   σ_total = √3.5 = 1.87 días
   </details>

### Nivel 3: Analizar/Evaluar

8. Un equipo tiene velocidad de 20 pts/sprint. Stakeholder quiere feature de 100 pts en 4 sprints. ¿Qué respondes?
   <details><summary>Respuesta</summary>
   "Basado en nuestra velocidad histórica (20 pts/sprint), 100 pts tomarían 5 sprints (10 semanas). Para hacerlo en 4 sprints necesitaríamos:
   - Aumentar velocidad a 25 pts/sprint (+25%, poco realista sin agregar gente), O
   - Reducir alcance a 80 pts (-20% de features)
   ¿Cuál prefieres?"
   </details>

9. ¿Por qué CPM falló en el caso A-B-C-D (Clase 3 preview)?
   <details><summary>Respuesta</summary>CPM dijo 25 días asumiendo recursos ilimitados. Pero Ana (recurso único) hace tareas B y D secuencialmente, no en paralelo. Duración real: 35 días. CPM ignoró restricción de recursos.</details>

10. Compara PERT vs Ágil: ¿Cuándo usar cada uno?
    <details><summary>Respuesta</summary>
    **PERT:** Proyectos con fases claras, baja incertidumbre, industria regulada (construcción, farmacéutica). Ej: Construcción de edificio.

    **Ágil:** Alta incertidumbre de requisitos, entregas incrementales, cliente disponible. Ej: Startup desarrollando app nueva.
    </details>

---

## 🎯 Para la Próxima Clase

**Clase 3: Cadena Crítica (CCPM)**

**Pregunta provocadora:**

Ya sabemos estimar mejor (PERT, Planning Poker).

Pero... ¿Y si el problema NO es estimar mejor, sino GESTIONAR la incertidumbre de forma diferente?

**Preview:**
- CCPM (Critical Chain Project Management)
- Estimaciones agresivas (50%) + Buffers agregados
- Caso A-B-C-D completo
- 20-30% reducción de timeline sin agregar recursos

---

**Curso:** Estimación de Proyectos
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 2.0 - Formato Remoto - Enero 2025
