# Guía del Profesor - Clase 2: Métodos de Estimación

**Duración:** 3 horas (180 minutos)
**Formato:** Remoto / Teórico con demostraciones
**Objetivos de Aprendizaje:** Dominar PERT, CPM, estimación ágil (Story Points, Planning Poker), y velocidad empírica

---

## 📋 Índice Completo de la Clase

| Slide | Tema | Duración | Tipo |
|-------|------|----------|------|
| 1 | Portada | 2 min | Intro |
| 2 | Agenda | 3 min | Overview |
| 3-5 | PERT (3 puntos) | 20 min | Teoría |
| 6 | CPM y Ruta Crítica | 15 min | Teoría |
| 7 | Ejercicio PERT | 10 min | Práctica |
| 8-10 | Estimación Ágil (Intro) | 20 min | Teoría |
| 11 | T-Shirt Sizing | 10 min | Técnica |
| 12 | Break | 15 min | Descanso |
| 13-17 | Planning Poker | 60 min | Demo Detallada |
| 18 | Velocidad y Forecasting | 15 min | Teoría |
| 19-20 | Refinamiento Progresivo | 15 min | Mejores Prácticas |
| 21-22 | Cuadro Comparativo | 10 min | Síntesis |
| 23 | Resumen | 3 min | Cierre |
| 24 | Próxima Clase | 2 min | Transición |

**Total:** 180 minutos (3 horas)

---

## 🎯 Objetivos de Aprendizaje Específicos

Al finalizar esta clase, los estudiantes podrán:

1. ✅ Calcular estimaciones PERT con 3 puntos (O, M, P)
2. ✅ Identificar la Ruta Crítica en un proyecto usando CPM
3. ✅ Explicar por qué Story Points > estimación en horas
4. ✅ Facilitar una sesión de Planning Poker
5. ✅ Calcular Velocidad de equipo y hacer forecasting
6. ✅ Elegir el método apropiado según contexto (Cascada vs Ágil)
7. ✅ Aplicar refinamiento progresivo conforme el proyecto avanza

---

## 🧠 Pensamiento Profundo: Estructura Pedagógica de Clase 2

### Análisis de la Progresión Conceptual:

**Clase 1** estableció el PROBLEMA:
- Estimaciones fallan 70% del tiempo
- Cono de Incertidumbre muestra que incertidumbre es REAL
- Padding distribuido falla por Parkinson/Estudiante
- Conclusión: Necesitamos NUEVOS métodos

**Clase 2** presenta las SOLUCIONES:

1. **PERT (1958):** Método clásico que RECONOCE incertidumbre
   - Usa 3 puntos (optimista, más probable, pesimista)
   - Calcula esperanza y varianza estadísticamente
   - Mejor que estimación puntual, pero aún asume cascada

2. **CPM (1957):** Identifica dependencias y camino crítico
   - Encuentra la secuencia MÁS LARGA de tareas dependientes
   - Permite priorizar esfuerzo en lo que realmente importa
   - Limitación: Ignora recursos (resuelto en Clase 3 con CCPM)

3. **Agile/Story Points (2000s):** Abandona tiempo absoluto
   - Estimación RELATIVA vs absoluta
   - Reconoce que humanos somos malos con tiempo pero buenos comparando
   - Calibración empírica con velocidad

4. **Planning Poker:** Consenso colaborativo
   - Expone suposiciones ocultas
   - Evita anclaje (votación simultánea)
   - Discusión de extremos identifica riesgos

### Estrategia de Enseñanza:

**Primeros 90 min (Pre-Break):**
- PERT/CPM: Métodos "clásicos" que reconocen incertidumbre
- Objetivo: Mostrar que hay MEJOR que "adivina un número"
- Estos son mejora sobre estimación puntual, pero limitados

**Últimos 90 min (Post-Break):**
- Agile/Planning Poker: Métodos que ABRAZAN incertidumbre
- Objetivo: Mostrar cambio de paradigma (relativo > absoluto)
- Estos son el estado del arte para proyectos con alta incertidumbre

### Conexión con Clase 1:

Cada método de Clase 2 RESUELVE un problema de Clase 1:

| Problema (Clase 1) | Solución (Clase 2) |
|--------------------|--------------------|
| Estimación puntual ignora incertidumbre | PERT usa 3 puntos (rango) |
| No sabemos qué tareas son críticas | CPM identifica Ruta Crítica |
| Estimación en tiempo es imprecisa | Story Points (relativo) |
| Suposiciones ocultas causan fallas | Planning Poker expone suposiciones |
| Padding distribuido falla | Velocidad calibra empíricamente |

---

## 📖 Desglose Slide por Slide

### **Slide 1: Portada** (2 min)

**Contenido:**
- Título: "Clase 2: Métodos de Estimación"
- Subtítulo: "De PERT a Planning Poker"
- Duración: 3 horas

**Script sugerido:**
```
"Bienvenidos a Clase 2. En Clase 1 diagnosticamos el problema:
estimaciones tradicionales fallan porque ignoran incertidumbre
y caen víctimas de Parkinson/Estudiante.

Hoy veremos las SOLUCIONES: métodos de estimación que reconocen
y gestionan la incertidumbre de forma explícita.

Cubriremos 4 enfoques:
1. PERT (clásico, 1958): 3 puntos optimista/realista/pesimista
2. CPM (clásico, 1957): Ruta Crítica
3. Agile (moderno, 2000s): Story Points y estimación relativa
4. Planning Poker (moderno, 2002): Consenso colaborativo

Al final de hoy, tendrán herramientas CONCRETAS para estimar
mejor en sus proyectos. Empecemos."
```

**Tips:**
- Reconecta con Clase 1 brevemente (30 segundos)
- Establece expectativa: hoy es "constructivo" vs "diagnóstico"
- Genera energía: "Herramientas que usarán MAÑANA"

---

### **Slide 2: Agenda** (3 min)

**Contenido:**
1. Métodos Clásicos: PERT y CPM (45 min)
2. Estimación Ágil (45 min)
3. ☕ Break (15 min)
4. Planning Poker: Demostración y Análisis (60 min)
5. Velocidad y Mejores Prácticas (30 min)
6. Síntesis (15 min)

**Script sugerido:**
```
"La agenda de hoy tiene 2 partes claramente diferenciadas:

PARTE 1 (pre-break): Métodos CLÁSICOS
- PERT: Cómo estimar con 3 puntos reconociendo incertidumbre
- CPM: Cómo identificar la Ruta Crítica en proyectos con dependencias

Estos métodos son de los años 50. Fueron desarrollados para proyectos
de ingeniería masivos (NASA, construcción). Son MEJORES que adivinar
un número, pero tienen limitaciones que discutiremos.

PARTE 2 (post-break): Métodos ÁGILES
- Story Points: Por qué estimación RELATIVA > absoluta
- Planning Poker: Cómo exponer suposiciones con consenso colaborativo
- Velocidad: Cómo calibrar empíricamente en lugar de adivinar

Estos métodos son de los 2000s. Fueron desarrollados para software
con alta incertidumbre. Representan un cambio de PARADIGMA.

Después del break profundizaremos en Planning Poker con un caso
práctico completo."
```

**Pregunta de warm-up:**
> "¿Cuántos han usado PERT o CPM? ¿Cuántos han usado Story Points?"

(Esto te da sentido de la audiencia - ajusta profundidad según respuesta)

**Tips:**
- Anticipa que habrá CONTRASTE entre métodos (clásico vs ágil)
- Menciona que verán CUÁNDO usar cada uno (no hay "mejor" universal)
- Genera curiosidad para Planning Poker (el bloque más largo)

---

### **Slide 3: Introducción a PERT** (8 min)

**Contenido:**
- **PERT:** Program Evaluation and Review Technique
- Desarrollado en 1958 por US Navy para proyecto Polaris (misiles)
- Problema que resolvía: Incertidumbre en proyectos complejos nunca antes hechos
- Innovación: Usar 3 puntos en lugar de 1

**Puntos clave:**
1. PERT reconoce que NO podemos estimar con precisión
2. En lugar de "adivina un número", usa RANGO
3. Calcula esperanza y desviación estándar estadísticamente

**Script sugerido:**
```
"Empecemos con PERT: Program Evaluation and Review Technique.

Contexto histórico: 1958, plena Guerra Fría. US Navy necesitaba
desarrollar misiles balísticos Polaris. Proyecto MASIVO: 250
contratistas, 9,000 sub-contratistas, tecnologías nunca intentadas.

El problema: ¿Cómo estimar algo que nunca se ha hecho?

Los métodos tradicionales ('Tarea X toma Y semanas') eran inútiles.
La incertidumbre era ENORME - esto es el Cono de Incertidumbre que
vimos en Clase 1, pero en 1958 no tenían ese concepto formal.

La innovación de PERT fue simple pero poderosa:

En lugar de pedir 'Estima cuánto tomará esta tarea', PERT pregunta:
1. ¿Cuál es el escenario OPTIMISTA? (todo sale perfecto)
2. ¿Cuál es el escenario MÁS PROBABLE? (expectativa realista)
3. ¿Cuál es el escenario PESIMISTA? (Murphy ataca)

Luego usa estos 3 puntos para calcular una estimación ponderada
con distribución estadística.

El resultado: Proyecto Polaris se completó 2 años ANTES de lo
originalmente estimado. PERT se acreditó como factor crítico."
```

**Conexión con Clase 1:**
```
"Recuerdan el Cono de Incertidumbre de Clase 1?

En fase de Concepto: ±400% de variabilidad.

PERT es una forma de CAPTURAR esa variabilidad explícitamente.
En lugar de dar un número puntual (que será incorrecto), das
un RANGO que refleja la incertidumbre real.

Es honestidad matemática."
```

**Analogía útil:**
```
"Piensen en preguntarle a alguien: '¿Cuánto tarda llegar del
aeropuerto a tu casa?'

Respuesta puntual: '30 minutos.'
Respuesta PERT:
- Optimista (3am, cero tráfico): 20 minutos
- Más probable (tráfico normal): 30 minutos
- Pesimista (hora pico, accidente): 60 minutos

¿Cuál es más útil? La respuesta PERT, porque puedes PLANIFICAR.
Si tienes reunión importante, no planeas con 30 min - planeas con
45-50 min para absorber variabilidad."
```

**Pregunta para el grupo:**
> "¿Por qué creen que estimación puntual es tan común si PERT
> existe desde 1958?"

**Respuestas esperadas:**
- "Es más simple"
- "Los stakeholders quieren UN número"
- "No sabemos de PERT"

**Contra-argumento:**
```
"Exacto. Simple ≠ correcto. Stakeholders QUIEREN un número, pero
eso no significa que debamos DAR un número si la incertidumbre
no lo permite. Es como si un doctor dijera 'Vivirás exactamente
78.4 años' porque el paciente quiere certeza. Es absurdo.

Hoy aprenderán CÓMO usar PERT para dar respuestas honestas."
```

**Tips:**
- El contexto histórico (Polaris, Guerra Fría) hace esto memorable
- Enfatiza que PERT NO es "nuevo" - tiene 65+ años
- Conecta explícitamente con Cono de Incertidumbre (Clase 1)
- Genera respeto por el método: Navy lo usó para misiles nucleares

---

### **Slide 4: Fórmula PERT** (7 min)

**Contenido:**
- **3 Estimaciones:**
  - **O (Optimista):** Todo sale perfecto (probabilidad ~1%)
  - **M (Más probable):** Expectativa realista (moda de distribución)
  - **P (Pesimista):** Todo sale mal (probabilidad ~1%)

- **Fórmulas:**
  - **Esperanza (μ):** `μ = (O + 4M + P) / 6`
  - **Desviación estándar (σ):** `σ = (P - O) / 6`
  - **Varianza (σ²):** `σ² = [(P - O) / 6]²`

**Puntos clave:**
1. **Ponderación 1-4-1:** El valor más probable pesa 4× más
2. **Distribución Beta:** PERT asume distribución Beta, no Normal
3. **6 divisor:** Viene de que O y P son ~3 desviaciones estándar

**Script sugerido:**
```
"Ahora la matemática de PERT. No se asusten - es simple.

Primero definimos los 3 puntos:

OPTIMISTA (O): Escenario donde TODO sale perfecto.
Cero interrupciones, cero bugs, performance perfecto.
Probabilidad: ~1%. Es posible pero MUY improbable.

MÁS PROBABLE (M): Tu expectativa realista.
'Si hago esta tarea 10 veces, en 5-6 de ellas toma este tiempo.'
Es la MODA - el valor más frecuente, no el promedio.

PESIMISTA (P): Escenario donde Murphy ataca.
Múltiples interrupciones, bugs críticos, bloqueos externos.
Probabilidad: ~1%. Tan raro como optimista, pero en dirección opuesta.

Con estos 3 puntos, calculamos 2 métricas:

ESPERANZA (μ): El valor 'promedio ponderado'
μ = (O + 4M + P) / 6

¿Por qué 4M? Porque el valor más probable es MÁS informativo
que los extremos. Pesa 4× más en el cálculo.

DESVIACIÓN ESTÁNDAR (σ): La 'incertidumbre'
σ = (P - O) / 6

Esta fórmula viene de la teoría de distribución Beta. El rango
entre O y P representa aproximadamente 6 desviaciones estándar
(±3σ en cada dirección).

σ alta = Alta incertidumbre
σ baja = Baja incertidumbre"
```

**Ejemplo numérico simple:**
```
"Ejemplo: Implementar módulo de autenticación.

Optimista (O): 3 días
'Si todo está listo: librerías funcionan, documentación clara,
cero interrupciones.'

Más probable (M): 7 días
'Expectativa realista con interrupciones normales y 1-2 bugs
menores.'

Pesimista (P): 15 días
'Si la librería tiene bug crítico, necesitamos investigar
alternativas, y hay bloqueo externo.'

Calculamos:

Esperanza: μ = (3 + 4×7 + 15) / 6 = (3 + 28 + 15) / 6 = 46/6 = 7.67 días

Desviación: σ = (15 - 3) / 6 = 12/6 = 2 días

INTERPRETACIÓN:
La estimación es 7.67 días (redondeamos a 8 días), con incertidumbre
de ±2 días.

Rango de confianza 68%: 8 ± 2 = 6-10 días
Rango de confianza 95%: 8 ± 4 = 4-12 días

Eso es MUCHO más útil que decir '8 días' sin contexto."
```

**Por qué la ponderación 1-4-1:**
```
"¿Por qué M pesa 4× más?

Porque los extremos (O y P) son eventos RAROS. Tienen probabilidad
~1% cada uno. Son útiles para definir el RANGO, pero no deberían
dominar la estimación.

M es lo que ESPERAMOS que ocurra 50-60% del tiempo. Es el valor
con más información.

Si usáramos promedio simple (O+M+P)/3, estaríamos dando igual
peso a eventos raros (O, P) que a eventos probables (M). Eso
sesgaría el resultado.

La ponderación 1-4-1 balancea correctamente."
```

**Conexión con distribución Beta:**
```
"PERT asume distribución Beta, NO Normal (Gaussiana).

¿Diferencia?

Normal: Simétrica. Optimista y pesimista equidistantes de media.
Beta: Asimétrica. Puede tener cola pesada hacia un lado.

En proyectos, las cosas tienden a salir MAL más que BIEN.
Es más común que algo tome 3× más tiempo estimado, que 3× menos.

Distribución Beta captura esa asimetría.

(No necesitan dominar la matemática - solo entender que PERT
es más sofisticado que promedio simple)"
```

**Tips:**
- Escribe la fórmula GRANDE en pizarra/pantalla: `(O + 4M + P) / 6`
- Haz el ejemplo numérico PASO A PASO
- Enfatiza interpretación (μ ± σ) más que matemática
- Menciona que pueden usar Excel/calculadora - no es cálculo mental

---

### **Slide 5: Agregación PERT** (5 min)

**Contenido:**
- **Cómo sumar múltiples tareas PERT:**
  - **Esperanza total:** Suma de esperanzas individuales: `μ_total = Σ μ_i`
  - **Varianza total:** Suma de varianzas individuales: `σ²_total = Σ σ²_i`
  - **Desviación total:** Raíz de varianza: `σ_total = √(σ²_total)`

- **Propiedades importantes:**
  - Esperanzas se suman linealmente (fácil)
  - Desviaciones NO se suman - varianzas sí (importante)
  - Incertidumbre crece con √n, no linealmente

**Script sugerido:**
```
"Ok, sabemos estimar UNA tarea con PERT. ¿Cómo estimamos un
proyecto con 10, 50, 100 tareas?

Respuesta: Agregación.

ESPERANZAS se suman:
Si Tarea A = 8 días y Tarea B = 5 días, el total es 13 días.
Fácil. Lineal. Intuitivo.

DESVIACIONES NO se suman así:
Si Tarea A tiene σ=2 días y Tarea B tiene σ=3 días,
la desviación total NO es 5 días. ¿Por qué?

Porque las incertidumbres NO se acumulan linealmente - se
cancelan parcialmente.

Matemáticamente: VARIANZAS se suman, luego sacas raíz.

σ²_A = 2² = 4
σ²_B = 3² = 9
σ²_total = 4 + 9 = 13
σ_total = √13 ≈ 3.6 días

La incertidumbre total (3.6) es MENOR que la suma simple (5).
Esto es bueno - proyectos son menos inciertos de lo que parecen
si sumas las partes independientes."
```

**Ejemplo con 3 tareas:**
```
"Ejemplo: Proyecto con 3 tareas secuenciales.

Tarea A: μ=5 días, σ=1 día
Tarea B: μ=10 días, σ=2 días
Tarea C: μ=7 días, σ=1.5 días

ESPERANZA TOTAL:
μ_total = 5 + 10 + 7 = 22 días

DESVIACIÓN TOTAL:
σ²_A = 1² = 1
σ²_B = 2² = 4
σ²_C = 1.5² = 2.25
σ²_total = 1 + 4 + 2.25 = 7.25
σ_total = √7.25 ≈ 2.7 días

RESULTADO:
Proyecto: 22 ± 2.7 días
Rango 68%: 19-25 días
Rango 95%: 17-27 días

Eso es lo que reportas al stakeholder: '22 días con rango de
confianza 95% de 17-27 días.'"
```

**Por qué varianzas se suman:**
```
"Estadísticamente: varianza mide 'dispersión cuadrada.'

Cuando sumas variables aleatorias independientes, sus dispersiones
se combinan. Pero como dispersión es cuadrática, usas varianza
(σ²), no desviación (σ).

Después de sumar varianzas, tomas raíz para regresar a unidades
originales (días).

La consecuencia práctica: Incertidumbre crece con √n.

10 tareas con σ=2 cada una → σ_total = 2×√10 ≈ 6.3
No es 20 (2×10). Es 6.3. La incertidumbre crece SUBLINEALMENTE.

Eso es bueno - significa que proyectos grandes NO son proporcionalmente
más inciertos."
```

**Limitación importante:**
```
"⚠️ IMPORTANTE: Esto asume tareas INDEPENDIENTES.

Si Tarea B depende del resultado de Tarea A, y Tarea A sale mal,
entonces Tarea B TAMBIÉN saldrá mal. Esas incertidumbres están
CORRELACIONADAS, no independientes.

PERT básico NO captura correlaciones. Es una limitación del método.

Solución avanzada: Simulación Monte Carlo (fuera del alcance de
este curso, pero sepan que existe)."
```

**Tips:**
- La matemática aquí es la más densa del curso - ve LENTO
- Haz el ejemplo numérico COMPLETO en pantalla
- Enfatiza la intuición: √n crecimiento sublineal
- Menciona la limitación (independencia) honestamente

---

### **Slide 6: CPM y Ruta Crítica** (15 min)

**Contenido:**
- **CPM:** Critical Path Method
- Desarrollado en 1957 por DuPont para proyectos de mantenimiento
- **Ruta Crítica:** La secuencia MÁS LARGA de tareas dependientes
- Propiedad: Retraso en ruta crítica = retraso en proyecto completo
- Tareas NO críticas tienen "holgura" (slack)

**Diagrama ejemplo:**
```
        [B: 5d]
       /        \
[A: 3d]          [D: 2d] → [Fin]
       \        /
        [C: 8d]
```

**Rutas posibles:**
- A → B → D = 3 + 5 + 2 = 10 días
- A → C → D = 3 + 8 + 2 = 13 días (CRÍTICA)

**Puntos clave:**
1. Ruta crítica determina duración MÍNIMA del proyecto
2. Tareas en ruta crítica tienen holgura = 0
3. Tareas fuera de ruta crítica tienen holgura > 0
4. Gestionar proyecto = Gestionar ruta crítica

**Script sugerido:**
```
"Ahora CPM: Critical Path Method.

Contexto: 1957, DuPont Chemical necesitaba optimizar mantenimiento
de plantas industriales. Problema: Proyectos complejos con 1000+
tareas interdependientes. ¿Cómo saber qué tareas son CRÍTICAS?

La innovación de CPM:

En un proyecto con dependencias, NO todas las tareas son igual
de importantes. Algunas están en el 'camino crítico' - si se
retrasan, todo el proyecto se retrasa. Otras tienen 'holgura' -
pueden retrasarse SIN afectar la fecha final.

Identificar la RUTA CRÍTICA permite:
1. Priorizar esfuerzo en lo que REALMENTE importa
2. Saber dónde NO perder tiempo optimizando
3. Gestionar riesgos en el lugar correcto

Definición formal:
RUTA CRÍTICA = La secuencia MÁS LARGA de tareas dependientes
desde inicio hasta fin del proyecto."
```

**Ejemplo con diagrama:**
```
"Veamos un ejemplo simple. Proyecto con 4 tareas: A, B, C, D.

Dependencias:
- A es inicio (no depende de nada)
- B depende de A
- C depende de A
- D depende de B Y C (ambas deben terminar)

Duraciones:
- A: 3 días
- B: 5 días
- C: 8 días
- D: 2 días

Diagrama:
        [B: 5d]
       /        \
[A: 3d]          [D: 2d] → [Fin]
       \        /
        [C: 8d]

¿Cuál es la ruta crítica?

Calculamos todas las rutas posibles:

Ruta 1: A → B → D = 3 + 5 + 2 = 10 días
Ruta 2: A → C → D = 3 + 8 + 2 = 13 días

La ruta MÁS LARGA es A → C → D = 13 días.

ESA es la ruta crítica. El proyecto tomará MÍNIMO 13 días,
independientemente de cuán rápido hagamos B.

HOLGURA:
Tarea B tiene holgura de 3 días. Puede retrasarse 3 días (de 5
a 8) SIN afectar el proyecto. ¿Por qué? Porque C toma 8 días,
y D espera a que AMBAS (B y C) terminen. C es el cuello de botella."
```

**Cálculo de holgura:**
```
"HOLGURA (Slack) = Cuánto puede retrasarse una tarea sin afectar
la fecha final.

Cálculo:
1. Calcular 'Earliest Start' (ES): Lo más temprano que puede empezar
2. Calcular 'Latest Start' (LS): Lo más tarde que puede empezar
   sin retrasar el proyecto
3. Holgura = LS - ES

Para nuestro ejemplo:

Tarea B:
- ES: Día 3 (cuando A termina)
- LS: Día 6 (para terminar en día 11, cuando C termina y D puede empezar)
- Holgura: 6 - 3 = 3 días

Tarea C:
- ES: Día 3
- LS: Día 3 (si empieza más tarde, retrasa a D y el proyecto)
- Holgura: 3 - 3 = 0 días → Está en ruta crítica

Tareas con holgura 0 = Ruta crítica."
```

**Aplicación práctica:**
```
"¿Para qué sirve conocer la ruta crítica?

PRIORIZACIÓN:
Si tienes recursos limitados (tiempo del PM, mejores devs),
ÁSIGNALOS a tareas de ruta crítica. Optimizar B es inútil si
C es el cuello de botella.

GESTIÓN DE RIESGOS:
Identifica riesgos en ruta crítica PRIMERO. Un riesgo en B
(3 días de holgura) es menos urgente que un riesgo en C (0 holgura).

COMUNICACIÓN:
Si stakeholder pide acelerar el proyecto, SOLO puedes hacerlo
acortando ruta crítica. Decirle 'haré B en 3 días en lugar de 5'
no ayuda - el proyecto sigue tomando 13 días por C."
```

**Limitación crítica de CPM:**
```
"⚠️ LIMITACIÓN DE CPM que resolveremos en Clase 3:

CPM asume RECURSOS ILIMITADOS.

En nuestro ejemplo, asumimos que B y C pueden ejecutarse EN
PARALELO. Pero ¿qué si la misma persona (Ana) hace AMBAS?

Entonces NO son paralelas - son SECUENCIALES.
Nueva duración: A (3d) → C (8d) → B (5d) → D (2d) = 18 días.

La 'ruta crítica' de CPM (13 días) es INCORRECTA porque ignoró
recursos.

Solución: CCPM (Critical Chain Project Management) - Clase 3.
CCPM considera TANTO dependencias COMO recursos."
```

**Pregunta para el grupo:**
> "En sus proyectos actuales, ¿saben cuál es la ruta crítica?
> ¿O gestionan todas las tareas con igual prioridad?"

(Probablemente admitirán que gestionan todo igual - esa es la
oportunidad de mejora)

**Tips:**
- Dibuja el diagrama CLARAMENTE (pizarra virtual si es posible)
- Usa colores: Ruta crítica en ROJO, no críticas en VERDE
- Haz el cálculo de holgura PASO A PASO con números
- Anticipa Clase 3: CPM es bueno pero limitado (CCPM resuelve)

---

### **Slide 7: Ejercicio PERT Rápido** (10 min)

**Contenido:**
- Ejercicio práctico: Estimar 3 tareas con PERT
- **Tarea propuesta:** "Migrar base de datos de MySQL a PostgreSQL"

**Setup del ejercicio:**
```
"Vamos a hacer un ejercicio rápido. Imaginen que deben estimar
esta tarea:

'Migrar base de datos de producción de MySQL a PostgreSQL.'

La base tiene 50 tablas, 2M registros, 10 aplicaciones conectadas.

Van a definir 3 puntos: Optimista, Más probable, Pesimista.

Tienen 3 minutos para pensarlo. Luego comparamos respuestas."
```

**Guía de pensamiento:**
```
"Piensen:

OPTIMISTA (O):
¿Qué debe salir perfecto?
- Scripts de migración funcionan a la primera
- Cero downtime
- Todas las aplicaciones se adaptan sin problemas
- No hay bugs en producción

MÁS PROBABLE (M):
¿Qué esperas realistamente?
- 1-2 iteraciones de scripts
- Downtime planificado aceptable
- 2-3 aplicaciones necesitan ajustes menores
- 1-2 bugs menores post-migración

PESIMISTA (P):
¿Qué puede salir mal?
- Scripts fallan, necesitas reescribir lógica
- Downtime extendido, clientes afectados
- Múltiples aplicaciones rompen
- Rollback necesario, segundo intento
- Bugs críticos en producción"
```

**Después de 3 minutos:**
```
"Ok, ¿qué valores estimaron? Escriban en el chat:
O = ? días
M = ? días
P = ? días

(Lee 3-4 respuestas del grupo)

Veamos algunas respuestas:
- Juan: O=3, M=7, P=15
- María: O=5, M=10, P=25
- Pedro: O=2, M=5, P=10

¿Por qué difieren?

Porque cada uno tiene DIFERENTES SUPOSICIONES:
- Juan asume equipo experimentado en migraciones
- María asume primera vez haciendo esto
- Pedro asume base de datos pequeña/simple

Eso es EXACTAMENTE el valor de PERT: EXPONE que las estimaciones
dependen de suposiciones. No hay 'respuesta correcta' sin
CONTEXTO."
```

**Cálculo con valores ejemplo:**
```
"Tomemos el valor medio: O=3, M=7, P=15

μ = (3 + 4×7 + 15) / 6 = (3 + 28 + 15) / 6 = 46/6 ≈ 7.7 días
σ = (15 - 3) / 6 = 12/6 = 2 días

RESULTADO: 8 días ± 2 días

Rango 68%: 6-10 días
Rango 95%: 4-12 días

Reportas al PM: 'La migración tomará aproximadamente 8 días, con
rango de confianza del 95% de 4-12 días. El optimista es 3 días
si todo sale perfecto (improbable). El pesimista es 15 días si
necesitamos rollback y segundo intento.'

ESO es una respuesta profesional que refleja incertidumbre."
```

**Lección del ejercicio:**
```
"Lecciones:

1. DIFERENCIAS en estimaciones exponen DIFERENCIAS en suposiciones.
   Si 3 personas dan números muy diferentes, NO es que 2 estén
   'equivocadas' - es que asumen contextos diferentes.

2. PERT FUERZA a hacer explícitas esas suposiciones. No puedes
   dar O/M/P sin pensar en escenarios concretos.

3. El RANGO (σ) es tan importante como el PUNTO (μ). Un proyecto
   con μ=10, σ=1 es MUY diferente de μ=10, σ=5. Ambos 'estiman'
   10 días, pero el segundo es mucho más incierto.

Esta es la base para Planning Poker (post-break): Discutir
SUPOSICIONES, no solo números."
```

**Tips:**
- Dales tiempo REAL para pensar (3 min)
- No juzgues respuestas como "correctas" o "incorrectas"
- Celebra la DIVERSIDAD de respuestas - prueba que contexto importa
- Conecta explícitamente con Planning Poker que verán después

---

(Continuaré con la segunda mitad de Clase 2 en el siguiente archivo...)

## 📌 Checkpoint: Primera Mitad de Clase 2

**Tiempo usado:** ~50 minutos
**Slides cubiertas:** 1-7

**Conceptos clave establecidos:**
✅ PERT reconoce incertidumbre con 3 puntos
✅ Fórmula (O + 4M + P) / 6 y desviación (P - O) / 6
✅ Agregación: esperanzas suman, varianzas suman (no desviaciones)
✅ CPM identifica ruta crítica (secuencia más larga)
✅ Holgura = flexibilidad en tareas no críticas
✅ Limitación CPM: ignora recursos (resolver en Clase 3)

**Próximo bloque:** Estimación Ágil (Story Points, T-Shirt Sizing) - 35 min hasta break

---

**Continúa en:** `GUIA_PROFESOR_CLASE2_PARTE2.md`
