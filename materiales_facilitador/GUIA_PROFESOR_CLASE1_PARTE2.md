# Guía del Profesor - Clase 1 PARTE 2: Factores Psicológicos

**Duración:** 85 minutos (post-break)
**Contenido:** Ley de Parkinson, Síndrome del Estudiante, Estudios Empíricos, Cierre

---

## 📋 Índice de la Segunda Mitad

| Slide | Tema | Duración | Tipo |
|-------|------|----------|------|
| 12 | Ley de Parkinson | 8 min | Teoría |
| 13 | Por qué Parkinson ocurre | 7 min | Análisis |
| 14 | Síndrome del Estudiante | 8 min | Teoría |
| 15 | El Ciclo Vicioso | 12 min | Análisis |
| 16 | Caso Microsoft (Parkinson) | 12 min | Estudio |
| 17 | Estudio MIT (Estudiante) | 13 min | Estudio |
| 18 | Conclusión Empírica | 10 min | Síntesis |
| 19 | La Pregunta Gancho | 5 min | Transición |
| 20 | Resumen Clase 1 | 5 min | Cierre |
| 21 | Cierre y Próxima Clase | 5 min | Despedida |

**Total:** 85 minutos

---

## 📖 Desglose Slide por Slide (Continuación)

### **Slide 12: Ley de Parkinson** (8 min)

**Contenido:**
- **Ley de Parkinson (1955):** "El trabajo se EXPANDE para llenar el tiempo disponible para su completación"
- Cyril Northcote Parkinson, historiador británico
- Publicado en "The Economist"

**Puntos clave:**
1. **No es sobre pereza** - Es naturaleza humana
2. **Ocurre incluso con gente motivada**
3. **El tiempo asignado DICTA el tiempo consumido**

**Script sugerido:**
```
"Bienvenidos de vuelta. Ahora hablaremos de algo incómodo:
factores PSICOLÓGICOS que sabotean nuestras estimaciones.

El primero es la Ley de Parkinson, enunciada en 1955 por
Cyril Northcote Parkinson, un historiador británico.

La ley dice: 'El trabajo se EXPANDE para llenar el tiempo
disponible para su completación.'

¿Qué significa esto?

Si le das a alguien 2 semanas para una tarea que objetivamente
toma 3 días, esa persona USARÁ 2 semanas. El trabajo se expandirá
milagrosamente para consumir las 2 semanas.

¿Cómo? Perfeccionismo innecesario. Revisar 10 veces. Agregar
'mejoras' no solicitadas. Simplemente... trabajar más lento.

Y lo más frustrante: NO es consciente. La persona genuinamente
SIENTE que la tarea tomó 2 semanas."
```

**Ejemplo cotidiano:**
```
"Ejemplo fuera del trabajo: tienes que escribir un email importante.

Si tienes 5 minutos antes de una reunión: escribes el email en
4 minutos. Directo, conciso, enviar.

Si tienes 2 horas libres: escribes el email en... 1 hora 45 minutos.
Escribes, borras, reescribes, cambias palabras, ajustas tono,
lo lees 5 veces... mismo email.

¿El email de 5 minutos es peor? No. Frecuentemente es MEJOR porque
es más directo. El de 2 horas tiene 'sobre-ingeniería.'"
```

**Conexión con estimaciones:**
```
"Ahora piensen en estimaciones de software.

Si estimas 'Implementar login: 10 días' (con padding generoso),
el desarrollador USARÁ 10 días. Tal vez la implementación core
tome 3 días, pero:
- Día 4-5: Refactoring 'porque podría ser más limpio'
- Día 6-7: Agregar validaciones 'por si acaso'
- Día 8-9: Optimizar performance (sin medir si es necesario)
- Día 10: 'Terminar detalles'

Si hubieras estimado 5 días, habría terminado en 5 días con la
MISMA funcionalidad core. El padding NO mejoró el producto,
solo lo hizo más LENTO."
```

**Pregunta provocadora:**
> "Levanten la mano (mentalmente): ¿Alguna vez terminaron una tarea
> el día ANTES del deadline? ¿O siempre 'milagrosamente' terminas
> justo a tiempo?"

(La mayoría terminan justo a tiempo - eso ES Parkinson)

**Tips:**
- Presenta Parkinson con EMPATÍA, no acusación
- Todos lo hacemos - es naturaleza humana
- Enfatiza que es INCONSCIENTE - no es "flojear"
- Menciona que veremos DATOS del mundo real en slides posteriores

---

### **Slide 13: Por qué Parkinson Ocurre** (7 min)

**Contenido:**
- **3 causas psicológicas:**
  1. Aversión al riesgo: "Si termino temprano, me darán más trabajo"
  2. Perfeccionismo: "Puedo mejorar esto si tengo más tiempo"
  3. Validación: "Si fue rápido, no puede ser valioso"

- **El padding se convierte en PROFECÍA AUTOCUMPLIDA**

**Puntos clave:**
1. No es malicia - son incentivos perversos
2. El sistema CASTIGA eficiencia (paradoja)
3. El padding garantiza su propio consumo

**Script sugerido:**
```
"¿Por qué ocurre Parkinson? ¿Por qué expandimos trabajo?

Hay 3 causas psicológicas:

CAUSA 1 - Aversión al riesgo:
Si terminas en 3 días una tarea estimada en 10 días, ¿qué pasa?
Te dan MÁS trabajo inmediatamente. 'Ya que terminaste, toma esta
otra tarea urgente.'

El INCENTIVO perverso es: trabajar LENTO para evitar más trabajo.
No es consciente, pero está ahí. Tu cerebro aprende: 'Si soy
eficiente, me castigan con más carga.'

CAUSA 2 - Perfeccionismo:
'Tengo 10 días, puedo hacer esto PERFECTO.'
Refactorizas. Optimizas. Agregas features 'nice to have.'
En tu mente, estás 'usando bien el tiempo.' En realidad, estás
agregando complejidad innecesaria que nadie pidió ni necesita.

CAUSA 3 - Validación:
'Si esto tomó solo 3 días, no puede ser TAN importante.'
Inconscientemente, asociamos TIEMPO con VALOR. Si algo es rápido,
nos sentimos menos valiosos. Entonces lo ALARGAMOS para sentir
que nuestro trabajo importa."
```

**El círculo vicioso:**
```
"Aquí está el círculo vicioso:

1. Estimas con padding (10 días para tarea de 3)
2. Desarrollador usa los 10 días (Parkinson)
3. PM dice: 'Ves? Tenía razón en dar 10 días.'
4. Próxima tarea similar: estimas 12 días (más padding)
5. Desarrollador usa 12 días
6. PM: 'Cada vez toma MÁS tiempo...'
7. Próxima estimación: 15 días
8. ...

El padding NO protege. GARANTIZA su propio consumo.
Y luego pides MÁS padding porque 'nunca es suficiente.'"
```

**El ejemplo del estudiante:**
```
"Todos hemos sido estudiantes. Tarea para entregar en 2 semanas.

¿Cuándo empiezas? Día 13. ¿Por qué? Porque SABES que 'se puede
hacer en 1 día si me apuro.'

Pero si solo tuvieras 3 días, empezarías en el día 1 y terminarías
en el día 3. Misma tarea, menos tiempo, MISMO resultado (y probablemente
mejor porque no hay sobre-ingeniería)."
```

**Pregunta para reflexión:**
> "¿Han visto esto en sus equipos? ¿Tareas que 'siempre llenan'
> exactamente el tiempo asignado, nunca terminan temprano?"

(Pide 1-2 ejemplos del grupo - validará la teoría)

**Tips:**
- Habla en primera persona: "YO hago esto", no "ustedes hacen"
- Valida que es NORMAL, no patológico
- Menciona que en Clase 3 veremos cómo CCPM resuelve esto (spoiler: buffers agregados)
- La clave: identificar el problema para poder mitigarlo

---

### **Slide 14: Síndrome del Estudiante** (8 min)

**Contenido:**
- **Síndrome del Estudiante:** Posponer el inicio del trabajo hasta la última fecha posible
- Complemento de Parkinson: Mientras Parkinson expande, Estudiante POSPONE
- Resultado: Trabajo se acumula al final, sin buffer para problemas

**Puntos clave:**
1. NO es procrastinación simple - es gestión de riesgo percibido
2. "Empezaré cuando TENGA que empezar, no antes"
3. Elimina buffer porque "todavía hay tiempo"

**Script sugerido:**
```
"El segundo factor psicológico es el Síndrome del Estudiante.

Todos lo hemos vivido como estudiantes: tarea para entregar en
2 semanas. Día 1: 'Tengo tiempo.' Día 7: 'Todavía tengo tiempo.'
Día 12: 'Debo empezar.' Día 13: PÁNICO y trasnochar.

¿Por qué?

Porque inconscientemente calculamos: 'Puedo hacer esto en X tiempo,
tengo 2X disponible, ergo empezaré cuando quede exactamente X.'

El problema: ese cálculo es OPTIMISTA. Asume:
- Cero interrupciones
- Cero problemas inesperados
- Performance perfecto (sin bugs, sin bloqueos)

Inevitablemente, alguno de esos falla. Y cuando falla, ya NO HAY
buffer. Estás en el día 13 de 14, el código no compila, y no hay
tiempo para arreglar correctamente."
```

**Diferencia con Parkinson:**
```
"Parkinson y Estudiante son complementarios:

PARKINSON: 'Si me dan 10 días, usaré 10 días (expandiendo trabajo).'
ESTUDIANTE: 'Si tengo 10 días, empezaré el día 7 (posponiendo inicio).'

Juntos son LETALES:
Día 1-6: No trabajas (Estudiante)
Día 7: Empiezas
Día 7-10: El trabajo se expande para llenar el tiempo (Parkinson)
Día 10: Terminas justo a tiempo, SIN buffer para problemas

Si hay UN problema (siempre lo hay), el proyecto se retrasa."
```

**Ejemplo de proyecto:**
```
"En un proyecto de 6 meses:

Mes 1-2: 'Todavía tenemos tiempo para definir requisitos.'
Mes 3-4: 'Empezaremos desarrollo pronto.'
Mes 5: '¡Debemos empezar YA!'
Mes 5-6: Desarrollo frenético
Mes 6 final: Testing encuentra 50 bugs críticos
Resultado: Retraso de 2 meses

¿Por qué? Síndrome del Estudiante eliminó los primeros 4 meses
de buffer. Parkinson expandió el trabajo para llenar los 2 meses
restantes. No quedó tiempo para problemas reales."
```

**La ilusión de control:**
```
"El Síndrome del Estudiante crea ILUSIÓN de control:

'Tengo buffer, puedo esperar para empezar.'

Pero ese buffer NO es tuyo para POSPONER inicio. Es para ABSORBER
imprevistos. Al posponer inicio, CONSUMES el buffer ANTES de empezar.

Es como tener $1000 de ahorro para emergencias, gastarlo en
caprichos porque 'todavía no hay emergencia', y luego cuando la
emergencia llega, no tienes nada."
```

**Pregunta para el grupo:**
> "¿Cuántos han estado en un proyecto donde los primeros meses
> fueron 'lentos' porque 'había tiempo', y los últimos meses fueron
> caos absoluto?"

(Esta es experiencia casi universal - valida con ejemplos)

**Tips:**
- Conecta explícitamente con experiencias de estudiante - todos se identifican
- Enfatiza que NO es pereza - es gestión de riesgo equivocada
- Menciona que en Clase 3 veremos cómo CCPM prohibe esto (tareas agresivas + buffers agregados)
- La lección: el buffer NO debe estar disponible para consumo casual

---

### **Slide 15: El Ciclo Vicioso del Padding** (12 min)

**Contenido:**
- Diagrama circular mostrando:
  1. PM agrega padding "por seguridad"
  2. Dev consume padding (Parkinson + Estudiante)
  3. Proyecto termina tarde IGUAL
  4. PM agrega MÁS padding próxima vez
  5. Dev consume MÁS padding
  6. Espiral infinita

- **El padding distribuido NO protege - alimenta el problema**

**Puntos clave:**
1. Padding OCULTO es padding VULNERABLE
2. Si el ejecutor SABE que hay padding, lo CONSUMIRÁ
3. Más padding = más consumo, no más seguridad
4. Solución: Buffers AGREGADOS y VISIBLES (Clase 3)

**Script sugerido:**
```
"Ahora juntemos todo: Parkinson + Estudiante + Padding.

Esto crea un CICLO VICIOSO que he visto en cientos de proyectos:

PASO 1: PM estima tarea en 3 días reales, agrega 7 días de padding
'por seguridad.' Total: 10 días asignados.

PASO 2: Developer recibe '10 días para feature X.'
Síndrome del Estudiante: No empieza hasta día 5.
Ley de Parkinson: Trabajo se expande para llenar días 5-10.

PASO 3: Día 9, descubre bug crítico. Pide extensión. Termina día 12.
¡El proyecto se retrasó AUNQUE había 7 días de padding!

PASO 4: PM concluye: 'El padding no fue suficiente. Próxima vez
daré 15 días para tareas similares.'

PASO 5: Developer recibe 15 días. Estudiante pospone más. Parkinson
expande más. Descubre problemas tarde. Termina día 17.

PASO 6: PM: 'NADA es suficiente.' Developer: 'Estas estimaciones
son imposibles.'

Espiral infinita. Cada iteración EMPEORA el problema."
```

**Por qué falla el padding distribuido:**
```
"El padding distribuido tiene 3 problemas fatales:

PROBLEMA 1 - Es INVISIBLE pero CONOCIDO:
El developer no ve los números exactos, pero SIENTE que hay holgura.
'10 días para esto? Wow, debo poder hacerlo mejor.' Y optimiza en
lugar de ejecutar.

PROBLEMA 2 - Es PROPIEDAD del ejecutor:
'Me dieron 10 días, son MIS 10 días.' No hay concepto de 'devolver'
tiempo no usado. Si termina en 5, se siente presionado a usar los
otros 5 en 'mejoras.'

PROBLEMA 3 - Es INDIVIDUAL, no del proyecto:
Cada tarea tiene su padding. Pero los problemas son a nivel PROYECTO.
Una tarea consume su padding en multitasking. Otra en bloqueos.
El proyecto pierde TODO el padding sin absorber UN problema grande."
```

**La metáfora del presupuesto:**
```
"Imagina que tienes presupuesto de $1000 para un viaje.

OPCIÓN A (Padding distribuido):
Das $100 a cada uno de 10 rubros: hotel, comida, transporte, etc.
Cada rubro GASTARÁ sus $100, aunque solo necesite $60. ¿Por qué?
Porque 'tengo $100 asignados, debo usarlos o pierden.'
Resultado: gastas $1000, sin buffer para emergencias.

OPCIÓN B (Buffer agregado):
Asignas lo MÍNIMO a cada rubro: $600 total.
Guardas $400 como buffer de emergencias.
Ese $400 NO está disponible para gasto casual. SOLO para emergencias.
Resultado: si hay emergencia, la absorbes. Si no, ahorras $400."
```

**Pregunta crítica:**
> "¿Por qué seguimos usando padding distribuido si sabemos que falla?"

**Respuestas comunes:**
- "Porque es lo que nos enseñaron"
- "Porque no conocemos alternativa"
- "Porque admitir incertidumbre se ve como debilidad"

**La solución (adelanto):**
```
"En Clase 3 veremos la solución: CCPM (Critical Chain).

En lugar de padding DISTRIBUIDO e INVISIBLE en cada tarea,
usamos:
- Estimaciones AGRESIVAS (50% probabilidad, sin padding)
- Buffers AGREGADOS al final del proyecto (visibles, gestionados)
- Buffer es PROPIEDAD del proyecto, no de tareas individuales

Resultado: El buffer NO se consume por Parkinson/Estudiante,
porque los ejecutores NO lo controlan. Solo se consume para
problemas REALES.

Pero estoy adelantando. Primero, veamos EVIDENCIA empírica de
que Parkinson y Estudiante son REALES, no teoría."
```

**Tips:**
- Este slide es CRUCIAL - conecta teoría con práctica
- Usa gestos/dibujos si tienes pizarra virtual
- Asegúrate que entienden POR QUÉ el padding distribuido falla
- Genera anticipación para Clase 3 (la solución)

---

### **Slide 16: Caso Microsoft - Parkinson en Acción** (12 min)

**Contenido:**
- **Estudio Microsoft (2009)** - Experimento interno
- **Setup:** Misma feature asignada a 2 equipos:
  - Equipo A: Deadline 6 semanas
  - Equipo B: Deadline 2 semanas
- **Resultado:**
  - Equipo A: Entregó en 6 semanas + scope creep
  - Equipo B: Entregó en 2 semanas, enfocado en esencial
  - **Calidad:** Idéntica en ambos equipos

- **Caso Standish Group CHAOS Report (2020)**
- Proyectos con estimaciones "holgadas" (>30% buffer):
  - 31% probabilidad de completarse dentro del buffer
  - 45% probabilidad de consumir TODO el buffer + extras
  - 24% probabilidad de ser más rápidos
- **Conclusión:** El buffer adicional NO mejora probabilidades de éxito

**Puntos clave:**
1. Parkinson NO es teoría - es DEMOSTRABLE con experimentos
2. Más tiempo NO = mejor calidad (después de cierto punto)
3. Tiempo adicional = scope creep + perfeccionismo innecesario

**Script sugerido:**
```
"Parkinson y Estudiante suenan a 'teoría soft' de management.
Pero hay EVIDENCIA empírica contundente.

CASO 1: Microsoft, 2009.

Microsoft hizo un experimento interno fascinante. Tomaron una
feature de complejidad media y la asignaron a 2 equipos diferentes:

Equipo A: 'Tienen 6 semanas para esta feature.'
Equipo B: 'Tienen 2 semanas para esta feature.'

Misma feature. Equipos de habilidad similar. Recursos similares.

¿Resultado?

Equipo A entregó en... 6 semanas. Pero con scope creep:
Agregaron features no solicitadas. 'Ya que teníamos tiempo...'
Refactorizaron código que funcionaba. 'Para hacerlo más limpio.'
Optimizaron performance sin medir si era necesario.

Equipo B entregó en... 2 semanas. Enfocado SOLO en esencial:
Implementaron lo pedido. Nada más, nada menos.
Sin 'mejoras' no solicitadas. Sin over-engineering.

¿Calidad? IDÉNTICA. Bugs similares. Performance similar.
La diferencia: Equipo A usó 3× más tiempo para el MISMO resultado.

Eso es Parkinson en acción. El trabajo se expandió para llenar
las 6 semanas disponibles."
```

**Análisis del resultado:**
```
"¿Por qué Equipo A tomó 6 semanas?

Semana 1-2: Diseño 'exhaustivo.' Debates sobre arquitectura.
'Tenemos tiempo para hacerlo bien.'

Semana 3-4: Implementación. Pero con 'extras' porque 'ya que
estamos haciendo esto, podríamos agregar...'

Semana 5: Testing. Descubren que las 'mejoras' agregaron bugs.

Semana 6: Arreglar bugs de features no solicitadas.

Equipo B no tuvo ESE lujo. 2 semanas = cero tiempo para extras.
Implementar lo pedido, testear, entregar. Punto.

¿Qué es mejor? Equipo B. Más rápido, sin complejidad innecesaria,
misma funcionalidad."
```

**Caso Standish Group:**
```
"Ahora veamos datos agregados: Standish Group CHAOS Report 2020.

Analizaron miles de proyectos. Filtraron aquellos con estimaciones
'holgadas' (>30% de buffer distribuido).

Pregunta: ¿El buffer adicional mejoró las probabilidades de éxito?

Resultados:
- 31% terminó dentro del buffer (exitoso)
- 45% consumió TODO el buffer Y pidió más (falló igual)
- 24% fue más rápido (¿suerte o buenos PMs?)

Conclusión estadística: El buffer adicional NO mejora las
probabilidades. 45% FALLA de todos modos.

¿Por qué? Porque el buffer se CONSUME por Parkinson/Estudiante,
NO por problemas reales. Cuando el problema real llega, el buffer
ya se gastó en perfeccionismo y postergación."
```

**La lección incómoda:**
```
"La lección incómoda es:

MÁS tiempo NO garantiza MÁS éxito.

Después de cierto punto, tiempo adicional solo genera:
- Scope creep (features no pedidas)
- Over-engineering (complejidad innecesaria)
- Perfeccionismo (más bonito, no más funcional)
- Postergación (Síndrome del Estudiante)

Y todo eso CONSUME el buffer que debería proteger contra imprevistos.

Por eso proyectos con 'mucho tiempo' frecuentemente terminan tarde.
El tiempo NO se usó como protección - se usó como invitación a
expandir."
```

**Pregunta provocadora:**
> "¿Han visto esto en sus organizaciones? ¿Proyectos con 'mucho
> tiempo' que de todos modos llegaron tarde?"

(Espera ejemplos - probablemente varios)

**Tips:**
- Los datos de Microsoft son gold - cítalos con confianza
- Enfatiza que son experimentos REALES, no opiniones
- Conecta explícitamente con Parkinson (el trabajo se expandió)
- Menciona que en Clase 3 veremos cómo CCPM evita esto

---

### **Slide 17: Estudio MIT - Síndrome del Estudiante** (13 min)

**Contenido:**
- **Estudio Dan Ariely (MIT, 2002)**
- **Setup:** 3 ensayos asignados a estudiantes con diferentes políticas de deadlines:
  - **Grupo A**: 1 deadline al final (día 84)
  - **Grupo B**: Auto-impuestos (flexible)
  - **Grupo C**: 3 deadlines fijos (días 28, 56, 84)

- **Resultados (Entrega + Calidad):**
  - Grupo A: 76% entregó en últimos 7 días | Calidad: 6.8/10
  - Grupo B: 62% entregó en últimos 10 días | Calidad: 7.2/10
  - Grupo C: Distribución uniforme | Calidad: 8.3/10

- **Conclusión:** Deadlines intermedios FORZADOS mejoran tanto timing como calidad

**Puntos clave:**
1. Estudiante NO es mito - es MEDIBLE científicamente
2. Autodisciplina NO funciona (Grupo B falló)
3. Deadlines EXTERNOS y FRECUENTES son la solución

**Script sugerido:**
```
"Ahora evidencia del Síndrome del Estudiante.

Dan Ariely, profesor de psicología conductual en MIT, hizo un
experimento brillante en 2002.

Dio a sus estudiantes 3 ensayos para entregar en 12 semanas (84 días).
Los dividió en 3 grupos con diferentes políticas de deadlines:

GRUPO A: 'Entreguen los 3 ensayos el día 84.'
Un solo deadline al final. Total flexibilidad para gestionar tiempo.

GRUPO B: 'Fijen sus propios deadlines para cada ensayo.'
Autodisciplina. Los estudiantes eligen cuándo entregar cada uno,
pero deben comprometerse desde el inicio.

GRUPO C: 'Ensayo 1 día 28, Ensayo 2 día 56, Ensayo 3 día 84.'
Deadlines FORZADOS. No negociables. Cada 28 días.

Pregunta: ¿Qué grupo tuvo mejor resultado en TIMING y CALIDAD?"
```

**Resultados detallados:**
```
"Resultados:

GRUPO A (1 deadline final):
Timing: 76% entregó en los ÚLTIMOS 7 DÍAS. Pánico absoluto.
Calidad: 6.8/10 - La más baja.

¿Por qué? Síndrome del Estudiante puro:
Día 1-70: 'Tengo tiempo.'
Día 71-77: 'Debo empezar ya.'
Día 78-84: Escriben 3 ensayos en 1 semana, trasnochando.

Resultado: Timing terrible (todo al final), calidad pobre (escritura
apresurada).

GRUPO B (auto-impuestos):
Timing: 62% entregó en últimos 10 días. Mejor que A, pero malo.
Calidad: 7.2/10 - Intermedia.

¿Por qué no funcionó? Los estudiantes SABEN que deberían espaciar,
pero:
- Fijan deadlines optimistas: 'Entregaré cada 20 días.'
- Día 20 llega: 'No terminé, pero puedo extender, es flexible.'
- Día 40: Igual.
- Día 60-70: Pánico y entregan todo.

Autodisciplina NO funciona cuando el deadline es autopuesto.

GRUPO C (3 deadlines forzados):
Timing: Distribución UNIFORME. 33% en cada período.
Calidad: 8.3/10 - La MÁS ALTA.

¿Por qué? Deadlines externos y frecuentes FUERZAN disciplina:
- Día 28: DEBEN entregar Ensayo 1, no hay opción.
- Día 56: DEBEN entregar Ensayo 2.
- Día 84: DEBEN entregar Ensayo 3.

Sin opción de postergación. Cada deadline 'reinicia' el Síndrome
del Estudiante. Resultado: Timing distribuido, calidad superior
porque NO escribieron todo apresurados."
```

**Análisis por qué Grupo C tuvo mejor CALIDAD:**
```
"Lo sorprendente: Grupo C tuvo mejor CALIDAD, no solo timing.

¿Por qué?

Grupo A/B escribieron 3 ensayos en 7-10 días, exhaustos, sin
tiempo para revisar. Calidad sufre.

Grupo C escribió 1 ensayo cada 28 días. Tiempo para:
- Investigar bien
- Escribir borrador
- Revisar y editar
- Entregar versión pulida

Y después de entregar Ensayo 1, tenían 28 días FRESCOS para el
siguiente. No hay agotamiento acumulativo.

La lección: Deadlines frecuentes NO solo mejoran timing - mejoran
CALIDAD porque previenen trabajo apresurado al final."
```

**Conexión con proyectos de software:**
```
"Esto mapea DIRECTO a metodologías ágiles:

Waterfall = Grupo A:
Un deadline al final (6-12 meses). Todo se entrega junto.
Resultado: Síndrome del Estudiante, pánico final, calidad pobre.

'Agile autoproclamado' = Grupo B:
'Haremos sprints... cuando podamos.' Flexible.
Resultado: Sprints se acumulan, entregas se posponen, igual pánico.

Scrum/Kanban = Grupo C:
Sprints de 2 semanas NO NEGOCIABLES. Cada sprint ENTREGA algo.
Resultado: Trabajo distribuido, entregas frecuentes, calidad alta
porque no hay pánico.

Por eso Scrum FUNCIONA: Es el Grupo C del experimento de Ariely,
aplicado a software."
```

**Pregunta para reflexión:**
> "¿Sus proyectos actuales se parecen más al Grupo A, B o C?
> Si no es C, ¿qué cambio podrían hacer para serlo?"

(Deja que procesen - esta es la pregunta más importante)

**Tips:**
- El estudio de Ariely es científicamente riguroso - úsalo con confianza
- La conclusión (deadlines intermedios forzados) es la BASE de Scrum
- Enfatiza que autodisciplina NO funciona (Grupo B falló)
- Conecta explícitamente con Agile: sprints cortos = deadlines forzados

---

### **Slide 18: Conclusión Empírica** (10 min)

**Contenido:**
- **Los Datos Confirman la Teoría:**
  - Parkinson es REAL (Microsoft, Standish)
  - Estudiante es REAL (MIT/Ariely)
  - Buffer distribuido FALLA (Standish 45%)
  - Solución efectiva: Deadlines estrictos + Buffers agregados visibles

- **Advertencia final:**
> ⚠️ Ignorar estos factores psicológicos garantiza que tu proyecto
> consumirá TODO el tiempo disponible y pedirá más

**Puntos clave:**
1. NO son "teorías soft" - son PATRONES MEDIBLES
2. Afectan a TODOS (incluso senior, motivados, inteligentes)
3. La solución NO es "trabajar más duro" - es CAMBIAR EL SISTEMA

**Script sugerido:**
```
"Perfecto. Hemos visto evidencia empírica sólida de 3 fuentes:

1. Microsoft (2009): Parkinson en acción. Mismo trabajo, 6 semanas
   vs 2 semanas = mismo resultado.

2. Standish CHAOS (2020): Buffer distribuido >30% falla en 45% de
   casos. NO mejora probabilidades de éxito.

3. MIT/Ariely (2002): Síndrome del Estudiante medido científicamente.
   Deadlines intermedios forzados mejoran timing Y calidad.

¿Qué nos dicen estos datos?

CONCLUSIÓN 1: Parkinson y Estudiante NO son mitos. Son REALES,
medibles, y afectan a TODOS (no solo juniors o 'flojos').

CONCLUSIÓN 2: Más tiempo NO = más éxito. Después de cierto punto,
tiempo adicional EMPEORA resultados por scope creep y postergación.

CONCLUSIÓN 3: Buffer distribuido e invisible FALLA. Se consume
por Parkinson/Estudiante, no por problemas reales.

CONCLUSIÓN 4: La solución NO es 'trabajar más duro' o 'ser más
disciplinado.' Es cambiar el SISTEMA:
- Deadlines FRECUENTES y EXTERNOS (no autopuestos)
- Buffers AGREGADOS y VISIBLES (no distribuidos)
- Estimaciones AGRESIVAS sin padding oculto

Veremos cómo hacer esto en Clase 3 con CCPM."
```

**El warning crítico:**
```
"Ahora la advertencia crítica:

Si ignoran estos factores psicológicos - Parkinson y Estudiante -
y siguen usando padding distribuido en estimaciones, les GARANTIZO
que:

1. Su proyecto consumirá TODO el tiempo asignado
2. Pedirá extensiones de todos modos
3. La calidad NO será mejor por el tiempo extra
4. El equipo estará exhausto por pánico de última hora

NO porque su equipo sea malo. Porque el SISTEMA está diseñado
para fallar.

Es como tener un balde con agujeros y sorprenderse de que el agua
se escape. No es el agua - es el balde.

Arreglen el SISTEMA (método de estimación), no culpen a las
PERSONAS (el equipo)."
```

**La conexión con todo lo anterior:**
```
"Conectemos TODO lo que vimos hoy:

PARTE 1: Cono de Incertidumbre
→ La incertidumbre es REAL y ALTA al inicio.
→ Estimaciones precisas tempranas son IMPOSIBLES.

PARTE 2: Factores y Riesgos
→ 16 factores afectan estimación (técnicos, humanos, entorno).
→ Riesgos deben ser clasificados y GESTIONADOS.

PARTE 3: Malvavisco
→ Probar suposiciones TEMPRANO es más valioso que planificar perfecto.
→ MBAs fallaron porque pusieron 'malvavisco' al final.

PARTE 4: Parkinson y Estudiante
→ Factores psicológicos SABOTEAN padding distribuido.
→ Más tiempo NO = más éxito sin cambio de sistema.

¿Cuál es la solución integrada?

CLASE 2: Métodos de estimación (PERT, Agile, Planning Poker)
que reconocen incertidumbre.

CLASE 3: CCPM (Critical Chain), que elimina padding distribuido
y usa buffers agregados + deadlines estrictos.

Estamos construyendo hacia eso."
```

**Pregunta final de cierre:**
> "¿Qué UN insight de hoy cambió su perspectiva sobre estimaciones?"

(Pide 2-3 respuestas breves del grupo - cierra con energía positiva)

**Tips:**
- Este slide CIERRA el argumento - debe sentirse conclusivo
- Recapitula TODOS los conceptos clave
- Genera anticipación para Clases 2-3
- Termina con energía - no dejes que decaiga

---

### **Slide 19: La Pregunta Gancho** (5 min)

**Contenido:**
- **"Entonces... ¿Cómo DEBEMOS estimar?"**
- Provocación: Todo lo visto muestra QUÉ NO hacer
- Promesa: Clases 2-3 mostrarán QUÉ SÍ hacer

**Script sugerido:**
```
"Perfecto. A este punto probablemente están pensando:

'Ok, entendimos QUE NO hacer:
- No estimar con ±400% como si fuera ±10%
- No usar padding distribuido
- No ignorar Parkinson y Estudiante
- No posponer validación de suposiciones
- No planificar 6 meses antes de ejecutar

¡Pero CÓMO estimamos entonces?!'

Esa es EXACTAMENTE la pregunta correcta.

Clase 1 fue diagnóstico: QUÉ está roto y POR QUÉ.
Clases 2-3 son tratamiento: QUÉ hacer al respecto.

CLASE 2 (próxima): Métodos de Estimación
- PERT (3 puntos): Cómo estimar reconociendo incertidumbre
- Agile (Story Points): Estimación relativa vs absoluta
- Planning Poker: Consenso colaborativo
- Velocidad: Calibración empírica

CLASE 3: Cadena Crítica (CCPM)
- Cómo eliminar padding distribuido
- Cómo usar buffers agregados
- Cómo gestionar recursos y riesgos
- Caso práctico completo

Van a salir con herramientas CONCRETAS para usar mañana en sus
proyectos."
```

**Tips:**
- Genera ANTICIPACIÓN para las próximas clases
- Valida que el diagnóstico (Clase 1) es NECESARIO antes del tratamiento
- Asegura que sienten que valió la pena el tiempo

---

### **Slide 20: Resumen Clase 1** (5 min)

**Contenido:**
Resumen ejecutivo de TODO lo cubierto:

✅ **El Problema:** 70% fracaso sistemático, no aleatorio
✅ **Cono de Incertidumbre:** ±400% → ±10% a través de 5 fases
✅ **16 Factores:** Técnicos, Humanos, Entorno
✅ **7 Riesgos:** Clasificados por Probabilidad × Impacto
✅ **Malvavisco:** MBAs 25cm vs Niños 66cm - probar suposiciones temprano
✅ **Parkinson:** Trabajo se expande para llenar tiempo disponible
✅ **Estudiante:** Postergación hasta última fecha posible
✅ **Evidencia:** Microsoft, Standish, MIT confirman teorías

**Mensaje central:**
> Estimar de forma real significa: Reconocer incertidumbre, gestionar
> factores humanos, y colocar seguridad en buffers visibles y estratégicos,
> NO en padding oculto y vulnerable.

**Script sugerido:**
```
"Perfecto, resumen ejecutivo de Clase 1:

Hoy cubrimos 8 conceptos clave:

1. El 70% de fracaso NO es azar - es problema sistémico.
2. Cono de Incertidumbre: ±400% al inicio, ±10% al final.
3. 16 Factores afectan estimación (más allá de complejidad técnica).
4. 7 Riesgos deben clasificarse y gestionarse proactivamente.
5. Malvavisco: Probar suposiciones TEMPRANO > planificar perfecto.
6. Parkinson: Trabajo se expande para llenar tiempo disponible.
7. Estudiante: Postergación consume buffer antes de empezar.
8. Evidencia empírica: Microsoft, Standish, MIT confirman todo esto.

El mensaje central:

Estimar BIEN significa:
- Reconocer que la incertidumbre es REAL (Cono)
- Gestionar factores humanos, no solo técnicos (16 Factores)
- Probar suposiciones críticas TEMPRANO (Malvavisco)
- Colocar seguridad en buffers ESTRATÉGICOS, no padding distribuido

NO es sobre 'estimar mejor con el mismo método roto.'
Es sobre CAMBIAR el método."
```

**Tips:**
- Habla con ENERGÍA - es el cierre, no dejes que decaiga
- Valida que cubriste MUCHO en 3 horas (es legítimo estar cansados pero energizados)
- Menciona que las próximas 2 clases serán más "constructivas" (herramientas vs diagnóstico)

---

### **Slide 21: Cierre y Próxima Clase** (5 min)

**Contenido:**
- **Felicitaciones** por completar Clase 1
- **Próxima Clase:** Métodos de Estimación (PERT, Agile, Planning Poker)
- **Tarea opcional:** Pensar en 1 proyecto actual y aplicar Cono de Incertidumbre
- **Contacto:** Alejandro Sfrede - Área de Arquitectura

**Script sugerido:**
```
"Excelente trabajo. Completamos Clase 1 exitosamente.

Cubrimos MUCHO material denso: Cono, Factores, Riesgos, Malvavisco,
Parkinson, Estudiante, evidencia empírica. Si sienten la cabeza
llena, es NORMAL. Esto es 3 horas de contenido concentrado.

PRÓXIMA CLASE: Métodos de Estimación

Veremos 3 enfoques:
1. PERT (Program Evaluation Review Technique): Cómo estimar con
   incertidumbre explícita usando 3 puntos (optimista, realista,
   pesimista).

2. Agile (Scrum): Story Points, estimación relativa, Planning Poker.
   Cómo estimar SIN tiempo absoluto.

3. Velocidad: Cómo calibrar empíricamente en lugar de adivinar.

Será más 'constructivo' - herramientas que pueden usar MAÑANA.

TAREA OPCIONAL (no obligatoria, pero útil):
Piensen en 1 proyecto actual. Pregúntense:
- ¿En qué fase del Cono está? (Concepto, Requisitos, Diseño...)
- ¿La estimación refleja la incertidumbre de esa fase?
- ¿Qué 'malvavisco' (suposición oculta) debería probar YA?

Si hacen este ejercicio mental 10 minutos, la próxima clase
resonará 10× más.

CONTACTO:
Alejandro Sfrede - Área de Arquitectura
Si tienen preguntas, envíenlas y las abordaré la próxima sesión.

¡Gracias por su participación activa! Nos vemos en Clase 2."
```

**Tips:**
- Termina en tiempo (3 horas exactas si es posible)
- Agradece participación específica si hubo buenos comentarios
- Deja canal abierto para preguntas asíncronas
- Genera energía positiva para la próxima clase

---

## 🎯 Resumen Completo Clase 1

### Tiempo Total: 180 minutos (3 horas)

**Pre-Break (90 min):**
- Intro y Problema (15 min)
- Cono de Incertidumbre (45 min)
- Factores y Riesgos (30 min)

**Post-Break (85 min):**
- Parkinson y Estudiante (35 min)
- Estudios Empíricos (35 min)
- Cierre y Resumen (15 min)

### Objetivos Alcanzados:
✅ Estudiantes entienden por qué 70% de proyectos falla
✅ Conocen el Cono y pueden identificar fase actual
✅ Pueden listar 16 factores que afectan estimación
✅ Pueden clasificar riesgos en matriz Probabilidad×Impacto
✅ Entienden por qué padding distribuido falla (Parkinson/Estudiante)
✅ Tienen evidencia empírica (no solo opiniones)

### Preparación para Clase 2:
- Clase 1 diagnosticó el PROBLEMA
- Clase 2 dará HERRAMIENTAS (PERT, Agile, Planning Poker)
- Clase 3 dará SISTEMA (CCPM con buffers agregados)

---

## 📌 Tips Generales para el Profesor

### Lo que funcionó bien:
✅ Gráficos visuales (Cono, Matriz) - tómate tiempo en ellos
✅ Estudios empíricos (Microsoft, MIT) - cítalos con confianza
✅ Analogías (Malvavisco, email de 5 min vs 2 hrs) - úsalas generosamente
✅ Preguntas al grupo cada 10-15 min - mantiene engagement

### Lo que puede salir mal:
❌ Quedarte sin tiempo en Cono (Slide 7) - es EL slide crítico
❌ Apurar Malvavisco (Slides 8-10) - es la analogía GOLD
❌ Sonar acusatorio con Parkinson/Estudiante - enfatiza que es naturaleza humana
❌ No conectar conceptos - cada parte construye sobre anterior

### Si te Quedas Corto de Tiempo:
- Prioridad 1: Slides 7 (Cono), 8-10 (Malvavisco), 16-17 (Evidencia)
- Prioridad 2: Slides 7b-7d (Factores/Riesgos), 12-15 (Parkinson/Estudiante)
- Puedes acelerar: Slides 3-6 (Intro, todos conocen el problema)

### Si te Sobra Tiempo:
- Profundiza en Slide 7d (Matriz Riesgos) - pide ejemplos del grupo
- Extiende Slide 15 (Ciclo Vicioso) - es crítico
- Agrega Q&A de 10 min antes de cerrar

### Métricas de Éxito:
✅ Al menos 5 preguntas/comentarios del grupo durante la clase
✅ Alguien dice "wow, nunca lo había pensado así" (especialmente en Malvavisco)
✅ Grupo puede explicar Parkinson en sus propias palabras
✅ Anticipación visible para Clase 2

---

**Próximo documento:** `GUIA_PROFESOR_CLASE2.md` (Métodos de Estimación completo)
