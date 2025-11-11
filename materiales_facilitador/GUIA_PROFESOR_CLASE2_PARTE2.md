# Guía del Profesor - Clase 2: Métodos de Estimación
## PARTE 2: Estimación Ágil y Planning Poker (Post-Slide 7)

**Duración:** 130 minutos (2 horas 10 min)
**Formato:** Remoto / Teórico con demostración de caso

---

## 📋 Contenido de Esta Parte

| Slide | Tema | Duración |
|-------|------|----------|
| 8 | Introducción a Estimación Ágil | 12 min |
| 9 | Story Points vs Horas | 10 min |
| 10 | Escala de Fibonacci | 8 min |
| 11 | T-Shirt Sizing | 10 min |
| *BREAK* | ☕ Descanso | 15 min |
| 12 | Planning Poker: Marco teórico | 12 min |
| 13 | Caso de Estudio: Backlog de Autenticación | 10 min |
| 14 | Demostración: Historia HU-3 (Password Reset) | 15 min |
| 15 | Proceso de Votación y Discusión | 12 min |
| 16 | Identificación de Suposiciones Ocultas | 13 min |
| 17 | Convergencia y Consenso | 8 min |
| 18 | Velocidad: Concepto y Cálculo | 10 min |
| 19 | Forecasting con Velocidad | 7 min |
| 20 | Refinamiento Progresivo | 5 min |
| 21 | Mejores Prácticas | 7 min |
| 22 | Cuadro Comparativo: PERT vs Ágil vs CCPM | 8 min |
| 23 | Síntesis de la Clase | 5 min |
| 24 | Cierre y Preview Clase 3 | 3 min |

**Total:** 130 minutos

---

## 🧠 Pensamiento Profundo: Segunda Mitad

### Propósito Pedagógico

La segunda mitad de Clase 2 es el **puente entre diagnóstico (Clase 1) y solución (Clase 3)**:

1. **Slides 8-11 (Ágil):** Introducir el cambio de paradigma:
   - De horas a puntos relativos
   - De precisión falsa a rango honesto
   - De individual a colaborativo

2. **Slides 12-17 (Planning Poker):** La **PIEZA CENTRAL** de Clase 2:
   - NO es solo una técnica de estimación
   - ES un mecanismo de **exposición de suposiciones ocultas**
   - Replica el momento "aha!" del Malvavisco (Clase 1)

3. **Slides 18-20 (Velocidad):** Cerrar el loop:
   - Story Points sin velocidad = inútiles
   - Velocidad convierte puntos en calendario
   - Introduce idea de "capacidad conocida" (setup para CCPM Clase 3)

4. **Slides 21-24 (Síntesis):** Preparar terreno para Clase 3:
   - Comparar todos los métodos vistos
   - Mostrar que TODOS fallan en gestionar incertidumbre
   - Anticipar: "¿Y si el problema NO es estimar mejor, sino GESTIONAR la incertidumbre?"

### Desafío Pedagógico Clave

**Problema:** Planning Poker originalmente era workshop hands-on. Ahora es remoto/teórico.

**Solución aplicada:**
- Presentar caso concreto (HU-3: Password Reset)
- Simular votación con EXTREMOS (2 pts vs 13 pts)
- Narrar la discusión que surgiría
- Mostrar cómo surfacing assumptions es el VERDADERO valor

**Riesgo:** Que parezca "aburrido" sin participación.

**Mitigación:**
- Pedir a participantes que PIENSEN su estimación (en chat o mentalmente)
- Hacer pausas para preguntar "¿Alguien estimaría 13? ¿Por qué?"
- Conectar con experiencias reales: "¿Les pasó que todos estimaron diferente?"

---

## 📖 Desglose Slide por Slide

---

### **Slide 8: Introducción a Estimación Ágil** (12 min)

**Objetivos:**
- Presentar cambio de paradigma: horas → puntos relativos
- Conectar con problemas vistos en Clase 1
- Introducir beneficios de estimación colaborativa

**Script sugerido:**

"Acabamos de ver PERT y CPM - métodos clásicos de los años 50-60.

Ahora saltamos a los años 2000: **Estimación Ágil**.

¿Cuál es la diferencia FUNDAMENTAL?

**PERT/CPM:**
- Estiman en HORAS o DÍAS (unidades de tiempo)
- Buscan PRECISIÓN (O-M-P pero al final un número)
- Lo hace el PM o especialista

**ÁGIL:**
- Estima en PUNTOS (unidades RELATIVAS de complejidad)
- Asume INCERTIDUMBRE (puntos NO son horas)
- Lo hace el EQUIPO completo

[PAUSA]

Pregunta: ¿Por qué PUNTOS en lugar de HORAS?

[Esperar respuestas, luego explicar:]

Porque las HORAS mienten. Dependen de:
- Quién hace la tarea (junior vs senior)
- Interrupciones (día tranquilo vs día de fuego)
- Estado mental (lunes vs viernes)
- Contexto (familiar vs nuevo)

Los PUNTOS son **relativos**:
- Esta tarea es 'el doble de compleja' que aquella
- Esta tiene 'incertidumbre similar' a la anterior
- Evitamos el sesgo de 'cuánto ME tomaría a MÍ'

[PAUSA]

En la slide ven los conceptos clave:

**Story Points:**
- Unidad abstracta de tamaño/complejidad/esfuerzo
- Fibonacci: 1, 2, 3, 5, 8, 13, 21...
- Relative Estimation: siempre comparamos con baseline

**Planning Poker:**
- Técnica colaborativa
- Todos votan simultáneamente
- Se discuten extremos
- Se busca CONSENSO (no promedio)

**Velocidad:**
- Puntos completados por sprint
- Se estabiliza después de 3-5 sprints
- Permite forecasting: '¿Cuándo terminamos este backlog?'

[CONECTAR con Clase 1]

¿Recuerdan el Malvavisco Challenge?

Los niños ganaban porque ITERABAN rápido. No pasaban tiempo planificando.

Estimación Ágil aplica el mismo principio:
- NO intentamos adivinar perfecto desde el inicio
- Estimamos rápido, refinamos progresivamente
- Usamos FEEDBACK empírico (velocidad) para ajustar

[TRANSICIÓN]

Vamos a profundizar en cada pieza. Primero: ¿Qué SON realmente los Story Points?"

---

**Preguntas para engagement:**

1. "¿Alguien ha usado Story Points antes? ¿Cómo les fue?"
2. "¿Cuál creen que es el mayor beneficio: puntos vs horas?"
3. "¿Cuál sería el mayor DESAFÍO de adoptar esto?"

**Tips para el facilitador:**

✅ **Enfatizar:** La diferencia NO es técnica (horas vs puntos), es FILOSÓFICA (precisión vs incertidumbre)

✅ **Analogía útil:** "Story Points son como comparar pesos sin balanza. Esta caja es 'el doble de pesada' que aquella, sin saber kilos exactos."

⚠️ **Evitar:** Decir "1 punto = X horas". Eso destruye el concepto. Puntos NO se convierten directamente.

⏰ **Timing:** 12 min total (5 min explicación inicial, 4 min ejemplos, 3 min preguntas)

---

### **Slide 9: Story Points vs Horas** (10 min)

**Objetivos:**
- Clarificar diferencia conceptual
- Mostrar tabla comparativa
- Explicar por qué puntos son más honestos

**Script sugerido:**

"Aquí está la comparación directa. Lean la tabla en pantalla.

[DAR 30 SEGUNDOS para leer]

Analicemos las filas más importantes:

**Fila 1: Unidad**
- Horas: Tiempo absoluto
- Puntos: Complejidad relativa

Ya lo dijimos. Pero profundicemos en las consecuencias...

**Fila 2: Precisión**
- Horas: Falsa sensación de exactitud
- Puntos: Reconoce incertidumbre

Cuando decimos '8 horas', suena científico. Pero es mentira.
Podría ser 4 o 16 dependiendo de mil factores.

Cuando decimos '5 puntos', estamos diciendo:
'Esto es más complejo que una tarea de 3, menos que una de 8.'
NO estamos mintiendo con falsa precisión.

**Fila 3: Quién estima**
- Horas: A menudo el PM solo
- Puntos: TODO el equipo

[PAUSA - Conectar con Clase 1]

¿Recuerdan que hablamos del 'conocimiento distribuido'?

En Planning Poker, el tester ve riesgos que el dev no ve.
El dev ve complejidad técnica que el PO no ve.
El arquitecto ve acoplamiento que nadie más ve.

Todos votan. Todos aportan su perspectiva.

**Fila 4: Estabilidad**
- Horas: Varían mucho según persona/contexto
- Puntos: Más estables (complejidad no cambia)

Ejemplo:
- 'Implementar login' puede tomar 8 horas al senior, 20 al junior
- Pero la COMPLEJIDAD es la misma: 5 puntos
- Luego la velocidad del equipo refleja capacidad real

**Fila 5: Propósito**
- Horas: Compromiso externo, contrato
- Puntos: Planificación interna, priorización

[ÉNFASIS]

Esto es CLAVE:

Story Points NO son para decirle al cliente '¿Cuándo estará listo?'

Son para que el EQUIPO decida:
- ¿Cuántas historias caben en este sprint?
- ¿Esta épica es monstruosa (100 pts) o manejable (30 pts)?
- ¿Progresamos bien o estamos atascados?

Para decirle al cliente '¿Cuándo?', usamos VELOCIDAD:
'Hacemos 25 puntos/sprint, tenemos 200 pts pendientes = ~8 sprints.'

[PAUSA]

**Fila 6: Presión**
- Horas: Generan compromiso prematuro
- Puntos: Menor presión, más honestidad

Cuando decís '16 horas', el stakeholder dice 'OK, entonces 2 días.'
Y si tomó 3 días, 'fallaste'.

Cuando decís '8 puntos', el stakeholder pregunta '¿Y eso cuánto es?'
Y respondés: 'Depende. Nuestra velocidad promedio dice ~1 sprint, con ±20% variación.'

Honestidad vs falsa certeza.

[TRANSICIÓN]

OK, entendimos la FILOSOFÍA. Ahora la práctica: ¿Cómo se usan?"

---

**Preguntas para engagement:**

1. "¿Alguna vez se comprometieron con horas y fallaron? ¿Qué pasó?"
2. "¿Qué objeción creen que pondría un cliente tradicional a los Story Points?"
3. "¿Cómo convencerían a un gerente de que puntos son MEJOR que horas?"

**Tips para el facilitador:**

✅ **Enfatizar:** NO es que puntos sean perfectos, es que son MÁS HONESTOS que horas.

✅ **Analogía útil:** "Horas son como predecir temperatura exacta el 15 de julio. Puntos son como decir 'será verano, hace calor'. Menos preciso pero más confiable."

⚠️ **Evitar:** Decir que Story Points "resuelven" el problema de estimación. NO lo resuelven, lo GESTIONAN mejor.

💡 **Anticipar objeción común:** "Pero el cliente QUIERE fechas."
- Respuesta: "Sí, y se las damos. Pero basadas en velocidad empírica, no en adivinar horas."

⏰ **Timing:** 10 min (6 min tabla, 4 min discusión)

---

### **Slide 10: Escala de Fibonacci** (8 min)

**Objetivos:**
- Explicar por qué Fibonacci (no lineal: 1,2,3,5,8,13...)
- Conectar con incertidumbre creciente
- Introducir concepto de "?"

**Script sugerido:**

"¿Por qué usamos números raros? 1, 2, 3, 5, 8, 13...

¿Por qué NO 1, 2, 3, 4, 5, 6, 7...?

[Esperar respuestas]

La razón es profunda:

**Fibonacci refleja INCERTIDUMBRE creciente.**

Cuando algo es pequeño (1, 2, 3 puntos), puedo distinguir:
- '1 punto': Cambiar un texto, corregir un typo
- '2 puntos': Agregar validación simple
- '3 puntos': Endpoint CRUD básico

La diferencia entre 1 y 2 es CLARA.

Pero cuando algo es grande (13, 21, 34 puntos):
- ¿13 puntos? Sistema de autenticación completo
- ¿21 puntos? Sistema de autenticación + OAuth + 2FA
- ¿34 puntos? TODO lo anterior + SSO + SAML

La diferencia entre 21 y 34 es BORROSA.

[PAUSA]

Fibonacci FUERZA honestidad:

NO puedes decir '15 puntos'. Tenés que elegir:
- ¿Es un 13? (grande pero manejable)
- ¿O es un 21? (épica que deberíamos dividir)

Esa distinción te obliga a PENSAR.

Si tuvieras escala lineal (10, 11, 12, 13, 14, 15...):
- Discutirías por horas si es 12 o 13
- Falsa precisión otra vez
- El punto se pierde

[VER TABLA en slide]

**Valores comunes:**

**1 punto:** Trivial
- Cambiar texto en UI
- Corregir typo en documentación
- Minutos de trabajo

**2 puntos:** Simple
- Agregar campo a form con validación
- Endpoint GET básico
- ~1-2 horas (pero NO lo decimos así)

**3 puntos:** Pequeño pero completo
- CRUD endpoint completo (GET/POST/PUT/DELETE)
- Componente React simple con estado
- Feature pequeño end-to-end

[ÉNFASIS]

**3 puntos es el BASELINE típico.**

En Planning Poker, el equipo elige una historia 'estándar' de 3 puntos.
Todo lo demás se compara con eso:
- ¿Más simple? → 1 o 2
- ¿Más complejo? → 5, 8, 13...

**5 puntos:** Moderado
- Feature con múltiples componentes
- Integración con API externa
- Testing complejo

**8 puntos:** Grande
- Sistema completo pequeño
- Refactoring significativo
- Ya estamos en zona de 'deberíamos dividir esto'

**13 puntos:** Muy grande
- SIEMPRE debería dividirse
- A menos que sea investigación/spike

**21, 34, ...:** Épicas
- NO son historias, son CONTENEDORES de historias
- Deben descomponerse antes de sprint

**?:** Demasiada incertidumbre
- No sabemos ni por dónde empezar
- Necesitamos spike/research primero
- Ejemplo: 'Integrar con API de proveedor nuevo' (nunca lo usamos)

**∞ (Infinito):** Imposible/No vale la pena
- Se usa raramente
- 'Reescribir TODO el sistema de cero'

[TRANSICIÓN]

Ahora que sabemos la escala, ¿cómo se USA en la práctica?"

---

**Preguntas para engagement:**

1. "¿Por qué 'cambiar texto en UI' es 1 punto pero 'endpoint CRUD' es 3?"
2. "¿Qué harían con una historia de 21 puntos?"
3. "¿Cuándo usarían '?' vs un número alto?"

**Tips para el facilitador:**

✅ **Enfatizar:** Fibonacci NO es mágico, es una herramienta para forzar conversación.

✅ **Analogía útil:** "Es como tallas de ropa: XS, S, M, L, XL, XXL. NO usamos talla 1, 2, 3, 4... porque la diferencia entre 4 y 5 no significa nada."

⚠️ **Evitar:** Dar equivalencias de horas ('3 pts = 1 día'). Destruye el concepto.

💡 **Tip práctico:** Si el equipo debate entre 5 y 8, probablemente es un 8. La duda indica complejidad oculta.

⏰ **Timing:** 8 min (5 min explicación, 3 min tabla)

---

### **Slide 11: T-Shirt Sizing** (10 min)

**Objetivos:**
- Presentar alternativa más simple que Fibonacci
- Explicar cuándo usar qué método
- Preparar para Planning Poker

**Script sugerido:**

"Fibonacci puede ser intimidante al principio.

Hay una alternativa más simple: **T-Shirt Sizing**.

[VER TABLA en slide]

**XS:** Extra Small - Trivial
**S:** Small - Simple
**M:** Medium - Moderado (el baseline típico)
**L:** Large - Grande, considerar dividir
**XL:** Extra Large - Muy grande, DEBE dividirse

[PAUSA]

¿Ventajas de T-Shirt Sizing?

1. **Intuitivo:** Todos entienden tallas de ropa
2. **Rápido:** Para backlog grooming inicial
3. **No intimidante:** Stakeholders lo entienden
4. **Menos debate:** Menos opciones = menos parálisis

¿Desventajas?

1. **Menos granular:** No puedes distinguir tanto
2. **Conversión a Fibonacci:** Eventualmente necesitas puntos numéricos para velocidad
3. **Tentación de agregar:** XXL, XXXL... (evitar)

[EQUIVALENCIAS]

Si tu equipo usa ambos sistemas:

XS = 1 punto
S = 2-3 puntos
M = 5 puntos
L = 8 puntos
XL = 13+ puntos (y debería dividirse)

[ÉNFASIS]

**¿Cuándo usar cada uno?**

**T-Shirt Sizing:**
- Backlog grooming inicial
- Muchas historias por clasificar rápido
- Equipo nuevo en Ágil
- Roadmap de alto nivel (épicas)

**Fibonacci:**
- Sprint planning formal
- Cuando necesitas velocidad numérica
- Equipo maduro en Ágil
- Historias listas para trabajar

[EJEMPLO PRÁCTICO]

Imaginemos Product Backlog nuevo con 50 historias:

**Paso 1:** T-Shirt Sizing en 1 hora
- 10 XS
- 20 S
- 15 M
- 4 L
- 1 XL

**Paso 2:** Las L y XL se dividen → 10 historias más

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

**Preguntas para engagement:**

1. "¿Qué método les parece más fácil para empezar?"
2. "Si tuvieran backlog de 100 historias, ¿cómo lo atacarían?"
3. "¿Ven algún riesgo en usar T-Shirt Sizing?"

**Tips para el facilitador:**

✅ **Enfatizar:** T-Shirt NO reemplaza Fibonacci, lo COMPLEMENTA para diferentes niveles de detalle.

✅ **Analogía útil:** "Es como GPS: vista satelital (T-Shirt) vs zoom de calle (Fibonacci). Ambas útiles, según necesidad."

⚠️ **Evitar:** Decir que uno es 'mejor' que el otro. Son herramientas para contextos diferentes.

💡 **Tip práctico:** Si el equipo resiste Fibonacci, empezar con T-Shirt. Migrar después cuando vean la necesidad.

⏰ **Timing:** 10 min (6 min explicación, 4 min ejemplo)

---

## ☕ **BREAK - 15 MINUTOS**

**Instrucciones para el facilitador:**

Antes del break, decir:

"OK, 15 minutos de break.

Cuando volvamos: **Planning Poker**.

Vamos a ver un CASO COMPLETO paso a paso.

Van a ver cómo el proceso de estimación expone suposiciones ocultas y genera alineación.

[Conectar con Clase 1]

Es el equivalente del momento 'aha!' del Malvavisco Challenge, pero para software.

Nos vemos en 15."

---

## 🎯 **POST-BREAK: Planning Poker - El Core de Clase 2**

### Contexto Pedagógico Crítico

**Lo que viene (Slides 12-17) es la PIEZA CENTRAL de Clase 2.**

**Por qué es importante:**

1. **Planning Poker NO es solo técnica de estimación**
   - Es mecanismo de **exposición de suposiciones**
   - Es catalizador de **alineación del equipo**
   - Es forma de **capturar conocimiento distribuido**

2. **Conexión con Clase 1:**
   - Marshmallow Challenge mostró: conocimiento oculto mata proyectos
   - Planning Poker es la SOLUCIÓN: forzar que conocimiento salga a la luz

3. **Setup para Clase 3:**
   - Planning Poker mejora estimaciones
   - Pero sigue sin resolver incertidumbre inherente
   - Eso lo veremos con CCPM (Clase 3)

**Desafío de entrega remota:**

Originalmente esto era workshop hands-on de 90 min.
Ahora es demostración teórica de 60 min.

**Cómo mantener engagement:**

- Narrar la historia como si fuéramos el equipo
- Simular debate realista
- Pedir a participantes que piensen SU estimación antes de revelar
- Usar chat para recoger opiniones

**Objetivo emocional:**

Que participantes SIENTAN el "aha!" moment:
"¡Ah! Los extremos revelaron que uno asumía API lista, el otro asumía escribirla desde cero."

---

### **Slide 12: Planning Poker - Marco Teórico** (12 min)

**Objetivos:**
- Explicar QUÉ es Planning Poker
- Explicar POR QUÉ funciona (no solo CÓMO)
- Preparar para caso de estudio

**Script sugerido:**

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

**Preguntas para engagement:**

1. "¿Alguien participó en Planning Poker antes? ¿Cómo fue?"
2. "¿Por qué creen que votar simultáneamente es importante?"
3. "¿Qué pasaría si se promediaran los votos sin discutir?"

**Tips para el facilitador:**

✅ **Enfatizar:** El DEBATE es más valioso que el número final.

✅ **Analogía útil:** "Es como diagóstico médico: pedir segunda opinión no es desconfianza, es capturar perspectivas diferentes."

⚠️ **Evitar:** Decir que Planning Poker 'elimina errores'. NO los elimina, los REDUCE al exponer suposiciones.

💡 **Anticipar:** "¿No es mucho tiempo?" Respuesta: "60-90 min planning ahorra 40 horas de retrabajo por suposiciones incorrectas."

⏰ **Timing:** 12 min (7 min marco teórico, 5 min beneficios)

---

### **Slide 13: Caso de Estudio - Backlog de Autenticación** (10 min)

**Objetivos:**
- Presentar contexto del caso
- Establecer baseline (HU-2 = 3 pts)
- Preparar para análisis detallado de HU-3

**Script sugerido:**

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

**Preguntas para engagement:**

1. "¿Por qué HU-3 podría ser MÁS compleja que HU-2?"
2. "¿Por qué podría ser MENOS compleja?"
3. "¿Qué suposiciones están haciendo para su estimación?"

**Tips para el facilitador:**

✅ **Enfatizar:** NO hay respuesta 'correcta' aún. Las suposiciones determinarán el número.

✅ **Crear suspense:** "Van a ver que el equipo tuvo un debate intenso. Extremos revelaron algo importante."

⚠️ **Evitar:** Dar respuesta anticipada. Mantener incertidumbre hasta siguiente slide.

💡 **Tip técnico:** Si participantes preguntan detalles técnicos no especificados ('¿Qué librería de email?'), decir: "Excelente pregunta. Justo ese tipo de pregunta surgió en el equipo."

⏰ **Timing:** 10 min (5 min presentar backlog, 5 min leer HU-3 y recoger votos)

---

### **Slide 14: Demostración - Historia HU-3 (Password Reset)** (15 min)

**Objetivos:**
- Narrar votación inicial con extremos (2 vs 13)
- Mostrar qué causó la diferencia
- Introducir discusión del equipo

**Script sugerido:**

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

**Preguntas para engagement:**

1. "¿Qué suposición les sorprendió más?"
2. "¿Ustedes habrían splitteado la historia?"
3. "¿Qué habría pasado si Ana estimaba sola (sin Planning Poker)?"

**Tips para el facilitador:**

✅ **Enfatizar:** Este debate de 10 minutos ahorra HORAS de retrabajo.

✅ **Narrar dramáticamente:** Hacer pausas, cambiar tono de voz por personaje, crear tensión.

⚠️ **Evitar:** Apurarse. Este es el CORE de Clase 2, merece 15 minutos completos.

💡 **Tip emocional:** Apuntar al momento "aha!": "¿Ven? Las suposiciones MATABAN el proyecto. Ahora están explícitas."

⏰ **Timing:** 15 min (10 min narración, 5 min debrief)

---

### **Slide 15: Proceso de Votación y Discusión** (12 min)

**Objetivos:**
- Generalizar lecciones del caso
- Explicar dinámica de segunda ronda
- Tips para facilitar Planning Poker

**Script sugerido:**

"Acabamos de ver UN ejemplo.

Ahora generalicemos: ¿Cómo funciona siempre el proceso?

[VER DIAGRAMA en slide]

**RONDA 1: Votación inicial**

Todos revelan simultáneamente.

**3 escenarios posibles:**

**Escenario A: CONSENSO INMEDIATO**
- Todos votaron mismo número o ±1 (ej: todos 5, o mix de 5 y 8)
- Scrum Master: 'OK, consenso: 5 puntos.'
- **Duración:** 2 minutos
- **Frecuencia:** ~30% de historias (las bien definidas)

**Escenario B: DISPERSIÓN MODERADA**
- Votos en rango 2x (ej: 3, 5, 5, 8)
- Scrum Master: 'Discutamos. Persona con 3, ¿por qué? Persona con 8, ¿por qué?'
- Debate 5 minutos
- Segunda ronda → consenso
- **Duración:** 7-8 minutos
- **Frecuencia:** ~50% de historias

**Escenario C: DISPERSIÓN EXTREMA (como HU-3)**
- Votos en rango 4x+ (ej: 2, 5, 13)
- Debate intenso
- Puede requerir:
  - Aclaración del PO
  - Split de historia
  - Spike/research primero
  - 2-3 rondas de votación
- **Duración:** 10-15 minutos
- **Frecuencia:** ~20% de historias (las ambiguas)

[ÉNFASIS]

**Escenario C es BUENO, no malo.**

Significa que la historia tenía incertidumbre OCULTA.

Mejor descubrirlo ahora que en día 3 de desarrollo.

[MECÁNICA DE DEBATE]

**Regla de oro: SIEMPRE hablan los extremos.**

¿Por qué?

Porque el CENTRO no aporta información nueva:

Si votos son: 2, 5, 5, 5, 13

Los '5' pensaron similar (mayoritario).
El '2' y el '13' tienen perspectivas únicas.

[EJEMPLO]

**Mal facilitado:**

Scrum Master: '¿Alguien quiere explicar su voto?'
Silencio incómodo.
Alguien dice: 'Yo puse 5 porque... bla.'
No converge.

**Bien facilitado:**

Scrum Master: 'María, vos pusiste 2, el más bajo. ¿Por qué?'
María explica.
Scrum Master: 'Pedro, vos pusiste 13, el más alto. ¿Por qué?'
Pedro explica.
Scrum Master: 'OK, ¿alguien cambió de opinión? Re-votamos.'

[SEGUNDA RONDA]

Típicamente los extremos se acercan:

**Antes:** 2, 5, 5, 5, 13
**Después:** 5, 5, 8, 8, 8

Ahora hay consenso en 5-8 → Scrum Master decide: '8 para ser conservadores.'

O pregunta: '¿5 u 8?' → Equipo rápidamente elige.

[TERCERA RONDA (rara)]

Si después de 2 rondas sigue disperso:

**Opciones:**

**A) Split la historia** (como hicimos con HU-3)

**B) Asignar '?' y hacer spike:**
- 'Hay demasiada incertidumbre'
- 'Hagamos 2-3 horas de investigación (spike)'
- 'Re-estimamos después'

**C) Escalar a PO/Arquitecto:**
- 'Necesitamos decisión de diseño antes de estimar'

**D) Tomar el voto CONSERVADOR (alto):**
- 'Hay incertidumbre, vamos con 13 para estar seguros'

[PAUSA]

**Regla: NUNCA promediar.**

Promedio esconde información:

(2 + 13) / 2 = 7.5 ≈ 8

Pero ese '8' es MENTIRA.
La realidad es: alguien ve 2, alguien ve 13.
Hay gap de conocimiento.

El debate DEBE pasar para cerrar ese gap.

[CONSEJOS PRÁCTICOS]

**Para Scrum Masters / Facilitadores:**

✅ **Timeboxear:** Máximo 10 min por historia. Si no converge, marcar para después.

✅ **Evitar 'expertismo':** No dejar que el dev senior domine. Todos votan igual.

✅ **Aceptar desacuerdo:** A veces 5 vs 8 es legítimo (incertidumbre real). Ir con el conservador.

✅ **Notar patrones:** Si TODAS las historias son 13+, el backlog está mal refinado.

⚠️ **Evitar parálisis:** No buscar 'el número perfecto'. Buscar 'suficientemente bueno para sprint planning'.

⚠️ **Evitar negociación:** No es regateo. No 'te doy 5 si vos bajás de 13 a 8'.

[TRANSICIÓN]

OK, vimos el proceso.

Ahora: ¿Cuáles son las suposiciones TÍPICAS que Planning Poker expone?"

---

**Preguntas para engagement:**

1. "¿Qué harían si después de 3 rondas siguen 5 vs 13?"
2. "¿Por qué promediar es malo?"
3. "¿Cuál de los 3 escenarios (A/B/C) les parece más valioso?"

**Tips para el facilitador:**

✅ **Enfatizar:** Escenario C (dispersión extrema) es REGALO, no problema.

✅ **Analogía útil:** "Es como revisión de código: los comentarios que duelen son los más valiosos."

⚠️ **Evitar:** Decir que Planning Poker debe ser 'rápido'. Prioridad es ALINEACIÓN, no velocidad.

💡 **Tip práctico:** Si equipo nuevo, primeras sesiones tomarán 2x tiempo. Normal. Se acelera con práctica.

⏰ **Timing:** 12 min (7 min escenarios, 5 min mecánica de debate)

---

### **Slide 16: Identificación de Suposiciones Ocultas** (13 min)

**Objetivos:**
- Listar suposiciones típicas que causan extremos
- Enseñar a identificarlas proactivamente
- Conectar con Clase 1 (Malvavisco)

**Script sugerido:**

"Ahora la pregunta clave:

¿CUÁLES son las suposiciones ocultas típicas?

Si las conocemos, podemos buscarlas PROACTIVAMENTE.

[VER TABLA en slide]

**10 Suposiciones Comunes que Causan Extremos:**

---

**1. ALCANCE (Scope)**

**Voto bajo:** 'Solo happy path'
**Voto alto:** 'Incluye edge cases, error handling, validaciones'

**Ejemplo HU-3:**
- Ana pensó: form + endpoint (happy path) → 2 pts
- Pedro pensó: + seguridad + edge cases → 13 pts

**Solución:** PO aclara: '¿Incluye manejo de errores?' → Explícito en Criterios de Aceptación

---

**2. INFRAESTRUCTURA**

**Voto bajo:** 'Ya existe / está lista'
**Voto alto:** 'Hay que construirla'

**Ejemplo HU-3:**
- Ana asumió: 'Email setup ya está' → 2 pts
- Pedro vio: 'Necesitamos tabla nueva tokens' → 13 pts

**Solución:** Arquitecto aclara: '¿Qué piezas tenemos listas?'

---

**3. TESTING**

**Voto bajo:** 'Solo testing manual smoke'
**Voto alto:** 'Unit + Integration + E2E + Edge cases'

**Ejemplo:**
- Dev: 'Funciona en mi máquina' → 3 pts
- Tester: 'Hay que testear 15 casos' → 8 pts

**Solución:** Definition of Done clara: '¿Testing incluido?'

---

**4. COMPLEJIDAD DE UI/UX**

**Voto bajo:** 'Form simple'
**Voto alto:** 'UX compleja con estados, animaciones, responsive'

**Ejemplo:**
- Backend dev: 'Es un form' → 2 pts
- Frontend dev: 'Loading states, error messages, validación real-time' → 5 pts

**Solución:** Mockups o wireframes antes de estimar

---

**5. DEPENDENCIAS EXTERNAS**

**Voto bajo:** 'No consideradas'
**Voto alto:** 'API externa, servicio de tercero, equipo externo'

**Ejemplo:**
- 'Integrar con API de pagos': ¿API está estable? ¿Documentada? ¿Tenemos sandbox?

**Solución:** Identificar dependencias ANTES de sprint planning

---

**6. DATOS / MIGRACIONES**

**Voto bajo:** 'DB vacía'
**Voto alto:** 'Hay que migrar 5M registros'

**Ejemplo:**
- 'Agregar columna a tabla': suena simple
- Pero si tabla tiene 10M filas → downtime, índices, rollback plan

**Solución:** Siempre preguntar: '¿Hay datos existentes?'

---

**7. PERFORMANCE / ESCALABILIDAD**

**Voto bajo:** 'Funciona para 10 usuarios'
**Voto alto:** 'Tiene que soportar 100k req/min'

**Ejemplo:**
- Dev: 'Query simple' → 2 pts
- Arquitecto: 'Esa query en prod matará la DB, necesita índices + cache' → 8 pts

**Solución:** Clarificar requisitos no funcionales (NFRs)

---

**8. SEGURIDAD / COMPLIANCE**

**Voto bajo:** 'No considerada'
**Voto alto:** 'GDPR, auditoría, encriptación, permisos'

**Ejemplo HU-3:**
- Reset password sin considerar: rate limiting, logging, abuse
- Voto bajo vs alto

**Solución:** Checklist de seguridad en DoD

---

**9. CONOCIMIENTO DEL EQUIPO**

**Voto bajo:** 'Yo sé hacerlo rápido'
**Voto alto:** 'Nadie del equipo lo hizo antes'

**Ejemplo:**
- 'Implementar WebSocket': senior que lo hizo 10 veces → 3 pts
- Equipo que nunca usó WebSocket → 13 pts

**Solución:** Considerar equipo REAL (no el dev ideal). ¿Alguien tiene experiencia?

---

**10. DOCUMENTACIÓN / DEPLOYMENT**

**Voto bajo:** 'Solo código'
**Voto alto:** '+ docs + deploy + configuración + rollback plan'

**Ejemplo:**
- Dev: 'Feature lista' (código funciona) → 3 pts
- DevOps: 'Hay que configurar 3 ambientes, actualizar docs, plan de rollback' → 8 pts

**Solución:** Definition of Done incluye deployment

---

[PAUSA]

**¿Ven el patrón?**

Los votos BAJOS típicamente asumen:
- ✅ Happy path
- ✅ Infraestructura lista
- ✅ Sin edge cases
- ✅ Testing mínimo
- ✅ Sin consideraciones de prod

Los votos ALTOS ven:
- ⚠️ Casos edge
- ⚠️ Construcción de infra
- ⚠️ Testing completo
- ⚠️ Seguridad, performance, deployment
- ⚠️ Complejidad oculta

[ÉNFASIS]

**Ambas perspectivas son valiosas:**

- Voto bajo: evita over-engineering
- Voto alto: evita subestimación

El DEBATE encuentra balance.

[CONECTAR con Clase 1]

¿Recuerdan el Malvavisco Challenge?

MBAs asumían:
- ✅ Palitos soportan peso (NO)
- ✅ Malvavisco es liviano (NO)
- ✅ Estructura se mantiene (NO)

Todas suposiciones incorrectas → colapso a los 17 minutos.

Planning Poker **fuerza exposición de suposiciones ANTES de construir**.

Es el malvavisco de prueba que los niños ponían cada 2 minutos.

[TIPS PARA FACILITAR]

**Como facilitador, preguntá proactivamente:**

Antes de votar:
- '¿Testing incluido?'
- '¿Qué piezas de infra necesitamos?'
- '¿Hay dependencias externas?'
- '¿Alguien del equipo tiene experiencia con esto?'

Después de extremos:
- 'Voto bajo: ¿Qué está excluido de tu estimación?'
- 'Voto alto: ¿Qué complejidad ves que otros no?'

[TRANSICIÓN]

OK, entendimos suposiciones.

Ahora: ¿Cómo el equipo converge a consenso?"

---

**Preguntas para engagement:**

1. "¿Cuál de las 10 suposiciones es la más peligrosa?"
2. "¿Les pasó alguna vez que una tarea 'simple' explotó? ¿Por qué?"
3. "¿Qué otras suposiciones agregarían a la lista?"

**Tips para el facilitador:**

✅ **Enfatizar:** Todas estas suposiciones están basadas en casos reales.

✅ **Invitar experiencias:** "¿Alguien tiene ejemplo de suposición que los quemó?"

⚠️ **Evitar:** Culpar a votos bajos. NO es error, es perspectiva diferente.

💡 **Tip práctico:** Imprimir los 10 tipos de suposiciones como checklist para Planning Poker.

⏰ **Timing:** 13 min (10 min tabla, 3 min conexión Clase 1)

---

### **Slide 17: Convergencia y Consenso** (8 min)

**Objetivos:**
- Explicar qué significa "consenso" en Planning Poker
- Diferencias entre consenso, promedio, y autoridad
- Cuándo escalar

**Script sugerido:**

"Después de debatir suposiciones, el equipo necesita CONVERGER.

¿Qué significa 'consenso'?

[PAUSA]

**Consenso NO es:**

❌ **Unanimidad:** Todos piensan exactamente igual
❌ **Promedio:** (3+5+8)/3 = 5.3 ≈ 5
❌ **Voto mayoritario:** 3 personas dicen 5, gana el 5
❌ **Autoridad:** El senior decide

**Consenso ES:**

✅ **Acuerdo suficiente para proceder**
✅ **Todos entienden la historia igual**
✅ **Nadie tiene objeción fuerte**
✅ **Alineación de expectativas**

[VER GRÁFICO en slide - Convergencia visual]

**Típicamente:**

**Ronda 1:**
- Dispersión: 2, 5, 5, 8, 13

**Después de debate:**
- Extremos se mueven
- Centro se mantiene o ajusta

**Ronda 2:**
- Convergencia: 5, 5, 5, 8, 8

**Consenso:**
- Scrum Master: '¿Estamos entre 5 y 8?'
- Equipo: 'Sí'
- Scrum Master: '¿Vamos con 8 para ser conservadores?'
- Equipo: 'OK'
- **Resultado: 8 puntos**

[ÉNFASIS]

El número exacto (5 vs 8) importa MENOS que:

1. ✅ Todos entendemos alcance igual
2. ✅ Suposiciones están explícitas
3. ✅ Nadie ve riesgo que otros ignoran

[CASOS ESPECIALES]

**Caso 1: Alguien no está convencido**

Después de 2-3 rondas:
- Mayoría: 5 pts
- Pedro: 13 pts (insiste)

Scrum Master: 'Pedro, ¿qué tendría que pasar para que bajes a 8?'

Pedro: 'Necesito que arquitecto confirme que tabla X ya existe.'

Arquitecto: 'Ah sí, existe. La creamos mes pasado.'

Pedro: 'OK entonces, bajo a 5.'

**Caso 2: Desacuerdo legítimo**

Después de debate:
- Backend devs: 3 pts (backend es simple)
- Frontend devs: 8 pts (frontend es complejo)

Ambos tienen razón. Hay incertidumbre REAL.

**Solución:**
- Tomar voto CONSERVADOR: 8 pts
- O split: HU-A (backend, 3 pts) + HU-B (frontend, 5 pts)

**Caso 3: Falta información**

Equipo: 'No podemos estimar sin saber qué API usamos.'

**Solución:**
- Marcar historia como '?'
- Asignar spike de investigación (2 pts)
- Re-estimar después

[CUÁNDO ESCALAR]

**Escalar a PO si:**
- Alcance ambiguo
- Criterios de aceptación insuficientes
- Decisión de negocio requerida

**Escalar a Arquitecto si:**
- Decisión de diseño técnico requerida
- Impacto en otros sistemas
- Necesita definición de APIs/contratos

**Escalar a Management si:**
- Historia demasiado grande (21+ pts)
- Necesita recursos externos (otro equipo)
- Bloqueo externo (vendor, legal)

[CONSENSO REAL vs FALSO]

**Consenso REAL:**
- Todos participaron en debate
- Extremos explicaron
- Suposiciones explícitas
- Decisión informada

**Consenso FALSO (evitar):**
- Equipo cansado, solo dice 'OK' para terminar
- Persona dominante (senior) impone su voto
- Promedio sin debate ('5+8 = 6.5, redondeo a 7')
- PO presiona: 'Tiene que ser 3 o no cabe en sprint'

[PAUSA]

Como facilitador, tu trabajo es detectar consenso FALSO:

Señales de alerta:
- Silencio incómodo
- Gente mirando teléfono
- Votos convergen sin debate
- Alguien dice 'OK como quieran'

Si ves eso:
- Parar
- Preguntar: '¿Todos cómodos con 5 pts?'
- Dar espacio para objeciones

[TRANSICIÓN]

OK, ya sabemos Planning Poker completo.

Ahora: ¿Qué hacemos con los Story Points?

Ahí entra **Velocidad**."

---

**Preguntas para engagement:**

1. "¿Alguna vez estuvieron en 'consenso falso'? ¿Qué pasó?"
2. "¿Cómo detectarían que alguien no está convencido pero no habla?"
3. "¿Preferirían errar conservador (alto) o agresivo (bajo)? ¿Por qué?"

**Tips para el facilitador:**

✅ **Enfatizar:** Consenso es acuerdo SUFICIENTE, no perfecto.

✅ **Crear espacio seguro:** "Objeciones son bienvenidas. Mejor ahora que en día 3 de sprint."

⚠️ **Evitar:** Presionar por consenso rápido. Prisa mata alineación.

💡 **Tip práctico:** Después de Planning Poker, chequear con individuos en privado si había objeciones no dichas.

⏰ **Timing:** 8 min (5 min convergencia, 3 min casos especiales)

---

### **Slide 18: Velocidad - Concepto y Cálculo** (10 min)

**Objetivos:**
- Definir Velocidad
- Explicar cómo se calcula
- Conectar Story Points → Calendario

**Script sugerido:**

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

**Preguntas para engagement:**

1. "¿Por qué NO contar historia 90% completa?"
2. "¿Qué harían si velocidad varía mucho (15 un sprint, 30 el siguiente)?"
3. "¿Deberían contar bugs en velocidad?"

**Tips para el facilitador:**

✅ **Enfatizar:** Velocidad NO es KPI de performance. Es herramienta de planificación.

✅ **Analogía útil:** "Es como medir tu velocidad promedio en auto. NO para competir, para saber 'cuánto tardo a destino'."

⚠️ **Evitar:** Comparar velocidades de equipos. Eso destruye la cultura.

💡 **Tip:** Si velocidad varía mucho, investigar: ¿interrupciones? ¿estimaciones inconsistentes? ¿dependencias?

⏰ **Timing:** 10 min (6 min concepto, 4 min cálculo)

---

### **Slide 19: Forecasting con Velocidad** (7 min)

**Objetivos:**
- Enseñar cálculo de forecast
- Mostrar rango de incertidumbre
- Conectar con Cono de Incertidumbre (Clase 1)

**Script sugerido:**

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

[AJUSTES dinámicos]

**Durante ejecución:**

Después de Sprint 6:
- Completamos 22 pts (menos que esperado)
- Re-forecast: 98 pts restantes / 22 = 4.5 sprints

**Nuevo forecast:** Sprint 6 + 4.5 = **Sprint 10-11** (antes era Sprint 10)

[VER GRÁFICO Burndown Chart en slide]

Línea ideal (25 pts/sprint) vs realidad (fluctúa).

Re-forecasting cada sprint basado en velocidad REAL.

[BENEFICIOS]

**1. Basado en evidencia:** No es adivinar, es medir

**2. Transparente:** Stakeholders ven progreso real

**3. Adaptable:** Forecast se ajusta con feedback empírico

**4. Honesto:** Rango de incertidumbre explícito

[LIMITACIONES]

**Velocidad asume:**
- ✅ Equipo estable (misma gente)
- ✅ Tipo de trabajo similar
- ✅ Sin cambios mayores (tecnología, proceso)

**Si algo cambia, velocidad histórica NO aplica:**
- Miembro clave sale → velocidad baja temporalmente
- Nueva tecnología → velocidad baja hasta aprender
- Interrupción mayor (prod issue) → velocidad baja ese sprint

[TRANSICIÓN]

OK, vimos Planning Poker + Velocidad.

Una pieza más: **Refinamiento Progresivo**."

---

**Preguntas para engagement:**

1. "¿Preferirían decir '10 semanas' o '8-14 semanas'? ¿Por qué?"
2. "¿Qué harían si después de 2 sprints la velocidad es MUY diferente a histórica?"
3. "¿Cómo explicarían forecast a un CEO que quiere 'una fecha'?"

**Tips para el facilitador:**

✅ **Enfatizar:** Forecast es proyección, NO compromiso.

✅ **Analogía útil:** "Es como GPS: 'llegarás en 25 minutos' pero puede ser 20-30 según tráfico."

⚠️ **Evitar:** Tratar forecast como promesa. Es planificación con información actual.

💡 **Tip:** Actualizar forecast cada sprint en dashboard visible a stakeholders.

⏰ **Timing:** 7 min (4 min cálculo, 3 min rango)

---

### **Slide 20: Refinamiento Progresivo** (5 min)

**Objetivos:**
- Explicar concepto de refinar estimaciones en olas
- Conectar con Cono de Incertidumbre
- Evitar over-planning

**Script sugerido:**

"Una pregunta común:

**'¿Tengo que estimar TODO el backlog con Planning Poker?'**

**Respuesta: NO.**

Ahí entra **Refinamiento Progresivo** (Progressive Refinement).

[CONCEPTO]

Estimaciones tienen **niveles de detalle** según cercanía:

**Historias en próximo sprint:**
- Estimación detallada (Planning Poker, Fibonacci)
- Criterios de aceptación completos
- Suposiciones explícitas

**Historias en próximos 2-3 sprints:**
- Estimación burda (T-Shirt Sizing)
- Criterios de aceptación básicos

**Historias en backlog lejano (3+ meses):**
- Épicas sin dividir
- Estimación muy burda ('grande', 'mediana')
- Criterios vagos (está OK)

[VER DIAGRAMA en slide - Cono de refinamiento]

**Por qué esto funciona:**

¿Recuerdan Cono de Incertidumbre (Clase 1)?

Al INICIO del proyecto: ±400% variación.
Cerca de ENTREGA: ±10% variación.

[PAUSA]

**NO tiene sentido estimar con precisión algo que está a 6 meses.**

Porque:
- Requisitos cambiarán
- Tecnología cambiará
- Equipo aprenderá cosas nuevas
- Prioridades cambiarán

Estimar detallado ahora es **trabajo desperdiciado**.

[ESTRATEGIA]

**Backlog Grooming continuo:**

**Cada 1-2 semanas:**
- Refinar historias que PODRÍAN entrar en próximos 2 sprints
- Dividir épicas grandes
- Estimar con Planning Poker
- Aclarar criterios de aceptación

**Resultado:**
- Siempre tenemos 20-30 historias 'ready' (refinadas)
- Resto del backlog es burdo
- Evitamos over-planning

[EJEMPLO]

**Backlog de 100 historias:**

**Sprint Actual (Sprint 10):**
- 6 historias en progreso (estimadas Fibonacci)

**Próximos 2 sprints:**
- 20 historias refinadas (Fibonacci)
- Criterios de aceptación completos

**Próximos 3-6 meses:**
- 30 historias con T-Shirt Sizing
- Criterios básicos

**Backlog lejano:**
- 44 épicas sin dividir
- 'Grande', 'Mediana', 'Pequeña'

**Total forecast:**
- Próximos 2 sprints: 50 pts (detallado)
- Resto: ~500 pts (burdo) → ~20 sprints

Suficiente para planificar roadmap SIN desperdiciar esfuerzo.

[CONECTAR con CCPM - Preview Clase 3]

Refinamiento Progresivo conecta con concepto que veremos en Clase 3:

**NO planificar todo al detalle desde el inicio.**

En CCPM (Critical Chain), vamos a llevar esto más lejos:
- Planificar detallado solo la Cadena Crítica
- Resto: alto nivel
- Agregrar Buffers para absorber incertidumbre

[TRANSICIÓN]

OK, completamos el contenido técnico de Clase 2.

Ahora: mejores prácticas y síntesis."

---

**Preguntas para engagement:**

1. "¿Cuánto adelante deberían refinar el backlog?"
2. "¿Qué riesgos ven en NO refinar suficiente? ¿En refinar DEMASIADO?"
3. "¿Cómo convencerían a un PM que quiere 'plan detallado de 12 meses'?"

**Tips para el facilitador:**

✅ **Enfatizar:** Refinamiento Progresivo es eficiencia, no pereza.

✅ **Analogía útil:** "Como GPS: planifica ruta completa (burdo), pero detalles solo próximas cuadras. Ruta cambia con tráfico."

⚠️ **Evitar:** Dar regla rígida ('SIEMPRE 2 sprints adelante'). Depende del contexto.

💡 **Tip:** Si stakeholders piden plan detallado 12 meses, dar forecast con rango amplio (±50%) para mostrar inutilidad.

⏰ **Timing:** 5 min (3 min concepto, 2 min ejemplo)

---

### **Slide 21: Mejores Prácticas de Estimación Ágil** (7 min)

**Objetivos:**
- Consolidar lecciones en lista actionable
- Anticipar problemas comunes
- Tips prácticos

**Script sugerido:**

"Ahora un checklist de mejores prácticas.

**10 Tips para Estimación Ágil Efectiva:**

---

**1. Establecer Baseline Clara**

✅ **Hacer:** Elegir historia 'estándar' de 3 puntos que todos conocen
✅ **Ejemplo:** 'Endpoint CRUD completo' o 'Feature simple end-to-end'
❌ **Evitar:** Estimar sin referencia, cada quien con criterio diferente

---

**2. Votar Simultáneamente**

✅ **Hacer:** Todos revelan cartas al mismo tiempo
❌ **Evitar:** Votar secuencialmente (primero habla senior, todos siguen)

**Por qué:** Previene 'anchoring bias'

---

**3. Debatir Extremos, Siempre**

✅ **Hacer:** Voto más bajo y más alto explican
❌ **Evitar:** Promediar sin discutir

**Por qué:** Los extremos revelan suposiciones ocultas

---

**4. Timeboxear (Máx 10 min/historia)**

✅ **Hacer:** Si no converge en 10 min, marcar '?' y seguir
❌ **Evitar:** Debates de 30 min sobre 3 vs 5 puntos

**Por qué:** Perfección es enemiga de suficientemente bueno

---

**5. Incluir Todo el Equipo**

✅ **Hacer:** Devs, testers, UX, DevOps votan
❌ **Evitar:** Solo devs estiman

**Por qué:** Cada rol ve complejidad diferente

---

**6. Estimar Complejidad, No Tiempo**

✅ **Hacer:** '¿Esto es más complejo que baseline?'
❌ **Evitar:** '¿Cuántas horas?' (volver a horas destruye el concepto)

**Por qué:** Story Points son relativos, no absolutos

---

**7. No Comparar Velocidades Entre Equipos**

✅ **Hacer:** Cada equipo mide SU velocidad
❌ **Evitar:** 'Equipo A hace 40 pts, equipo B hace 25, B es peor'

**Por qué:** Puntos son relativos, no universales

---

**8. Re-calibrar Periodicamente**

✅ **Hacer:** Cada 3-6 meses, revisar baseline (¿sigue siendo 3 pts?)
❌ **Evitar:** Nunca revisar, estimaciones derivan

**Por qué:** Equipo mejora, tecnología cambia, baseline debe ajustarse

---

**9. Aceptar Incertidumbre**

✅ **Hacer:** Dar rangos ('10-14 semanas'), usar '?' cuando no se sabe
❌ **Evitar:** Falsa precisión ('12.3 semanas')

**Por qué:** Honestidad > Precisión falsa

---

**10. Refinar Continuamente**

✅ **Hacer:** Backlog Grooming cada 1-2 semanas
❌ **Evitar:** Estimar todo el backlog una vez, nunca revisar

**Por qué:** Refinamiento Progresivo previene desperdicio

---

[ERRORES COMUNES]

**Error 1:** 'Esta historia es 2 días, entonces 2 puntos'
- Puntos NO son días. Destruye el concepto.

**Error 2:** 'No cabe en el sprint, estimemos 5 en vez de 8'
- NO manipular estimación para que 'quepa'. Es mentirse.

**Error 3:** 'Senior dev dice 3, debe ser 3'
- Expertismo mata conocimiento distribuido.

**Error 4:** 'Velocidad bajó, equipo es flojo'
- Velocidad NO es KPI de performance. Puede bajar por deuda técnica, interrupciones, etc.

**Error 5:** 'Planificar 12 meses con Fibonacci'
- Over-planning. Usar Refinamiento Progresivo.

[SEÑALES de que funciona bien]

✅ Debates son cortos pero informativos
✅ Descubren suposiciones en cada sesión
✅ Velocidad se estabiliza después de 5 sprints
✅ Pocas sorpresas mid-sprint ('no sabíamos que...')
✅ Equipo confía en sus estimaciones

[SEÑALES de problemas]

⚠️ Planning Poker toma 3+ horas (debería ser 60-90 min)
⚠️ Siempre votan lo mismo (no hay debate)
⚠️ Velocidad fluctúa wildly (15, 35, 18, 40...)
⚠️ Historias nunca se completan (todo queda 80%)
⚠️ Stakeholders no entienden Story Points (no se explicó bien)

[TRANSICIÓN]

OK, tenemos todas las piezas de Estimación Ágil.

Ahora: ¿Cómo se compara con los otros métodos?"

---

**Preguntas para engagement:**

1. "¿Cuál de los 10 tips les parece más importante?"
2. "¿Cuál error común les pasó?"
3. "¿Qué señal de problema tienen en su equipo actual?"

**Tips para el facilitador:**

✅ **Enfatizar:** Estos tips vienen de experiencia real, no teoría.

✅ **Invitar ejemplos:** "¿Alguien vivió el Error 2 (manipular estimación)?"

⚠️ **Evitar:** Hacer parecer que Ágil es 'perfecto'. Tiene problemas también.

💡 **Tip:** Imprimir los 10 tips como poster para sala de Planning Poker.

⏰ **Timing:** 7 min (5 min tips, 2 min errores)

---

### **Slide 22: Cuadro Comparativo - PERT vs Ágil vs CCPM** (8 min)

**Objetivos:**
- Sintetizar todos los métodos vistos
- Mostrar cuándo usar cada uno
- Preparar para Clase 3

**Script sugerido:**

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

[ANALOGÍA]

Es como preguntar: '¿Qué es mejor: martillo, destornillador, o sierra?'

Depende de qué estás construyendo.

---

**Proyecto grande, regulado, fases claras:**
→ **PERT/CPM**

Ejemplo: Construcción de puente
- Fases: diseño → permisos → excavación → pilares → estructura → terminación
- Poco espacio para 'iteración'
- PERT da timeline con varianza

---

**Software con requisitos emergentes, equipo ágil:**
→ **Ágil (Scrum, Planning Poker)**

Ejemplo: App móvil startup
- No sabemos qué quiere el usuario hasta probar
- Releases cada 2 semanas
- Planning Poker + Velocidad da forecast

---

**Múltiples proyectos, recursos compartidos, necesidad de velocidad:**
→ **CCPM (veremos Clase 3)**

Ejemplo: Empresa con 10 proyectos paralelos, equipos compartidos
- No puedes hacer PERT de cada proyecto independiente (ignora interdependencias)
- No puedes hacer Scrum puro (proyectos más grandes que sprints)
- CCPM gestiona cartera completa con buffers estratégicos

---

[PREVIEW Clase 3]

**En Clase 3 veremos:**

**CCPM (Critical Chain Project Management)**

La idea central:

**NO gestionar incertidumbre tarea por tarea.**

**Gestionar incertidumbre CENTRALIZADAMENTE con buffers agregados.**

[ANALOGÍA]

**PERT:** Cada tarea tiene 'colchón' individual
- Resultado: Se desperdicia (Parkinson, Estudiante)

**Ágil:** Iteraciones cortas previenen desperdicio
- Funciona para software, NO para proyectos con fases

**CCPM:** Quitar colchones individuales, agregar buffer AL FINAL
- Protege entrega sin permitir desperdicio
- Funciona para proyectos complejos con dependencias

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

**Preguntas para engagement:**

1. "¿Qué método usan en su organización actual?"
2. "¿Ven algún proyecto donde deberían cambiar de método?"
3. "¿Qué expectativas tienen de CCPM (Clase 3)?"

**Tips para el facilitador:**

✅ **Enfatizar:** NO hay método 'mejor', hay método apropiado para contexto.

✅ **Crear interés:** "Clase 3 va a mostrar cómo CCPM puede acortar timelines 20-30% sin agregar gente."

⚠️ **Evitar:** Decir que Ágil 'reemplaza' PERT. Son para contextos diferentes.

💡 **Tip:** Si grupo es escéptico de CCPM, decir: "Clase 3 tiene caso real que muestra cómo 4 tareas de 10 días c/u NO toman 40 días."

⏰ **Timing:** 8 min (6 min tabla, 2 min preview)

---

### **Slide 23: Síntesis de Clase 2** (5 min)

**Objetivos:**
- Recapitular puntos clave
- Conectar con Clase 1 y anticipar Clase 3
- Cerrar con mensajes clave

**Script sugerido:**

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

**Refinamiento Progresivo:**
- Estimar detallado solo lo cercano
- Backlog lejano: estimación burda
- Evita over-planning

---

**PARTE 3: Comparación y Preview (15 min)**

**PERT vs Ágil vs CCPM:**
- PERT: fases claras, regulado
- Ágil: alta incertidumbre, iterativo
- CCPM: múltiples proyectos, buffers centralizados

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

**5. Refinamiento Progresivo > Over-planning**
- Detallar solo lo cercano
- Backlog lejano puede ser burdo

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

**Preguntas finales:**

1. "¿Qué concepto de hoy les resultó más útil?"
2. "¿Qué van a aplicar el lunes en su trabajo?"
3. "¿Qué dudas tienen antes de Clase 3?"

**Tips para el facilitador:**

✅ **Cerrar con energía:** Clase 3 es el clímax, generar expectativa.

✅ **Recapitular conexiones:** Clase 1 → 2 → 3 es narrativa continua.

⚠️ **Evitar:** Apurarse en síntesis. Es consolidación crítica.

💡 **Tip:** Después de clase, enviar por email la tabla comparativa (PERT vs Ágil vs CCPM) como referencia.

⏰ **Timing:** 5 min (4 min síntesis, 1 min cierre)

---

### **Slide 24: Cierre y Preview Clase 3** (3 min)

**Objetivos:**
- Agradecer participación
- Anticipar Clase 3
- Motivar asistencia

**Script sugerido:**

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

**Tarea opcional antes de Clase 3:**

Si quieren adelantarse, lean:
- `doc/adminpro/09_Critical_Chain.pdf` (primeros 20 págs)
- O el libro 'Critical Chain' de Goldratt (novela, fácil de leer)

Pero NO es obligatorio. Clase 3 es self-contained.

---

**¡Nos vemos en Clase 3!**

**Preguntas finales antes de cerrar?"**

---

**Tips para el facilitador:**

✅ **Generar expectativa:** "Clase 3 tiene el 'aha!' moment más grande del curso."

✅ **Agradecer:** Participación hace la diferencia en formato remoto.

⚠️ **Evitar:** Terminar abruptamente. Dar espacio para preguntas finales.

💡 **Tip:** Enviar por email después de clase:
- Link a materiales
- Fecha/hora de Clase 3
- Lectura opcional
- Formulario de feedback

⏰ **Timing:** 3 min (2 min preview, 1 min cierre)

---

## 🎯 **FIN DE GUÍA PROFESOR CLASE 2 - PARTE 2**

---

## 📌 Resumen de PARTE 2

**Tiempo total cubierto:** 130 minutos (post-break de Clase 2)

**Slides cubiertas:** 8-24 (17 slides)

**Contenido creado:**

1. ✅ Estimación Ágil (Story Points, Fibonacci, T-Shirt) - 40 min
2. ✅ Planning Poker completo (caso HU-3, proceso, suposiciones) - 60 min
3. ✅ Velocidad y Forecasting - 17 min
4. ✅ Refinamiento Progresivo - 5 min
5. ✅ Mejores Prácticas - 7 min
6. ✅ Comparación PERT vs Ágil vs CCPM - 8 min
7. ✅ Síntesis y Cierre - 8 min

**Total:** 130 minutos + 15 min break = 145 minutos (segunda mitad de clase)

---

**Archivo completo:** `GUIA_PROFESOR_CLASE2_PARTE2.md`

**Continuación:** `GUIA_PROFESOR_CLASE3.md` (siguiente tarea)

---

**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 2.0 - Formato Remoto
**Fecha:** Enero 2025
