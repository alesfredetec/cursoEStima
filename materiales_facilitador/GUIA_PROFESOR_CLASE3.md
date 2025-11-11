# Guía del Profesor - Clase 3: Cadena Crítica (CCPM)
## PARTE 1: Introducción a CCPM y Gestión de Buffers (Pre-Break)

**Duración:** 90 minutos (primera mitad de 180 min totales)
**Formato:** Remoto / Teórico con demostraciones visuales

---

## 📋 Contenido de Esta Parte

| Slide | Tema | Duración |
|-------|------|----------|
| 1 | Portada: Cadena Crítica (CCPM) | 2 min |
| 2 | Agenda de la Clase | 3 min |
| 3 | Eliyahu Goldratt y Teoría de Restricciones | 8 min |
| 4 | El Problema que Goldratt Vio en CPM | 10 min |
| 5 | Cadena Crítica vs Ruta Crítica | 10 min |
| 6 | Los 3 Principios Fundamentales de CCPM | 12 min |
| 7 | Holgura vs Buffer | 10 min |
| 8 | Los 3 Tipos de Buffers | 12 min |
| 9 | Dimensionamiento de Buffers | 8 min |
| 10 | Ejemplo Visual de Buffers | 10 min |
| 10b | Diagrama Completo de los 3 Buffers (SVG) | 5 min |
| *BREAK* | ☕ Descanso | 15 min |

**Total Parte 1:** 90 minutos

---

## 🧠 Pensamiento Profundo: La Narrativa de Clase 3

### El Arco Dramático del Curso Completo

**Clase 3 es el CLÍMAX del curso.** Es donde todo converge:

**ACTO 1 (Clase 1): El Problema**
- Estimaciones fallan sistemáticamente
- Factores técnicos + psicológicos
- Cono de Incertidumbre: ±400% al inicio
- Malvavisco Challenge: suposiciones ocultas matan proyectos

**ACTO 2 (Clase 2): Intentos de Solución**
- PERT: reconocer incertidumbre con 3 puntos
- CPM: optimizar ruta crítica
- Ágil: iteración corta + velocidad empírica
- Planning Poker: exponer suposiciones

**ACTO 3 (Clase 3): La Solución**
- CCPM: cambio de paradigma completo
- NO gestionar tarea por tarea
- Gestionar el SISTEMA con buffers agregados
- 20-30% reducción de timeline sin agregar recursos

### El Cambio de Paradigma Central

**ANTES de CCPM:**
"Cada tarea necesita protección → agregar tiempo extra a cada una"

**DESPUÉS de CCPM:**
"Las tareas NO necesitan protección individual → el PROYECTO necesita protección estratégica"

**Analogía:**

Imagina un viaje en auto de 1000 km con 10 paradas:

**Enfoque tradicional (CPM con holgura):**
- Cada tramo tiene 30 min extra "por si acaso"
- Total: 10 tramos × 30 min = 5 horas de colchón
- Resultado: Ley de Parkinson → se gastan los 30 min en cada parada (café, baño, fotos)
- Timeline inflado, llegada igual de incierta

**Enfoque CCPM:**
- Cada tramo: tiempo agresivo (sin colchón)
- Buffer agregado: 2.5 horas AL FINAL
- Resultado: Viajamos rápido, usamos buffer SOLO si hay problema REAL (tráfico, pinchazo)
- Timeline 50% más corto, buffer visible y gestionable

### El Momento "Aha!" de Clase 3

**Ocurrirá en el Caso A-B-C-D (post-break):**

Participantes verán:
- 4 tareas de 10 días cada una (secuenciales)
- Timeline tradicional: 40 días (cada una con 100% buffer)
- Timeline CCPM: 20 días + 10 días buffer = 30 días
- **25% más rápido, MISMA protección**

**La revelación:** "¿Por qué nadie me enseñó esto antes?"

### Desafíos Pedagógicos de Clase 3

**1. Es contra-intuitivo:**
   - Eliminar protección individual SUENA peligroso
   - "¿Cómo voy a estimar con 50% probabilidad? Es muy arriesgado"
   - Facilitador debe mostrar que buffers agregados protegen MEJOR

**2. Es técnicamente más complejo que Clase 1-2:**
   - 3 tipos de buffers (no solo 1)
   - Cálculos de dimensionamiento
   - Fever Chart con zonas
   - Requiere paciencia y ejemplos claros

**3. Puede sonar "mágico" o "demasiado bueno":**
   - "¿En serio puedo acortar 20-30% sin agregar gente?"
   - Escepticismo natural
   - Facilitador debe anclar en EVIDENCIA: Goldratt, casos reales

**4. La tentación de sobre-simplificar:**
   - NO es solo "agregar un buffer al final"
   - ES un sistema completo: estimaciones agresivas + prohibir multitarea + monitoreo activo
   - Facilitador debe enfatizar que las 3 piezas son necesarias

### Objetivos Emocionales de la Primera Mitad

**Al final de los primeros 90 min, participantes deben:**

1. **Entender** la diferencia conceptual Ruta Crítica vs Cadena Crítica
2. **Ver claramente** por qué holgura distribuida falla (Parkinson)
3. **Comprender** los 3 tipos de buffers y sus propósitos
4. **Sentir curiosidad** por ver cómo funciona en un caso real (setup para post-break)
5. **Estar listos** para el momento "aha!" del Caso A-B-C-D

**NO debe ocurrir:**
- ❌ Confusión total ("no entendí nada")
- ❌ Escepticismo destructivo ("esto no puede funcionar")
- ❌ Aburrimiento ("es solo teoría")

**Si pasa algo de lo anterior, PARAR y re-explicar con más ejemplos.**

---

## 📖 Desglose Slide por Slide

---

### **Slide 1: Portada - Cadena Crítica (CCPM)** (2 min)

**Objetivos:**
- Dar bienvenida a Clase 3
- Posicionar CCPM como "La Solución"
- Generar expectativa

**Script sugerido:**

"Bienvenidos a Clase 3: **Cadena Crítica - CCPM**.

[PAUSA]

Si Clase 1 diagnosticó el problema...
Y Clase 2 presentó herramientas para mejorar estimación...

Clase 3 presenta **LA SOLUCIÓN sistémica**.

[LEER slide]

**Título:** Cadena Crítica (CCPM - Critical Chain Project Management)

**Subtítulo:** La Solución de Goldratt

**Objetivo:** Dominar la gestión de buffers y resolver el problema de la seguridad

[ÉNFASIS]

Hoy van a aprender el método que permite:

✅ Acortar timelines **20-30%** sin agregar recursos
✅ Aumentar tasa de proyectos on-time de **40% a 85%**
✅ Gestionar carteras de múltiples proyectos simultáneos

[PAUSA]

Y lo mejor:

**NO requiere estimar mejor.**

Requiere **GESTIONAR la incertidumbre mejor**.

[TRANSICIÓN]

Empecemos."

---

**Tips para el facilitador:**

✅ **Tono:** Confianza + humildad. Es poderoso pero no mágico.

✅ **Anticipar:** "Sonará contra-intuitivo al principio. Confíen en el proceso."

⚠️ **Evitar:** Over-selling. No decir "resuelve todo". Decir "resuelve problemas específicos muy bien".

⏰ **Timing:** 2 min (intro corta, ir directo a contenido)

---

### **Slide 2: Agenda de la Clase** (3 min)

**Objetivos:**
- Mostrar estructura de 3 horas
- Anticipar el taller (caso A-B-C-D)
- Establecer expectativas

**Script sugerido:**

"Aquí está nuestra agenda para hoy:

[LEER slide]

**1. Introducción a CCPM y Teoría de Restricciones** (45 min)
   - Quién es Goldratt
   - Qué problema vio en CPM
   - Cadena Crítica vs Ruta Crítica
   - Los 3 principios fundamentales

**2. Gestión de Buffers: Proyecto, Alimentación, Recursos** (45 min)
   - Tipos de buffers
   - Cómo dimensionarlos
   - Diagrama visual completo

**3. ☕ Break** (15 min)

**4. 🎮 Taller: Caso de Estudio CCPM Completo** (75 min)
   - Caso A-B-C-D paso a paso
   - Cálculos de Cadena Crítica
   - Dimensionamiento de buffers
   - Monitoreo con Fever Chart
   - **Este es el momento "aha!" del curso**

**5. Síntesis Final y Cuadro Comparativo** (15 min)
   - Comparar CPM vs Ágil vs CCPM
   - Cuándo usar qué
   - Cierre del curso completo

[ÉNFASIS]

**El taller (parte 4) es lo MÁS importante.**

Es donde todo hace click.

Van a ver:
- 4 tareas de 10 días cada una
- Timeline CPM: 40 días
- Timeline CCPM: 30 días (25% más rápido)
- **Misma protección, menos tiempo**

[PAUSA]

La primera mitad (hasta break) es SETUP teórico.

La segunda mitad es aplicación práctica.

[TRANSICIÓN]

Empecemos con la teoría."

---

**Preguntas para engagement:**

1. "¿Alguien escuchó de Goldratt o Teoría de Restricciones antes?"
2. "¿Qué expectativas tienen de CCPM?"

**Tips para el facilitador:**

✅ **Crear anticipación:** El taller es la joya, pero necesitamos fundamentos primero.

✅ **Gestionar tiempo:** Si la primera parte se extiende, recortar teoría, NO el taller.

⚠️ **Evitar:** Decir "la teoría es aburrida". Decir "la teoría es NECESARIA para entender el taller".

⏰ **Timing:** 3 min (2 min leer, 1 min enfatizar taller)

---

### **Slide 3: Eliyahu Goldratt y Teoría de Restricciones** (8 min)

**Objetivos:**
- Presentar a Goldratt (credibilidad)
- Introducir TOC (contexto)
- Preparar conceptualmente para CCPM

**Script sugerido:**

"Antes de entrar a CCPM, ¿quién lo inventó?

[VER slide - foto de Goldratt si hay]

**Eliyahu M. Goldratt**
- 1947-2011
- Físico israelí
- Consultor empresarial
- Autor best-seller

[PAUSA]

Goldratt es famoso por 2 libros:

**1. 'The Goal' (1984):**
- Novela de negocios (no es manual técnico)
- Protagonista: Alex Rogo, gerente de planta industrial
- Problema: Planta pierde dinero, va a cerrar
- Solución: Aplicar Teoría de Restricciones
- Resultado: Récord de ventas, planta salvada

**Best-seller mundial:**
- +6 millones de copias
- Traducido a 35 idiomas
- Usado en MBAs de todo el mundo

**2. 'Critical Chain' (1997):**
- Aplica TOC a gestión de proyectos
- Base conceptual de CCPM
- También es novela (fácil de leer)

[PAUSA - TEORÍA DE RESTRICCIONES]

**TOC - Theory of Constraints**

La idea central:

[LEER slide - caja destacada]

**'Una cadena no es más fuerte que su eslabón más débil'**

[ÉNFASIS]

Todo sistema tiene una RESTRICCIÓN que limita su rendimiento.

**Ejemplos:**

**Sistema: Fábrica**
- Restricción: Máquina más lenta (cuello de botella)
- Si esa máquina produce 100 unidades/hora, la fábrica NUNCA hará más de 100/hora
- No importa que otras máquinas hagan 500/hora
- Optimizar otras máquinas NO mejora el sistema

**Sistema: Restaurante**
- Restricción: Parrilla (solo caben 8 bifes simultáneos)
- Si parrilla es el cuello de botella, agregar meseros NO ayuda
- Agregar cocineros en otras estaciones NO ayuda
- Solo mejora el sistema: optimizar la parrilla

**Sistema: Proyecto de software**
- Restricción: Arquitecto senior (recurso único, compartido en 5 tareas)
- Si arquitecto está saturado, el proyecto se retrasa
- Agregar devs juniors NO ayuda (necesitan al arquitecto)
- Solo mejora: optimizar trabajo del arquitecto

[PAUSA]

**5 Pasos de TOC (Enfocamiento):**

1. **IDENTIFICAR** la restricción del sistema
2. **EXPLOTAR** la restricción (sacarle máximo provecho)
3. **SUBORDINAR** todo lo demás a la restricción
4. **ELEVAR** la restricción (si necesario, agregar capacidad)
5. Si la restricción se movió, **VOLVER al paso 1**

[APLICACIÓN A PROYECTOS]

**En un proyecto:**

La restricción es la **Cadena Crítica**:
- Secuencia de tareas + recursos que determina duración total
- Si la Cadena Crítica demora, TODO el proyecto demora
- Tareas fuera de Cadena Crítica: optimizarlas NO acorta proyecto

**CCPM aplica TOC:**

1. **Identificar:** ¿Cuál es la Cadena Crítica? (considerando recursos)
2. **Explotar:** Eliminar desperdicios en Cadena Crítica (multitarea, Parkinson)
3. **Subordinar:** Todas las demás tareas se alinean con Cadena Crítica
4. **Elevar:** Proteger Cadena Crítica con buffers estratégicos
5. **Monitorear:** Fever Chart para detectar si restricción se mueve

[TRANSICIÓN]

OK, entendimos TOC.

Ahora: ¿Qué problema específico vio Goldratt en CPM (Critical Path Method)?"

---

**Preguntas para engagement:**

1. "¿Alguien leyó 'The Goal'? ¿Qué les pareció?"
2. "¿Qué restricción tiene SU proyecto actual?"
3. "¿Por qué optimizar cosas fuera de la restricción NO ayuda?"

**Tips para el facilitador:**

✅ **Recomendar libro:** "Si tienen tiempo, lean 'The Goal'. Es novela, muy entretenido, aprenden TOC sin darse cuenta."

✅ **Analogía útil:** "TOC es como tráfico: no importa que 99% del camino sea autopista, si hay un semáforo lento, ESE determina tu tiempo total."

⚠️ **Evitar:** Profundizar demasiado en TOC. Es contexto, no el foco.

💡 **Anticipar pregunta:** "¿Cómo identifico la restricción?" Respuesta: "En CCPM, es la Cadena Crítica (lo veremos ya)."

⏰ **Timing:** 8 min (3 min Goldratt, 5 min TOC)

---

### **Slide 4: El Problema que Goldratt Vio en CPM** (10 min)

**Objetivos:**
- Exponer limitación crítica de CPM
- Mostrar que CPM ignora recursos
- Preparar para concepto de Cadena Crítica

**Script sugerido:**

"¿Qué problema vio Goldratt en CPM?

[PAUSA - Leer caja roja en slide]

**CPM (Critical Path Method) asume RECURSOS ILIMITADOS**

[ÉNFASIS]

Esto es ENORME.

CPM identifica 'Ruta Crítica' basado SOLO en:
- Secuencia de tareas (A antes que B, B antes que C)
- Duración de cada tarea

CPM ignora COMPLETAMENTE:
- ¿QUIÉN hace cada tarea?
- ¿Esa persona está disponible?
- ¿Esa persona hace OTRAS tareas en paralelo?

[EJEMPLO del slide]

Proyecto con 2 rutas paralelas:

**Ruta A:** 10 días (5 tareas × 2 días cada una)
**Ruta B:** 15 días (3 tareas × 5 días cada una)

[DIBUJAR en pizarra virtual si es posible, o describir:]

```
Inicio
  ├─ Ruta A (10 días) ─┐
  └─ Ruta B (15 días) ─┤
                      Fin
```

**Pregunta: ¿Cuál es la Ruta Crítica según CPM?**

[Esperar respuestas]

**Respuesta CPM:** Ruta B (15 días)

**Duración del proyecto según CPM:** 15 días

[PAUSA]

**PERO...**

¿Qué pasa si **Ana** es la ÚNICA persona que hace AMBAS rutas?

[ÉNFASIS]

**Realidad:**

Ana hace Ruta A: 10 días
DESPUÉS Ana hace Ruta B: 15 días
**Total: 25 días**

¡NO 15 días!

[PAUSA LARGA]

**CPM dijo:** "15 días"
**Realidad:** "25 días" (67% más largo)

[EXPLICACIÓN]

CPM asumió que:
- Ruta A y Ruta B se hacen en PARALELO
- Por gente diferente (o recursos infinitos)

Pero si hay **dependencia de recursos** (Ana hace ambas):
- Las rutas NO son paralelas en realidad
- Son SECUENCIALES
- CPM está equivocado

[OTRO EJEMPLO - Más sutil]

**Proyecto con 3 tareas:**

**Tarea 1:** Backend API (10 días, hace Pedro)
**Tarea 2:** Frontend Web (8 días, hace Ana)
**Tarea 3:** Integración (5 días, hace Pedro)

**Precedencias:**
- Tarea 1 ANTES de Tarea 3
- Tarea 2 no depende de nadie
- Tarea 3 depende de Tarea 1

[DIBUJAR]

```
Inicio
  ├─ Tarea 1 (Pedro, 10d) ─ Tarea 3 (Pedro, 5d) ─┐
  └─ Tarea 2 (Ana, 8d) ───────────────────────────┤
                                                  Fin
```

**CPM dice:**

- Ruta Crítica: Tarea 1 → Tarea 3 = 15 días
- Tarea 2 tiene holgura (puede empezar hasta día 7 sin retrasar)
- **Duración total: 15 días**

[PAUSA]

**PERO Pedro está en Tarea 1 y Tarea 3.**

¿Qué pasa si Pedro tiene que hacer AMBAS secuencialmente?

**Realidad:**

- Día 1-10: Pedro hace Tarea 1
- Día 1-8: Ana hace Tarea 2 (en paralelo, OK)
- Día 11-15: Pedro hace Tarea 3

**Duración real: 15 días** (en este caso CPM acertó)

Pero ahora modificamos:

**¿Qué pasa si Tarea 3 también la tiene que hacer Ana (no Pedro)?**

[CAMBIAR asignación]

**Tarea 1:** Backend API (10 días, Pedro)
**Tarea 2:** Frontend Web (8 días, Ana)
**Tarea 3:** Integración (5 días, **Ana**)

**CPM sigue diciendo:** 15 días (Tarea 1 → Tarea 3)

**Pero realidad:**

- Día 1-10: Pedro hace Tarea 1
- Día 1-8: Ana hace Tarea 2
- Día 11-15: **ESPERA** (Tarea 3 necesita que Tarea 1 termine)
- Día 11-15: Ana podría hacer Tarea 3, pero...
  - Día 8 terminó Tarea 2
  - Día 11 recién está disponible Tarea 1
  - Día 11-15: Ana hace Tarea 3

**Duración real: 15 días** (sigue OK)

[AHORA el caso problemático]

**¿Qué pasa si Ana tiene que hacer Tarea 2 y Tarea 3, pero Tarea 2 es MÁS LARGA?**

**Tarea 1:** Backend API (10 días, Pedro)
**Tarea 2:** Frontend Web (**12 días**, Ana)
**Tarea 3:** Integración (5 días, Ana)

**CPM dice:**

- Ruta Crítica: Tarea 1 (10d) → Tarea 3 (5d) = 15 días
- Tarea 2 tiene 3 días de holgura
- **Duración: 15 días**

**Realidad:**

- Día 1-10: Pedro hace Tarea 1
- Día 1-12: Ana hace Tarea 2
- Día 13-17: Ana hace Tarea 3 (tiene que esperar a que termine Tarea 1 en día 10, pero ella está ocupada hasta día 12)

**Duración real: 17 días** (NO 15)

[ÉNFASIS]

**CPM falló.**

Porque ignoró que **Ana es recurso compartido** entre Tarea 2 y Tarea 3.

[PAUSA]

**Esto es lo que Goldratt vio:**

CPM es **matemáticamente correcto** para el modelo simplificado (recursos infinitos).

Pero es **operativamente ingenuo** en la realidad (recursos limitados, compartidos).

[CITA del slide]

'CPM es matemáticamente correcto pero operativamente ingenuo'

[TRANSICIÓN]

Goldratt propuso solución: **Cadena Crítica** (Critical Chain).

NO es Ruta Crítica.

Es algo diferente."

---

**Preguntas para engagement:**

1. "¿En sus proyectos, tienen gente haciendo múltiples tareas?"
2. "¿Alguna vez CPM les dio timeline optimista?"
3. "¿Cómo harían para considerar recursos en planificación?"

**Tips para el facilitador:**

✅ **Usar pizarra virtual:** Dibujar los diagramas ayuda enormemente.

✅ **Ir despacio:** Este concepto es CRÍTICO. Si no se entiende, el resto de clase falla.

⚠️ **Evitar:** Apurarse. Vale la pena tomar 10-12 min en este slide.

💡 **Señal de entendimiento:** Si alguien dice "Ah, entonces CPM no sirve", corregir: "CPM SÍ sirve si recursos son abundantes. Pero si hay cuellos de botella, necesitamos CCPM."

⏰ **Timing:** 10 min (5 min primer ejemplo, 5 min ejemplo detallado)

---

### **Slide 5: Cadena Crítica vs Ruta Crítica** (10 min)

**Objetivos:**
- Definir Cadena Crítica formalmente
- Contrastar con Ruta Crítica
- Introducir concepto de nivelación de recursos

**Script sugerido:**

"Ahora la diferencia formal:

[VER slide - dos columnas]

**Lado izquierdo (rojo):**

**RUTA CRÍTICA (CPM)**

Definición:
'Secuencia de tareas DEPENDIENTES más larga, basada SOLO en la lógica de precedencias'

Características:
- ❌ Ignora recursos
- ❌ Asume multitarea perfecta
- ❌ Holgura distribuida (vulnerable)

[PAUSA]

**Lado derecho (verde):**

**CADENA CRÍTICA (CCPM)**

Definición:
'Secuencia más larga considerando TANTO tareas COMO recursos'

Características:
- ✅ Incorpora restricciones de recursos
- ✅ Elimina multitarea mala
- ✅ Buffers agregados (visibles, gestionables)

[PAUSA - EXPLICAR DIFERENCIAS]

**1. Incorpora restricciones de recursos**

Cadena Crítica pregunta:
- ¿QUIÉN hace cada tarea?
- ¿Ese recurso está disponible o hace otra cosa primero?
- ¿Hay dependencias ocultas por recursos compartidos?

**Ejemplo:**

```
CPM:
  Tarea A (5d) → Tarea C (3d)
  Tarea B (7d) → Fin

Ruta Crítica: B (7d)
```

```
CCPM (si Pedro hace A, B y C):
  Tarea A (5d, Pedro) → Tarea B (7d, Pedro) → Tarea C (3d, Pedro)

Cadena Crítica: A→B→C (15d) - NO solo B
```

[ÉNFASIS]

Cadena Crítica es MÁS LARGA que Ruta Crítica cuando hay recursos compartidos.

---

**2. Elimina multitarea mala**

**Multitarea mala:** Cambiar entre proyectos o tareas frecuentemente.

**Ejemplo:**

Pedro tiene 3 tareas en 3 proyectos diferentes:
- Proyecto X: Tarea de 10 días
- Proyecto Y: Tarea de 10 días
- Proyecto Z: Tarea de 10 días

**Enfoque tradicional (multitarea):**

Pedro alterna cada día:
- Día 1: Proyecto X
- Día 2: Proyecto Y
- Día 3: Proyecto Z
- Día 4: Proyecto X
- ...

Cada cambio pierde ~2 horas (cambio de contexto, recordar dónde estaba, setup).

**Resultado:**
- Primera tarea completa: día 30 (después de rotar 10 veces)
- Segunda tarea: día 30
- Tercera tarea: día 30
- **NINGÚN proyecto termina antes de día 30**

**Enfoque CCPM (focus and finish):**

Pedro hace UNA tarea a la vez:
- Día 1-10: Proyecto X completo
- Día 11-20: Proyecto Y completo
- Día 21-30: Proyecto Z completo

**Resultado:**
- Primera tarea: día 10 ✅
- Segunda tarea: día 20 ✅
- Tercera tarea: día 30 ✅
- **2 proyectos terminan ANTES**, todos terminan en mismo día 30

[PAUSA]

**Beneficio de focus and finish:**

- Entrega temprana de valor (2 proyectos listos en día 10 y 20)
- Sin pérdida por cambio de contexto
- Menor Work-in-Progress (WIP)

---

**3. Buffers agregados (vs holgura distribuida)**

Ya lo vimos en slides anteriores:

**CPM:** Holgura distribuida en tareas no críticas
- Invisible
- Se desperdicia (Parkinson, Estudiante)

**CCPM:** Buffers agregados en puntos estratégicos
- Visibles
- Gestionados activamente
- Protegen el proyecto sin permitir desperdicio

[VER caja destacada en slide]

**Fórmula conceptual:**

**Cadena Crítica = Ruta Crítica + Nivelación de Recursos**

[EXPLICAR]

**Nivelación de Recursos:**

Proceso de ajustar el plan considerando:
- Disponibilidad real de cada recurso
- Evitar sobrecarga (una persona en 3 tareas simultáneas)
- Serializar tareas del mismo recurso

**Resultado:**

La Cadena Crítica puede ser DIFERENTE a la Ruta Crítica.

**Ejemplo:**

**Antes de nivelación (CPM):**

```
Ruta A: 10 días (crítica)
Ruta B: 8 días (holgura 2 días)
```

**Después de nivelación (CCPM):**

Si Ruta B la hace el mismo recurso que una tarea de Ruta A:

```
Cadena Crítica: Tarea de A → Ruta B completa → Resto de A
Duración: 10 + 8 = 18 días (NO 10)
```

[ÉNFASIS]

**La Cadena Crítica es la RESTRICCIÓN del proyecto.**

TODO lo demás se subordina a ella.

[TRANSICIÓN]

OK, entendimos la diferencia conceptual.

Ahora: ¿Cuáles son los principios operativos de CCPM?"

---

**Preguntas para engagement:**

1. "¿En su proyecto actual, cuál es la Cadena Crítica? (considerando recursos)"
2. "¿Hacen multitarea mala? ¿Cuánto tiempo pierden por cambio de contexto?"
3. "¿Por qué focus-and-finish es mejor que alternar?"

**Tips para el facilitador:**

✅ **Enfatizar:** Cadena Crítica NO es solo "Ruta Crítica con otro nombre". Es concepto diferente.

✅ **Analogía útil:** "Ruta Crítica mira el mapa. Cadena Crítica mira el mapa + el equipo disponible."

⚠️ **Evitar:** Decir que CPM es "malo". Es apropiado cuando recursos NO son restricción.

💡 **Anticipar:** "¿Cómo calculo Cadena Crítica?" Respuesta: "Herramientas como MS Project con nivelación, o a mano (lo veremos en caso)."

⏰ **Timing:** 10 min (3 min definiciones, 4 min multitarea, 3 min nivelación)

---

### **Slide 6: Los 3 Principios Fundamentales de CCPM** (12 min)

**Objetivos:**
- Presentar los 3 pilares de CCPM
- Explicar por qué cada uno es necesario
- Preparar para gestión de buffers

**Script sugerido:**

"CCPM tiene 3 principios operativos.

Los 3 son NECESARIOS. No se puede aplicar solo uno o dos.

Es un sistema completo.

[VER slide - 3 cajas]

---

**PRINCIPIO 1 (caja azul):**

**Eliminar padding de las tareas individuales**

[LEER]

'Usar estimaciones AGRESIVAS (50% de probabilidad de éxito).
No añadir colchones de seguridad ocultos en cada tarea.'

[PAUSA - EXPLICAR]

¿Qué significa 'estimación agresiva con 50% probabilidad'?

**En PERT (Clase 2):**

Usamos 3 puntos:
- Optimista (O): 1% probabilidad
- Más probable (M): moda
- Pesimista (P): 99% probabilidad
- μ = (O + 4M + P) / 6

Resultado: ~80-90% probabilidad de cumplir.

**En CCPM:**

Usamos el punto MEDIO:
- 50% de veces terminará ANTES
- 50% de veces terminará DESPUÉS

**Ejemplo:**

Tarea: Implementar autenticación

**Estimación tradicional (80% probabilidad):**
- Optimista: 3 días
- Más probable: 5 días
- Pesimista: 10 días
- PERT: (3 + 4×5 + 10) / 6 = 5.5 días
- **Estimación con colchón: 8 días** (agregaron buffer oculto)

**Estimación CCPM (50% probabilidad):**
- **Estimación agresiva: 5 días** (el valor más probable, SIN colchón)

[ÉNFASIS]

¿Por qué hacer esto?

**Problema del colchón oculto:**

Si cada tarea tiene 50% buffer oculto:
- Ley de Parkinson: se expande para llenar tiempo
- Síndrome del Estudiante: se posterga hasta cerca del deadline
- Buffer se DESPERDICIA

Si quitamos el buffer individual:
- Tarea tiene presión real de terminar rápido
- NO hay colchón que desperdiciar
- Entrega más rápida

[PAUSA]

"Pero espera, eso es PELIGROSO. 50% de veces me atrasaré."

**Respuesta:** SÍ, pero esa variación se absorbe en BUFFER AGREGADO (Principio 2).

---

**PRINCIPIO 2 (caja verde):**

**Agregar seguridad como buffers estratégicos**

[LEER]

'Colocar la protección en puntos ESTRATÉGICOS, no distribuida en cada tarea.'

[EXPLICAR]

Como quitamos el 50% de cada tarea individual:
- Esa seguridad NO desaparece
- Se AGREGA al final como buffer visible

**Ejemplo:**

**4 tareas secuenciales:**

**Tradicional:**
- Tarea A: 5 días estimación agresiva + 2.5 días colchón = 7.5 días
- Tarea B: 3 días + 1.5 días = 4.5 días
- Tarea C: 8 días + 4 días = 12 días
- Tarea D: 4 días + 2 días = 6 días
- **Total: 30 días**

**CCPM:**
- Tarea A: 5 días (sin colchón)
- Tarea B: 3 días
- Tarea C: 8 días
- Tarea D: 4 días
- **Subtotal tareas: 20 días**
- **Buffer agregado: ~10 días** (50% del total)
- **Total: 30 días**

[PAUSA]

"Espera, 30 días = 30 días. ¿Cuál es la ventaja?"

**Ventaja:**

**Tradicional:**
- Los 10 días extras están DISTRIBUIDOS
- Se gastan por Parkinson (cada tarea se expande)
- Proyecto termina en 30 días o MÁS (si algo falla)

**CCPM:**
- Los 10 días están AL FINAL, VISIBLES
- Tareas se hacen en 20 días (sin colchón que desperdiciar)
- Buffer de 10 días se usa SOLO si hay problemas reales
- Proyecto puede terminar en 20-25 días (si no hay problemas)
- O 30 días (si hay problemas y se consume todo el buffer)

[ÉNFASIS]

**CCPM tiene MISMA protección que tradicional, pero timeline más corto.**

---

**PRINCIPIO 3 (caja púrpura):**

**Prohibir la multitarea mala**

[LEER]

'Focus and Finish - Terminar una tarea antes de empezar la siguiente.
El cambio de contexto mata la productividad.'

[EXPLICAR]

Ya lo vimos antes:

**Multitarea mala:**
- Cambiar entre proyectos/tareas frecuentemente
- Pérdida de 20-40% productividad por cambio de contexto

**CCPM prohíbe esto:**

Regla:
- Una persona, una tarea a la vez
- Terminar ANTES de empezar siguiente
- Proyectos se priorizan (A, luego B, luego C - no A+B+C simultáneos)

[BENEFICIOS]

1. **Mayor velocidad real:**
   - Sin pérdida por cambio de contexto
   - Flujo continuo

2. **Entregas tempranas:**
   - Primer proyecto termina ANTES
   - Valor entregado más rápido

3. **Menos Work-in-Progress:**
   - Menos cosas a medias
   - Más cosas terminadas

[EJEMPLO visual del slide anterior - reforzar]

3 proyectos de 10 días c/u:

**Multitarea:** Todos terminan día 30
**Focus-and-Finish:** Terminan día 10, 20, 30 (2 proyectos ANTES)

[PAUSA]

**Objeción común:**

"Pero el stakeholder de Proyecto B me va a matar si empiezo B en día 10 en vez de día 1."

**Respuesta:**

"Prefiere que:
- (A) Proyecto B empiece día 1 y termine día 30, o
- (B) Proyecto B empiece día 10 y termine día 20?"

Opción B es MEJOR (10 días antes, mismo esfuerzo).

---

[SÍNTESIS DE LOS 3 PRINCIPIOS]

**1. Estimaciones agresivas (50%):**
   - Quita colchón oculto
   - Previene Parkinson

**2. Buffers agregados:**
   - Protección visible y gestionable
   - Se usa solo si hay problemas reales

**3. Focus and finish:**
   - Elimina pérdida por multitarea
   - Acelera entregas

[ÉNFASIS]

**Los 3 juntos crean el sistema CCPM.**

Uno solo NO funciona:
- Solo (1) sin (2): proyecto desprotegido
- Solo (2) sin (1): buffer insuficiente (tareas tienen colchón oculto)
- Solo (3) sin (1+2): ayuda pero no resuelve problema sistémico

[TRANSICIÓN]

OK, Principio 2 dice 'buffers agregados'.

¿Cuáles buffers? ¿Cuántos?

Ahí vamos."

---

**Preguntas para engagement:**

1. "¿Cuál principio les parece más difícil de implementar?"
2. "¿Qué objeción pondrían los stakeholders a 'estimaciones 50%'?"
3. "¿En su proyecto, qué % de tiempo se pierde en cambio de contexto?"

**Tips para el facilitador:**

✅ **Enfatizar:** Los 3 principios son un SISTEMA. No se pueden aplicar parcialmente.

✅ **Analogía útil:** "Es como cinturón de seguridad + airbag + ABS. Uno solo ayuda, los 3 juntos salvan vidas."

⚠️ **Evitar:** Decir "es fácil". Es contra-intuitivo y requiere cambio cultural.

💡 **Anticipar:** "¿Mi jefe aceptará estimaciones 50%?" Respuesta: "Si entiende que buffer agregado protege MEJOR, sí. Educación es clave."

⏰ **Timing:** 12 min (4 min por principio)

---

### **Slide 7: Holgura vs Buffer** (10 min)

**Objetivos:**
- Contrastar holgura (CPM) con buffer (CCPM)
- Explicar por qué holgura falla
- Preparar para tipos de buffers

**Script sugerido:**

"Ahora profundicemos en la diferencia clave:

**Holgura (Slack) vs Buffer**

[VER slide - dos columnas]

**Lado izquierdo (rojo):**

**HOLGURA (CPM)**

5 características:

**1. Distribuida:**
- Cada tarea no crítica tiene holgura propia
- Ejemplo: Tarea B puede retrasarse 3 días sin afectar proyecto

**2. Invisible:**
- No aparece explícitamente en el plan
- Es cálculo implícito (Late Start - Early Start)
- Nadie la "ve" como recurso

**3. Propiedad del ejecutor:**
- "Tengo 5 días para esta tarea y 3 días de holgura"
- El ejecutor SABE que tiene colchón
- Incentivo perverso a usarlo

**4. Vulnerable a Parkinson y Estudiante:**
- Parkinson: trabajo se expande para llenar tiempo disponible
- Estudiante: se posterga hasta cerca del deadline
- Holgura se DESPERDICIA sistemáticamente

**5. No se gestiona:**
- PM no monitorea consumo de holgura
- No hay alerta temprana si se está gastando
- Pasiva, reactiva

**Resultado:**

❌ Mecanismo de seguridad FALLIDO

Holgura existe teóricamente, pero en práctica se pierde.

---

**Lado derecho (verde):**

**BUFFER (CCPM)**

5 características:

**1. Agregado:**
- NO distribuido en tareas individuales
- Colocado en puntos estratégicos:
  - Al final de Cadena Crítica
  - Donde cadenas NO críticas alimentan la crítica
  - Antes de recursos críticos

**2. Visible:**
- Aparece explícitamente en el plan
- Tamaño definido (días o % del proyecto)
- Todos SABEN que existe

**3. Propiedad del proyecto (PM):**
- NO es del ejecutor de tarea
- Es del PM o Project Manager
- Ejecutor NO puede "usar" buffer sin autorización
- Estimaciones de tareas son AGRESIVAS (sin colchón)

**4. Protegido de consumo temprano:**
- Como tareas son agresivas (50%), NO tienen colchón que desperdiciar
- Buffer solo se consume si hay PROBLEMA REAL (no por Parkinson)
- Ley de Murphy vs Ley de Parkinson: buffer absorbe Murphy, previene Parkinson

**5. Monitoreado constantemente:**
- PM revisa consumo de buffer DIARIAMENTE o SEMANALMENTE
- Gráfico de Fiebre (Fever Chart) muestra estado
- Alertas tempranas:
  - Verde: buffer bajo control
  - Amarillo: monitorear de cerca
  - Rojo: acción inmediata
- Activo, proactivo

**Resultado:**

✅ Mecanismo de seguridad ROBUSTO

Buffer es visible, gestionado, y protegido.

---

[PAUSA - ANALOGÍA]

**Holgura es como:**

Darle a cada miembro del equipo $100 de "fondo discrecional":
- Cada uno gasta sus $100 (porque puede)
- Nadie sabe cuánto queda en total
- Cuando hay emergencia real: NO hay dinero

**Buffer es como:**

Mantener $1000 en cuenta de emergencia centralizada:
- Nadie toca ese dinero para gastos cotidianos
- PM controla acceso
- Cuando hay emergencia REAL: hay $1000 disponibles
- Si no hay emergencia: sobra dinero (proyecto termina antes)

[ÉNFASIS]

**Pregunta clave:**

¿Prefieres:
- (A) 10 personas con $100 c/u que gastan todo, o
- (B) $1000 centralizados que se usan solo en emergencias?

Opción B protege MEJOR con MISMO dinero.

[CONECTAR con Clase 1]

¿Recuerdan Clase 1?

**Ley de Parkinson:**
"El trabajo se expande para llenar el tiempo disponible"

**Síndrome del Estudiante:**
"Se posterga hasta cerca del deadline"

**Holgura distribuida es VULNERABLE a ambos.**

Cada ejecutor sabe que tiene colchón → lo gasta.

**Buffer agregado es INMUNE:**

Ejecutor NO tiene colchón en su tarea → no puede gastarlo.
Buffer está lejos, controlado por PM.

[PAUSA]

**Objeción común:**

"Pero si doy estimación 50%, el equipo se va a estresar."

**Respuesta:**

1. Estimación 50% NO es "imposible", es realista:
   - 50% de veces lo lograrás
   - La otra 50% usarás buffer (para eso está)

2. Estrés viene de DEADLINES FALSOS con colchón oculto:
   - Te dan 8 días (5 real + 3 colchón)
   - Trabajas 7 días (Parkinson)
   - Fallas el deadline de 8 días
   - Estrés y culpa

3. CCPM es más honesto:
   - Te dan 5 días (real, sin colchón)
   - Trabajas 5-6 días
   - Si llegas a 6, buffer absorbe
   - Sin culpa, sin falso deadline

[TRANSICIÓN]

OK, entendimos buffer vs holgura.

Ahora: ¿CUÁNTOS tipos de buffer hay?"

---

**Preguntas para engagement:**

1. "¿En sus proyectos, la holgura se respeta o se consume?"
2. "¿Prefieren holgura distribuida o buffer centralizado? ¿Por qué?"
3. "¿Cómo convencerían a un equipo escéptico de estimar con 50%?"

**Tips para el facilitador:**

✅ **Enfatizar:** Holgura NO es mala en teoría, es mala en PRÁCTICA (por comportamiento humano).

✅ **Analogía útil:** "Holgura es como dejar billetes de $100 en cada escritorio. Buffer es como caja fuerte."

⚠️ **Evitar:** Decir que "holgura es inútil". En contexto ideal (sin Parkinson), holgura funciona. Pero realidad no es ideal.

💡 **Anticipar:** "¿Y si ejecutor termina en 4 días (antes de 5)?" Respuesta: "Perfecto! Empieza siguiente tarea. El tiempo ganado se acumula como colchón en buffer."

⏰ **Timing:** 10 min (5 min holgura, 5 min buffer + analogía)

---

### **Slide 8: Los 3 Tipos de Buffers en CCPM** (12 min)

**Objetivos:**
- Presentar los 3 tipos de buffers
- Explicar propósito de cada uno
- Preparar para dimensionamiento

**Script sugerido:**

"CCPM usa NO uno, sino TRES tipos de buffers.

Cada uno con propósito específico.

[VER slide - 3 cajas]

---

**BUFFER 1 (caja azul):**

**Buffer de Proyecto (Project Buffer - PB)**

[LEER slide]

'Colocado al FINAL de la Cadena Crítica, antes de la fecha de entrega.
Protege la fecha de compromiso contra variabilidad de la Cadena Crítica.'

[EXPLICAR]

**Ubicación:**
- Después de última tarea de Cadena Crítica
- Antes de fecha de entrega al cliente

**Propósito:**
- Absorber retrasos en CUALQUIER tarea de Cadena Crítica
- Proteger compromiso externo (fecha al cliente)

**Tamaño típico:**
- 50% de la duración de Cadena Crítica
- Ejemplo: CC = 40 días → PB = 20 días
- Total = 60 días comprometidos al cliente

**Ejemplo:**

Proyecto de 4 tareas en Cadena Crítica:

```
Tarea A (5d) → Tarea B (8d) → Tarea C (3d) → Tarea D (4d) → [PB: 10d] → ENTREGA
```

**Sin CCPM (tradicional):**
- Cada tarea tiene colchón:
  - A: 5d + 2.5d = 7.5d
  - B: 8d + 4d = 12d
  - C: 3d + 1.5d = 4.5d
  - D: 4d + 2d = 6d
- Total: 30 días

**Con CCPM:**
- Tareas SIN colchón: 5 + 8 + 3 + 4 = 20 días
- Buffer al final: 10 días
- Total: 30 días
- Pero ahora buffer es VISIBLE y GESTIONADO

[ÉNFASIS]

**Project Buffer es el MÁS IMPORTANTE.**

Es lo que protege la promesa al cliente.

Si Project Buffer se consume completamente → proyecto se retrasa.

---

**BUFFER 2 (caja verde):**

**Buffer de Alimentación (Feeding Buffer - FB)**

[LEER slide]

'Colocado donde una cadena NO crítica se une a la Cadena Crítica.
Protege la Cadena Crítica contra retrasos en cadenas no críticas.'

[EXPLICAR]

**Ubicación:**
- Al final de cada cadena NO crítica
- Justo antes de que esa cadena "alimente" a la Crítica

**Propósito:**
- Evitar que retraso en cadena NO crítica retrase la Crítica
- Permitir que Cadena Crítica fluya sin interrupciones

**Tamaño típico:**
- 50% de la cadena NO crítica que protege
- Ejemplo: Cadena NO crítica = 12 días → FB = 6 días

**Ejemplo:**

Proyecto con 2 cadenas:

```
[Cadena NO crítica]
Tarea X (5d) → Tarea Y (7d) → [FB: 6d] ──┐
                                           ├─→ Tarea C (Crítica) → ...
[Cadena Crítica]                           │
Tarea A (8d) → Tarea B (4d) ──────────────┘
```

**Sin Feeding Buffer:**

Si Tarea Y se retrasa 3 días:
- Tarea C (crítica) debe esperar
- Cadena Crítica se retrasa
- Project Buffer se consume

**Con Feeding Buffer de 6 días:**

Si Tarea Y se retrasa 3 días:
- Feeding Buffer absorbe (queda 3 días)
- Tarea C empieza a tiempo
- Cadena Crítica NO se afecta
- Project Buffer NO se consume

[ÉNFASIS]

**Feeding Buffers protegen la Cadena Crítica de perturbaciones externas.**

Son "amortiguadores" que aíslan la Crítica del resto del proyecto.

---

**BUFFER 3 (caja púrpura):**

**Buffer de Recurso (Resource Buffer - RB)**

[LEER slide]

'Alerta colocada ANTES de que un recurso crítico sea necesario.
NO es tiempo, es ALERTA para asegurar disponibilidad.'

[PAUSA - ESTE ES DIFERENTE]

**Importante:**

Resource Buffer NO es TIEMPO, es AVISO.

**Propósito:**
- Asegurar que recurso crítico esté DISPONIBLE cuando se necesite
- Prevenir esperas por recurso no disponible

**Ejemplo:**

Proyecto necesita a Pedro (arquitecto) en Tarea C:

```
Tarea A (5d) → Tarea B (8d) → [RB: avisar a Pedro] → Tarea C (4d, Pedro) → ...
```

**Sin Resource Buffer:**

- Tarea B termina día 13
- Tarea C necesita empezar día 13
- Pedro está en reunión / otro proyecto / vacaciones
- Tarea C se retrasa 2 días esperando a Pedro
- Cadena Crítica se retrasa

**Con Resource Buffer:**

- 3-5 días antes de que termine Tarea B:
  - PM avisa a Pedro: "Día 13 necesitamos que empieces Tarea C"
  - Pedro cancela reuniones, termina otros compromisos, se prepara
- Día 13: Pedro LISTO, empieza Tarea C inmediatamente
- Sin esperas, sin retrasos

[ÉNFASIS]

**Resource Buffer es coordinación proactiva.**

Es decir al recurso crítico: "Te necesitamos pronto, preparate."

[ANALOGÍA]

**Cirugía:**

**Sin Resource Buffer:**
- Paciente anestesiado
- Cirujano llega 20 min tarde (estaba en otra cirugía)
- Paciente espera bajo anestesia (riesgoso)

**Con Resource Buffer:**
- 30 min antes de cirugía: página al cirujano
- Cirujano termina lo que está haciendo, se prepara
- Llega a tiempo, cirugía empieza sin retraso

---

[RESUMEN DE LOS 3]

**Project Buffer (PB):**
- Al FINAL de Cadena Crítica
- Protege fecha de entrega
- ~50% de duración de CC
- ES TIEMPO (días)

**Feeding Buffer (FB):**
- Entre cadenas NO críticas y Crítica
- Protege CC de perturbaciones
- ~50% de cadena NO crítica
- ES TIEMPO (días)

**Resource Buffer (RB):**
- ANTES de que recurso crítico sea necesario
- Asegura disponibilidad
- 3-5 días de aviso
- NO es tiempo, es ALERTA

[PAUSA]

**Pregunta común:**

"¿Por qué 50%?"

**Respuesta:** Es regla empírica de Goldratt:

- Si estimaciones de tareas son 50% probabilidad (median)
- Y usas PERT stats: varianzas se suman
- Buffer agregado de 50% da ~90% probabilidad de éxito total

Matemática (simplificada):

- N tareas, cada una 50% probabilidad
- Varianza total = suma de varianzas
- Buffer = 0.5 × sqrt(N) × duración promedio
- Aproximadamente ~50% del total

(Lo veremos en siguiente slide con cálculo)

[TRANSICIÓN]

Ahora: ¿Cómo se calcula exactamente el tamaño de cada buffer?"

---

**Preguntas para engagement:**

1. "¿Cuál buffer les parece más importante?"
2. "¿En su proyecto, qué recurso necesitaría Resource Buffer?"
3. "¿Alguna vez esperaron a alguien y retrasó todo? (caso para RB)"

**Tips para el facilitador:**

✅ **Enfatizar:** Los 3 tipos de buffer trabajan JUNTOS. No es solo "agregar tiempo al final".

✅ **Analogía útil (RB):** "Es como llamar al plomero 3 días antes: 'Martes necesito que vengas'. Así no esperas."

⚠️ **Evitar:** Confundir RB con tiempo. Es aviso, no días extra.

💡 **Tip visual:** Dibujar el diagrama de las 3 cadenas con los 3 buffers. Ayuda enormemente.

⏰ **Timing:** 12 min (4 min por buffer)

---

### **Slide 9: Dimensionamiento de Buffers** (8 min)

**Objetivos:**
- Dar fórmulas para calcular buffers
- Explicar lógica estadística detrás
- Preparar para ejemplo visual

**Script sugerido:**

"¿Cómo calculamos el TAMAÑO de cada buffer?

Goldratt propuso varias reglas:

[VER slide - debe tener fórmulas]

---

**MÉTODO 1: Regla del 50%**

La más simple:

**Project Buffer (PB) = 50% de Cadena Crítica**

**Feeding Buffer (FB) = 50% de cadena NO crítica**

**Ejemplo:**

Cadena Crítica = 40 días
→ PB = 20 días

Cadena NO crítica = 12 días
→ FB = 6 días

[EXPLICAR por qué 50%]

Si estimaciones son medianas (50% probabilidad):
- Estadísticamente, algunas tareas terminarán antes, otras después
- Variabilidad individual se promedia
- Buffer de 50% da ~90% confianza en el agregado

[ANALOGÍA]

Lanzar 10 monedas:
- Cada moneda: 50% cara, 50% cruz
- Esperanza: 5 caras
- Probabilidad de ≥8 caras: ~5% (bajo)
- Probabilidad de 4-6 caras: ~66% (alto)

Mismo principio: variaciones se cancelan.

---

**MÉTODO 2: Raíz Cuadrada (más preciso)**

Basado en estadística de PERT:

**PB = 0.5 × sqrt(Σ varianzas de tareas en CC)**

O simplificado:

**PB = 0.5 × sqrt(N) × duración_promedio**

Donde N = número de tareas en CC

**Ejemplo:**

4 tareas en CC: 5, 8, 3, 4 días
- N = 4
- Duración total = 20 días
- Promedio = 5 días
- PB = 0.5 × sqrt(4) × 5 = 0.5 × 2 × 5 = 5 días

(Menos que 50% porque pocas tareas)

**Si CC tiene muchas tareas (N=16):**

16 tareas, promedio 3 días
- Duración total = 48 días
- PB = 0.5 × sqrt(16) × 3 = 0.5 × 4 × 3 = 6 días

(Solo 12.5%, porque muchas tareas promedian variabilidad)

[ÉNFASIS]

**Regla:**
- Pocas tareas largas: buffer ~50%
- Muchas tareas cortas: buffer ~25-30%

---

**MÉTODO 3: Percentil de confianza**

Ajustar según riesgo:

**Proyecto de bajo riesgo:**
- Buffer = 30-40% (aceptas más probabilidad de usar todo)

**Proyecto de medio riesgo:**
- Buffer = 50% (estándar)

**Proyecto de alto riesgo:**
- Buffer = 60-70% (proteges más)

**Factores de riesgo:**
- Tecnología nueva
- Equipo nuevo
- Requisitos ambiguos
- Dependencias externas

---

**MÉTODO 4: Empírico (después de varios proyectos)**

Después de ejecutar 5-10 proyectos con CCPM:
- Medir consumo promedio de buffer
- Ajustar fórmula

**Ejemplo:**

Primeros 5 proyectos:
- Proyecto 1: consumió 60% de PB
- Proyecto 2: consumió 45% de PB
- Proyecto 3: consumió 80% de PB
- Proyecto 4: consumió 40% de PB
- Proyecto 5: consumió 70% de PB
- **Promedio: 59%**

**Conclusión:** Buffer de 50% es insuficiente para esa organización.
**Nuevo estándar:** 60-65%

---

**FEEDING BUFFER:**

Mismo concepto que Project Buffer:

**FB = 50% de cadena NO crítica**

O ajustar según riesgo de esa cadena.

---

**RESOURCE BUFFER:**

NO es tiempo, es aviso:

**RB = 3-5 días de anticipación**

O ajustar según disponibilidad del recurso:

- Recurso muy ocupado: avisar 1 semana antes
- Recurso dedicado: avisar 2 días antes

---

[PAUSA - PRAGMATISMO]

**En la práctica:**

La mayoría usa **Regla del 50%**:
- Simple
- Funciona bien
- Fácil de comunicar

Si proyecto es crítico o de alto riesgo:
- Usar método 2 (raíz cuadrada) o 3 (percentil)

[TRANSICIÓN]

Ahora veamos un ejemplo visual completo."

---

**Preguntas para engagement:**

1. "¿Qué método les parece más práctico?"
2. "Su proyecto es bajo/medio/alto riesgo? ¿Qué buffer usarían?"
3. "¿Cómo medirían consumo de buffer para ajustar en futuros proyectos?"

**Tips para el facilitador:**

✅ **Enfatizar:** Regla del 50% es punto de partida. Ajustar según experiencia.

✅ **No asustar con matemática:** Método 2 es opcional, para quienes gusten precisión.

⚠️ **Evitar:** Decir que hay "fórmula perfecta". Todas son heurísticas.

💡 **Tip práctico:** "Empiecen con 50%. Después de 3 proyectos, revisen y ajusten."

⏰ **Timing:** 8 min (2 min por método)

---

### **Slide 10: Ejemplo Visual de Buffers** (10 min)

**Objetivos:**
- Mostrar proyecto completo con buffers
- Visualizar diferencia antes/después
- Preparar para diagrama SVG (Slide 10b)

**Script sugerido:**

"Ahora un ejemplo completo visual.

[VER slide - debe tener diagrama]

**Proyecto:**

3 cadenas de tareas:

**Cadena Crítica (azul):**
- Tarea A: 8 días (Pedro)
- Tarea B: 4 días (Ana)
- Tarea C: 6 días (Pedro)
- **Subtotal: 18 días**

**Cadena NO crítica 1 (amarilla):**
- Tarea X: 5 días (María)
- Tarea Y: 7 días (Juan)
- **Subtotal: 12 días**
- Esta cadena alimenta a Tarea C (crítica)

**Cadena NO crítica 2 (amarilla):**
- Tarea M: 4 días (Luis)
- Tarea N: 3 días (Clara)
- **Subtotal: 7 días**
- Esta cadena alimenta a Tarea B (crítica)

---

**PLAN SIN CCPM (tradicional):**

Cada tarea tiene colchón:
- Tarea A: 8d + 4d = 12d
- Tarea B: 4d + 2d = 6d
- Tarea C: 6d + 3d = 9d
- Tarea X: 5d + 2.5d = 7.5d
- Tarea Y: 7d + 3.5d = 10.5d
- Tarea M: 4d + 2d = 6d
- Tarea N: 3d + 1.5d = 4.5d

**Timeline tradicional:**

```
Inicio
  ├─ X (7.5d) → Y (10.5d) ────────────────┐
  ├─ M (6d) → N (4.5d) ───────────┐       │
  └─ A (12d) ─────────────→ B (6d)┴─→ C (9d)┴─→ FIN
```

**Duración:**

Cadena Crítica tradicional: 12 + 6 + 9 = 27 días

(Asumiendo que cadenas NO críticas terminan a tiempo)

---

**PLAN CON CCPM:**

Tareas SIN colchón:
- Cadena Crítica: 8 + 4 + 6 = 18 días
- Cadena NO crítica 1: 5 + 7 = 12 días
- Cadena NO crítica 2: 4 + 3 = 7 días

**Buffers:**
- **Project Buffer (PB):** 50% de 18d = 9 días (al final de CC)
- **Feeding Buffer 1 (FB1):** 50% de 12d = 6 días (después de Y, antes de C)
- **Feeding Buffer 2 (FB2):** 50% de 7d = 3.5 días (después de N, antes de B)
- **Resource Buffer (RB):** Avisar a Pedro 3 días antes de Tarea C

**Timeline CCPM:**

```
Inicio
  ├─ X (5d) → Y (7d) → [FB1: 6d] ────────────┐
  ├─ M (4d) → N (3d) → [FB2: 3.5d] ──┐       │
  └─ A (8d, Pedro) ───→ [RB] B (4d, Ana)┴─→ C (6d, Pedro)┴─→ [PB: 9d] → FIN
```

**Duración total:**

Cadena Crítica: 18 días
Project Buffer: 9 días
**Total: 27 días**

[PAUSA]

"Espera, 27 días = 27 días. ¿Dónde está el beneficio?"

---

**BENEFICIOS (explicar):**

**1. Probabilidad de terminar ANTES:**

**Tradicional:**
- Cada tarea con colchón
- Ley de Parkinson: colchón se gasta
- Proyecto termina en 27 días o MÁS (si algo falla)
- Probabilidad de terminar antes: ~5%

**CCPM:**
- Tareas sin colchón: terminan en 18 días o menos
- Si NO hay problemas: proyecto termina día 18-22 (usa buffer parcial)
- Si HAY problemas: proyecto termina día 27 (usa buffer completo)
- **Probabilidad de terminar antes de día 27: ~90%**

**2. Visibilidad:**

**Tradicional:**
- Colchón oculto
- No sabes cuánto "margen" queda
- Sorpresas al final

**CCPM:**
- Buffer visible
- Puedes medir: "Consumimos 40% de Project Buffer"
- Alertas tempranas

**3. Gestión proactiva:**

**Tradicional:**
- Reactivo: problemas se detectan tarde

**CCPM:**
- Proactivo: Fever Chart muestra estado
- Verde: OK
- Amarillo: monitorear
- Rojo: actuar YA

---

[MOSTRAR CÁLCULO ESPERADO]

**Duración esperada CCPM:**

- 50% de tareas terminan antes de estimación
- Promedio: tareas terminan en 90-95% de estimado (Parkinson reducido)
- Cadena Crítica: 18d × 95% = 17 días
- Buffer usado: ~40% = 3.6 días
- **Duración real esperada: 20-21 días**

vs

**Duración tradicional:**
- Colchón se gasta (Parkinson)
- Duración real: 27 días o más

**Ahorro: 6-7 días (22-25% más rápido)**

[ÉNFASIS]

**Mismo esfuerzo, menos tiempo, mejor protección.**

[TRANSICIÓN]

En el siguiente slide veremos el diagrama completo de los 3 buffers."

---

**Preguntas para engagement:**

1. "¿Por qué CCPM termina antes si total es 27d = 27d?"
2. "¿Qué pasa si cadena NO crítica se retrasa 8 días (más que FB)?"
3. "¿Cómo convencerían a stakeholder de este enfoque?"

**Tips para el facilitador:**

✅ **Usar colores:** Crítica en azul, NO críticas en amarillo, buffers en verde/punteado.

✅ **Dibujar en vivo:** Si plataforma permite, dibujar el diagrama paso a paso.

⚠️ **Evitar:** Apurarse en este slide. Es donde todo se une conceptualmente.

💡 **Anticipar:** "¿Y si buffer no es suficiente?" Respuesta: "Entonces proyecto se retrasa, PERO tienes visibilidad temprana para avisar al cliente."

⏰ **Timing:** 10 min (5 min diagrama, 5 min beneficios)

---

### **Slide 10b: Diagrama Completo de los 3 Buffers (SVG)** (5 min)

**Objetivos:**
- Mostrar gráfico profesional con todos los elementos
- Reforzar visualmente lo explicado
- Cerrar primera mitad con imagen memorable

**Script sugerido:**

"Aquí está el diagrama visual completo.

[VER slide - gráfico SVG con los 3 buffers]

Este gráfico resume todo CCPM:

[DESCRIBIR elementos]

**Top (amarillo):**
- Cadena NO crítica 1 (arriba)
- Tareas X → Y
- Termina en **Feeding Buffer 1 (FB1)** (punteado verde)
- FB alimenta a Tarea C de Cadena Crítica

**Bottom (amarillo):**
- Cadena NO crítica 2 (abajo)
- Tareas M → N
- Termina en **Feeding Buffer 2 (FB2)** (punteado verde)
- FB alimenta a Tarea B de Cadena Crítica

**Center (azul):**
- **Cadena Crítica** (centro)
- Tareas A → B → C
- Termina en **Project Buffer (PB)** (punteado azul/verde grande)
- PB protege fecha de entrega

**Resource Buffer (campanita 🔔):**
- Antes de Tarea C
- Aviso a Pedro: "3 días antes, preparate"

**Finish (bandera 🏁):**
- Final del proyecto después de PB

---

[LEER LEYENDA]

La leyenda muestra:

1. **Tareas Cadena Crítica** (rectángulo azul sólido)
2. **Tareas NO Críticas** (rectángulo amarillo sólido)
3. **Project Buffer (PB)** (rectángulo punteado al final)
4. **Feeding Buffers (FB)** (rectángulos punteados entre cadenas)
5. **Resource Buffer (RB)** (campanita)
6. **Flechas** (flujo de dependencias)

---

[ÉNFASIS]

**Este diagrama es la ESENCIA de CCPM:**

✅ Cadena Crítica identificada (azul)
✅ Tareas agresivas sin colchón individual
✅ Feeding Buffers protegen CC de perturbaciones externas
✅ Project Buffer protege fecha de entrega
✅ Resource Buffer asegura disponibilidad

**Sistema completo de protección.**

[PAUSA]

Tomen una foto mental de este diagrama.

Es lo que deben replicar en SUS proyectos.

[TRANSICIÓN]

OK, terminamos la primera mitad de la clase.

Vimos:
- Qué es CCPM (Teoría de Restricciones, Goldratt)
- Por qué CPM falla (ignora recursos)
- Cadena Crítica vs Ruta Crítica
- Los 3 principios (estimaciones agresivas, buffers agregados, focus-and-finish)
- Holgura vs Buffer
- Los 3 tipos de buffers (PB, FB, RB)
- Cómo dimensionarlos
- Ejemplo visual completo

**15 minutos de break.**

Después del break:
- **Caso A-B-C-D completo**
- Cálculos paso a paso
- Fever Chart
- Momento "aha!"

Nos vemos en 15."

---

**Tips para el facilitador:**

✅ **Dejar slide visible durante break:** Que participantes la absorban.

✅ **Recapitular rápido:** "3 tipos de buffer: PB al final, FB entre cadenas, RB como aviso."

⚠️ **Evitar:** Pasar demasiado rápido. Este gráfico es el resumen visual de todo.

💡 **Sugerencia:** "Tomen screenshot para referencia. Después lo usarán en sus proyectos."

⏰ **Timing:** 5 min (3 min describir, 2 min recapitular)

---

## 📌 Checkpoint: Final de Primera Mitad

**Tiempo transcurrido:** 90 minutos

**Slides cubiertas:** 1-10b (11 slides)

**Objetivos logrados:**

✅ Presentación de Goldratt y TOC
✅ Diferencia CPM vs CCPM (recursos)
✅ Cadena Crítica vs Ruta Crítica
✅ Los 3 principios fundamentales
✅ Holgura vs Buffer
✅ Los 3 tipos de buffers (PB, FB, RB)
✅ Dimensionamiento de buffers
✅ Ejemplo visual completo

**Estado emocional esperado del grupo:**

✅ "Entiendo la teoría conceptualmente"
✅ "Veo por qué holgura falla y buffer funciona"
✅ "Tengo curiosidad por ver cómo se aplica"
✅ "Listo para el caso práctico"

**Próximo bloque (post-break):**

- Caso A-B-C-D (paso a paso, 60 min)
- Fever Chart y monitoreo (15 min)
- Síntesis final y comparación (15 min)

---

**Archivo completo:** `GUIA_PROFESOR_CLASE3.md` (Parte 1)

**Continuación:** `GUIA_PROFESOR_CLASE3_PARTE2.md` (próxima tarea)

---

**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 2.0 - Formato Remoto
**Fecha:** Enero 2025
