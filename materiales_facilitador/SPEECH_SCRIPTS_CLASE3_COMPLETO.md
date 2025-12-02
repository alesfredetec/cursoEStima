# Speech Scripts - CLASE 3 COMPLETA: Cadena Crítica (CCPM)

**Versión:** 2.0 - Formato Remoto
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Tono:** Amigable, relajado, conversacional
**Duración total:** 3 horas (180 minutos)

---

## 🎯 Estructura de Clase 3

**PARTE 1:** Introducción a CCPM y Gestión de Buffers - 90 minutos
**BREAK:** 15 minutos
**PARTE 2:** Caso A-B-C-D Completo (Taller) - 60 minutos
**PARTE 3:** Síntesis Final y Comparación - 15 minutos

---

## Slide 1: Portada (2 min)

"Bienvenidos a la Clase 3: **Cadena Crítica - CCPM**.

[PAUSA - sonreír]

Este es el momento que estábamos esperando.

[ÉNFASIS]

Si Clase 1 diagnosticó el problema...
Y Clase 2 mostró las herramientas de estimación...

Clase 3 presenta **LA SOLUCIÓN SISTÉMICA**.

[LEER slide]

**Título:** Cadena Crítica (CCPM - Critical Chain Project Management)

**Subtítulo:** La Solución de Goldratt

**Objetivo:** Dominar la gestión de buffers y resolver el problema de la seguridad

[PAUSA]

Hoy van a aprender el método que permite:

✅ Acortar timelines **20-30%** sin agregar recursos
✅ Aumentar tasa de proyectos on-time de **40% a 85%**
✅ Gestionar carteras de múltiples proyectos simultáneos

[ÉNFASIS]

Y lo mejor:

**NO requiere estimar mejor.**

Requiere **GESTIONAR la incertidumbre mejor**.

[ANALOGÍA]

Es como pasar de llevar 10 paraguas pequeños (uno en cada bolsillo, que probablemente olvides usar)...

...a llevar UN paraguas grande bien visible (que usarás cuando realmente llueva).

MISMA protección. MEJOR gestión.

[TRANSICIÓN]

Empecemos."

---

## Slide 2: Agenda (3 min)

"OK, el plan de hoy.

[LEER agenda relajadamente]

**Primera mitad (90 min antes del break):**

**1. Introducción a CCPM y Teoría de Restricciones** (45 min)
   - Quién es Goldratt y qué es TOC
   - El problema que vio en CPM (ignora recursos)
   - Cadena Crítica vs Ruta Crítica
   - Los 3 principios fundamentales de CCPM

**2. Gestión de Buffers** (45 min)
   - Buffer de Proyecto (al final de Cadena Crítica)
   - Buffer de Alimentación (entre cadenas no críticas y crítica)
   - Buffer de Recursos (alarma, no tiempo)
   - Cómo dimensionarlos (50%, SSQ)
   - Gráfico de Fiebre (monitoreo visual)

**☕ Break - 15 minutos**

**Segunda mitad (75 min):**

**3. 🎮 Taller: Caso de Estudio A-B-C-D** (60 min)
   - Proyecto de 4 tareas con restricción de recursos
   - Calcular Ruta Crítica con CPM (nos da 25 días - EQUIVOCADO)
   - Identificar que Ana hace tareas B y D (conflicto de recursos)
   - Calcular Cadena Crítica real (35 días con padding)
   - Aplicar CCPM: quitar padding + agregar buffers (27 días)
   - **Este es el momento "aha!" del curso completo**

**4. Síntesis Final** (15 min)
   - Comparación CPM vs Ágil vs CCPM
   - Cuándo usar qué
   - Hibridación (CCPM + Ágil)
   - Recapitulación del curso completo

[ÉNFASIS]

**El Caso A-B-C-D (parte 3) es el CLÍMAX.**

Van a ver con sus propios ojos cómo:
- CPM da un número imposible (25 días)
- La realidad es 35 días (con padding tradicional)
- CCPM logra 27 días (más rápido Y más robusto)

[PAUSA]

Clase 1 y 2 fueron el setup.

Clase 3 es el payoff.

[TRANSICIÓN]

Empecemos con Goldratt..."

---

## Slide 3: Eliyahu Goldratt y TOC (8 min)

"Antes de entrar a CCPM, ¿quién lo inventó?

[VER slide]

**Eliyahu M. Goldratt**
- 1947-2011
- Físico israelí (sí, físico, no ingeniero industrial ni MBA)
- Consultor empresarial
- Autor best-seller

[PAUSA]

Goldratt es famoso por DOS libros que cambiaron la gestión de operaciones:

**1. 'The Goal' (1984)**

[CONTAR como historia]

Es una **novela**, no un manual técnico.

Protagonista: Alex Rogo, gerente de una planta industrial que está perdiendo dinero.

El dueño le da **3 meses** para salvarla o la cierra.

Alex conoce a Jonah (su viejo profesor de física) en un aeropuerto por casualidad.

Jonah le hace preguntas socráticas que lo llevan a descubrir la **Teoría de Restricciones**.

Resultado: Alex salva la planta, logra récord de ventas, lo ascienden.

[ÉNFASIS]

Este libro vendió **+6 millones de copias**.

Se usa en MBAs de todo el mundo.

Si tienen tiempo, léanlo. Es entretenido como novela Y aprenden TOC sin darse cuenta.

**2. 'Critical Chain' (1997)**

Aplica TOC específicamente a **gestión de proyectos**.

También es novela (Goldratt odiaba los manuales aburridos).

Esta es la base de CCPM.

[PAUSA - TEORÍA DE RESTRICCIONES]

OK, ¿qué es TOC - Theory of Constraints?

[LEER caja destacada en slide]

**'Una cadena no es más fuerte que su eslabón más débil'**

[PAUSA]

La idea central:

**Todo sistema tiene UNA RESTRICCIÓN que limita su rendimiento.**

Si querés mejorar el sistema, identificá y gestioná ESA restricción.

Optimizar cualquier otra cosa es **desperdicio de esfuerzo**.

[EJEMPLOS]

**Sistema: Fábrica**

Tenés 5 máquinas en línea de producción:
- Máquina A: produce 200 unidades/hora
- Máquina B: 150 unidades/hora
- Máquina C: **100 unidades/hora** ← CUELLO DE BOTELLA
- Máquina D: 180 unidades/hora
- Máquina E: 220 unidades/hora

[PREGUNTA]

¿Cuánto produce la fábrica por hora?

[Esperar respuestas mentales]

**Respuesta: 100 unidades/hora.**

NO importa que E haga 220. La restricción es C con 100.

[ÉNFASIS]

Si duplicás la velocidad de E (220 → 440), ¿mejora la fábrica?

**NO.**

Sigue limitada por C (100).

Si duplicás la velocidad de C (100 → 200), ¿mejora la fábrica?

**SÍ.**

Ahora la restricción se mueve a B (150).

[OTRO EJEMPLO]

**Sistema: Restaurante**

- Parrilla: 8 bifes simultáneos (10 min cada uno)
- Cocineros: 5 personas disponibles
- Meseros: 10 personas

[PREGUNTA]

Si querés servir más clientes por hora, ¿dónde invertís?

[Esperar]

**Respuesta: En la parrilla** (es la restricción).

Agregar meseros NO ayuda. La parrilla sigue haciendo 8 bifes cada 10 min.

[APLICACIÓN A PROYECTOS]

**En un proyecto de software:**

Restricción típica: Arquitecto senior único.

10 tareas necesitan al arquitecto.

Arquitecto puede hacer solo UNA tarea a la vez.

[PAUSA]

NO importa cuántos devs juniors tengas.

Si el arquitecto está saturado, el proyecto se retrasa.

Agregar más devs juniors **empeora el problema** (interrumpen al arquitecto con preguntas).

[5 PASOS DE TOC]

Goldratt formalizó el proceso de gestionar restricciones:

**1. IDENTIFICAR** la restricción del sistema
   - ¿Qué determina la velocidad del proyecto?

**2. EXPLOTAR** la restricción
   - Sacarle el máximo provecho (eliminar interrupciones, optimizar su trabajo)

**3. SUBORDINAR** todo lo demás a la restricción
   - Todo el sistema se alinea para apoyar la restricción

**4. ELEVAR** la restricción (si necesario)
   - Agregar capacidad (contratar otro arquitecto)

**5. VOLVER al paso 1**
   - Si la restricción se movió, repetir el proceso

[CONEXIÓN CON CCPM]

**En CCPM, la restricción es la CADENA CRÍTICA.**

No es la Ruta Crítica (esa es CPM).

Es la **Cadena Crítica**: secuencia de tareas + recursos que determina duración total.

[PAUSA]

CCPM aplica TOC:

1. Identificar: ¿Cuál es la Cadena Crítica? (considerando recursos)
2. Explotar: Eliminar desperdicios (multitarea, Parkinson)
3. Subordinar: Todo se alinea con Cadena Crítica
4. Elevar: Proteger con buffers estratégicos
5. Monitorear: Fever Chart detecta si restricción se mueve

[TRANSICIÓN]

OK, entendimos TOC.

Ahora: ¿Qué problema específico vio Goldratt en CPM?"

---

## Slide 4: El Problema que Goldratt Vio en CPM (10 min)

"¿Qué problema vio Goldratt en CPM (Critical Path Method)?

[PAUSA - Leer caja roja en slide]

**CPM asume RECURSOS ILIMITADOS**

[ÉNFASIS - tono dramático]

Esto es ENORME.

Es como asumir que tenés presupuesto infinito.

O tiempo infinito.

Es matemáticamente conveniente pero operativamente **absurdo**.

[EXPLICAR]

CPM identifica 'Ruta Crítica' basado SOLO en:
- Secuencia de tareas (A antes que B, B antes que C)
- Duración de cada tarea

CPM ignora COMPLETAMENTE:
- ¿QUIÉN hace cada tarea?
- ¿Esa persona está disponible?
- ¿Esa persona hace OTRAS tareas en paralelo?

[EJEMPLO DEL SLIDE - ir despacio]

Proyecto con 2 rutas paralelas:

**Ruta A:** 5 tareas de 2 días cada una = **10 días** total
**Ruta B:** 3 tareas de 5 días cada una = **15 días** total

[DIBUJAR mentalmente o en aire]

```
Inicio
  ├─ Ruta A (10 días) ─┐
  └─ Ruta B (15 días) ─┤
                      Fin
```

[PREGUNTA]

¿Cuál es la Ruta Crítica según CPM?

[Esperar respuestas]

**Respuesta CPM:** Ruta B (15 días) ← Esta es la más larga

**Duración del proyecto según CPM:** 15 días

[PAUSA]

**Parece lógico, ¿no?**

Ruta A termina en día 10 (espera 5 días).
Ruta B termina en día 15.
Proyecto completo: día 15.

[TONO DRAMÁTICO]

**PERO...**

¿Qué pasa si **Ana** es la ÚNICA persona que hace AMBAS rutas?

[DEJAR que procesen]

[ÉNFASIS]

Ana NO puede hacer las 2 rutas en paralelo.

Ana NO se puede clonar.

**Realidad:**

- Día 1-10: Ana hace Ruta A
- Día 11-25: Ana hace Ruta B
- **Total: 25 días**

¡NO 15 días!

[PAUSA LARGA]

**CPM dijo:** "15 días"

**Realidad:** "25 días"

**Diferencia:** 67% más largo

[EXPLICACIÓN]

CPM asumió que:
- Ruta A y Ruta B se hacen en PARALELO
- Por gente diferente (o recursos infinitos)

Pero si hay **dependencia de recursos** (Ana hace ambas):
- Las rutas NO son paralelas en realidad
- Son SECUENCIALES
- CPM está EQUIVOCADO

[ANALOGÍA]

Imaginen que tienen que:
- Tarea 1: Lavar la ropa (30 min)
- Tarea 2: Cocinar cena (40 min)

CPM dice: "40 minutos" (hacés ambas en paralelo).

Realidad: Si estás SOLO en la casa, son 70 minutos (30+40).

[OTRO EJEMPLO - MÁS SUTIL]

**Proyecto de software con 3 tareas:**

**Tarea 1:** Backend API (10 días, **Pedro**)
**Tarea 2:** Frontend Web (8 días, **Ana**)
**Tarea 3:** Integración (5 días, **Pedro**)

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

¿Es correcto esto?

**SÍ**, en este caso SÍ.

Porque Pedro hace T1 (día 1-10) y T3 (día 11-15).
Ana hace T2 (día 1-8) en paralelo.

Todo bien.

[AHORA EL PROBLEMA]

¿Qué pasa si cambiamos quién hace Tarea 3?

**Tarea 1:** Backend API (10 días, Pedro)
**Tarea 2:** Frontend Web (12 días, **Ana**) ← Ahora 12, no 8
**Tarea 3:** Integración (5 días, **Ana**) ← Ahora Ana, no Pedro

**CPM dice:**

- Ruta Crítica: Tarea 1 (10d) → Tarea 3 (5d) = 15 días
- Tarea 2 tiene 3 días de holgura
- **Duración: 15 días**

**Realidad:**

- Día 1-10: Pedro hace Tarea 1
- Día 1-12: Ana hace Tarea 2
- Día 13-17: Ana hace Tarea 3 (tiene que esperar a que termine T1 en día 10, pero ella está ocupada hasta día 12)

**Duración real: 17 días** (NO 15)

[ÉNFASIS]

**CPM falló.**

Porque ignoró que **Ana es recurso compartido** entre Tarea 2 y Tarea 3.

[PAUSA]

**Esto es lo que Goldratt vio:**

CPM es **matemáticamente correcto** para el modelo simplificado (recursos infinitos).

Pero es **operativamente ingenuo** en la realidad (recursos limitados, compartidos).

[LEER CITA del slide]

'CPM es matemáticamente correcto pero operativamente ingenuo'

[CONEXIÓN CON EXPERIENCIA]

[PREGUNTA]

¿Alguna vez en sus proyectos...

...el PM hizo un plan hermoso con Gantt chart...

...todo parecía posible en papel...

...y cuando empezaron a ejecutar, TODO se atrasó porque la misma gente estaba en múltiples tareas?

[Dejar que asienten]

Eso es CPM ignorando recursos.

[TRANSICIÓN]

Goldratt propuso solución: **Cadena Crítica** (Critical Chain).

NO es Ruta Crítica.

Es algo diferente."

---

## Slide 5: Cadena Crítica vs Ruta Crítica (10 min)

"Ahora la diferencia formal entre los dos conceptos.

[VER slide - dos columnas lado a lado]

**Lado izquierdo (rojo):**

**RUTA CRÍTICA (CPM)**

Definición:
'Secuencia de tareas DEPENDIENTES más larga, basada SOLO en la lógica de precedencias'

Características:
- ❌ Ignora recursos
- ❌ Asume multitarea perfecta
- ❌ Holgura distribuida (vulnerable a Parkinson)

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

**Diferencia 1: Incorpora restricciones de recursos**

Cadena Crítica pregunta:
- ¿QUIÉN hace cada tarea?
- ¿Ese recurso está disponible o hace otra cosa primero?
- ¿Hay dependencias ocultas por recursos compartidos?

**Ejemplo:**

```
CPM (ignorando recursos):
  Tarea A (5d) → Tarea C (3d)
  Tarea B (7d) → Fin

Ruta Crítica: B (7d) ← La más larga
```

```
CCPM (si Pedro hace A, B y C):
  Tarea A (5d, Pedro) → Tarea B (7d, Pedro) → Tarea C (3d, Pedro)

Cadena Crítica: A→B→C (15d) ← NO solo B
```

[ÉNFASIS]

Cadena Crítica es **MÁS LARGA** que Ruta Crítica cuando hay recursos compartidos.

Esto es crítico: el plan realista es MÁS LARGO que el plan ingenuo.

---

**Diferencia 2: Elimina multitarea mala**

[DEFINICIÓN]

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
- Día 4: Proyecto X (de vuelta)
- ...

Cada cambio pierde **~2 horas** (cambio de contexto, recordar dónde estaba, setup, recargar contexto mental).

[CÁLCULO]

10 días de trabajo real por tarea.

Pero con cambios constantes:
- 30 cambios totales (10 días × 3 proyectos)
- 30 cambios × 2 horas = 60 horas perdidas = 7.5 días

**Resultado:**

- Primera tarea completa: día **37** (30 días de trabajo + 7 días de pérdida)
- Segunda tarea: día **37**
- Tercera tarea: día **37**
- **NINGÚN proyecto termina antes de día 37**

[PAUSA]

**Enfoque CCPM (focus and finish):**

Pedro hace UNA tarea a la vez:
- Día 1-10: Proyecto X completo ✅
- Día 11-20: Proyecto Y completo ✅
- Día 21-30: Proyecto Z completo ✅

**Resultado:**

- Primera tarea: día **10** ✅ (27 días ANTES)
- Segunda tarea: día **20** ✅ (17 días ANTES)
- Tercera tarea: día **30** ✅ (7 días ANTES)

[ÉNFASIS]

**Beneficios de focus and finish:**

1. **Entrega temprana de valor:** 2 proyectos listos mucho antes
2. **Sin pérdida por cambio de contexto:** 7 días ahorrados
3. **Menor Work-in-Progress (WIP):** Menos cosas a medias, más cosas terminadas

[OBJECIÓN COMÚN]

"Pero el stakeholder de Proyecto Y me va a matar si empiezo Y en día 10 en vez de día 1."

[RESPUESTA]

Preguntale:

"¿Preferís que:
- (A) Proyecto Y empiece día 1 y termine día 37, o
- (B) Proyecto Y empiece día 10 y termine día 20?"

Opción B es **17 días mejor**, mismo esfuerzo.

El stakeholder racional prefiere B.

---

**Diferencia 3: Buffers agregados (vs holgura distribuida)**

Ya vimos esto en Clase 1 y lo profundizaremos hoy:

**CPM:** Holgura distribuida en tareas no críticas
- Invisible (cálculo implícito)
- Se desperdicia (Parkinson, Estudiante)

**CCPM:** Buffers agregados en puntos estratégicos
- Visibles (bloques explícitos en el plan)
- Gestionados activamente (Fever Chart)
- Protegen el proyecto sin permitir desperdicio

[VER caja destacada en slide]

**Fórmula conceptual:**

**Cadena Crítica = Ruta Crítica + Nivelación de Recursos**

[EXPLICAR]

**Nivelación de Recursos:**

Proceso de ajustar el plan considerando:
- Disponibilidad real de cada recurso
- Evitar sobrecarga (una persona en 3 tareas simultáneas)
- Serializar tareas del mismo recurso (focus and finish)

**Resultado:**

La Cadena Crítica puede ser **COMPLETAMENTE DIFERENTE** a la Ruta Crítica.

[EJEMPLO FINAL]

**Antes de nivelación (CPM):**

```
Ruta A: 10 días (crítica según CPM)
Ruta B: 8 días (holgura 2 días según CPM)
```

**Después de nivelación (CCPM):**

Si Ruta B la hace el mismo recurso que una tarea de Ruta A:

```
Cadena Crítica: Tarea de A → Ruta B completa → Resto de A
Duración: 10 + 8 = 18 días (NO 10)
```

[ÉNFASIS]

**La Cadena Crítica es la RESTRICCIÓN del proyecto** (concepto de TOC).

TODO lo demás se subordina a ella.

[TRANSICIÓN]

OK, entendimos la diferencia conceptual.

Ahora: ¿Cuáles son los 3 principios operativos de CCPM?"

---

## Slide 6: Los 3 Principios Fundamentales de CCPM (12 min)

"CCPM tiene 3 principios operativos fundamentales.

[ÉNFASIS]

Los 3 son **NECESARIOS**.

No se puede aplicar solo uno o dos.

Es un **sistema completo**.

Como un trípode: sacás una pata, se cae todo.

[VER slide - 3 cajas de colores]

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
- Optimista (O): mejor caso
- Más probable (M): caso normal
- Pesimista (P): peor caso
- μ = (O + 4M + P) / 6

Resultado: ~80-90% probabilidad de cumplir (conservador).

**En CCPM:**

Usamos el punto **MEDIO** (mediana):
- 50% de veces terminará ANTES
- 50% de veces terminará DESPUÉS

[EJEMPLO]

Tarea: Implementar autenticación

**Estimación tradicional (80% probabilidad):**
- Optimista: 3 días
- Más probable: 5 días
- Pesimista: 10 días
- PERT: (3 + 4×5 + 10) / 6 = 5.5 días
- **Con colchón oculto: 8 días** (agregaron 50% por las dudas)

**Estimación CCPM (50% probabilidad):**
- **5 días** (el valor más probable, SIN colchón)

[PREGUNTA OBVIA]

"Espera, eso es PELIGROSO. 50% de veces me atrasaré."

[RESPUESTA]

**SÍ, pero esa variación se absorbe en BUFFER AGREGADO (Principio 2).**

[EXPLICAR POR QUÉ HACEMOS ESTO]

**Problema del colchón oculto:**

Si cada tarea tiene 50% buffer individual:
- **Ley de Parkinson:** el trabajo se expande para llenar el tiempo disponible
- **Síndrome del Estudiante:** se posterga hasta cerca del deadline
- Buffer se **DESPERDICIA** (no se usa para problemas reales, se gasta en procrastinación)

Si quitamos el buffer individual:
- Tarea tiene presión real de terminar rápido
- NO hay colchón que desperdiciar
- Entrega más rápida en promedio

[ANALOGÍA]

Es como darle a un adolescente:
- **(A)** Tarea para el viernes (hoy es lunes) → La hace el jueves a la noche
- **(B)** Tarea para mañana → La hace hoy

Misma tarea, diferente urgencia.

CCPM crea urgencia quitando el colchón visible.

---

**PRINCIPIO 2 (caja verde):**

**Agregar seguridad como buffers estratégicos**

[LEER]

'Colocar la protección en puntos ESTRATÉGICOS, no distribuida en cada tarea.'

[EXPLICAR]

Como quitamos el 50% de cada tarea individual:
- Esa seguridad NO desaparece
- Se AGREGA al final como **buffer visible**

[EJEMPLO CON NÚMEROS]

**4 tareas secuenciales:**

**Estimación tradicional (con colchón oculto):**
- Tarea A: 5 días agresivo + 2.5 días colchón = **7.5 días**
- Tarea B: 3 días agresivo + 1.5 días colchón = **4.5 días**
- Tarea C: 8 días agresivo + 4 días colchón = **12 días**
- Tarea D: 4 días agresivo + 2 días colchón = **6 días**
- **Total: 30 días**

**Estimación CCPM:**
- Tarea A: **5 días** (sin colchón)
- Tarea B: **3 días**
- Tarea C: **8 días**
- Tarea D: **4 días**
- **Subtotal tareas: 20 días**
- **Buffer agregado: ~10 días** (50% del total cortado)
- **Total comprometido: 30 días**

[PAUSA]

"Espera, 30 días = 30 días. ¿Cuál es la ventaja?"

[EXPLICAR LA VENTAJA]

**Tradicional:**
- Los 10 días extras están DISTRIBUIDOS e INVISIBLES
- Se gastan por Parkinson (cada tarea se expande)
- Proyecto termina en **30 días o MÁS** (si algo falla y se come el colchón)

**CCPM:**
- Los 10 días están AL FINAL, VISIBLES
- Tareas se hacen en **20 días** (sin colchón que desperdiciar)
- Buffer de 10 días se usa **SOLO si hay problemas reales**
- Proyecto puede terminar en **20-25 días** (si no hay problemas graves)
- O 30 días (si hay problemas y se consume todo el buffer)

[ÉNFASIS]

**CCPM tiene MISMA protección total que tradicional, pero timeline esperado más corto.**

Es redistribución inteligente del mismo tiempo.

---

**PRINCIPIO 3 (caja púrpura):**

**Prohibir la multitarea mala**

[LEER]

'Focus and Finish - Terminar una tarea antes de empezar la siguiente.
El cambio de contexto mata la productividad.'

[EXPLICAR]

Ya lo vimos antes (slide 5):

**Multitarea mala:**
- Cambiar entre proyectos/tareas frecuentemente
- Pérdida de **20-40%** productividad por cambio de contexto

**CCPM prohíbe esto explícitamente:**

Regla:
- Una persona, una tarea a la vez
- **Terminar** ANTES de empezar siguiente
- Proyectos se priorizan: A primero, luego B, luego C (NO A+B+C simultáneos)

[BENEFICIOS]

1. **Mayor velocidad real:**
   - Sin pérdida por cambio de contexto
   - Flujo continuo (zona de flow)

2. **Entregas tempranas:**
   - Primer proyecto termina ANTES
   - Valor entregado más rápido

3. **Menos Work-in-Progress (WIP):**
   - Menos cosas a medias
   - Más cosas terminadas (Done is better than perfect at 80%)

[EJEMPLO VISUAL - reforzar del slide anterior]

3 proyectos de 10 días c/u:

**Con multitarea:** Todos terminan día 37
**Focus-and-Finish:** Terminan día 10, 20, 30 (2 proyectos 17 y 7 días ANTES)

[OBJECIÓN COMÚN - anticipar]

"Pero mi jefe/stakeholder me obliga a trabajar en 3 cosas a la vez."

[RESPUESTA]

Mostrales los números:
- Multitarea: 3 proyectos terminan día 37
- Focus: 3 proyectos terminan día 10, 20, 30

Pregunta: "¿Preferís entregar el primero en día 10 o en día 37?"

**Si el stakeholder es racional, prefiere focus.**

Si no es racional... bueno, ahí el problema no es técnico, es político. Pero al menos sabés dónde está el problema.

---

[SÍNTESIS DE LOS 3 PRINCIPIOS]

**1. Estimaciones agresivas (50%):**
   - Quita colchón oculto
   - Previene Parkinson
   - Crea urgencia real

**2. Buffers agregados:**
   - Protección visible y gestionable
   - Se usa solo si hay problemas reales
   - PM controla el buffer (no el ejecutor)

**3. Focus and finish:**
   - Elimina pérdida por multitarea
   - Acelera entregas
   - Reduce WIP

[ÉNFASIS]

**Los 3 juntos crean el sistema CCPM.**

Uno solo NO funciona:

- Solo (1) sin (2): proyecto **desprotegido** (50% probabilidad no es suficiente sin buffer)
- Solo (2) sin (1): buffer **insuficiente** (tareas tienen colchón oculto, no cortaste suficiente)
- Solo (3) sin (1+2): ayuda pero no resuelve problema sistémico de seguridad

[ANALOGÍA FINAL]

Es como seguridad en un auto:

- Principio 1: Conducir a velocidad apropiada (no exceso de precaución)
- Principio 2: Airbag y cinturón (protección centralizada)
- Principio 3: Atención en una cosa (no usar celular manejando)

Los 3 juntos te protegen. Uno solo no alcanza.

[TRANSICIÓN]

OK, Principio 2 dice 'buffers agregados'.

¿Cuáles buffers? ¿Cuántos? ¿Dónde?

Ahí vamos."

---

## Slide 7: Holgura vs Buffer (10 min)

"Antes de ver los tipos de buffers, clarifiquemos la diferencia clave:

**Holgura (Slack en CPM) vs Buffer (CCPM)**

[VER slide - dos columnas]

**Lado izquierdo (rojo):**

**HOLGURA (CPM)**

5 características que la hacen vulnerable:

**1. Distribuida:**
- Cada tarea no crítica tiene holgura propia
- Ejemplo: 'Tarea B puede retrasarse 3 días sin afectar proyecto'

**2. Invisible:**
- No aparece explícitamente en el Gantt
- Es cálculo implícito: Late Start - Early Start
- Nadie la 've' como recurso protegido

**3. Propiedad del ejecutor:**
- "Tengo 5 días para esta tarea y 3 días de holgura"
- El ejecutor **SABE** que tiene colchón
- Incentivo perverso a usarlo

[ANALOGÍA]

Es como decirle a alguien: "Tenés $100 de presupuesto, pero en realidad te doy $150 por si acaso."

¿Qué va a pasar? Va a gastar $150.

**4. Vulnerable a Parkinson y Estudiante:**
- **Parkinson:** el trabajo se expande para llenar tiempo disponible
- **Estudiante:** se posterga hasta cerca del deadline
- Holgura se **DESPERDICIA** sistemáticamente

[PAUSA]

¿Recuerdan Clase 1?

Los estudios de Microsoft y MIT mostraron que proyectos con padding distribuido terminaban **IGUAL o PEOR** que proyectos sin padding.

Porque el padding se gastaba, no se usaba para problemas reales.

**5. No se gestiona:**
- PM no monitorea consumo de holgura día a día
- No hay alerta temprana si se está gastando
- Es pasiva, reactiva ("ups, se acabó la holgura, ahora sí hay problema")

**Resultado:**

❌ **Mecanismo de seguridad FALLIDO**

Holgura existe teóricamente en el plan, pero en práctica se pierde.

---

**Lado derecho (verde):**

**BUFFER (CCPM)**

5 características que lo hacen robusto:

**1. Agregado:**
- NO distribuido en tareas individuales
- Colocado en puntos estratégicos:
  - Al final de Cadena Crítica (Buffer de Proyecto)
  - Donde cadenas NO críticas alimentan la crítica (Buffer de Alimentación)
  - Antes de recursos críticos (Buffer de Recursos - es alarma)

**2. Visible:**
- Aparece **explícitamente** como bloque en el plan
- Tamaño definido: "9 días de buffer" (no es cálculo oculto)
- Todos SABEN que existe y cuánto es

**3. Propiedad del proyecto (PM):**
- NO es del ejecutor de tarea
- Es del **PM** o Project Manager
- Ejecutor NO puede "usar" buffer sin que sea visible
- Estimaciones de tareas son agresivas (50%), sin colchón individual

[ANALOGÍA]

Es como una cuenta de ahorros de emergencia:
- NO está en tu billetera (no la gastás en café)
- Está en el banco (visible pero separada)
- Solo la usás en emergencia REAL

**4. Protegido de consumo temprano:**
- Como tareas son agresivas (50%), NO tienen colchón individual que desperdiciar
- Buffer solo se consume si hay **PROBLEMA REAL** (bug complejo, tecnología más difícil de lo pensado)
- NO se consume por Parkinson (no hay tiempo extra en la tarea para expandir)

[ÉNFASIS]

**Ley de Murphy vs Ley de Parkinson:**

- **Murphy:** "Si algo puede salir mal, saldrá mal" → Buffer absorbe esto
- **Parkinson:** "El trabajo se expande para llenar tiempo" → Eliminado (no hay tiempo extra en tareas)

**5. Monitoreado constantemente:**
- PM revisa consumo de buffer **DIARIAMENTE** o **SEMANALMENTE**
- **Gráfico de Fiebre** (Fever Chart) muestra estado visual
- Alertas tempranas por zonas:
  - **Verde:** buffer bajo control (todo bien)
  - **Amarillo:** monitorear de cerca (ojo, se está consumiendo rápido)
  - **Rojo:** acción inmediata (se está agotando el buffer)
- Es activo, proactivo

**Resultado:**

✅ **Mecanismo de seguridad ROBUSTO**

Buffer es visible, gestionado activamente, y protegido.

---

[ANALOGÍA FINAL]

**Holgura es como:**

Darle a cada miembro del equipo $100 de "fondo discrecional":
- Cada uno gasta sus $100 (porque puede, y nadie lo monitorea)
- Nadie sabe cuánto queda en total
- Cuando hay emergencia real: NO hay dinero (ya se gastó en cosas no esenciales)

**Buffer es como:**

Mantener $1000 en cuenta de emergencia **centralizada**:
- Nadie toca ese dinero para gastos cotidianos
- PM/CFO controla acceso (requiere justificación)
- Cuando hay emergencia REAL: hay $1000 disponibles
- Si no hay emergencia: sobra dinero al final (proyecto termina antes o bajo presupuesto)

[PREGUNTA RETÓRICA]

¿Qué protege mejor tu familia?

Opción B (buffer centralizado) protege MEJOR con **MISMO dinero total**.

[CONECTAR CON CLASE 1]

¿Recuerdan Clase 1?

**Ley de Parkinson:** "El trabajo se expande para llenar el tiempo disponible"

**Síndrome del Estudiante:** "Se posterga hasta cerca del deadline"

**Holgura distribuida es VULNERABLE a ambos.**

Cada ejecutor sabe que tiene colchón → lo gasta (consciente o inconscientemente).

**Buffer agregado es INMUNE:**

Ejecutor NO tiene colchón en su tarea → no puede gastarlo (no está ahí).

Buffer está lejos, controlado por PM, se usa solo cuando hay problema real.

[OBJECIÓN COMÚN - anticipar]

"Pero si doy estimación 50%, el equipo se va a estresar. Van a pensar que soy un jefe cruel."

[RESPUESTA]

1. **Estimación 50% NO es "imposible"**, es **realista:**
   - 50% de veces lo lograrás (o mejor)
   - La otra 50%, usarás buffer (para eso está)
   - Es honesto: "No sabemos exacto, estimamos en el medio"

2. **Estrés viene de DEADLINES FALSOS** con colchón oculto:
   - Tradicional: Te dan "8 días" (5 real + 3 colchón oculto)
   - Trabajas 7 días (Parkinson expande)
   - Fallas el deadline de 8 días → Estrés, culpa, "no soy bueno estimando"

3. **CCPM es más honesto y menos estresante:**
   - Te dan "5 días" (real, sin colchón, pero con buffer al final)
   - Trabajas 5-6 días (no hay colchón que expandir)
   - Si llegas a 6, buffer absorbe (no es "tu culpa")
   - Sin falso deadline individual, sin culpa personal

[PAUSA]

El estrés en CCPM viene de **urgencia** (bueno, motiva), no de **culpa** (malo, paraliza).

[TRANSICIÓN]

OK, entendimos buffer vs holgura conceptualmente.

Ahora: ¿CUÁNTOS tipos de buffer hay en CCPM?"

---

## Slide 8: Los 3 Tipos de Buffers en CCPM (12 min)

"CCPM usa NO uno, sino **TRES tipos de buffers**.

Cada uno con propósito específico y ubicación diferente.

[VER slide - 3 cajas de colores]

---

**BUFFER 1 (caja azul):**

**Buffer de Proyecto (Project Buffer - PB)**

[LEER slide]

'Colocado al FINAL de la Cadena Crítica, antes de la fecha de entrega.
Protege la fecha de compromiso contra variabilidad de la Cadena Crítica.'

[EXPLICAR]

**Ubicación:**
- **Después** de la última tarea de Cadena Crítica
- **Antes** de la fecha de entrega al cliente

**Propósito:**
- Absorber retrasos en **CUALQUIER** tarea de Cadena Crítica
- Proteger el compromiso externo (fecha prometida al cliente)

**Propiedad:**
- Del proyecto (PM), NO de la última tarea
- Ejecutor de última tarea NO sabe que existe este colchón

**Tamaño típico:**
- **50%** de la duración de Cadena Crítica
- Ejemplo: Cadena Crítica = 40 días → Project Buffer = 20 días
- Total comprometido al cliente = 60 días

[EJEMPLO VISUAL - ver diagrama en slide]

Proyecto de 4 tareas en Cadena Crítica:

```
A (5d) → B (8d) → C (3d) → D (4d) → [PB: 10d] → 🏁 ENTREGA
```

**Sin CCPM (tradicional con padding distribuido):**
- Cada tarea tiene colchón oculto:
  - A: 5d + 2.5d = 7.5d
  - B: 8d + 4d = 12d
  - C: 3d + 1.5d = 4.5d
  - D: 4d + 2d = 6d
- Total: **30 días** (pero vulnerable a Parkinson)

**Con CCPM:**
- Tareas SIN colchón: 5 + 8 + 3 + 4 = **20 días**
- Buffer al final: **10 días**
- Total comprometido: **30 días**
- Pero ahora buffer es **VISIBLE** y **GESTIONADO**

[ÉNFASIS]

**Project Buffer es el MÁS IMPORTANTE.**

Es lo que protege la **promesa al cliente**.

Si Project Buffer se consume completamente → proyecto se retrasa (hay que avisar al cliente).

Si Project Buffer se consume solo parcialmente → proyecto termina ANTES de lo prometido (cliente feliz).

[VER DIAGRAMA en slide con flechas]

---

**BUFFER 2 (caja amarilla):**

**Buffer de Alimentación (Feeding Buffer - FB)**

[LEER slide]

'Colocado donde una cadena NO crítica se une a la Cadena Crítica.
Protege la Cadena Crítica contra retrasos en cadenas no críticas.'

[EXPLICAR]

**Ubicación:**
- Al final de cada cadena **NO crítica**
- Justo **antes** de que esa cadena "alimente" a la Crítica

**Propósito:**
- Evitar que retraso en cadena NO crítica retrase la Cadena Crítica
- Permitir que Cadena Crítica fluya sin interrupciones (es la restricción, recordar TOC)

**Tamaño típico:**
- **50%** de la duración de la cadena NO crítica que protege
- Ejemplo: Cadena NO crítica = 12 días → Feeding Buffer = 6 días

[EJEMPLO VISUAL - ver diagrama en slide]

Proyecto con 2 cadenas:

```
[Cadena NO crítica - amarilla]
X (5d) → Y (7d) → [FB: 6d] ──┐
                              ├─→ C (Crítica) → ...
[Cadena Crítica - azul]       │
A (8d) → B (4d) ──────────────┘
```

**Sin Feeding Buffer:**

Si Tarea Y (no crítica) se retrasa 3 días:
- Tarea C (crítica) debe **esperar** 3 días
- Cadena Crítica se retrasa 3 días
- **Project Buffer se consume** 3 días

**Con Feeding Buffer de 6 días:**

Si Tarea Y se retrasa 3 días:
- **Feeding Buffer absorbe** los 3 días (queda 3 días de FB)
- Tarea C empieza **a tiempo** (no espera)
- Cadena Crítica **NO se afecta**
- Project Buffer **NO se consume**

[ÉNFASIS]

**Feeding Buffers son "amortiguadores"** que aíslan la Cadena Crítica del resto del proyecto.

Son como fusibles en electricidad: se queman ellos antes que el sistema principal.

[ANALOGÍA]

Imaginen que la Cadena Crítica es una autopista principal.

Las cadenas NO críticas son calles laterales que se unen a la autopista.

Feeding Buffers son **rampas de aceleración** en la entrada:
- Si el auto de la calle lateral viene lento, tiene rampa para acelerar
- NO bloquea el tráfico de la autopista principal
- Autopista fluye sin interrupciones

---

**BUFFER 3 (caja púrpura):**

**Buffer de Recursos (Resource Buffer - RB)**

[LEER slide]

'Alerta colocada ANTES de que un recurso crítico sea necesario.
NO es tiempo, es ALERTA para asegurar disponibilidad.'

[PAUSA - ESTE ES DIFERENTE]

⚠️ **IMPORTANTE:**

Resource Buffer NO es TIEMPO, es **AVISO / ALARMA**.

Es el único buffer que **NO suma días al plan**.

[EXPLICAR]

**Propósito:**
- Asegurar que recurso crítico esté **DISPONIBLE** cuando la Cadena Crítica lo necesite
- Prevenir esperas por "recurso no disponible" (está en reunión, vacaciones, otro proyecto)

**Cómo funciona:**

Colocás una **alarma** 3-5 días ANTES de que necesites al recurso crítico.

Cuando suena la alarma, el PM verifica:
- ¿El recurso estará disponible?
- ¿Tiene conflictos? (otra reunión, otro proyecto)
- Si hay conflicto, **ACTUAR AHORA** para resolverlo

[EJEMPLO DEL SLIDE]

Proyecto necesita a María (experta en seguridad) en Tarea C:

```
A (5d) → B (8d) → [RB: 🔔 avisar a María] → C (4d, María) → ...
```

**Sin Resource Buffer:**

- Tarea B termina día 13
- Tarea C necesita empezar día 13
- PM intenta asignar a María → María está en **reunión todo el día** / en **otro proyecto** / de **vacaciones**
- Tarea C se retrasa 2 días esperando a María
- Cadena Crítica se retrasa 2 días
- Project Buffer se consume 2 días

**Con Resource Buffer:**

- **3-5 días ANTES** de que termine Tarea B:
  - PM recibe **ALERTA:** "Resource Buffer: María necesaria en 3 días para Tarea C"
  - PM contacta a María: "Día 13 necesitamos que estés lista para empezar Tarea C"
  - María **cancela reuniones**, termina otros compromisos, **se prepara**
- Día 13: María está **LISTA**, empieza Tarea C **inmediatamente**
- Sin esperas, sin retrasos

[ÉNFASIS]

**Resource Buffer es coordinación proactiva.**

Es decir al recurso crítico con anticipación: "Te necesitamos pronto, preparate."

NO es agregar días al plan. Es agregar **visibilidad y coordinación**.

[ANALOGÍA - Quirófano]

**Sin Resource Buffer (reactivo):**
- Paciente anestesiado en mesa de operaciones
- Enfermera llama al cirujano: "Doctor, ya estamos listos"
- Cirujano está en **otra cirugía**, llega 30 min tarde
- Paciente espera bajo anestesia (riesgoso, caro)

**Con Resource Buffer (proactivo):**
- **30 minutos ANTES** de la cirugía: página al cirujano
- Cirujano termina lo que está haciendo, se lava, se prepara
- Llega **justo a tiempo**, cirugía empieza sin retraso
- Sin esperas, sin riesgo

[PAUSA]

Resource Buffer es como esa página al cirujano: "En 30 min te necesitamos, vení preparándote."

---

[RESUMEN DE LOS 3 BUFFERS]

Déjenme resumir los 3:

**1. Project Buffer (PB):**
- **Ubicación:** Al FINAL de Cadena Crítica
- **Protege:** Fecha de entrega al cliente
- **Tamaño:** ~50% de duración de Cadena Crítica
- **Tipo:** ES TIEMPO (días/semanas)

**2. Feeding Buffer (FB):**
- **Ubicación:** Entre cadenas NO críticas y Crítica
- **Protege:** Cadena Crítica de perturbaciones externas
- **Tamaño:** ~50% de cadena NO crítica
- **Tipo:** ES TIEMPO (días/semanas)

**3. Resource Buffer (RB):**
- **Ubicación:** ANTES de tarea que necesita recurso crítico
- **Protege:** Disponibilidad de recurso
- **Tamaño:** 3-5 días de **aviso** anticipado
- **Tipo:** NO es tiempo, es **ALERTA** 🔔

[PAUSA]

**Pregunta común:**

"¿Por qué específicamente 50% para PB y FB?"

[RESPUESTA]

Es regla empírica de Goldratt basada en estadística:

- Si estimaciones de tareas son 50% probabilidad (mediana)
- Y usamos teoría de probabilidades: **varianzas se suman, no se promedian**
- Buffer agregado de 50% del total cortado da ~**90% probabilidad** de éxito del proyecto completo

[MATEMÁTICA SIMPLIFICADA - opcional, no profundizar mucho]

- N tareas, cada una 50% probabilidad individual
- Varianza total = suma de varianzas individuales
- Buffer = 0.5 × √N × duración promedio
- Aproximadamente ~50% del total en la práctica

(No hace falta memorizar esto, es el "por qué" teórico)

[TRANSICIÓN]

Ahora que sabemos los 3 tipos...

¿Cómo calculamos **exactamente** el tamaño de cada buffer?"

---

## Slide 11: Dimensionamiento de Buffers - Método 1 (8 min)

"¿Cuán grande debe ser el Buffer de Proyecto?

[VER slide - caja azul con fórmula]

**Método 1: Corte del 50% (Cut & Paste)**

Este es el método **más simple** y más usado en la práctica.

[PROCESO]

**Paso 1:** Calcular cuánto tiempo **CORTASTE** al eliminar padding de cada tarea

**Paso 2:** Buffer de Proyecto = **50% del tiempo total cortado**

[FÓRMULA en slide]

```
PB = 50% × Σ(Tiempo Cortado)
```

[EJEMPLO del slide]

Tenés 3 tareas en Cadena Crítica:

**Tarea A:**
- Estimación tradicional (con padding): 10 días
- Estimación agresiva CCPM (50%): 5 días
- **Cortado:** 5 días

**Tarea B:**
- Tradicional: 8 días
- Agresiva: 4 días
- **Cortado:** 4 días

**Tarea C:**
- Tradicional: 12 días
- Agresiva: 6 días
- **Cortado:** 6 días

[CÁLCULO]

**Total cortado:** 5 + 4 + 6 = **15 días**

**Buffer de Proyecto:** 50% × 15 = **7.5 días** ≈ **8 días**

[PAUSA]

**Plan final:**

- Cadena Crítica: 5 + 4 + 6 = **15 días** (tareas agresivas)
- Project Buffer: **8 días**
- **Total comprometido al cliente:** 15 + 8 = **23 días**

**Comparación:**

- Plan tradicional inflado: 10 + 8 + 12 = **30 días**
- Plan CCPM: **23 días**
- **Ahorro:** 7 días (23% más rápido)

[ÉNFASIS]

Y ojo: los 23 días de CCPM tienen **MEJOR protección** que los 30 tradicionales.

¿Por qué?

Porque el buffer de 8 días:
- Es **visible** (no se desperdicia por Parkinson)
- Está **gestionado** (PM lo monitorea)
- Se usa **solo en problemas reales**

El padding de 15 días tradicional:
- Es **invisible** (distribuido)
- NO se gestiona
- Se **desperdicia** (Parkinson garantiza que las tareas se expanden)

[ANALOGÍA]

Es como tener 8 litros de agua en una cantimplora bien cerrada (CCPM)...

vs tener 15 litros en una bolsa con agujeros (tradicional).

Menos agua, pero mejor contenedor → llegas más lejos.

[CUÁNDO USAR ESTE MÉTODO]

**Ventajas:**
- Súper simple (suma y dividí por 2)
- Rápido de calcular
- Fácil de explicar a stakeholders

**Usa este método cuando:**
- Proyecto pequeño-mediano (hasta 50 tareas)
- Necesitas velocidad en la planificación
- Tareas tienen variabilidad similar

[TRANSICIÓN]

Hay un método más sofisticado estadísticamente: SSQ.

Veámoslo..."

---

## Slide 12: Método SSQ (8 min)

"**Método 2: Raíz Cuadrada de Suma de Cuadrados (SSQ - Sum of Squares)**

[TONO]

Este es más técnico. Si les gusta matemática, van a amar esto.

Si no, quédense con el Método 1 (50%) que funciona perfecto.

[EXPLICAR]

SSQ es **estadísticamente más robusto** porque está basado en teoría de probabilidades.

Goldratt lo tomó de la teoría de PERT (que vimos en Clase 2).

[FÓRMULA en slide]

```
PB = √(Σ(Tiempo_Cortado_i)²)
```

Traducción: suma los **cuadrados** de los tiempos cortados, después sacá raíz cuadrada.

[MISMO EJEMPLO con SSQ]

Tareas A, B, C (mismo caso anterior):

**Tarea A cortado:** 5 días → 5² = **25**
**Tarea B cortado:** 4 días → 4² = **16**
**Tarea C cortado:** 6 días → 6² = **36**

**Suma de cuadrados:** 25 + 16 + 36 = **77**

**Buffer de Proyecto:** √77 ≈ **8.8 días** ≈ **9 días**

[COMPARAR RESULTADOS]

- **Método 50%:** 7.5 días ≈ 8 días
- **Método SSQ:** 8.8 días ≈ 9 días

Diferencia: 1 día (despreciable en este caso).

[PAUSA]

"¿Por qué SSQ da número un poquito más grande?"

[EXPLICAR - opcional, para curiosos]

SSQ pondera más las tareas con **mayor variabilidad**.

En este ejemplo:
- Tarea C cortó 6 días (mucha variabilidad)
- Tarea B cortó 4 días (media)
- Tarea A cortó 5 días (alta)

SSQ dice: "Tarea C es más riesgosa, démosle más peso" (6² = 36 es desproporcionadamente alto).

Por eso SSQ da buffer un poco más grande → más protección.

[CUÁNDO SSQ ES MEJOR QUE 50%]

**Usa SSQ cuando:**

1. **Tareas tienen variabilidades MUY diferentes:**
   - Ej: Tarea A cortó 2 días, Tarea B cortó 15 días
   - SSQ dará más peso a B (más riesgosa)

2. **Proyecto grande (50+ tareas):**
   - Con muchas tareas, ley de grandes números aplica
   - SSQ es más preciso estadísticamente

3. **Proyecto crítico (alto costo de falla):**
   - Proyecto de millones de dólares
   - Falla es inaceptable
   - SSQ da protección extra

[EJEMPLO DONDE SSQ BRILLA]

Proyecto con 10 tareas:

- 8 tareas cortaron 2 días cada una (cortado pequeño)
- 2 tareas cortaron 20 días cada una (cortado GRANDE)

**Método 50%:**
- Total cortado: (8 × 2) + (2 × 20) = 16 + 40 = 56 días
- Buffer: 50% × 56 = **28 días**

**Método SSQ:**
- Suma de cuadrados: (8 × 2²) + (2 × 20²) = (8 × 4) + (2 × 400) = 32 + 800 = 832
- Buffer: √832 ≈ **28.8 días** ≈ **29 días**

Similar, pero SSQ da un día más de protección (reconoce que las 2 tareas grandes son más riesgosas).

[VER CAJA en slide]

💡 **Regla práctica:**

SSQ da resultados similares al 50% cuando las tareas tienen variabilidad pareja.

SSQ da más buffer cuando hay tareas con variabilidad muy distinta.

[RECOMENDACIÓN]

En la práctica:

- **Proyectos normales:** Usa 50% (más simple)
- **Proyectos complejos o críticos:** Usa SSQ (más robusto)

Ambos funcionan. La diferencia suele ser 10-15%.

[TRANSICIÓN]

OK, ya sabemos calcular buffers.

Ahora: ¿Cómo **MONITOREAMOS** el buffer durante la ejecución?"

---

## Slide 13: Gráfico de Fiebre (Fever Chart) (10 min)

"Ahora la herramienta de **monitoreo visual** de CCPM:

**Gráfico de Fiebre (Fever Chart)**

[VER slide - gráfico SVG con zonas de colores]

Este gráfico es el **corazón del control** en CCPM.

Sin esto, CCPM es solo planificación. Con esto, CCPM es **gestión activa**.

[EXPLICAR EL GRÁFICO]

Es un gráfico de 2 ejes:

**Eje X (horizontal):** % de Cadena Crítica completada
- 0% (inicio) a 100% (fin)

**Eje Y (vertical):** % de Buffer consumido
- 0% (buffer intacto) a 100% (buffer agotado)

[ZONAS DE COLOR]

Hay 3 zonas diagonales:

**ZONA VERDE (abajo):**
- Buffer consumido **< progreso completado**
- Ejemplo: 50% completado, solo 20% buffer consumido
- **Significado:** ¡Excelente! Vas bien, sobra buffer

**ZONA AMARILLA (diagonal central):**
- Buffer consumido **≈ progreso completado**
- Ejemplo: 50% completado, 45-55% buffer consumido
- **Significado:** Alerta. Monitorear de cerca. Buffer se está usando rápido.

**ZONA ROJA (arriba):**
- Buffer consumido **> progreso completado**
- Ejemplo: 50% completado, 80% buffer consumido
- **Significado:** 🚨 CRISIS. Acción inmediata necesaria. Se está agotando el buffer.

[LÍNEA DIAGONAL IDEAL]

La línea azul punteada es el **caso ideal**:
- Buffer consumido = % completado
- Significa que usaste buffer proporcionalmente

Si tu línea está:
- **Por debajo:** Mejor que ideal ✅
- **Sobre la línea:** Problema 🚨

[EJEMPLO EN EL GRÁFICO - seguir la línea blanca]

Proyecto empieza:
- Punto 1 (0% completado, 0% buffer): OK, inicio
- Punto 2 (15% completado, 5% buffer): Verde, vamos bien
- Punto 3 (30% completado, 15% buffer): Verde, seguimos bien
- Punto 4 (50% completado, 35% buffer): Verde, excelente
- Punto 5 (65% completado, 60% buffer): Amarillo, ojo, se consume rápido
- Punto 6 (75% completado, 75% buffer): Amarillo-Rojo, alerta
- Punto 7 (85% completado, 85% buffer): Rojo, crisis

[INTERPRETAR CADA ZONA]

**ZONA VERDE:**

**Acción:** Ninguna especial. Seguir trabajando.

**Mensaje al equipo:** "Vamos bien, hay margen."

**ZONA AMARILLA:**

**Acción:** Monitorear **diariamente** (no semanal).

**Mensaje al equipo:** "Ojo, se está consumiendo buffer rápido. ¿Hay algún problema oculto?"

**Preguntas a hacer:**
- ¿Qué tareas están tomando más tiempo?
- ¿Hay bloqueos que no vemos?
- ¿Necesitamos agregar recursos?

**ZONA ROJA:**

**Acción:** **Reunión de emergencia YA.**

**Mensaje al stakeholder:** "Proyecto en riesgo de retraso. Necesitamos decidir:"
- Opción A: Agregar recursos (horas extra, contratar, etc)
- Opción B: Reducir alcance (quitar features no críticos)
- Opción C: Aceptar retraso (mover fecha de entrega)

**Preguntas críticas:**
- ¿Qué salió mal? (retrospectiva rápida)
- ¿Es recuperable? (horas extra, paralelizar)
- ¿Hay que avisar al cliente YA? (transparencia)

[ÉNFASIS]

**Lo crítico del Fever Chart:**

Es **proactivo**, no reactivo.

En gestión tradicional:
- Descubrís problemas cuando ya es tarde (sprint final, todos trabajan 16hs/día)

En CCPM con Fever Chart:
- Ves el problema cuando estás en **Amarillo** (todavía hay tiempo de actuar)
- Si llegás a Rojo, **al menos sabés temprano** (podés avisar al cliente con anticipación)

[ANALOGÍA]

**Sin Fever Chart (gestión tradicional):**

Es como conducir un auto sin tablero:
- No ves gasolina hasta que se apaga el motor (tarde)
- No ves temperatura hasta que humea (tarde)

**Con Fever Chart (CCPM):**

Tenés tablero con alertas:
- Luz amarilla de gasolina cuando queda 1/4 tanque (tiempo de actuar)
- Luz roja de temperatura antes de que hierva (podés parar y enfriar)

[FRECUENCIA DE MONITOREO]

**Recomendación:**

- **Verde:** Revisar semanalmente (lunes, por ejemplo)
- **Amarillo:** Revisar **diariamente** (cada mañana, 5 min)
- **Rojo:** Revisar **cada pocas horas** (monitoreo continuo)

[PAUSA]

El Fever Chart es **LA** herramienta de gestión de CCPM.

Sin él, estás volando a ciegas.

Con él, tenés visibilidad total del estado del proyecto.

[TRANSICIÓN]

OK, terminamos la teoría de buffers.

**15 minutos de break.**

Cuando volvamos: **EL CASO A-B-C-D.**

El momento "aha!" donde todo se integra."

---

## Slide 14: Break (2 min)

"Perfecto, llegamos al break.

[VER slide - emoji café]

**15 minutos de descanso.**

[RECAPITULAR RÁPIDO]

En estos primeros 90 minutos vimos:

✅ Goldratt y Teoría de Restricciones (TOC)
✅ Por qué CPM falla (ignora recursos)
✅ Cadena Crítica vs Ruta Crítica
✅ Los 3 principios de CCPM (estimaciones agresivas, buffers agregados, focus-and-finish)
✅ Holgura vs Buffer (distribuida vs agregada)
✅ Los 3 tipos de buffers (Proyecto, Alimentación, Recursos)
✅ Cómo dimensionarlos (50%, SSQ)
✅ Cómo monitorearlos (Fever Chart)

[ÉNFASIS]

Esa fue la **teoría**.

Ahora viene la **práctica**.

**Después del break: Caso A-B-C-D completo.**

Van a ver paso a paso:
1. Calcular Ruta Crítica con CPM (resultado: 25 días - equivocado)
2. Descubrir que Ana hace tareas B y D (conflicto de recursos)
3. Calcular Cadena Crítica real (resultado: 35 días con padding tradicional)
4. Aplicar CCPM (quitar padding + agregar buffers)
5. Resultado final: 27 días (más rápido que 35, más realista que 25)

[PAUSA]

**Este caso es el "aha! moment" del curso completo.**

Es el equivalente del Marshmallow Challenge de Clase 1.

Van a ver con números concretos por qué CCPM funciona.

[TRANSICIÓN]

OK, **15 minutos de break**.

Nos vemos en 15."

---

## ☕ BREAK - 15 MINUTOS

---

## 🎯 POST-BREAK: Caso A-B-C-D (60 minutos)

---

## Slide 15: Taller Intro (3 min)

"Bienvenidos de vuelta.

[PAUSA]

Ahora sí: **El Caso de Estudio A-B-C-D.**

[VER slide - caja púrpura con emoji]

🎯 **Objetivo del Taller:**

Vamos a resolver un proyecto COMPLETO paso a paso, aplicando TODO lo que vimos:

1. Calcular **Ruta Crítica** con CPM
2. Identificar **restricción de recursos** (Ana hace B y D)
3. Calcular **Cadena Crítica** real
4. Aplicar CCPM: eliminar padding + agregar buffers
5. Comparar resultados finales

[ÉNFASIS]

Este es un proyecto **pequeño** (solo 4 tareas).

Pero es **representativo** de problemas reales.

La lección que aprendan acá aplica a proyectos de 100 tareas.

[PAUSA]

Mientras cuento el caso, **piensen ustedes** qué harían en cada paso.

Al final compararemos.

[TONO NARRATIVO]

Imaginen que son el Project Manager de este proyecto.

Les acaban de dar 4 tareas para planificar.

[TRANSICIÓN]

Veamos el setup..."

---

## Slide 16: Proyecto Setup (5 min)

"Aquí está el proyecto.

[VER slide - tabla con las 4 tareas]

**Tareas y Dependencias:**

| Tarea | Depende de | Duración Inflada | Recurso |
|-------|------------|------------------|---------|
| **A** | -          | 10 días          | Juan    |
| **B** | A          | 10 días          | **Ana** |
| **C** | A          | 5 días           | Pedro   |
| **D** | C          | 10 días          | **Ana** |

[LEER despacio, remarcar recursos]

**Tarea A:**
- No depende de nadie (es la primera)
- Duración: 10 días
- La hace **Juan**

**Tarea B:**
- Depende de A (no puede empezar hasta que A termine)
- Duración: 10 días
- La hace **Ana** ← Ojo con esto

**Tarea C:**
- Depende de A (en paralelo con B)
- Duración: 5 días
- La hace **Pedro**

**Tarea D:**
- Depende de C
- Duración: 10 días
- La hace **Ana** ← Ojo, de nuevo Ana

[VER CAJA ROJA en slide]

⚠️ **Nota la trampa:** Ana hace TANTO B como D

[PAUSA - dejar que procesen]

¿Vieron el problema?

**Ana está en 2 tareas diferentes: B y D.**

[ÉNFASIS]

Esto va a ser el **núcleo** del caso.

CPM va a ignorar esto.

CCPM va a resolverlo.

[PREGUNTA RETÓRICA]

Si ustedes fueran el PM y les den esta tabla...

¿Cuánto dura el proyecto?

[PAUSA]

Piénsenlo mientras vemos el análisis paso a paso.

[TRANSICIÓN]

Paso 1: Calcular Ruta Crítica con CPM (método tradicional)."

---

## Slide 17: Paso 1 - CPM (5 min)

"**Paso 1: Calcular Ruta Crítica con CPM**

[LEER subtítulo]

Sin considerar recursos (esa es la suposición de CPM).

[IDENTIFICAR RUTAS]

Hay 2 rutas desde Inicio hasta Fin:

**Ruta 1: A → B**

[VER diagrama en slide]

```
A (10d) → B (10d)
```

Duración Total: 10 + 10 = **20 días**

**Ruta 2: A → C → D**

[VER diagrama en slide]

```
A (10d) → C (5d) → D (10d)
```

Duración Total: 10 + 5 + 10 = **25 días**

[PREGUNTA]

Según CPM, ¿cuál es la **Ruta Crítica**?

[Esperar respuestas mentales]

**Respuesta CPM:** Ruta 2 (A-C-D) con **25 días** ← Es la más larga

[VER CAJA AZUL en slide]

**Ruta Crítica (CPM) = A-C-D = 25 días**

[PAUSA]

CPM dice: "El proyecto toma 25 días."

[EXPLICAR]

**Plan según CPM:**

- Día 1-10: Juan hace A
- Día 11-15: Pedro hace C (en Ruta Crítica)
- Día 11-20: Ana hace B (en paralelo con C, tiene 5 días de holgura)
- Día 16-25: Ana hace D (en Ruta Crítica)

**Duración: 25 días** ✅ (según CPM)

[TONO]

Parece lógico, ¿no?

La ruta más larga es 25 días.

B tiene holgura (puede empezar hasta día 15 sin retrasar).

Todo calza perfecto en papel.

[PAUSA DRAMÁTICA]

**Pero...**

[TRANSICIÓN]

Hay un problema que CPM NO ve..."

---

## Slide 18: Paso 2 - La Revelación (5 min)

"**Paso 2: La Revelación del Recurso**

[VER slide - caja roja grande]

El PM (ustedes) están revisando el plan.

Y se dan cuenta:

[LEER caja grande con énfasis]

**Ana hace TANTO la tarea B COMO la tarea D**

[PAUSA]

Ana NO puede hacer multitarea.

Ana NO se puede clonar.

[ÉNFASIS]

Ana tiene que hacer una tarea, **DESPUÉS** la otra.

**NO en paralelo.**

[VER CAJA AZUL en slide]

**Pregunta Crítica:**

¿El plan de 25 días (CPM) sigue siendo válido?

[PAUSA - dejar suspenso]

[LEER RESPUESTA GRANDE]

**NO**

[EXPLICAR POR QUÉ]

El plan de CPM asumía que:
- B (Ana) ocurre días 11-20
- D (Ana) ocurre días 16-25

**Pero si Ana hace B, NO puede hacer D al mismo tiempo.**

Días 16-20 hay **conflicto**.

[DIBUJAR MENTALMENTE]

```
Día 11-20: Ana en B
Día 16-25: Ana en D ← ¡CHOQUE!
```

Ana está en 2 lugares a la vez días 16-20.

**Imposible.**

[PAUSA]

Esto es lo que Goldratt vio en proyectos reales:

CPM daba planes que en **papel** eran perfectos...

...pero en **realidad** eran imposibles de ejecutar.

[TONO REFLEXIVO]

¿Alguna vez les pasó?

PM hace un Gantt hermoso, todo en paralelo...

...y cuando empiezan a ejecutar, TODO se choca porque la misma gente está en múltiples tareas?

Eso es CPM ignorando recursos.

[TRANSICIÓN]

OK, CPM falló.

¿Cómo lo arreglamos?"

---

## Slide 19: Paso 3 - Cadena Crítica (8 min)

"**Paso 3: Identificar la Cadena Crítica**

[LEER subtítulo]

Re-planificar con recursos nivelados (Ana no puede hacer B y D simultáneamente).

[PROBLEMA]

Tenemos que serializar las tareas de Ana.

**Pregunta:** ¿Qué hace Ana primero, B o D?

[VER CAJA en slide]

**Decisión: Para minimizar duración total, Ana debe hacer PRIMERO la tarea de la ruta más larga.**

[EXPLICAR LÓGICA]

- D está en ruta A-C-D (25 días - la crítica)
- B está en ruta A-B (20 días - más corta)

**Si Ana hace D primero:**
- Ruta crítica A-C-D fluye sin interrupción
- B espera (pero tiene holgura)

**Si Ana hace B primero:**
- B termina antes, pero D se retrasa
- Ruta crítica A-C-D se alarga

[CONCLUSIÓN]

**Ana debe hacer D primero (está en ruta crítica), después B.**

[VER DIAGRAMA en slide]

**Nueva Secuencia Real:**

```
A (10d) → C (5d) → D (10d) → B (10d)
```

[LEER DESPACIO]

- Día 1-10: Juan hace A
- Día 11-15: Pedro hace C
- Día 16-25: **Ana hace D** (está libre, C terminó)
- Día 26-35: **Ana hace B** (ahora sí puede empezar, D terminó)

[VER CAJA ROJA en slide]

**Cadena Crítica Real = A-C-D-B = 35 días**

[PAUSA LARGA]

**35 días.**

NO 25 días como dijo CPM.

[ÉNFASIS]

**CPM se equivocó por 10 días (40% de error).**

¿Por qué?

Porque ignoró que Ana era recurso compartido.

[CONECTAR CON TOC]

¿Recuerdan Teoría de Restricciones?

**Ana es la restricción del proyecto.**

Ana determina la duración total.

NO importa cuán rápido sean Juan o Pedro.

Si Ana está saturada, el proyecto se retrasa.

[PAUSA]

Este es un proyecto **PEQUEÑO** (4 tareas).

Imaginen un proyecto de 100 tareas con 10 recursos compartidos...

CPM se equivocaría MUCHO más.

[TRANSICIÓN]

OK, ahora sabemos la **duración real:** 35 días.

Pero esos 35 días incluyen **padding oculto** (cada tarea tiene colchón).

¿Qué pasa si aplicamos CCPM?"

---

## Slide 20: El Momento "Aha!" (5 min)

"**El Momento "Aha!"**

[VER slide - caja grande gradiente]

Déjenme resumir lo que descubrimos:

[LEER con énfasis dramático]

**CPM nos dio 25 días**

[PAUSA]

(IMPOSIBLE de cumplir)

[PAUSA]

**La duración REAL con recursos nivelados es 35 días**

(con padding tradicional distribuido)

[PAUSA LARGA]

[LEER caja gris]

Esta es la razón por la que tantos proyectos CPM "fallan":

**El plan inicial era matemáticamente correcto pero operativamente imposible**

[ÉNFASIS]

Esto pasa TODO EL TIEMPO en la industria:

1. PM hace plan con CPM o MS Project
2. Plan se ve hermoso (25 días)
3. Cliente/jefe aprueba (25 días suena bien)
4. Equipo empieza a ejecutar
5. Día 20: "Eh... vamos a tardar más"
6. Día 25: "Necesitamos 10 días más"
7. Día 35: Proyecto termina (retraso de 10 días vs plan)
8. Cliente enojado, equipo estresado, PM culpado

[PAUSA]

**El problema NO fue mala ejecución.**

El problema fue **plan irreal desde el inicio**.

[VER CAJA VERDE en slide]

**CCPM identifica la Cadena Crítica REAL considerando recursos**

[ÉNFASIS]

CCPM habría dicho desde el día 1:

"Con recursos limitados, la duración base es 35 días (sin buffers)."

**Expectativa realista desde el inicio.**

Sin sorpresas.

[TRANSICIÓN]

Pero 35 días tiene padding vulnerable (Parkinson).

Apliquemos CCPM para mejorar..."

---

## Slide 21: Paso 4 - Aplicar CCPM (8 min)

"**Paso 4: Aplicar CCPM**

Ahora sí, la solución completa.

[LEER título]

**4a. Eliminar padding (cortar al 50%)**

[VER TABLA en slide]

Cada tarea tiene estimación "inflada" (80-90% probabilidad).

Vamos a cortarlas al **50%** (mediana).

| Tarea | Duración Inflada | Duración Agresiva (50%) | Cortado |
|-------|------------------|-------------------------|---------|
| **A** | 10 días          | 5 días                  | 5 días  |
| **B** | 10 días          | 5 días                  | 5 días  |
| **C** | 5 días           | 3 días                  | 2 días  |
| **D** | 10 días          | 5 días                  | 5 días  |
| **TOTAL** | **35 días**  | **18 días**             | **17 días** |

[EXPLICAR]

**Tarea A (10 días):**
- Optimista: 4 días
- Más probable: 6 días
- Pesimista: 12 días
- Mediana (50%): **5 días** ← Cortamos 5 días

**Tarea B (10 días):**
- Similar a A
- Mediana: **5 días** ← Cortamos 5 días

**Tarea C (5 días):**
- Más corta, menos padding proporcionalmente
- Mediana: **3 días** ← Cortamos 2 días

**Tarea D (10 días):**
- Similar a A y B
- Mediana: **5 días** ← Cortamos 5 días

[VER FILA TOTAL en tabla]

**TOTAL:**
- Duración inflada: **35 días**
- Duración agresiva: **18 días**
- **Total cortado: 17 días**

[PAUSA]

**Nueva Cadena Crítica agresiva:**

```
A (5d) → C (3d) → D (5d) → B (5d) = 18 días
```

[ÉNFASIS]

18 días es la **duración base sin protección**.

50% de veces terminará en 18 días o menos.

50% de veces terminará en más de 18 días.

[PAUSA]

Pero NO podemos prometer 18 días al cliente.

Necesitamos **buffer**.

[TRANSICIÓN]

Siguiente paso: calcular y agregar buffer..."

---

## Slide 22: Paso 5 - Buffer (8 min)

"**Paso 5: Calcular y Agregar Buffer de Proyecto**

[VER CAJA en slide]

**Método del 50%:**

[FÓRMULA]

```
PB = 50% × Total Cortado
PB = 50% × 17 días
PB = 8.5 días ≈ 9 días
```

[PAUSA]

**Project Buffer = 9 días**

[VER DIAGRAMA en slide]

**Plan CCPM Final:**

```
A (5d) → C (3d) → D (5d) → B (5d) → [PB: 9d] → 🏁
```

[LEER CON ÉNFASIS]

- **Cadena Crítica:** 5 + 3 + 5 + 5 = **18 días**
- **Project Buffer:** **9 días**
- **Total comprometido al cliente:** 18 + 9 = **27 días**

[VER CAJA VERDE en slide]

**Plan CCPM = 18d + 9d = 27 días**

Con fecha de entrega **PROTEGIDA** y **REALISTA**

[PAUSA - dejar que absorban]

[COMPARAR]

Déjenme poner los 3 números juntos:

- **CPM (ingenuo):** 25 días ← Equivocado (ignora recursos)
- **Tradicional inflado:** 35 días ← Correcto pero lento (padding vulnerable)
- **CCPM:** 27 días ← Correcto, protegido, más rápido

[ÉNFASIS]

**CCPM es 8 días más rápido que tradicional (23% mejora).**

Y es **realista** (no como CPM que prometía lo imposible).

[PAUSA]

¿Cómo CCPM logra esto?

[EXPLICAR EL "TRUCO"]

**No es magia. Es redistribución inteligente:**

1. **Quitamos 17 días de padding distribuido**
   - Ese padding se desperdiciaba (Parkinson)
   - Era vulnerable (Estudiante)

2. **Agregamos 9 días de buffer centralizado**
   - Buffer está protegido (no se desperdicia)
   - Buffer se gestiona (Fever Chart)

3. **Ahorro neto: 17 - 9 = 8 días**

[ANALOGÍA]

Es como pasar de llevar 10 mochilas chicas (una en cada bolsillo, que perdés)...

...a llevar 1 mochila grande bien visible (que NO perdés).

**Menos equipaje total, mejor organizado.**

[ÉNFASIS FINAL]

Y además:

**El buffer de 9 días protege MEJOR** que el padding de 17 días distribuido.

¿Por qué?

Porque:
- Es **visible:** PM lo monitorea
- Es **gestionable:** Fever Chart alerta temprano
- Se usa **solo en problemas reales:** No se desperdicia

[TRANSICIÓN]

Veamos la tabla comparativa final..."

---

## Slide 23: Resultado Final - Comparativa (8 min)

"**Resultado Final: Comparativa**

[VER slide - tabla con 3 filas]

Aquí está el resumen de los 3 enfoques:

[LEER FILA POR FILA]

---

**Fila 1 (roja):**

**CPM (ingenuo)**

- **Duración:** 25 días
- **Validez:** ❌ INCORRECTO (ignora que Ana hace B y D)
- **Protección:** Ignora recursos → Plan imposible de ejecutar

[PAUSA]

CPM prometía lo imposible.

25 días se veía bien en papel, pero era mentira.

---

**Fila 2 (amarilla):**

**Tradicional inflado**

- **Duración:** 35 días
- **Validez:** ✓ Correcto (considera recursos, Ana hace D después de B)
- **Protección:** ❌ Padding vulnerable (distribuido, se desperdicia por Parkinson)

[PAUSA]

Tradicional era realista en duración, pero ineficiente.

Los 35 días incluyen 17 días de padding que se desperdiciarían.

Proyecto terminaría en 35 días (o más si algo falla).

---

**Fila 3 (verde):**

**CCPM**

- **Duración:** 27 días (18 días Cadena Crítica + 9 días buffer)
- **Validez:** ✓ Correcto (considera recursos)
- **Protección:** ✅ Buffer protegido (agregado, visible, gestionado)

[PAUSA]

CCPM es realista Y eficiente.

Los 27 días son **fecha comprometida** al cliente.

Pero expectativa real es terminar en **22-25 días** (si no hay problemas graves).

---

[VER CAJA AZUL en slide]

**💡 Conclusión del Caso:**

[LEER con énfasis]

- CCPM entrega **8 días ANTES** que el plan inflado tradicional (23% más rápido)
- CCPM es **REALISTA** (considera recursos, no como CPM)
- CCPM es **ROBUSTO** (buffer protegido, no vulnerable como padding distribuido)
- CCPM es **GESTIONABLE** (visibilidad del buffer con Fever Chart)

[PAUSA]

**Este es el poder de CCPM.**

No estima "mejor" (sigue habiendo incertidumbre).

**Gestiona la incertidumbre mejor.**

[ANALOGÍA FINAL]

Es como la diferencia entre:

**Conducir sin GPS (CPM):**
- "El viaje toma 3 horas" (en papel)
- En realidad: 5 horas (tráfico, no sabías)
- Llegas tarde, sorpresa

**Conducir con GPS pero sin Waze (Tradicional):**
- "El viaje toma 5 horas" (con colchón)
- Usas todo el tiempo (Parkinson: paras en cada estación de servicio)
- Llegas en 5 horas exactas

**Conducir con Waze en tiempo real (CCPM):**
- "El viaje toma 3 horas base + 1 hora buffer = 4 horas comprometidas"
- Conduces rápido (3 horas sin paradas innecesarias)
- Usas buffer solo si hay accidente/tráfico REAL
- Llegas en 3.5 horas (antes de lo prometido)

[TRANSICIÓN]

Hagamos un debriefing rápido del caso..."

---

## Slide 24: Debriefing del Caso (5 min)

"**Debriefing: Lecciones del Caso A-B-C-D**

[VER slide - caja gradiente con 3 preguntas]

Reflexionemos sobre lo que vimos.

---

**Pregunta 1: ¿Por qué CPM falló?**

[LEER respuesta]

Porque asumió que B y D podían ocurrir en paralelo (recursos ilimitados).

En realidad, **Ana** las hace secuencialmente.

[PAUSA]

**Lección:**

CPM es apropiado cuando recursos NO son restricción.

Pero en proyectos reales (software, ingeniería, consultoría), recursos SIEMPRE son restricción.

**CCPM es necesario.**

---

**Pregunta 2: ¿Por qué el plan tradicional inflado (35d) es lento?**

[LEER respuesta]

Porque el padding está DISTRIBUIDO e INVISIBLE.

Parkinson y el Síndrome del Estudiante lo consumirán inevitablemente.

El proyecto IGUALMENTE llegará a 35 días o más (si algo falla).

[PAUSA]

**Lección:**

Padding distribuido NO protege.

Se **desperdicia** en lugar de usarse para problemas reales.

Es como tener airbags que se inflan al arrancar el auto (inútil).

---

**Pregunta 3: ¿Por qué CCPM (27d) es mejor?**

[LEER respuesta]

• Cadena crítica **correcta** (considera recursos, no ignora como CPM)
• Tareas **agresivas** (sin padding oculto, sin Parkinson)
• Buffer **agregado** y visible (protegido, gestionado con Fever Chart)
• **Resultado:** Más rápido Y más robusto que tradicional

[PAUSA]

**Lección:**

CCPM combina lo mejor de ambos mundos:
- Velocidad (tareas agresivas)
- Protección (buffer centralizado)

[ÉNFASIS]

**Este caso es pequeño (4 tareas), pero la lección escala.**

En proyecto de 100 tareas con 20 recursos compartidos:
- CPM fallaría MUCHO más (error 50-100%)
- CCPM daría 30-40% de aceleración vs tradicional

[PAUSA]

Los números reales de la industria:

**Empresas que adoptan CCPM reportan:**
- 20-35% reducción en duración de proyectos
- Tasa de proyectos on-time: de 40% a 85%
- Sin agregar recursos (misma gente, mejor gestión)

[TRANSICIÓN]

OK, cerremos con comparación de métodos y síntesis final..."

---

## Slide 25: Tabla Comparativa Final (8 min)

"**Cuadro Comparativo Final: CPM vs Agile vs CCPM**

[VER slide - tabla grande]

Hora de poner los 3 enfoques uno al lado del otro.

[LEER FILA POR FILA]

---

**Fila: Foco**

- **CPM:** Secuencia de tareas (dependencias lógicas)
- **Agile:** Valor y adaptabilidad (feedback del cliente)
- **CCPM:** Flujo y recursos (restricciones, cuellos de botella)

[COMENTAR]

Cada uno tiene foco diferente porque resuelve problema diferente.

---

**Fila: Incertidumbre**

- **CPM:** Holgura distribuida (vulnerable)
- **Agile:** Iteración (re-planificar cada sprint)
- **CCPM:** Buffers agregados (protegidos, visibles)

[COMENTAR]

Agile maneja incertidumbre **re-planeando** frecuentemente.

CCPM maneja incertidumbre **absorbiendo** con buffers.

---

**Fila: Factores Psicológicos**

- **CPM:** ❌ Muy vulnerable (Parkinson, Estudiante destruyen holgura)
- **Agile:** ⚠️ Media (sprints cortos reducen, pero no eliminan)
- **CCPM:** ✅ Baja - eliminada (sin padding individual, sin incentivo a desperdiciar)

[COMENTAR]

Esta es una diferencia CLAVE.

CPM ignora comportamiento humano.

Agile lo mitiga con sprints cortos.

CCPM lo **elimina** quitando el colchón individual.

---

**Fila: Recursos**

- **CPM:** ❌ Asume ilimitados (ignora, como vimos en caso A-B-C-D)
- **Agile:** Equipo dedicado (mejora, pero sigue siendo abstracto)
- **CCPM:** ✅ Central (recursos son el foco, la restricción)

[COMENTAR]

Esta es la diferencia más importante entre CPM y CCPM.

CCPM **nació** para resolver el problema de recursos limitados que CPM ignora.

---

**Fila: Multitarea**

- **CPM:** Permitida implícitamente (asume paralelismo perfecto)
- **Agile:** Minimizada (WIP limits en Kanban, un sprint a la vez en Scrum)
- **CCPM:** Prohibida explícitamente (focus-and-finish, una tarea a la vez)

[COMENTAR]

CCPM es el más estricto aquí.

"Una persona, una tarea, terminar antes de empezar siguiente."

No negociable.

---

**Fila: Ideal para**

- **CPM:** Proyectos simples y predecibles (construcción pequeña, instalación)
- **Agile:** Requisitos emergentes (software con cliente iterativo)
- **CCPM:** Recursos compartidos/limitados (manufactura, multi-proyecto, ingeniería)

[ÉNFASIS]

**No hay "mejor método universal".**

Hay **"método apropiado para este contexto".**

[PAUSA]

**Regla general:**

- **Alta incertidumbre de requisitos** → Agile
- **Recursos limitados/compartidos** → CCPM
- **Proyecto simple y predecible** → CPM (o hasta Excel)

[PREGUNTA RETÓRICA]

"¿Y si tengo AMBOS problemas: requisitos cambiantes Y recursos limitados?"

[TRANSICIÓN]

Ahí entra la hibridación..."

---

## Slide 26: ¿Cuándo usar qué? (5 min)

"**¿Cuándo Usar Cada Método?**

[VER slide - 3 cajas de colores]

Seamos específicos sobre cuándo aplicar cada uno.

---

**CAJA ROJA: CPM**

[LEER]

- **Proyectos muy predecibles:** Construcción simple, instalación de equipos estándar
- **Recursos abundantes:** Equipos grandes, no hay cuellos de botella
- **Uso académico:** Para aprender planificación básica (educación)

[COMENTAR]

CPM es apropiado cuando:
- Sabés exactamente qué hacer (ya lo hiciste 100 veces)
- Tenés toda la gente que necesites (no hay escasez)

**Ejemplo:** Instalar 50 aires acondicionados iguales en un edificio.

---

**CAJA AZUL: Agile (Scrum)**

[LEER]

- **Software, I+D:** Requisitos cambiantes o poco claros
- **Innovación:** Necesidad de feedback rápido del mercado
- **Equipos autoorganizados:** Alta autonomía y colaboración

[COMENTAR]

Agile es apropiado cuando:
- NO sabés exactamente qué construir (exploración)
- Cliente necesita ver iteraciones tempranas (feedback)
- El QUÉ cambia, pero el QUIÉN está estable (equipo dedicado)

**Ejemplo:** Startup desarrollando MVP de app nueva.

---

**CAJA VERDE: CCPM**

[LEER]

- **Manufactura, Ingeniería:** Requisitos estables pero recursos limitados
- **Multi-proyecto:** Múltiples proyectos compiten por mismos recursos
- **Ambientes con alta presión de tiempo:** Necesidad de entregar rápido

[COMENTAR]

CCPM es apropiado cuando:
- Sabés QUÉ construir (requisitos claros)
- Tenés ESCASEZ de recursos (gente compartida entre proyectos)
- Necesitás VELOCIDAD (competencia, deadline regulatorio)

**Ejemplo:** Empresa de ingeniería con 5 proyectos y 10 ingenieros compartidos.

---

[PAUSA]

**Pregunta común:**

"Mi proyecto tiene características de 2 o 3 de estos. ¿Qué hago?"

[RESPUESTA]

**Combinás enfoques.**

Eso se llama **hibridación**.

Veámoslo..."

---

## Slide 27: Hibridación Agile + CCPM (7 min)

"**Hibridación: Agile + CCPM**

[VER slide - caja gradiente con 2 niveles]

En la práctica, las organizaciones **maduras** combinan enfoques.

No son mutuamente excluyentes.

[LEER subtítulo]

En la práctica, las organizaciones maduras combinan enfoques.

---

**Modelo Híbrido Común:**

[VER CAJA AZUL]

**Nivel Proyecto/Portfolio (CCPM)**

[LEER]

• Usar CCPM para planificar el **proyecto general**
• Identificar Cadena Crítica considerando recursos compartidos
• Dimensionar Buffers de Proyecto y Alimentación
• Gestionar prioridades entre proyectos (cuál va primero)

[PAUSA]

**CCPM gestiona el nivel macro:**
- ¿Cuándo empezamos cada proyecto?
- ¿Qué recursos críticos necesitamos?
- ¿Cuándo prometemos entrega al cliente?

---

[VER CAJA VERDE]

**Nivel Ejecución (Agile)**

[LEER]

• Dentro de cada bloque de la cadena crítica, usar **Scrum/Sprints**
• Estimar con Story Points y Planning Poker
• Iterar y adaptar el **CÓMO** se construye
• Mantener velocidad para forecasting

[PAUSA]

**Agile gestiona el nivel micro:**
- ¿Cómo implementamos este módulo?
- ¿Qué features priorizamos este sprint?
- ¿Necesitamos cambiar enfoque técnico?

---

[EJEMPLO CONCRETO]

Proyecto de 6 meses con 3 equipos:

**Nivel CCPM:**

Cadena Crítica:
- Fase 1: Arquitectura (Equipo A, 4 semanas) [recurso crítico: Arquitecto X]
- Fase 2: Módulo Core (Equipo B, 8 semanas) [depende de Fase 1]
- Fase 3: Integración (Equipo A+C, 6 semanas) [depende de Fase 2]
- Buffer de Proyecto: 4 semanas
- **Total:** 18 + 4 = 22 semanas comprometidas

**Nivel Agile (dentro de cada fase):**

Fase 2 (Módulo Core, 8 semanas):
- Sprint 1 (2 sem): Features X, Y, Z (Story Points, Planning Poker)
- Sprint 2 (2 sem): Features A, B (iteración, adaptación)
- Sprint 3 (2 sem): Features C, D
- Sprint 4 (2 sem): Refactoring, tests

[PAUSA]

**CCPM dice CUÁNDO y CON QUIÉN.**

**Agile dice CÓMO y QUÉ en cada sprint.**

[VER CAJA GRIS en slide]

[LEER]

CCPM gestiona el **CUÁNDO** y los **recursos**.
Agile gestiona el **CÓMO** y el **feedback**.

[ÉNFASIS]

Son complementarios, no competidores.

**CCPM sin Agile:** Rígido en la ejecución (no adaptas si requisitos cambian).

**Agile sin CCPM:** Caótico en multi-proyecto (no gestionás recursos críticos entre proyectos).

**CCPM + Agile:** Lo mejor de ambos mundos.

[TRANSICIÓN]

OK, cerremos con síntesis del curso completo..."

---

## Slide 28: Resumen Completo del Curso (7 min)

"**Resumen Completo del Curso: Las 3 Clases**

[VER slide - 3 cajas]

Hicimos un viaje de 9 horas.

Recapitulemos.

---

**CAJA AZUL:**

**Clase 1: La Crisis**

[LEER]

Cono de Incertidumbre, Parkinson, Síndrome del Estudiante, Ciclo vicioso del padding

[COMENTAR]

Clase 1 fue el **DIAGNÓSTICO**.

"¿Por qué las estimaciones tradicionales fallan sistemáticamente?"

**Lecciones clave:**
- Incertidumbre inherente (±400% al inicio, ±10% al final)
- Factores psicológicos (Parkinson: el trabajo se expande, Estudiante: se posterga)
- Ciclo vicioso: padding → desperdicio → más padding → más desperdicio

**Momento memorable:** Estudios de Microsoft y MIT (padding distribuido NO ayuda).

---

**CAJA PÚRPURA:**

**Clase 2: Los Métodos**

[LEER]

PERT (3 puntos), CPM, T-Shirt Sizing, Story Points, Planning Poker, Velocidad

[COMENTAR]

Clase 2 fue las **HERRAMIENTAS**.

"¿Qué técnicas existen para mejorar estimación?"

**Lecciones clave:**
- PERT: Capturar incertidumbre con 3 puntos (O-M-P)
- CPM: Identificar Ruta Crítica (pero ignora recursos)
- Agile: Story Points (complejidad relativa), Planning Poker (consenso)
- Velocidad: Forecast empírico (basado en datos reales)

**Momento memorable:** Caso de Planning Poker (HU-3 Password Reset: votos de 2 a 13, suposiciones expuestas).

---

**CAJA VERDE:**

**Clase 3: La Solución**

[LEER]

CCPM, Cadena Crítica, 3 tipos de Buffers (PB, FB, RB), Gráfico de Fiebre, Caso A-B-C-D

[COMENTAR]

Clase 3 fue la **SOLUCIÓN SISTÉMICA**.

"¿Cómo gestionar la incertidumbre sin agregar tiempo?"

**Lecciones clave:**
- Cadena Crítica ≠ Ruta Crítica (considera recursos)
- 3 principios: estimaciones agresivas (50%), buffers agregados, focus-and-finish
- 3 tipos de buffers: Proyecto (al final), Alimentación (entre cadenas), Recursos (alarma)
- Fever Chart: monitoreo visual (Verde OK, Amarillo alerta, Rojo crisis)

**Momento memorable:** Caso A-B-C-D (CPM dijo 25 días - equivocado, CCPM logró 27 días - realista y rápido).

---

[VER CAJA AZUL en slide]

**🎯 Mensaje Central del Curso**

[LEER con énfasis]

**Estimar de forma real** significa:

Reconocer la incertidumbre,
gestionar factores humanos,
y colocar la seguridad en **buffers visibles y estratégicos**,
no en padding oculto y vulnerable

[PAUSA]

**El cambio de paradigma:**

**ANTES:** "Cada tarea necesita protección → agregar colchón a cada una"

**DESPUÉS:** "El PROYECTO necesita protección → buffer centralizado y gestionado"

[ANALOGÍA FINAL]

**Es como pasar de:**

"Cada jugador de fútbol tiene su propia pelota" (caos, nadie coordina)

**A:**

"El equipo tiene UNA pelota, todos juegan juntos" (flujo, coordinación)

[TRANSICIÓN]

Últimas 2 slides: qué NO hacer y qué SÍ hacer..."

---

## Slide 29: Lo que NO hacer (5 min)

"**Lo que NO Hacer (Recapitulación de Anti-Patrones)**

[VER slide - lista con íconos ❌]

Después de 9 horas de curso, estas son las **trampas que deben evitar**.

[LEER LISTA]

❌ NO tratar estimaciones iniciales (±400%) como compromisos fijos

[COMENTAR]

En fase de concepto, decir "3 meses" es deshonesto.

Decir "2-6 meses" es honesto.

---

❌ NO planificar durante meses sin comenzar a ejecutar

[COMENTAR]

El plan perfecto es enemigo del plan ejecutable.

Empezar rápido, aprender, ajustar.

---

❌ NO distribuir padding oculto en cada tarea

[COMENTAR]

Clase 1 lo demostró: padding distribuido se desperdicia.

---

❌ NO ignorar factores psicológicos (Parkinson, Estudiante)

[COMENTAR]

Técnicas sin psicología = fracaso garantizado.

---

❌ NO usar CPM sin considerar restricciones de recursos

[COMENTAR]

Caso A-B-C-D lo demostró: CPM falla si hay recursos limitados.

---

❌ NO permitir multitarea mala (cambio de contexto constante)

[COMENTAR]

Focus-and-finish es 30-40% más rápido que multitarea.

---

❌ NO dejar los buffers sin monitorear (Gráfico de Fiebre obligatorio)

[COMENTAR]

Buffer sin monitoreo es padding disfrazado.

Fever Chart es NO negociable en CCPM.

---

❌ NO estimar en tiempo absoluto cuando la incertidumbre es alta

[COMENTAR]

Story Points > horas cuando requisitos son ambiguos.

---

[VER CAJA ROJA en slide]

[LEER]

Estos anti-patrones son la causa del **70% de fracasos de proyectos**

[PAUSA]

Si eliminan estos 8 errores, sus proyectos ya mejorarán 50%.

[TRANSICIÓN]

Ahora lo positivo..."

---

## Slide 30: Lo que SÍ hacer (5 min)

"**Lo que SÍ Hacer (Mejores Prácticas)**

[VER slide - lista con íconos ✅]

Aquí están las prácticas que **SÍ generan resultados**.

[LEER LISTA]

✅ SÍ reconocer el Cono de Incertidumbre y actuar según la fase del proyecto

[COMENTAR]

±400% en inicio → Rango amplio, no fecha fija
±10% en fin → Compromiso preciso

---

✅ SÍ iterar y obtener feedback rápido para estrechar el cono

[COMENTAR]

Cada iteración reduce incertidumbre.

No esperes 6 meses para mostrar algo.

---

✅ SÍ usar estimación relativa (T-Shirt, Story Points) en lugar de absoluta

[COMENTAR]

Complejidad relativa es más estable que tiempo absoluto.

---

✅ SÍ aplicar Planning Poker para consenso y exposición de suposiciones

[COMENTAR]

El valor está en la **discusión**, no en el número final.

---

✅ SÍ identificar la Cadena Crítica considerando recursos

[COMENTAR]

No CPM, CCPM (recursos son clave).

---

✅ SÍ eliminar padding de tareas y agregar Buffers estratégicos

[COMENTAR]

Buffer centralizado protege mejor que padding distribuido.

---

✅ SÍ monitorear activamente los buffers con Gráfico de Fiebre

[COMENTAR]

Verde-Amarillo-Rojo. Simple, visual, efectivo.

---

✅ SÍ prohibir multitarea mala: "Focus and Finish"

[COMENTAR]

Una persona, una tarea, terminar antes de empezar siguiente.

---

✅ SÍ considerar hibridación Agile-CCPM según contexto

[COMENTAR]

No son excluyentes. Combiná lo mejor de ambos.

---

[VER CAJA VERDE en slide]

[LEER]

Estas prácticas incrementan la probabilidad de éxito del proyecto en un **40-60%**

[PAUSA]

No son garantía (nada lo es).

Pero mejoran drásticamente las chances.

[TRANSICIÓN]

Recursos adicionales para seguir aprendiendo..."

---

## Slide 31: Recursos Adicionales (3 min)

"**Recursos Adicionales para Profundizar**

[VER slide - 3 cajas]

Si quieren seguir aprendiendo:

---

**Libros Fundamentales:**

[LEER]

- **"Critical Chain"** - Eliyahu M. Goldratt (1997)
  → EL libro de CCPM. Es novela, fácil de leer.

- **"The Goal"** - Eliyahu M. Goldratt (1984)
  → Teoría de Restricciones (base de CCPM). También novela.

- **"Software Estimation: Demystifying the Black Art"** - Steve McConnell
  → 700 páginas sobre estimación en software. Denso pero completo.

- **"Agile Estimating and Planning"** - Mike Cohn
  → Story Points, Planning Poker, Velocity. Práctico.

---

**Herramientas:**

[LEER]

- Microsoft Project (con extensión CCPM)
  → Puede calcular Cadena Crítica y buffers

- Jira (para Planning Poker y Story Points)
  → Integración con Scrum

- Azure DevOps Boards (para Scrum completo)
  → Todo-en-uno para Agile

- ProChain / Exepron (software especializado en CCPM)
  → Caros, pero potentes para CCPM multi-proyecto

---

**Certificaciones:**

[LEER]

- PMI-ACP (Agile Certified Practitioner)
  → Certificación PMI para Agile

- Certified Scrum Master (CSM)
  → Certificación oficial de Scrum

- TOC for Education (TOCICO)
  → Certificación en Teoría de Restricciones

---

[COMENTAR]

Recomendación personal:

**Empiecen con libros de Goldratt** ("Critical Chain" o "The Goal").

Son novelas, entretenidas, aprenden sin que se sienta como estudio.

[TRANSICIÓN]

Y finalmente..."

---

## Slide 32: Cierre del Curso (5 min)

"**¡Fin del Curso!**

[VER slide - título grande]

[PAUSA]

Felicitaciones.

Completaron 3 clases, 9 horas, un montón de conceptos.

[VER emoji 🎓]

[PAUSA - tono reflexivo]

**Déjenme decirles algo:**

La mayoría de los profesionales nunca aprende esto.

Pasan 20 años estimando mal, sin entender por qué.

Ustedes ahora tienen **ventaja competitiva**.

[VER CAJA GRADIENTE en slide]

**Ahora Saben:**

[LEER con énfasis]

✅ **Por qué** las estimaciones tradicionales fallan
   (Incertidumbre, Parkinson, Estudiante)

✅ **Cómo** gestionar la incertidumbre con el Cono
   (±400% → ±10%, estrechar con iteración)

✅ **Métodos** de estimación: PERT, Agile, CCPM
   (3 puntos, Story Points, Buffers)

✅ **Cómo** proteger proyectos con buffers estratégicos
   (Agregados, visibles, gestionados)

✅ **Cuándo** usar cada método según el contexto
   (CPM simple, Agile incierto, CCPM recursos limitados)

[PAUSA]

**No esperen a proyecto "perfecto" para aplicar esto.**

Empiecen mañana:

- **Mañana:** Identificá la Cadena Crítica de tu proyecto (considerando recursos)
- **Esta semana:** Probá Planning Poker con tu equipo (una historia, 15 min)
- **Este mes:** Calculá un buffer y monitorealo con Fever Chart

[ÉNFASIS]

**Aprender haciendo > aprender leyendo.**

[PAUSA - tono de cierre]

Fue un placer compartir estas 9 horas con ustedes.

Espero que les sirva en sus carreras.

[LEER información del instructor]

**Alejandro Sfrede**
Área de Arquitectura

[VER BOTONES en slide]

Si quieren repasar algo:
- ← Clase 2 (Métodos)
- 🏠 Portal (Índice completo)

[PAUSA FINAL]

**¿Preguntas finales antes de cerrar?**

[Esperar si hay preguntas]

[CIERRE]

Muchas gracias.

¡Éxito en sus proyectos!"

---

## 🎯 FIN DE SPEECH SCRIPTS - CLASE 3 COMPLETA

---

**Total Clase 3:** 32 slides
**Duración:** 180 minutos (3 horas)

**Estructura:**
- Portada y Agenda: 5 min
- Introducción a CCPM y TOC: 45 min
- Gestión de Buffers: 40 min
- Break: 15 min
- Caso A-B-C-D (Taller): 60 min
- Síntesis Final y Comparación: 15 min

**Timing por bloque:**
- Pre-break: 90 min (slides 1-14)
- Break: 15 min
- Post-break: 75 min (slides 15-32)

---

**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 2.0 - Formato Remoto
**Fecha:** Enero 2025
**Tono:** Amigable, relajado, conversacional (igual que Clase 1 y 2)

---

## 📝 NOTAS PARA EL FACILITADOR

**Momentos clave para enfatizar:**

1. **Slide 4 (Problema de CPM):** Ir DESPACIO. Este es el "setup" del problema que CCPM resuelve.

2. **Slide 6 (3 Principios):** Enfatizar que los 3 son NECESARIOS juntos (sistema completo).

3. **Slide 7 (Holgura vs Buffer):** Conectar con Clase 1 (Parkinson, Estudiante). Es el "por qué" psicológico.

4. **Slides 16-23 (Caso A-B-C-D):** Este es el CLÍMAX. Ir paso a paso, dejar pausas, crear suspenso.

5. **Slide 20 (Momento Aha!):** Tomarse tiempo aquí. Es el payoff emocional del curso completo.

**Ajustes de timing:**

- Si vas atrasado pre-break: Recortar slides 9-12 (dimensionamiento SSQ es opcional).
- Si vas atrasado post-break: NO recortar caso A-B-C-D (es el core), recortar slides 28-31 (síntesis).

**Engagement:**

- Preguntar frecuentemente: "¿Esto les resuena con sus proyectos?"
- Caso A-B-C-D: Pedir que piensen cuántos días ANTES de revelar respuesta.
- Fever Chart: Mostrar ejemplo de proyecto real si es posible.

**Errores comunes a evitar:**

- NO apurarse en Caso A-B-C-D (es el momento más importante).
- NO sobrevender CCPM como "solución mágica" (es herramienta poderosa pero no resuelve todo).
- NO olvidar conectar con Clases 1 y 2 (es un curso integrado, no 3 clases independientes).
