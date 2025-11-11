# Guía del Profesor - Clase 3: Cadena Crítica (CCPM)
## PARTE 2: Caso A-B-C-D y Síntesis Final (Post-Break)

**Duración:** 90 minutos (segunda mitad de 180 min totales)
**Formato:** Remoto / Walkthrough guiado paso a paso

---

## 📋 Contenido de Esta Parte

| Slide | Tema | Duración |
|-------|------|----------|
| 15 | Introducción al Caso A-B-C-D | 3 min |
| 16 | Setup del Proyecto (tareas y recursos) | 5 min |
| 17 | Paso 1: Calcular Ruta Crítica (CPM) | 8 min |
| 18 | Paso 2: La Revelación del Recurso | 7 min |
| 19 | Paso 3: Identificar Cadena Crítica Real | 10 min |
| 20 | El Momento "Aha!" | 8 min |
| 21 | Paso 4: Aplicar CCPM (eliminar padding) | 10 min |
| 22 | Paso 5: Calcular y Agregar Buffer | 8 min |
| 23 | Resultado Final: Comparativa | 8 min |
| 24 | Debriefing del Caso | 8 min |
| 25 | Cuadro Comparativo Final: CPM vs Ágil vs CCPM | 10 min |
| 26 | Síntesis del Curso Completo | 5 min |

**Total Parte 2:** 90 minutos

---

## 🧠 Pensamiento Profundo: El Caso A-B-C-D

### Por Qué Este Caso Es El Corazón Del Curso

**El caso A-B-C-D es DELIBERADAMENTE SIMPLE** para que el concepto quede cristalino:

- Solo 4 tareas (A, B, C, D)
- Solo 3 recursos (Juan, Ana, Pedro)
- Solo 1 restricción de recurso (Ana hace B y D)
- Matemática básica (sumas, 50%)

**Pero revela el PROBLEMA FUNDAMENTAL de CPM:**

CPM dice 25 días → Imposible de cumplir (realidad es 35 días)

**Y muestra la SOLUCIÓN de CCPM:**

CCPM dice 27 días → Realista, protegido, 23% más rápido que tradicional

### La Progresión Pedagógica

**Paso 1-2:** Mostrar que CPM falla (diagnosis)
**Paso 3:** Identificar la causa (recurso compartido)
**Paso 4-5:** Aplicar la solución (CCPM con buffers)
**Paso 6:** Comparar resultados (el "aha!")

### El Momento "Aha!" - Qué Debe Pasar Emocionalmente

**Cuando lleguemos a Slide 20 (El Momento "Aha!"), participantes deben:**

1. **Sentir frustración retrospectiva:**
   - "¿Por qué nadie me enseñó esto antes?"
   - "¿Cuántos proyectos fallaron por ignorar esto?"

2. **Ver claridad conceptual:**
   - "Ah, entonces CPM no es malo, es incompleto"
   - "CCPM es CPM + nivelación de recursos + buffers"

3. **Querer aplicarlo:**
   - "Quiero probar esto en mi proyecto"
   - "¿Cómo empiezo?"

**Si no pasa esto, el caso falló pedagógicamente.**

### Desafíos Comunes En Este Bloque

**1. "Es muy simple, mi proyecto es más complejo"**

**Respuesta:**
"Exacto, es simple PARA ENSEÑAR. En proyecto real con 50 tareas y 10 recursos, el problema se MULTIPLICA. Herramientas como MS Project con CCPM hacen los cálculos. El concepto es lo importante."

**2. "En mi organización no puedo prohibir multitarea"**

**Respuesta:**
"Entiendo. CCPM es cambio cultural, no solo técnico. Empieza con 1 proyecto piloto. Muestra resultados. Expande después."

**3. "Mi jefe nunca aceptará estimaciones 50%"**

**Respuesta:**
"Muestra ESTE caso. 35 días con padding vs 27 días con CCPM. Pregunta: '¿Prefieres promesa falsa de 35 días que se convierte en 40+, o promesa honesta de 27 días que cumples?' Educa, no impongas."

**4. "¿Y si el buffer no alcanza?"**

**Respuesta:**
"Entonces el proyecto se retrasa. PERO tienes visibilidad temprana (Fever Chart) para avisar al cliente con 50% del proyecto hecho, NO al 95%. Eso es valor."

---

## 📖 Desglose Slide por Slide

---

### **Slide 15: Introducción al Caso A-B-C-D** (3 min)

**Objetivos:**
- Enmarcar el caso como el "momento aha!"
- Generar expectativa
- Establecer objetivos del walkthrough

**Script sugerido:**

"Bienvenidos de vuelta del break.

Ahora: **EL caso que integra todo**.

[VER slide]

**Caso de Estudio: Proyecto A-B-C-D**

**Objetivo del Taller:**

Vamos a resolver un proyecto COMPLETO paso a paso:

1. Calcular Ruta Crítica con CPM (ignora recursos)
2. Identificar restricción de recursos
3. Calcular Cadena Crítica (con recursos)
4. Aplicar CCPM (eliminar padding + agregar buffers)
5. Comparar resultados: CPM vs Tradicional vs CCPM

[ÉNFASIS]

**Este es el momento 'aha!' donde todo se integra.**

Van a ver:

✅ Por qué CPM falla (da timeline imposible)
✅ Por qué plan tradicional inflado es lento
✅ Por qué CCPM es más rápido Y más robusto

[PAUSA]

El caso es SIMPLE a propósito:
- 4 tareas
- 3 personas
- 1 restricción

Matemática fácil, concepto profundo.

[TRANSICIÓN]

Empecemos."

---

**Tips para el facilitador:**

✅ **Tono:** Energía alta. Este es el clímax del curso.

✅ **Anticipar:** "Van a tener un momento de 'Ohhhh, por ESO mis proyectos fallan'. Es normal."

⚠️ **Evitar:** Apurarse. Cada paso debe quedar claro antes de seguir.

⏰ **Timing:** 3 min (corto, ir directo al caso)

---

### **Slide 16: Setup del Proyecto** (5 min)

**Objetivos:**
- Presentar las 4 tareas (A, B, C, D)
- Mostrar dependencias
- Revelar recursos (ESPECIALMENTE que Ana hace B y D)

**Script sugerido:**

"Aquí está el proyecto:

[VER TABLA en slide]

**Tareas y Dependencias:**

| Tarea | Depende de | Duración Inflada | Recurso |
|-------|------------|------------------|---------|
| **A** | - | 10 días | Juan |
| **B** | A | 10 días | Ana |
| **C** | A | 5 días | Pedro |
| **D** | C | 10 días | Ana |

[LEER fila por fila]

**Tarea A:**
- No depende de nadie (empieza al inicio)
- Duración: 10 días
- La hace Juan

**Tarea B:**
- Depende de A (no puede empezar hasta que A termine)
- Duración: 10 días
- La hace **Ana**

**Tarea C:**
- Depende de A (no puede empezar hasta que A termine)
- Duración: 5 días
- La hace Pedro

**Tarea D:**
- Depende de C (no puede empezar hasta que C termine)
- Duración: 10 días
- La hace **Ana**

[PAUSA - VER CAJA ROJA en slide]

⚠️ **Nota la trampa: Ana hace TANTO B como D**

[ÉNFASIS]

Esto es CLAVE.

Ana es un **recurso compartido** entre dos tareas.

Por ahora, solo noten esto. Lo vamos a usar después.

[PAUSA - DIBUJAR mentalmente]

Imaginen el diagrama:

```
Inicio
  ├─ A (Juan) ─┬─ B (Ana)
  └────────────┴─ C (Pedro) ─ D (Ana)
```

Dos rutas que salen de A:
- Ruta 1: A → B
- Ruta 2: A → C → D

[ACLARACIÓN]

**"Duración Inflada"** significa:
- Estimación tradicional
- Incluye padding oculto (~100% buffer individual)
- Como las estimaciones que hacen PMs normalmente

Más adelante vamos a CORTAR ese padding.

[TRANSICIÓN]

OK, tenemos el proyecto. Ahora hagamos CPM tradicional."

---

**Preguntas para engagement:**

1. "¿Ven algún problema potencial con este plan?"
2. "¿Qué pasa si Ana hace B y D simultáneamente? (es posible?)"
3. "¿Cuál creen que es la ruta más larga?"

**Tips para el facilitador:**

✅ **Marcar la trampa:** "Apunten en sus notas: Ana hace B y D. Esto es importante."

✅ **Dibujar si es posible:** Pizarra virtual con el diagrama ayuda enormemente.

⚠️ **Evitar:** Revelar el final. Mantener suspense.

💡 **Señal de entendimiento:** Si alguien dice "Ana va a ser el cuello de botella", perfecto: "Exacto, lo vamos a ver."

⏰ **Timing:** 5 min (2 min tabla, 3 min diagrama mental)

---

### **Slide 17: Paso 1 - Calcular Ruta Crítica (CPM)** (8 min)

**Objetivos:**
- Aplicar CPM ignorando recursos
- Identificar las 2 rutas
- Calcular Ruta Crítica = 25 días

**Script sugerido:**

"Paso 1: Aplicar CPM.

Recordatorio: CPM asume **recursos ilimitados** (o que no son restricción).

[VER slide - dos cajas]

Tenemos 2 rutas que salen de A:

---

**RUTA 1: A → B**

[VER DIAGRAMA en slide]

```
A (10d) → B (10d)
```

**Duración Total:**
10 + 10 = **20 días**

[PAUSA]

---

**RUTA 2: A → C → D**

[VER DIAGRAMA en slide]

```
A (10d) → C (5d) → D (10d)
```

**Duración Total:**
10 + 5 + 10 = **25 días**

[PAUSA]

---

**Pregunta: ¿Cuál es la Ruta Crítica?**

[Esperar respuestas]

**Respuesta:**

La más larga: **Ruta 2 (A → C → D) = 25 días**

[VER CAJA DESTACADA en slide]

**Ruta Crítica (CPM) = A-C-D = 25 días**

[EXPLICAR]

Según CPM:

- Ruta A-C-D es crítica (25 días)
- Ruta A-B es NO crítica (20 días)
- Tarea B tiene **5 días de holgura**
  - Puede empezar hasta día 15 (en vez de día 10) sin retrasar proyecto

**Plan CPM:**

```
Día 0: Inicio
Día 1-10: Juan hace A
Día 11-20: Ana hace B (o puede esperar hasta día 15)
Día 11-15: Pedro hace C (en paralelo con B)
Día 16-25: Ana hace D
Día 25: Fin
```

[PAUSA]

**Según CPM, el proyecto toma 25 días.**

B y D se hacen "en paralelo" (B días 11-20, D días 16-25).

[ÉNFASIS - preparar revelación]

¿Ven algún problema con este plan?

[DAR 10 SEGUNDOS - algunos verán, otros no]

[Si alguien dice "Ana no puede hacer B y D al mismo tiempo"]

Perfecto, exacto. Vamos a ver eso.

[Si nadie lo ve]

Vamos al siguiente paso."

---

**Preguntas para engagement:**

1. "¿Por qué Ruta 2 es más larga que Ruta 1?"
2. "¿Qué significa que B tiene 5 días de holgura?"
3. "¿Este plan de 25 días les parece correcto?"

**Tips para el facilitador:**

✅ **Ir despacio en los cálculos:** 10+10=20, 10+5+10=25. Obvio pero importante.

✅ **Dibujar timeline:** Si hay pizarra virtual, mostrar días 1-25 con tareas superpuestas.

⚠️ **Evitar:** Decir "CPM está mal". Decir "CPM es correcto BAJO SU SUPOSICIÓN (recursos ilimitados)."

💡 **Anticipar:** "¿Por qué B y D se superponen?" Respuesta: "Porque CPM asume que Ana puede hacer ambas simultáneamente, o que hay 2 Anas."

⏰ **Timing:** 8 min (4 min Ruta 1, 4 min Ruta 2 + conclusión)

---

### **Slide 18: Paso 2 - La Revelación del Recurso** (7 min)

**Objetivos:**
- Revelar el problema: Ana hace B y D
- Mostrar que CPM es imposible de cumplir
- Generar tensión dramática

**Script sugerido:**

"Paso 2: La Revelación.

[VER slide - caja grande destacada]

**El PM se da cuenta:**

[LEER con dramatismo]

**'Ana hace TANTO la tarea B COMO la tarea D'**

[PAUSA LARGA]

**Ana NO puede hacer multitarea.**

**Tiene que hacer una, DESPUÉS la otra.**

[PAUSA]

Volvamos al plan CPM:

```
Día 11-20: Ana hace B
Día 16-25: Ana hace D (en paralelo?)
```

[ÉNFASIS]

**Días 16-20: Ana haría B Y D simultáneamente.**

[PAUSA]

¿Es esto posible?

[Esperar respuestas]

**NO.**

Ana es una persona. No puede hacer 2 tareas al mismo tiempo.

[ANALOGÍA]

Es como si el plan dijera:
- Lunes: Ana escribe código para B
- Lunes (al mismo tiempo): Ana escribe código para D

Imposible.

[VER CAJA en slide - Pregunta Crítica]

**Pregunta Crítica:**

¿El plan de 25 días (CPM) sigue siendo válido?

[PAUSA DRAMÁTICA]

[VER RESPUESTA en slide]

**NO**

[ÉNFASIS]

El plan de 25 días es **MATEMÁTICAMENTE CORRECTO** bajo la suposición de CPM (recursos ilimitados).

Pero es **OPERATIVAMENTE IMPOSIBLE** en la realidad (Ana es UNA persona).

[PAUSA]

**Esto pasa en proyectos reales TODO EL TIEMPO:**

PM usa CPM, calcula 6 meses, promete al cliente.

Día 1 del proyecto:
- Recurso X está en 3 tareas "paralelas"
- Recurso Y está en 5 proyectos simultáneos

Resultado:
- Proyecto toma 9 meses (50% más)
- PM culpado: "Estimaste mal"
- Pero no estimó mal. **Usó herramienta que ignora recursos.**

[CONECTAR con Clase 1]

¿Recuerdan el Cono de Incertidumbre?

Una de las fuentes de incertidumbre es:
**Suposiciones incorrectas sobre disponibilidad de recursos**

CPM hace esa suposición incorrecta por diseño.

[TRANSICIÓN]

OK, CPM falló. ¿Cuál es la duración REAL del proyecto?"

---

**Preguntas para engagement:**

1. "¿Alguna vez les pasó: plan dice X meses, toma 1.5X o 2X?"
2. "¿Cuál creen que es la duración real considerando que Ana hace B y D secuencialmente?"
3. "¿CPM es malo o simplemente incompleto?"

**Tips para el facilitador:**

✅ **Dramatismo:** Este es el "plot twist" del caso. Usar pausas, tono sorprendido.

✅ **Empatía:** "No es culpa de ustedes. CPM se enseña en todas las universidades, pero con esta limitación."

⚠️ **Evitar:** Culpar a CPM. Es herramienta útil cuando recursos NO son restricción (ej: proyecto con presupuesto alto, puede contratar gente).

💡 **Anticipar:** "¿Por qué no contratar otra Ana?" Respuesta: "Si es recurso especializado (ej: arquitecto senior único), no puedes. O es muy caro."

⏰ **Timing:** 7 min (3 min revelación, 4 min implicaciones)

---

### **Slide 19: Paso 3 - Identificar Cadena Crítica Real** (10 min)

**Objetivos:**
- Re-planificar con recursos nivelados
- Decidir: ¿Ana hace B o D primero?
- Calcular Cadena Crítica = 35 días

**Script sugerido:**

"Paso 3: Re-planificar con la REALIDAD de recursos.

[VER slide]

**Restricción:**

Ana NO puede hacer B y D simultáneamente.

Tiene que hacer una PRIMERO, después la otra.

**Pregunta: ¿Cuál hace primero?**

[VER CAJA en slide - Decisión]

**Decisión:**

Para minimizar duración total del proyecto, Ana debe hacer PRIMERO la tarea de la **ruta más larga**.

[EXPLICAR]

Tenemos:
- Ruta 1 (A→B): 20 días
- Ruta 2 (A→C→D): 25 días

**D está en la ruta de 25 días.**
**B está en la ruta de 20 días.**

[PAUSA]

Si Ana hace **D primero:**

```
A (día 1-10)
  ├─ C (día 11-15, Pedro) → D (día 16-25, Ana) → Fin Ruta 2
  └─ B espera hasta que Ana termine D (día 26-35)
```

**Duración total: 35 días**

---

Si Ana hace **B primero:**

```
A (día 1-10)
  ├─ B (día 11-20, Ana) → Fin Ruta 1
  └─ C (día 11-15, Pedro) → D espera hasta que Ana termine B (día 21-30)
```

**Duración total: 30 días**

[PAUSA]

**Espera, 30 días < 35 días. ¿No debería Ana hacer B primero entonces?**

[ACLARACIÓN - ERROR COMÚN]

Buen punto, pero hay trampa:

Si Ana hace B primero (día 11-20):
- C termina día 15
- D necesita esperar a que:
  1. C termine (día 15) ✓
  2. Ana esté disponible (día 20) ✓
- D empieza día 21, termina día 30
- **Duración: 30 días**

Si Ana hace D primero:
- C termina día 15
- D empieza día 16 (INMEDIATAMENTE después de C)
- D termina día 25
- B empieza día 26, termina día 35
- **Duración: 35 días**

[ÉNFASIS]

**CORREGIDO:**

Tienes razón. Ana DEBE hacer D primero para que D empiece inmediatamente después de C.

Si hace B primero, D debe esperar 5 días extra (día 16-20).

[RECALCULAR]

**Estrategia óptima: Ana prioriza D (ruta crítica)**

Secuencia:

```
A (10d) → C (5d) → D (10d, Ana) → B (10d, Ana)
```

[VER DIAGRAMA en slide]

**A (10d) → C (5d) → D (10d) → B (10d)**

[CALCULAR]

10 + 5 + 10 + 10 = **35 días**

[VER CAJA DESTACADA en slide]

**Cadena Crítica Real = A-C-D-B = 35 días**

**¡10 días MÁS que lo que CPM dijo!**

[PAUSA LARGA]

[ÉNFASIS]

**CPM:** "El proyecto toma 25 días"
**Realidad:** "El proyecto toma 35 días"

**Error: 40%**

[PAUSA]

Esto explica por qué tantos proyectos CPM "fallan":

El plan inicial era **matemáticamente correcto pero operativamente imposible**.

[TRANSICIÓN]

OK, ahora sabemos que duración REAL es 35 días (con padding tradicional).

¿Podemos hacerlo más rápido?

Ahí entra CCPM."

---

**Preguntas para engagement:**

1. "¿Por qué A-C-D-B es 35 días?"
2. "Si contratamos otra persona para B, ¿volvemos a 25 días?"
3. "¿En sus proyectos, cuántas 'Anas' tienen (recursos compartidos)?"

**Tips para el facilitador:**

✅ **Admitir error si lo cometes:** El razonamiento de "Ana hace D primero" puede ser confuso. Ir paso a paso.

✅ **Dibujar timeline día por día:** Si es posible, mostrar días 1-35 con quién hace qué.

⚠️ **Evitar:** Apurarse. Este es el cálculo MÁS IMPORTANTE del caso.

💡 **Tip pedagógico:** Si hay confusión, dibujar AMBOS escenarios (B primero vs D primero) lado a lado.

⏰ **Timing:** 10 min (5 min decisión, 5 min cálculo)

---

### **Slide 20: El Momento "Aha!"** (8 min)

**Objetivos:**
- Consolidar revelación: CPM = 25d (imposible), Realidad = 35d
- Generar impacto emocional
- Preparar para solución CCPM

**Script sugerido:**

"Pausa. Absorbamos esto.

[VER slide - caja grande]

[LEER con énfasis]

**CPM nos dio 25 días**

**(IMPOSIBLE de cumplir)**

**La duración REAL con recursos nivelados es 35 días**

[PAUSA LARGA - 5 SEGUNDOS]

[ÉNFASIS]

**Esta es la razón por la que tantos proyectos CPM 'fallan':**

[LEER]

'El plan inicial era matemáticamente correcto pero operativamente imposible'

[PAUSA]

Levanten la mano si esto les pasó:

[Preguntar]

- ¿Alguna vez un proyecto "se retrasó" 40-50%?
- ¿El PM dijo "No sé qué pasó, estimamos bien"?
- ¿El equipo fue culpado de "lento"?

[Varios levantarán la mano]

[ÉNFASIS]

**Probablemente NO estimaron mal.**

**Probablemente usaron CPM que ignora recursos.**

El "retraso" no fue retraso. Fue que el plan inicial era **fantasía**.

[PAUSA]

**Ejemplo real:**

Proyecto de 6 meses según CPM.

Realidad: 9 meses (50% más).

¿Qué pasó?

- Arquitecto senior en 5 proyectos simultáneos
- 2 devs compartidos con otro equipo
- DBA disponible solo 50% (otro proyecto prioritario)

CPM asumió: recursos ilimitados.

Realidad: todos son cuellos de botella.

[PAUSA]

[VER CAJA VERDE en slide]

**CCPM identifica la Cadena Crítica REAL considerando recursos**

[ÉNFASIS]

**CCPM NO adivina mejor.**

**CCPM planifica con la REALIDAD, no con suposiciones.**

[TRANSICIÓN]

OK, sabemos que:
- CPM: 25 días (fantasía)
- Tradicional inflado: 35 días (realista pero lento)

¿Puede CCPM hacerlo más rápido que 35 días?

Sí.

Veamos cómo."

---

**Preguntas para engagement:**

1. "¿Cuántos proyectos 'retrasados' en realidad tenían plan imposible desde el inicio?"
2. "¿Por qué organizaciones siguen usando CPM si tiene esta limitación?"
3. "¿Qué harían diferente en su próximo proyecto?"

**Tips para el facilitador:**

✅ **Impacto emocional:** Este es EL momento del curso. Pausas largas, tono serio.

✅ **Validar experiencias:** "No es culpa de ustedes. Es limitación de la herramienta."

⚠️ **Evitar:** Seguir adelante sin que absorban esto. Vale la pena 8 minutos completos.

💡 **Señal de éxito:** Si alguien dice "Wow, esto explica TANTAS cosas", misión cumplida.

⏰ **Timing:** 8 min (4 min revelación, 4 min implicaciones)

---

### **Slide 21: Paso 4 - Aplicar CCPM (Eliminar Padding)** (10 min)

**Objetivos:**
- Aplicar Principio 1: estimaciones agresivas 50%
- Cortar padding de cada tarea
- Recalcular Cadena Crítica sin padding

**Script sugerido:**

"Paso 4: Aplicar CCPM.

Recordamos Principio 1 de CCPM:

**'Eliminar padding de las tareas individuales'**

[PAUSA]

Nuestras duraciones actuales son "infladas":
- Incluyen ~100% de colchón oculto
- Estimaciones con 80-90% probabilidad de éxito

CCPM usa estimaciones **agresivas**:
- 50% de probabilidad
- Sin colchón oculto

[VER TABLA en slide]

**4a. Eliminar padding (cortar al 50%):**

| Tarea | Duración Inflada | Duración Agresiva (50%) | Cortado |
|-------|------------------|-------------------------|---------|
| **A** | 10 días | 5 días | 5 días |
| **B** | 10 días | 5 días | 5 días |
| **C** | 5 días | 3 días | 2 días |
| **D** | 10 días | 5 días | 5 días |
| **TOTAL** | **35 días** | **18 días** | **17 días** |

[EXPLICAR fila por fila]

**Tarea A:**
- Inflada: 10 días
- Agresiva (50%): 5 días
- Cortado: 5 días de padding

[PAUSA - EXPLICAR el 50%]

¿Qué significa "50% probabilidad"?

Si hacemos tarea A 10 veces:
- 5 veces terminará en ≤5 días
- 5 veces terminará en >5 días (necesitará 6, 7, 8... días)

**NO es imposible.** Es el valor MEDIO.

**Tarea B:**
- Inflada: 10 días
- Agresiva: 5 días
- Cortado: 5 días

**Tarea C:**
- Inflada: 5 días
- Agresiva: 3 días (redondeamos 2.5 → 3)
- Cortado: 2 días

**Tarea D:**
- Inflada: 10 días
- Agresiva: 5 días
- Cortado: 5 días

[VER FILA TOTAL]

**TOTAL:**
- Suma inflada: 35 días
- Suma agresiva: 5+5+3+5 = **18 días**
- Total cortado: 17 días

[PAUSA]

**Nueva Cadena Crítica agresiva:**

```
A (5d) → C (3d) → D (5d) → B (5d) = 18 días
```

[ÉNFASIS]

De 35 días → 18 días.

**Cortamos casi 50%.**

[PAUSA - ANTICIPAR OBJECIÓN]

"Pero espera, eso es PELIGROSO. Las tareas tienen 50% de fallar su deadline individual."

**Respuesta:**

SÍ, individualmente son agresivas.

PERO vamos a agregar BUFFER AL FINAL para proteger.

[TRANSICIÓN]

Veamos el buffer."

---

**Preguntas para engagement:**

1. "¿50% les parece demasiado agresivo?"
2. "Si tarea toma 6 días en vez de 5, ¿qué pasa?"
3. "¿Cómo convencerían a un ejecutor de estimar 50%?"

**Tips para el facilitador:**

✅ **Enfatizar:** 50% NO es imposible, es HONESTO.

✅ **Analogía útil:** "Estimación inflada 10d es como decir 'llego en 20 min' cuando sabes que son 10 min, para 'estar seguro'. CCPM dice 'llego en 10 min + buffer de proyecto'."

⚠️ **Evitar:** Decir "vamos a cortar TODO el padding". Decir "vamos a MOVERLO al final como buffer visible."

💡 **Anticipar:** "¿Qué pasa con el 50% cortado?" Respuesta: "Va al buffer. Lo vemos ya."

⏰ **Timing:** 10 min (5 min tabla, 5 min explicación 50%)

---

### **Slide 22: Paso 5 - Calcular y Agregar Buffer de Proyecto** (8 min)

**Objetivos:**
- Aplicar Principio 2: buffer agregado
- Calcular PB = 50% de CC
- Mostrar plan CCPM final

**Script sugerido:**

"Paso 5: Agregar Buffer de Proyecto.

Recordamos Principio 2 de CCPM:

**'Agregar seguridad como buffers estratégicos'**

[VER CAJA en slide]

**Método del 50%:**

```
PB = 50% × 17 días cortados = 8.5 días ≈ 9 días
```

[EXPLICAR]

Cortamos 17 días de padding total (5+5+2+5).

Buffer de Proyecto = 50% de eso = 8.5 días.

Redondeamos a **9 días**.

[PAUSA]

**¿Por qué 50% y no 100%?**

Porque las variaciones individuales se PROMEDIAN:

- Algunas tareas terminarán ANTES de 50% (ej: 4 días en vez de 5)
- Otras terminarán DESPUÉS (ej: 6 días en vez de 5)
- En promedio, se cancelan

Buffer de 50% da ~85-90% confianza de terminar dentro de timeline.

[VER DIAGRAMA en slide]

**Plan CCPM Final:**

```
A (5d) → C (3d) → D (5d) → B (5d) → [PB: 9d] → 🏁
```

[CALCULAR]

Cadena Crítica: 5 + 3 + 5 + 5 = 18 días
Project Buffer: 9 días
**Total: 27 días**

[VER CAJA VERDE en slide]

**Plan CCPM = 18d + 9d = 27 días**

**Con fecha de entrega PROTEGIDA y REALISTA**

[ÉNFASIS]

Comparemos:

- **CPM:** 25 días (imposible - ignora recursos)
- **Tradicional inflado:** 35 días (realista pero lento - padding desperdiciado)
- **CCPM:** 27 días (realista Y rápido - buffer protegido)

[PAUSA]

**CCPM es 23% más rápido que tradicional (8 días menos).**

**Con MISMA protección (mismo total de padding, pero agregado).**

[TRANSICIÓN]

Veamos la comparativa completa."

---

**Preguntas para engagement:**

1. "¿Por qué 27 días CCPM vs 35 días tradicional?"
2. "¿El buffer de 9 días es suficiente?"
3. "¿Qué pasa si se consumen los 9 días de buffer?"

**Tips para el facilitador:**

✅ **Enfatizar:** Misma protección (17 días cortados → 9d buffer + holgura estadística), timeline más corto.

✅ **Analogía útil:** "Es como consolidar deudas: mismo dinero total, mejor gestión."

⚠️ **Evitar:** Decir que CCPM es "gratis". Requiere disciplina (prohibir Parkinson, monitorear buffer).

💡 **Anticipar:** "¿Y si 4 tareas se atrasan?" Respuesta: "Buffer absorbe. Si buffer se agota, proyecto se retrasa a 27+ días. Pero Fever Chart alertó temprano."

⏰ **Timing:** 8 min (3 min cálculo, 5 min plan final)

---

### **Slide 23: Resultado Final - Comparativa** (8 min)

**Objetivos:**
- Mostrar tabla comparativa de 3 métodos
- Explicar validez y protección de cada uno
- Consolidar aprendizaje del caso

**Script sugerido:**

"Resultado final del caso A-B-C-D.

[VER TABLA en slide]

**Comparativa de los 3 métodos:**

| Método | Duración | Validez | Protección |
|--------|----------|---------|------------|
| **CPM (ingenuo)** | 25 días | ❌ INCORRECTO | ❌ Ignora recursos |
| **Tradicional inflado** | 35 días | ✓ Correcto | ❌ Padding vulnerable |
| **CCPM** | 27 días (18+9) | ✓ Correcto | ✅ Buffer protegido |

[EXPLICAR fila por fila]

---

**Fila 1: CPM (ingenuo)**

- **Duración:** 25 días
- **Validez:** ❌ INCORRECTO
  - Asume Ana puede hacer B y D simultáneamente
  - Operativamente imposible
- **Protección:** ❌ Ignora recursos
  - No considera cuellos de botella
  - Plan condenado a fallar desde inicio

[ÉNFASIS]

CPM da timeline **optimista pero inalcanzable**.

---

**Fila 2: Tradicional inflado**

- **Duración:** 35 días
- **Validez:** ✓ Correcto
  - Considera recursos (Ana hace B y D secuencialmente)
  - Operativamente posible
- **Protección:** ❌ Padding vulnerable
  - Cada tarea tiene colchón oculto
  - Ley de Parkinson: colchón se desperdicia
  - Síndrome del Estudiante: se posterga hasta deadline

[ÉNFASIS]

Tradicional da timeline **realista pero inflado**.

Proyecto tomará 35 días o más (si algo falla Y padding se gastó).

---

**Fila 3: CCPM**

- **Duración:** 27 días (18 tareas + 9 buffer)
- **Validez:** ✓ Correcto
  - Considera recursos (Ana hace D luego B)
  - Tareas agresivas (50% probabilidad)
  - Operativamente posible
- **Protección:** ✅ Buffer protegido
  - Padding agregado al final, visible
  - NO vulnerable a Parkinson (tareas sin colchón)
  - Gestionado activamente (Fever Chart)

[ÉNFASIS]

CCPM da timeline **realista, protegido y acelerado**.

[PAUSA]

[VER CAJA DESTACADA en slide - Conclusión]

**💡 Conclusión del Caso:**

✅ CCPM entrega **8 días ANTES** que plan inflado tradicional (23% más rápido)

✅ CCPM es **REALISTA** (considera recursos, no fantasía como CPM)

✅ CCPM es **ROBUSTO** (buffer protegido, no vulnerable a Parkinson)

✅ CCPM es **GESTIONABLE** (visibilidad del buffer con Fever Chart)

[PAUSA]

**Pregunta crítica:**

'¿Por qué NO usar SIEMPRE CCPM?'

[Esperar respuestas]

**Respuesta:**

CCPM requiere:
1. **Cambio cultural:** Aceptar estimaciones 50%, prohibir multitarea
2. **Disciplina:** Monitorear buffer diariamente/semanalmente
3. **Herramientas:** MS Project con CCPM, o software especializado

**NO es "gratis".**

Pero el ROI es enorme: 20-30% reducción de timeline, 85% on-time vs 40% tradicional.

[TRANSICIÓN]

Hagamos debriefing del caso."

---

**Preguntas para engagement:**

1. "¿Cuál método usarían en su próximo proyecto? ¿Por qué?"
2. "¿Qué objeciones anticipan de stakeholders?"
3. "¿Vale la pena 23% aceleración a cambio de cambio cultural?"

**Tips para el facilitador:**

✅ **Enfatizar:** CCPM no es "mejor" universalmente, es mejor CUANDO recursos son restricción.

✅ **Ser honesto:** CCPM requiere inversión (capacitación, herramientas, cambio cultura).

⚠️ **Evitar:** Over-selling. CCPM no resuelve TODOS los problemas (ej: requisitos ambiguos).

💡 **Dato útil:** "Goldratt reportó 85% on-time en proyectos CCPM vs 40% tradicional (CHAOS Report)."

⏰ **Timing:** 8 min (4 min tabla, 4 min conclusión)

---

### **Slide 24: Debriefing del Caso** (8 min)

**Objetivos:**
- Consolidar lecciones con preguntas guiadas
- Asegurar entendimiento profundo
- Conectar con conceptos de Clase 1-2

**Script sugerido:**

"Debriefing: ¿Qué aprendimos?

[VER slide - caja con 3 preguntas]

Voy a hacer 3 preguntas. Piensen antes de que responda.

---

**Pregunta 1: ¿Por qué CPM falló?**

[DAR 10 SEGUNDOS]

[LEER RESPUESTA en slide]

'Porque asumió que B y D podían ocurrir en paralelo (recursos ilimitados).
En realidad, Ana las hace secuencialmente.'

[EXPLICAR]

CPM es **matemáticamente correcto** bajo su modelo.

Pero su modelo (recursos ilimitados) NO refleja realidad en proyectos con cuellos de botella.

**Lección:** Usar herramienta apropiada para contexto.

---

**Pregunta 2: ¿Por qué el plan tradicional inflado (35d) es lento?**

[DAR 10 SEGUNDOS]

[LEER RESPUESTA en slide]

'Porque el padding está DISTRIBUIDO e INVISIBLE. Parkinson y el Síndrome del Estudiante lo consumirán, y el proyecto IGUALMENTE llegará a 35 días o más.'

[EXPLICAR - CONECTAR con Clase 1]

¿Recuerdan Clase 1?

**Ley de Parkinson:**
'El trabajo se expande para llenar el tiempo disponible'

**Síndrome del Estudiante:**
'Se posterga hasta cerca del deadline'

Si tarea A tiene estimación 10 días (5 real + 5 colchón):

- **Parkinson:** Ejecutor usa 10 días (desperdicia colchón explorando soluciones, sobre-ingeniera, perfeccionismo)
- **Estudiante:** Ejecutor espera hasta día 7, hace tarea en día 7-10 (desperdicia días 1-6)

Resultado: Colchón se GASTA, no se AHORRA.

**Lección:** Padding distribuido es ilusión de protección.

---

**Pregunta 3: ¿Por qué CCPM (27d) es mejor?**

[DAR 10 SEGUNDOS]

[LEER RESPUESTA en slide - bullets]

**• Cadena crítica correcta (considera recursos)**

No fantasía. Plan operativamente posible.

**• Tareas agresivas (sin padding oculto)**

Estimación 50%. No hay colchón que desperdiciar.

**• Buffer agregado y visible (protegido)**

9 días al final. PM controla. Monitorea con Fever Chart.

**• Resultado: Más rápido Y más robusto**

27 días vs 35 días. Misma protección, mejor gestión.

[ÉNFASIS]

**CCPM NO adivina mejor.**

**CCPM gestiona la incertidumbre mejor.**

[PAUSA]

[CONECTAR con curso completo]

**Clase 1:** Diagnosticó problema (estimaciones fallan, Parkinson, Estudiante)

**Clase 2:** Presentó herramientas (PERT, Ágil, Planning Poker - mejoran estimaciones)

**Clase 3:** Solución sistémica (CCPM - NO mejora estimación, mejora GESTIÓN)

[ÉNFASIS]

**El secreto:**

NO es estimar las tareas perfectamente.

ES gestionar el proyecto como SISTEMA con buffer agregado.

[TRANSICIÓN]

Última comparación: CPM vs Ágil vs CCPM."

---

**Preguntas para engagement:**

1. "¿Cuál lección les parece más valiosa?"
2. "¿Cómo explicarían CCPM a su jefe en 30 segundos?"
3. "¿Qué harán diferente el lunes?"

**Tips para el facilitador:**

✅ **Conectar con Clase 1-2:** Mostrar que curso es narrativa coherente, no temas sueltos.

✅ **Invitar reflexiones:** "¿Alguien tiene ejemplo propio de padding desperdiciado?"

⚠️ **Evitar:** Apurarse. Este es el cierre conceptual del caso más importante.

💡 **Elevator pitch CCPM:** "Estimaciones 50% + buffer agregado visible + prohibir multitarea = 20-30% más rápido con misma protección."

⏰ **Timing:** 8 min (2.5 min por pregunta)

---

### **Slide 25: Cuadro Comparativo Final - CPM vs Ágil vs CCPM** (10 min)

**Objetivos:**
- Integrar TODOS los métodos del curso
- Mostrar cuándo usar cada uno
- Dar criterios de selección

**Script sugerido:**

"Última pieza: Comparar TODOS los métodos.

[VER TABLA en slide - debe tener ~10 filas]

Voy a leer las características más importantes:

---

**Fila: Contexto ideal**

- **CPM:** Proyectos con fases claramente definidas, recursos abundantes, baja incertidumbre (ej: construcción, manufactura)
- **Ágil (Scrum):** Software con requisitos emergentes, iteraciones cortas, feedback frecuente
- **CCPM:** Proyectos con recursos limitados compartidos, múltiples proyectos paralelos, necesidad de velocidad

---

**Fila: Unidad de estimación**

- **CPM:** Horas/días (tiempo absoluto)
- **Ágil:** Story Points (complejidad relativa)
- **CCPM:** Días/horas pero estimación 50% + buffers

---

**Fila: Gestión de incertidumbre**

- **CPM:** Varianza distribuida en tareas (PERT 3 puntos)
- **Ágil:** Velocidad empírica + refinamiento progresivo
- **CCPM:** Buffers centralizados (proyecto, feeding, resource)

---

**Fila: Fortalezas**

- **CPM:**
  - ✅ Simple, bien conocido
  - ✅ Funciona en contextos predecibles
  - ✅ Identifica ruta crítica (dependencias)

- **Ágil:**
  - ✅ Alta adaptabilidad a cambios
  - ✅ Entrega incremental de valor
  - ✅ Feedback empírico continuo

- **CCPM:**
  - ✅ Considera recursos explícitamente
  - ✅ Protección robusta con buffers
  - ✅ 20-30% reducción timeline
  - ✅ Visibilidad (Fever Chart)

---

**Fila: Debilidades**

- **CPM:**
  - ❌ Ignora restricciones de recursos
  - ❌ Baja adaptación a cambios
  - ❌ Holgura vulnerable a Parkinson

- **Ágil:**
  - ❌ Difícil para proyectos con fases fijas
  - ❌ Requiere cliente disponible
  - ❌ Menos útil en entornos regulados

- **CCPM:**
  - ❌ Requiere cambio cultural significativo
  - ❌ Resistencia a estimaciones 50%
  - ❌ Necesita herramientas especializadas

---

**Fila: ¿Cuándo usar?**

[LEER con énfasis]

**Usa CPM si:**
- Proyecto con fases claramente definidas (diseño → construcción → testing)
- Recursos NO son restricción (puedes contratar)
- Baja incertidumbre técnica
- Industria regulada (farmacéutica, construcción)

**Usa Ágil (Scrum) si:**
- Alta incertidumbre de requisitos ('no sabemos qué quiere el cliente hasta probar')
- Posibilidad de entregas incrementales cada 2-4 semanas
- Equipo co-ubicado o bien coordinado
- Cliente disponible para feedback

**Usa CCPM si:**
- Recursos limitados compartidos entre tareas/proyectos
- Múltiples proyectos compitiendo por misma gente
- Necesidad de acortar timeline SIN agregar recursos
- Cuellos de botella críticos (arquitecto único, especialista raro)

---

[PAUSA]

**¿Se pueden combinar?**

**SÍ:**

**Ágil + CCPM:**
- Sprints con Scrum
- CCPM para gestionar cartera de múltiples equipos/proyectos
- Buffers para proteger releases mayores

**CPM + CCPM:**
- CPM para identificar dependencias
- CCPM para nivelar recursos y agregar buffers

[ÉNFASIS]

**NO hay "bala de plata".**

**Contexto determina método apropiado.**

[TRANSICIÓN]

Síntesis final del curso completo."

---

**Preguntas para engagement:**

1. "¿Qué método describe mejor su proyecto actual?"
2. "¿Podrían combinar Ágil + CCPM? ¿Cómo?"
3. "¿Cuál sería el primer paso para adoptar CCPM?"

**Tips para el facilitador:**

✅ **No dogmatizar:** "CCPM es poderoso pero NO reemplaza todo. Es herramienta para contexto específico."

✅ **Dar ejemplos:** "Netflix usa Ágil para features. SpaceX usa CCPM para cohetes (recursos limitados, timeline crítico)."

⚠️ **Evitar:** Decir "uno es mejor que otro". Depende de contexto.

💡 **Tip práctico:** "Empiecen con proyecto piloto pequeño. Aprendan. Expandan después."

⏰ **Timing:** 10 min (6 min tabla, 4 min cuándo usar)

---

### **Slide 26: Síntesis del Curso Completo** (5 min)

**Objetivos:**
- Cerrar narrativa completa Clase 1-2-3
- Recapitular mensajes clave
- Motivar aplicación

**Script sugerido:**

"Llegamos al final del curso.

Recapitulemos el viaje completo:

---

**CLASE 1: La Crisis de la Estimación**

**Diagnosticamos el problema:**

✅ Estimaciones fallan sistemáticamente (Standish CHAOS: 64% proyectos fallan)

✅ Cono de Incertidumbre: ±400% al inicio → ±10% al final

✅ Factores técnicos: complejidad, tecnología, tamaño

✅ Factores humanos: experiencia, comunicación, motivación

✅ Factores psicológicos:
- **Ley de Parkinson:** Trabajo se expande para llenar tiempo
- **Síndrome del Estudiante:** Se posterga hasta deadline

✅ Malvavisco Challenge: Probar suposiciones temprano evita colapso

**Mensaje:** El problema NO es técnico solo, es SISTÉMICO.

---

**CLASE 2: Métodos de Estimación**

**Presentamos herramientas:**

✅ **PERT:** 3 puntos (O-M-P), reconoce incertidumbre con varianza

✅ **CPM:** Identifica ruta crítica, optimiza duración (pero ignora recursos)

✅ **Ágil:**
- Story Points (complejidad relativa, NO horas)
- Planning Poker (exposición de suposiciones)
- Velocidad empírica (forecast basado en datos)
- Refinamiento Progresivo (estimar solo lo cercano)

**Mensaje:** Mejorar ESTIMACIÓN ayuda, pero no resuelve problema sistémico.

---

**CLASE 3: Cadena Crítica (CCPM)**

**Presentamos solución sistémica:**

✅ **Teoría de Restricciones (TOC):** Sistema es tan fuerte como eslabón más débil

✅ **Cadena Crítica ≠ Ruta Crítica:** Considera recursos, no solo dependencias

✅ **3 Principios:**
1. Eliminar padding individual (estimaciones 50%)
2. Agregar buffers estratégicos (visible, protegido)
3. Prohibir multitarea mala (focus-and-finish)

✅ **3 Tipos de Buffers:**
- Project Buffer (al final de CC)
- Feeding Buffer (entre cadenas)
- Resource Buffer (aviso, no tiempo)

✅ **Caso A-B-C-D:**
- CPM: 25 días (imposible)
- Tradicional: 35 días (realista pero inflado)
- CCPM: 27 días (23% más rápido, mismo nivel de protección)

**Mensaje:** NO estimar mejor, GESTIONAR la incertidumbre mejor.

---

[PAUSA]

**Mensaje FINAL del curso:**

[ÉNFASIS]

**La estimación perfecta NO existe.**

**La incertidumbre es INHERENTE a proyectos complejos.**

**El secreto NO es eliminar incertidumbre.**

**El secreto es GESTIONARLA sistémicamente:**

✅ Reconocer incertidumbre (Cono, PERT)
✅ Exponer suposiciones (Planning Poker, Malvavisco)
✅ Medir empíricamente (Velocidad)
✅ Proteger estratégicamente (CCPM Buffers)
✅ Monitorear proactivamente (Fever Chart)

[PAUSA]

**¿Qué hacer el lunes?**

**NO intentar implementar TODO.**

**Empezar con 1-2 cosas:**

**Opción 1:** Planning Poker en próximo sprint
- Capturar suposiciones
- Ver si extremos revelan algo

**Opción 2:** Identificar "Ana" en tu proyecto
- ¿Quién es recurso compartido?
- ¿Ese recurso determina timeline real?

**Opción 3:** Calcular velocidad empírica
- ¿Cuántos story points hicieron últimos 3 sprints?
- Forecast próximo sprint

**Opción 4:** Proyecto piloto CCPM
- Proyecto pequeño (3-6 meses)
- Aplicar 3 principios
- Medir resultados
- Expandir si funciona

[ÉNFASIS]

**Cambio incremental > Big Bang.**

[PAUSA]

**¿Preguntas finales?**

[DAR 2-3 MINUTOS para preguntas]

**Muchas gracias por su participación.**

**Éxito en sus proyectos.**"

---

**Tips para el facilitador:**

✅ **Cerrar con energía positiva:** "Tienen herramientas poderosas ahora. Úsenlas."

✅ **Acción concreta:** "Lunes: identifiquen SU 'Ana' (recurso crítico)."

⚠️ **Evitar:** Terminar abruptamente. Dejar espacio para preguntas finales.

💡 **Follow-up:** Enviar por email:
- Slides del curso
- Links a libros (The Goal, Critical Chain)
- Plantilla de Fever Chart
- Contacto para consultas

⏰ **Timing:** 5 min (3 min síntesis, 2 min cierre)

---

## 🎯 **FIN DE GUÍA PROFESOR CLASE 3 - PARTE 2**

---

## 📌 Resumen de PARTE 2

**Tiempo total cubierto:** 90 minutos (post-break de Clase 3)

**Slides cubiertas:** 15-26 (12 slides)

**Contenido creado:**

1. ✅ Introducción Caso A-B-C-D - 3 min
2. ✅ Setup del proyecto - 5 min
3. ✅ Paso 1: CPM (25 días) - 8 min
4. ✅ Paso 2: Revelación (Ana hace B y D) - 7 min
5. ✅ Paso 3: Cadena Crítica real (35 días) - 10 min
6. ✅ Paso 4: Eliminar padding (18 días agresivos) - 10 min
7. ✅ Paso 5: Agregar buffer (9 días → 27 días total) - 8 min
8. ✅ Resultado: Comparativa 3 métodos - 8 min
9. ✅ Debriefing con 3 preguntas - 8 min
10. ✅ Tabla comparativa CPM vs Ágil vs CCPM - 10 min
11. ✅ Síntesis curso completo - 5 min

**Total:** 90 minutos

---

## 🎓 Logros de la Guía Completa Clase 3

**Parte 1 + Parte 2 = 180 minutos (3 horas)**

**33 slides cubiertas con:**

- Scripts palabra por palabra
- Timing minuto a minuto
- Preguntas de engagement
- Analogías y ejemplos
- Anticipación de objeciones
- Conexiones con Clase 1-2
- Tips pedagógicos
- Momento "aha!" diseñado

---

**Archivos completos:**
- `GUIA_PROFESOR_CLASE3.md` (Parte 1 - pre-break)
- `GUIA_PROFESOR_CLASE3_PARTE2.md` (Parte 2 - post-break)

---

**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 2.0 - Formato Remoto
**Fecha:** Enero 2025
