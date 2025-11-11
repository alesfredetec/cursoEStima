# Anexo 1: Ejercicios Interactivos y Guías de Facilitación

**Curso:** Estimación de Proyectos
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 1.0 - Enero 2025

---

## 📋 Índice de Contenidos

1. [Ejercicios de Clase 1: Ley de Parkinson](#ejercicios-clase-1)
2. [Ejercicios de Clase 2: Planning Poker Extendido](#ejercicios-clase-2)
3. [Ejercicios de Clase 3: CCPM Práctico](#ejercicios-clase-3)
4. [Guías de Facilitación](#guías-facilitación)

---

## 🎯 Ejercicios de Clase 1: Ley de Parkinson {#ejercicios-clase-1}

### Ejercicio 1A: Sopa de Letras - Demostración de Parkinson

**Ubicación del material:** `materiales_alumnos/EJERCICIO_PARKINSON_SOPA_LETRAS.md`

**Duración total:** 20-25 minutos
- Ejecución: Variable (3 min o 15 min según grupo)
- Debriefing: 15 minutos

**Objetivo pedagógico:**
Demostrar empíricamente que el tiempo asignado determina el tiempo consumido, no la complejidad de la tarea.

**Instrucciones para el facilitador:**

**PASO 1: Dividir grupos SIN revelar el propósito (5 min)**

```
"Vamos a hacer un ejercicio rápido. Los voy a dividir en 2 grupos
aleatoriamente. NO les voy a decir por qué todavía - esa es parte
del experimento."

Grupo A: Sala principal (o mitad izquierda)
Grupo B: Breakout room (o mitad derecha)

"Este ejercicio es INDIVIDUAL. No hablen entre ustedes."
```

**PASO 2: Asignar tiempos diferentes SIN que lo sepan (1 min)**

- **Grupo A:** "Tienen 15 minutos. Empiecen... ¡YA!"
- **Grupo B:** "Tienen 3 minutos. Empiecen... ¡YA!"

⚠️ **CRÍTICO:** NO mencionar que hay diferentes tiempos entre grupos.

**PASO 3: Monitorear en silencio**

Observa (pero no comentes):
- Grupo A (15 min): Trabajan con calma, dudan, corrigen, revisan
- Grupo B (3 min): Trabajan intensamente, sin dudar, escriben rápido

**PASO 4: Recoger resultados**

Al terminar el tiempo:
```
"TIEMPO. Dejen de escribir inmediatamente. ¿Cuántas palabras
encontraron?"
```

Anota en pizarra/pantalla compartida:
- Grupo A (15 min): Promedio típico 12-14 palabras de 18
- Grupo B (3 min): Promedio típico 10-13 palabras de 18

**PASO 5: La Revelación (10 min)**

```
"Ahora viene lo interesante.

Grupo A, ustedes tuvieron 15 minutos.
Grupo B, ustedes tuvieron solo 3 minutos.

[PAUSA - deja que procesen]

Miren los resultados:
- Grupo A: 12-14 palabras en 15 minutos
- Grupo B: 10-13 palabras en 3 minutos

Grupo B logró el 85-95% del resultado en solo 20% del tiempo.

¿Qué pasó?"
```

**Preguntas guiadas para debriefing:**

1. **"Grupo A, ¿qué hicieron con el tiempo extra?"**
   - Respuestas típicas: "Busqué palabras raras", "Revisé varias veces", "Dudé sobre algunas", "Me relajé al principio"

2. **"Grupo B, ¿cómo se sintieron con solo 3 minutos?"**
   - Respuestas típicas: "Presionado", "Enfocado", "Sin tiempo para pensar mucho", "Directo al grano"

3. **"¿Qué implica esto para proyectos reales?"**
   - Conexión: Tareas con mucho tiempo asignado se expanden (Parkinson)
   - Buffer distribuido se desperdicia
   - Presión de tiempo puede forzar foco

**Cierre del ejercicio:**

```
"Esto es la Ley de Parkinson en acción:

'El trabajo se expande hasta llenar el tiempo disponible.'

No es que el Grupo A fuera más lento o menos capaz.
Es que el TIEMPO ASIGNADO determinó cuánto tiempo USARON.

En proyectos de software:
- Una tarea de 2 días reales con 10 días asignados → toma 10 días
- La misma tarea con 3 días asignados → toma 3 días

El colchón 'de seguridad' no protege. Se DESPERDICIA."
```

---

### Ejercicio 1B: Vacaciones - Variante Creativa

**Ubicación del material:** `materiales_alumnos/EJERCICIO_PARKINSON_VACACIONES.md`

**Duración total:** 20-25 minutos

**Variante del ejercicio de Sopa de Letras** (usar uno u otro, no ambos)

**Ventajas de esta variante:**
- ✅ Más creativo (menos "escolar")
- ✅ No hay respuesta "correcta" (elimina ansiedad)
- ✅ Más fácil de adaptar a remoto (solo texto)

**Desventajas:**
- ❌ Puede ser más variable (personas con experiencia en planificación tienen ventaja)
- ❌ Menos "objetivo" (no hay 18 palabras fijas)

**Instrucciones:** Idénticas al Ejercicio 1A, pero con:
- Tarea: "Escribe 10 pasos para planificar vacaciones ideales"
- Métrica: Cantidad de pasos completados + nivel de detalle

**Resultados típicos:**
- Grupo A (15 min): 9-10 pasos con oraciones largas y detalladas
- Grupo B (3 min): 8-10 pasos con oraciones cortas y directas

**Punto clave:** Ambos grupos completan la tarea, pero A usa 5x más tiempo para 10-15% más contenido.

---

### Ejercicio 1C: Reflexión Post-Parkinson (NUEVO)

**Duración:** 10 minutos
**Modalidad:** Individual + Discusión grupal

**Instrucciones:**

Pide a los estudiantes que respondan por escrito (5 min):

```
1. Piensa en un proyecto reciente donde trabajaste.
   ¿Había "colchones de tiempo" ocultos en las tareas?

2. ¿Qué pasó con esos colchones?
   a) Se usaron para emergencias reales
   b) Se desperdiciaron en perfeccionismo o procrastinación
   c) No estoy seguro

3. ¿En tu organización actual, cómo reaccionan si alguien
   termina una tarea 3 días antes de lo estimado?
   a) Lo celebran y le dan la siguiente tarea
   b) Sospechan que la estimación estaba inflada
   c) El dev no reporta que terminó (para evitar más trabajo)
```

**Discusión grupal (5 min):**

Comparte respuestas anónimas. Típicamente:
- 70-80% responde (b) en pregunta 2: buffer se desperdició
- 50-60% responde (c) en pregunta 3: cultura tóxica de estimación

**Conexión con CCPM:**
```
"Estos patrones son por qué CCPM propone:
- Eliminar buffers ocultos en tareas
- Agregar buffer visible al final
- Cambiar la cultura: terminar antes es BUENO, no sospechoso"
```

---

## 🎯 Ejercicios de Clase 2: Planning Poker Extendido {#ejercicios-clase-2}

### Ejercicio 2A: Planning Poker con Backlog Completo

**Duración:** 45-60 minutos
**Modalidad:** Taller práctico grupal

El material base de Clase 2 incluye 5 historias de usuario (HU-1 a HU-5). Este anexo expande con historias adicionales.

#### Backlog Extendido: Módulo de Suscripciones

Usa este backlog si quieres practicar Planning Poker más allá de las 5 HUs básicas:

| ID | Historia de Usuario |
|----|---------------------|
| **HU-6** | Como usuario premium, quiero poder pausar mi suscripción por 1-3 meses, para no pagar cuando no uso el servicio pero mantener mi cuenta. |
| **HU-7** | Como usuario, quiero recibir un email 7 días antes de que se renueve mi suscripción, para decidir si quiero continuar. |
| **HU-8** | Como administrador, quiero un dashboard con métricas de churn (cancelaciones), para identificar problemas de retención. |
| **HU-9** | Como usuario, quiero poder cambiar mi plan (upgrade o downgrade) en cualquier momento, con ajuste prorrateado de precio. |
| **HU-10** | Como usuario que canceló, quiero poder exportar todos mis datos antes de que se eliminen, para cumplir con mi derecho a portabilidad (GDPR). |

#### Proceso de Facilitación (60 min)

**Setup (5 min):**
```
"Vamos a hacer Planning Poker real con 5 historias adicionales.

Roles:
- Yo (facilitador) seré el Product Owner
- Todos ustedes son el equipo de desarrollo
- Usen las cartas de Fibonacci: 0, 1, 2, 3, 5, 8, 13, 21

Recordatorio: HU-2 (Login) vale 3 puntos - esa es nuestra referencia."
```

**Por cada historia (10 min/historia):**

1. **PO lee historia** (1 min)
2. **Clarificación** (2 min) - equipo hace preguntas
3. **Votación simultánea** (30 seg)
4. **Discusión de extremos** (3 min)
5. **Re-votación si necesario** (30 seg)
6. **Consenso final** (1 min)

**Guía de facilitación para cada HU:**

**HU-6: Pausar suscripción**

Preguntas típicas:
- "¿La base de datos ya tiene campo 'status'?" → Sí, pero necesita nuevo valor 'paused'
- "¿Hay lógica para no cobrar?" → Necesita ajustar billing schedule
- "¿Qué pasa con features durante pausa?" → Acceso bloqueado temporalmente

Estimación esperada: **5 puntos**
- Más complejo que login (3) por lógica de billing
- Menos que payment completo (13) porque infra de subs ya existe

**HU-7: Email de renovación**

Preguntas típicas:
- "¿Ya tenemos email service?" → Sí (usado en HU-3 password reset)
- "¿Es solo un template nuevo?" → Sí, pero necesita scheduled job
- "¿Qué pasa si usuario cancela después del email?" → Solo informativo, no afecta

Estimación esperada: **3 puntos**
- Similar a login porque reutiliza infraestructura
- Template + cron job semanal

**HU-8: Dashboard de churn**

Preguntas típicas:
- "¿Incluye gráficos?" → Sí, línea de tiempo + tasas
- "¿Datos históricos o solo forward?" → Necesita calcular retroactivo 6 meses
- "¿Exportable?" → No en v1, solo visualización

Estimación esperada: **8 puntos**
- Requiere queries complejas (calcular churn rate)
- Frontend con gráficos (nueva librería?)
- Posible performance issue con mucho histórico

**HU-9: Cambiar plan con prorrateo**

⚠️ **HISTORIA TRAMPA** - parece simple pero es compleja

Preguntas típicas:
- "¿Cómo calculamos prorrateo?" → Días restantes × diferencia de precio
- "¿Upgrade inmediato o próximo ciclo?" → Inmediato, downgrade próximo ciclo
- "¿Qué pasa si cambian 5 veces en un mes?" → Necesita validación/límite
- "¿Refund en downgrade?" → Crédito a favor, no refund

Estimación esperada: **13 puntos** (¡sorpresa!)
- Lógica financiera compleja
- Casos edge múltiples
- Necesita audit trail
- Testing exhaustivo para billing

**Momento de aprendizaje:**
```
"¿Ven cómo una historia que PARECE simple ('cambiar plan')
terminó siendo 13 puntos?

Esto es POR QUÉ hacemos Planning Poker. Sin la discusión,
alguien hubiera dicho '3 puntos - es solo cambiar un campo.'

La votación alta (13) forzó la conversación que expuso la
complejidad oculta."
```

**HU-10: Exportar datos (GDPR)**

Preguntas típicas:
- "¿En qué formato?" → JSON + CSV opciones
- "¿Incluye qué datos?" → Todo: perfil, suscripciones, pagos, uso
- "¿Es async?" → Sí, job en background + email cuando listo
- "¿Hay límite de tiempo para descargar?" → Link válido 7 días

Estimación esperada: **8 puntos**
- Similar a dashboard (8) en complejidad
- Múltiples tablas, formateo, zip file
- Background job + email notification

#### Resumen Final del Ejercicio (5 min)

**Velocidad hipotética:**

Si este equipo tiene velocidad de 25 puntos/sprint:

```
Backlog completo estimado:
HU-1: (no estimada en taller, asumimos 5)
HU-2: 3 (referencia)
HU-3: 8 (password reset)
HU-4: 5 (reporte admin)
HU-5: 13 (payment)
HU-6: 5 (pausar suscripción)
HU-7: 3 (email renovación)
HU-8: 8 (dashboard churn)
HU-9: 13 (cambiar plan)
HU-10: 8 (exportar datos)

Total: 71 puntos

Forecast:
71 ÷ 25 = 2.84 sprints ≈ 3 sprints (6 semanas en sprints de 2 semanas)
```

**Pregunta de cierre:**
```
"Si no hubiéramos hecho Planning Poker, ¿cuánto hubieran estimado
este proyecto? ¿4 sprints? ¿5 sprints?

Planning Poker NO nos hizo más rápidos. Nos hizo más HONESTOS
sobre la complejidad real."
```

---

### Ejercicio 2B: Detectar Estimaciones Infladas

**Duración:** 15 minutos
**Modalidad:** Análisis de caso

**Escenario:**

Un equipo tiene esta velocidad histórica:
- Sprint 1: 23 puntos
- Sprint 2: 27 puntos
- Sprint 3: 21 puntos (tuvieron 2 días feriados)
- Sprint 4: 25 puntos
- Sprint 5: 26 puntos

**Velocidad promedio: 24.4 puntos/sprint**

Ahora están estimando un nuevo módulo:

| Historia | Estimación | Justificación |
|----------|-----------|---------------|
| HU-A | 21 puntos | "Es muy compleja, tiene machine learning" |
| HU-B | 13 puntos | "Integración con sistema legacy" |
| HU-C | 8 puntos | "CRUD normal pero con validaciones" |

**Preguntas para discusión:**

1. **¿HU-A (21 puntos) es realista?**
   - Análisis: 21 puntos = 87% de un sprint COMPLETO
   - ¿Realmente esta historia es equivalente a TODO el trabajo de 2 semanas?
   - Si es TAN grande, ¿debería splitarse?

2. **¿Qué preguntas harías sobre HU-A?**
   - ¿El modelo ML ya está entrenado o hay que entrenarlo?
   - ¿Hay expertise de ML en el equipo?
   - ¿Se puede separar en "integrar modelo existente" (5) + "entrenar modelo" (13)?

3. **¿HU-B (13 puntos) tiene señales de padding?**
   - "Sistema legacy" es un red flag común para inflar estimación
   - ¿Qué específicamente del legacy es complejo?
   - ¿Ya integraron con ese sistema antes?

**Respuestas guiadas:**

```
"Cuando vean estimaciones muy altas, pregunten:

1. ¿Es realmente UNA historia o varias disfrazadas?
2. ¿La justificación es específica o genérica?
   - ❌ 'Es complejo' → vago
   - ✅ 'Necesita validar 15 reglas de negocio interdependientes' → específico
3. ¿Hay precedente? Si hicieron algo similar antes, ¿cuánto tomó?

Estimaciones infladas no son malicia - son miedo al castigo.
Planning Poker con cultura de confianza reduce este problema."
```

---

## 🎯 Ejercicios de Clase 3: CCPM Práctico {#ejercicios-clase-3}

### Ejercicio 3A: Caso A-B-C-D Paso a Paso (Repaso)

Este es el caso principal de Clase 3. El slide deck ya lo incluye, pero aquí está la **guía de facilitación detallada** para maximizar el "momento aha!".

#### Setup del Problema (5 min)

**Proyecto:** Implementar nuevo módulo de reporting

| Tarea | Descripción | Depende de | Duración (inflada) | Recurso |
|-------|-------------|------------|-------------------|---------|
| **A** | Diseñar esquema de base de datos | - | 10 días | Juan (DB) |
| **B** | Implementar backend API | A | 10 días | Ana (Backend) |
| **C** | Diseñar UI/UX | A | 5 días | Pedro (Designer) |
| **D** | Implementar frontend | C | 10 días | Ana (Frontend) |

**Detalles clave:**
- Ana hace TANTO B como D (restricción de recurso)
- Duraciones incluyen padding "por las dudas"

#### Paso 1: CPM Tradicional (10 min)

**Pregunta:** "Calculen la Ruta Crítica ignorando recursos"

Rutas posibles:
- Ruta 1: A → B = 10+10 = 20 días
- Ruta 2: A → C → D = 10+5+10 = 25 días

**Ruta Crítica (CPM):** A → C → D = **25 días**

```
Facilitador: "Perfecto. CPM dice 25 días.
¿Cuándo pueden empezar a trabajar?"

Respuesta típica: "¡Ahora mismo!"

Facilitador: "OK, arranquen el cronómetro ficticio..."
```

#### Paso 2: El Problema Oculto (5 min)

```
Facilitador dibuja diagrama en pizarra/pantalla:

Día 1-10: Juan hace A
Día 11:   A termina
Día 12-16: Pedro hace C (5 días)
Día 12-21: Ana hace B (10 días) ← EMPIEZA PARALELO

[PAUSA dramática]

Día 17: Pedro termina C
Día 17: ¿Ana puede empezar D?

[Espera respuesta]

NO. Ana está ocupada haciendo B hasta día 21.

Día 22-31: Ana hace D (10 días)

DURACIÓN REAL: 31 días, no 25
```

**Momento de enseñanza:**
```
"CPM calculó 25 días porque asume RECURSOS ILIMITADOS.

'A y C pueden ir en paralelo' es cierto...
SOLO si diferentes personas las hacen.

Pero Ana hace B y D. Esa restricción de recurso ALARGA
el proyecto 6 días.

Esto es lo que Goldratt llamó la Cadena Crítica."
```

#### Paso 3: Calcular Cadena Crítica Real (10 min)

**Pregunta:** "Ahora consideren recursos. ¿Cuál es la secuencia MÁS LARGA?"

Cadena Crítica = **A → B → D** (Ana no puede hacer B y D en paralelo)
- A: 10 días (Juan)
- B: 10 días (Ana)
- D: 10 días (Ana)
- Total: **30 días**

(C queda fuera porque termina antes que B y tiene holgura)

```
Facilitador: "30 días es la Cadena Crítica REAL.

¿Es mejor que CPM (25)? No - es PEOR.
Pero es HONESTA. Refleja la realidad."
```

#### Paso 4: Aplicar CCPM - Eliminar Padding (15 min)

**Pregunta:** "¿Estas duraciones (10, 10, 5, 10) tienen padding oculto?"

```
Facilitador: "Pregunto diferente:

Si Juan dice 'Tarea A toma 10 días', ¿cuál es la probabilidad
de que termine en EXACTAMENTE 10 días?"

Respuestas típicas: "30%", "40%", "50%"

Facilitador: "Exacto. Esos 10 días ya incluyen colchón.

CCPM dice: 'Dame la estimación con 50% de probabilidad.'

Juan: 'Con 50% probabilidad, tomo 5 días.'
Ana (B): '5 días'
Pedro (C): '3 días'
Ana (D): '5 días'"
```

**Cadena Crítica agresiva:**
- A: 5 días
- B: 5 días
- D: 5 días
- Total: **15 días**

**Tiempo cortado:** 30 - 15 = 15 días

#### Paso 5: Agregar Buffers (10 min)

**Project Buffer:** 50% × 15 días cortados = 7.5 ≈ **8 días**

**Timeline CCPM:**
- Cadena Crítica: 15 días
- Project Buffer: 8 días
- **Total: 23 días**

**Feeding Buffer para C:**
C (3 días agresivos) alimenta a D.
Cortado: 5 → 3 = 2 días
FB = 50% × 2 = **1 día**

#### Paso 6: La Revelación Final (5 min)

**Comparación:**

| Enfoque | Timeline | Protección |
|---------|----------|------------|
| **CPM (teórico)** | 25 días | ❌ Imposible (ignora recursos) |
| **CPM real** | 31 días | ⚠️ Holgura en C (vulnerable a Parkinson) |
| **Tradicional con padding** | 30 días | ❌ Padding en cada tarea (Parkinson come todo) |
| **CCPM** | **23 días** | ✅ Buffer agregado de 8 días (visible, gestionado) |

```
Facilitador: "CCPM es 23% más rápido que el enfoque tradicional (30 días).

¿Cómo? NO estimando mejor. NO trabajando más horas.

Simplemente:
1. Quitando el padding que se iba a desperdiciar
2. Poniéndolo donde SÍ protege

Mismo equipo. Mismo trabajo. 7 días menos."

[PAUSA para que procesen]

"Este es el 'momento aha' de CCPM."
```

---

### Ejercicio 3B: Fever Chart - Interpretar Escenarios (NUEVO)

**Duración:** 20 minutos
**Modalidad:** Análisis de casos

Presenta 3 proyectos en diferentes estados del Fever Chart:

#### Escenario 1: "El Proyecto Verde"

```
Datos:
- Cadena Crítica: 50% completada
- Project Buffer: 15% consumido
- Posición en Fever Chart: Zona VERDE
```

**Pregunta:** "¿Qué acciones debe tomar el PM?"

**Respuesta esperada:**
- ✅ Continuar sin intervención
- ✅ Monitoreo de rutina
- ❌ NO agregar recursos
- ❌ NO presionar al equipo

**Punto de enseñanza:**
```
"Zona verde NO significa 'sin problemas.'
Significa 'dentro de expectativa normal.'

Buffer se consume porque PARA ESO ESTÁ.
15% de consumo en 50% de progreso es PERFECTO."
```

#### Escenario 2: "El Proyecto Amarillo"

```
Datos:
- Cadena Crítica: 40% completada
- Project Buffer: 55% consumido
- Posición: Zona AMARILLA (cerca de línea ideal)
- Tendencia: Últimas 2 semanas consumieron 25% del buffer
```

**Pregunta:** "¿Qué hace el PM?"

**Respuesta esperada:**
- ⚠️ Investigar causas del consumo acelerado
- ⚠️ Daily standups más frecuentes
- ⚠️ Identificar si hay bloqueos ocultos
- ✅ AÚN no agregar recursos (prematuro)

**Análisis:**
```
"40% completo, 55% buffer consumido.

Si proyectamos linealmente:
- 100% completo → buffer 100%+ consumido ❌

Acción: Identificar QUÉ está causando retrasos.
¿Es una tarea específica? ¿Un recurso bloqueado?

NO es momento de pánico, pero SÍ de atención."
```

#### Escenario 3: "El Proyecto Rojo"

```
Datos:
- Cadena Crítica: 30% completada
- Project Buffer: 80% consumido
- Posición: Zona ROJA (muy por encima de línea ideal)
- Tendencia: Acelerando hacia 100% buffer
```

**Pregunta:** "¿Qué hace el PM INMEDIATAMENTE?"

**Respuesta esperada:**
- 🚨 Reunión de crisis con stakeholders HOY
- 🚨 Analizar si hay forma de acortar tareas restantes
- 🚨 Considerar agregar recursos (solo si ayuda)
- 🚨 Evaluar re-negociar alcance o fecha

**Decisiones posibles:**

1. **Agregar recursos (solo si útil):**
   - ✅ SI: Tarea paralelizable, recurso aporta valor inmediato
   - ❌ NO: Tarea en Knowledge Transfer (agregar gente ralentiza)

2. **Reducir alcance:**
   - Identificar features no-críticas
   - Mover a fase 2

3. **Extender deadline:**
   - Negociar con cliente
   - Usar buffer si hay buffers de otros proyectos (gestión de cartera)

**Punto clave:**
```
"Zona roja con 30% completo es SEÑAL DE ALARMA TEMPRANA.

Sin Fever Chart, te enteras del problema en el día 80 de 100.
Con Fever Chart, te enteras en día 30.

Esos 50 días extra de anticipación pueden SALVAR el proyecto."
```

---

## 📚 Guías de Facilitación {#guías-facilitación}

### Gestión de Tiempo en Talleres

**Problema común:** Los ejercicios se extienden y el curso se atrasa.

**Solución:**

1. **Timeboxing estricto:**
   - Usa un timer visible (online: timer.google.com)
   - Avisa: "Quedan 2 minutos"
   - Corta EN PUNTO (incluso si no terminaron)

2. **Priorización:**
   - Si te quedas sin tiempo, SALTA teoría adicional
   - NUNCA cortes ejercicios prácticos (son el núcleo del aprendizaje)

3. **Gestión de preguntas:**
   - "Gran pregunta. La respondo en 1 minuto y luego seguimos."
   - Si es larga: "Anotémosla para el Q&A final."

### Manejo de Grupos Difíciles

#### Tipo 1: "El Escéptico Agresivo"

**Comportamiento:**
> "Esto no funciona en el mundo real. En mi empresa probamos Agile y fue un desastre."

**Respuesta:**

```
"Entiendo tu experiencia. ¿Puedes ser más específico sobre qué falló?"

[Escucha]

"OK, suena a que [problema X] fue el issue. Eso NO es un problema
de Agile/CCPM en sí, es un problema de implementación.

[Explica la diferencia]

Para este curso, te pido: entiende primero CÓMO funcionan estos métodos
en su forma ideal. Luego podemos discutir adaptaciones para
contextos complejos."
```

**Clave:** Validar experiencia, pero no dejar que secuestre la clase.

#### Tipo 2: "El Que Sabe Todo"

**Comportamiento:**
> "Ah sí, yo uso Story Points hace 10 años. También hago estimación por
> analogía, planning poker modificado, velocity tracking con..."

**Respuesta:**

```
"¡Excelente! Tu experiencia será muy valiosa. ¿Podrías compartir
un ejemplo de [X] al final de este bloque? Me encantaría que el
grupo aprenda de tu experiencia práctica."
```

**Clave:** Canalizar su energía para CONTRIBUIR, no dominar.

#### Tipo 3: "El Silencioso Perdido"

**Comportamiento:**
- Cámara apagada (si remoto)
- No participa nunca
- Posiblemente no entiende pero no pregunta

**Respuesta:**

```
"Voy a hacer un ejercicio rápido en breakout rooms de 2-3 personas.
[Asigna al silencioso con alguien conversador]

Durante el break:
'Hola [Nombre], ¿cómo vas con el contenido? ¿Hay algo confuso que
pueda clarificar?'"
```

**Clave:** Crear espacios 1-on-1 o small group donde se sientan seguros de hablar.

---

### Adaptaciones para Contextos Específicos

#### Adaptación para equipos NO de software

Si tu audiencia es construcción, manufactura, marketing, etc.:

**Ejemplo de Planning Poker adaptado:**

En lugar de "Historias de usuario", usa:
- **Construcción:** Tareas de obra (instalar plomería, electrical, drywall)
- **Marketing:** Campañas (landing page, email series, video ad)
- **Manufactura:** Procesos (setup de máquina, producción lote, QA)

**Ejemplo CCPM adaptado (Construcción):**

```
Proyecto: Construir casa

Tarea A: Cimientos (10 días → 5 días agresivo)
Tarea B: Estructura (15 días → 8 días agresivo)
Tarea C: Instalaciones (20 días → 10 días agresivo)
Tarea D: Terminaciones (10 días → 5 días agresivo)

Project Buffer: 14 días (50% del cortado)
```

**Punto clave:** Los PRINCIPIOS son universales, los ejemplos se adaptan.

---

## ✅ Checklist del Facilitador

Antes de cada clase:

**24 horas antes:**
- [ ] Slides abiertos y navegados (verificar que funcionen)
- [ ] Materiales de ejercicios descargados
- [ ] Timer configurado
- [ ] Breakout rooms configurados (si remoto)
- [ ] Ejemplos adicionales preparados para tu industria

**1 hora antes:**
- [ ] Tech check (pantalla compartir, audio, video)
- [ ] Abrir slides en pantalla secundaria
- [ ] Tener agua cerca
- [ ] Silenciar notificaciones

**Durante la clase:**
- [ ] Tomar notas de preguntas frecuentes (para mejorar próxima vez)
- [ ] Observar lenguaje corporal / chat (detectar confusión)
- [ ] Ajustar velocidad según engagement

**Después de la clase:**
- [ ] Enviar materiales complementarios prometidos
- [ ] Responder preguntas del chat que quedaron pendientes
- [ ] Actualizar guía con aprendizajes

---

## 📞 Contacto y Soporte

**Instructor:** Alejandro Sfrede
**Área:** Arquitectura
**Email:** [tu_email_aquí]

**Repositorio del curso:**
`C:\tmp\cursoEStima\`

**Materiales adicionales:**
- `materiales_alumnos/` - Material de lectura para estudiantes
- `materiales_facilitador/` - Guías del profesor con scripts detallados
- `anexos/` - Este documento y otros anexos complementarios

---

**Versión:** 1.0
**Última actualización:** Enero 2025
**Licencia:** Material educativo interno

---

¡Éxito con tus talleres! 🎓
