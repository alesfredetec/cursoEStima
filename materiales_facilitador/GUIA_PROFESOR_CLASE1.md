# Guía del Profesor - Clase 1: La Crisis de la Estimación

**Duración:** 3 horas
**Formato:** Remoto / Teórico
**Objetivos de Aprendizaje:** Comprender por qué las estimaciones tradicionales fallan, el Cono de Incertidumbre, y factores psicológicos que afectan la estimación

---

## 📋 Índice de la Clase

| Slide | Tema | Duración | Tipo |
|-------|------|----------|------|
| 1 | Portada | 2 min | Intro |
| 2 | Agenda | 3 min | Overview |
| 3-4 | El Problema Fundamental | 10 min | Teoría |
| 5-6 | Cono de Incertidumbre | 20 min | Teoría |
| 7 | Gráfico del Cono (SVG) | 15 min | Visual |
| 7b | Factores de Estimación | 10 min | Teoría |
| 7c | Clasificación de Riesgos | 10 min | Teoría |
| 7d | Matriz de Riesgos Visual | 10 min | Visual |
| 8-10 | Investigación Malvavisco | 30 min | Caso de Estudio |
| 11 | Break | 15 min | Descanso |
| 12-15 | Factores Psicológicos | 35 min | Teoría |
| 16-18 | Estudios Empíricos | 25 min | Casos |
| 19-21 | Cierre | 15 min | Síntesis |

**Total:** 180 minutos (3 horas)

---

## 🎯 Objetivos de Aprendizaje Específicos

Al finalizar esta clase, los estudiantes podrán:

1. ✅ Explicar por qué el 70% de proyectos software fallan en estimaciones
2. ✅ Describir el Cono de Incertidumbre y sus 5 fases
3. ✅ Identificar 16 factores que afectan la estimación (técnicos, humanos, entorno)
4. ✅ Clasificar riesgos por probabilidad e impacto
5. ✅ Explicar la Ley de Parkinson y el Síndrome del Estudiante con evidencia empírica
6. ✅ Reconocer por qué el padding distribuido falla sistemáticamente

---

## 📊 Preparación Previa

### Materiales Necesarios:
- ✅ Acceso a `clase1.html` (verificar que carga correctamente)
- ✅ Plataforma de videoconferencia configurada (Zoom/Teams/Meet)
- ✅ Compartir pantalla funcionando
- ✅ Micrófono y cámara OK
- ✅ OPCIONAL: Pizarra virtual (Miro, Mural) para Q&A

### Conocimientos Previos Requeridos (estudiantes):
- Ninguno - Esta es la clase introductoria
- Experiencia previa en proyectos es útil pero no requerida

### Preparación del Profesor:
1. Lee esta guía completa ANTES de la clase
2. Navega `clase1.html` al menos 1 vez completa
3. Practica explicar el gráfico del Cono (Slide 7)
4. Revisa los datos de los estudios (Tom Wujec, Microsoft, Dan Ariely)
5. Prepara 2-3 ejemplos propios de proyectos fallidos

---

## 📖 Desglose Slide por Slide

### **Slide 1: Portada** (2 min)

**Contenido:**
- Título: "Clase 1: La Crisis de la Estimación"
- Subtítulo: "Por qué el 70% de proyectos falla"
- Duración: 3 horas

**Script sugerido:**
```
"Bienvenidos a la Clase 1 del curso de Estimación de Proyectos.
Hoy vamos a explorar una pregunta incómoda: ¿Por qué el 70% de
proyectos de software fallan en sus estimaciones iniciales?

No es por falta de inteligencia o esfuerzo. Es porque estamos
usando métodos que ignoran la naturaleza fundamental de la
incertidumbre. Vamos a ver POR QUÉ esto sucede, y qué podemos
hacer al respecto."
```

**Tips:**
- Establece tono: curioso, no culposo
- Menciona que veremos EVIDENCIA, no opiniones
- Asegura que todos pueden ver y escuchar OK

---

### **Slide 2: Agenda** (3 min)

**Contenido:**
1. Introducción al problema (30 min)
2. Cono de Incertidumbre con gráfico visual (45 min)
3. Factores y riesgos (30 min)
4. Investigación Malvavisco - Análisis teórico (30 min)
5. ☕ Break (15 min)
6. Factores Psicológicos (35 min)
7. Estudios de Caso y Evidencia (25 min)

**Script sugerido:**
```
"La agenda de hoy tiene 7 bloques. Vamos a empezar entendiendo
el problema fundamental, luego exploraremos el famoso Cono de
Incertidumbre - un concepto que cambiará cómo piensan sobre
estimaciones.

Después del break, hablaremos de factores psicológicos: la Ley
de Parkinson y el Síndrome del Estudiante. Estos son patrones
de comportamiento humano que sabotean nuestros proyectos, y
veremos evidencia empírica de estudios reales."
```

**Tips:**
- Menciona que habrá 1 break de 15 min
- Indica que pueden hacer preguntas en cualquier momento (chat o micrófono)
- Confirma que la clase es teórica/remota (sin talleres físicos)

---

### **Slide 3: El Problema Fundamental** (5 min)

**Contenido:**
- 70% de proyectos excede tiempo/presupuesto
- Falla sistemática ≠ falla aleatoria
- La pregunta: ¿Estimamos mal o es el enfoque el problema?

**Puntos clave a enfatizar:**
1. **No es tu culpa personal**: Es un problema sistémico
2. **70% no es azar**: Si fuera aleatorio sería ~50%
3. **El método está roto**: No las personas

**Script sugerido:**
```
"Standish Group lleva 30 años estudiando proyectos de software.
El número es consistente: 70% falla en estimaciones iniciales.

Piensen en esto: si fuera aleatorio, sería 50/50. Pero es 70%.
Eso significa que hay un SESGO SISTEMÁTICO. No estamos tirando
una moneda y teniendo mala suerte. Hay algo fundamentalmente
equivocado en CÓMO estimamos.

La pregunta que exploraremos hoy es: ¿Somos malos estimando,
o estamos usando un enfoque que garantiza el fracaso?"
```

**Pregunta para el grupo:**
> "¿Alguien ha estado en un proyecto que CUMPLIÓ la estimación inicial?"

(Espera respuestas - probablemente pocas o ninguna)

**Tips:**
- No nombres culpables (ni PMs, ni devs, ni clientes)
- Establece que buscaremos causas estructurales, no personales
- Si alguien comparte ejemplo de éxito, pregunta: "¿En qué fase se hizo esa estimación?"

---

### **Slide 4: Estimación vs Plan** (5 min)

**Contenido:**
Distinción crítica:
- **Estimación**: Predicción de magnitud (esfuerzo/tiempo)
- **Plan**: Organización de trabajo con fechas y recursos

**Puntos clave:**
- Estimación ≠ Compromiso
- Plan usa estimaciones como INPUT
- Confundirlos causa problemas políticos

**Script sugerido:**
```
"Antes de continuar, necesitamos una distinción crítica:

ESTIMACIÓN es una predicción. 'Esta feature probablemente
tomará 2 semanas de trabajo efectivo.'

PLAN es un compromiso organizacional. 'Entregaremos el 15 de marzo.'

El problema ocurre cuando tratamos estimaciones como compromisos.
Un PM pregunta: '¿Cuánto toma?' Un dev dice: '3 semanas, creo.'
El PM escucha: 'Compromiso de 3 semanas.'

La estimación era una predicción con incertidumbre. El plan
la convirtió en una promesa fija. ESE es el problema."
```

**Ejemplo práctico:**
```
"Es como preguntarle a un meteorólogo: '¿Lloverá el sábado?'
Él dice: 'Hay 60% de probabilidad.'
Tú PLANEAS un picnic asumiendo que NO lloverá.
Llueve.
¿Falló el meteorólogo? No. Tú convertiste una probabilidad
en una certeza."
```

**Tips:**
- Esta distinción es FUNDAMENTAL para todo el curso
- Si no queda clara, todo lo demás se malinterpreta
- Repite: "Estimación = predicción con incertidumbre, no compromiso"

---

### **Slide 5: Cono de Incertidumbre - Concepto** (10 min)

**Contenido:**
- Concepto de Steve McConnell (1997)
- Variabilidad de estimaciones según fase del proyecto
- Inicio: ±400% | Final: ±10%

**Puntos clave:**
1. **La incertidumbre DISMINUYE con el tiempo**
2. **No linealmente - exponencialmente al principio**
3. **Sólo disminuye si EJECUTAS y aprendes**

**Script sugerido:**
```
"Steve McConnell, en su libro 'Software Estimation: Demystifying
the Black Art', documentó algo fascinante: la incertidumbre en
estimaciones no es constante. Cambia dramáticamente según la
fase del proyecto.

Al principio - fase de 'concepto' - la variabilidad es ENORME:
±400%. Si estimas '1 año', el proyecto real puede tomar entre
3 meses y 4 años. Ambos extremos son IGUALMENTE probables.

Al final - cuando estás por entregar - la variabilidad es ±10%.
Si dices 'terminamos en 1 semana', será entre 6 y 8 días.

¿Por qué? Porque al principio NO SABES QUÉ VAS A CONSTRUIR.
Al final, ya casi lo terminaste."
```

**Pregunta para reflexión:**
> "¿Cuándo les suelen pedir la estimación más importante? ¿Al inicio o al final?"

(Respuesta obvia: al inicio - ahí está el problema)

**Analogía útil:**
```
"Es como estimar cuánto costará 'unas vacaciones.'
Sin saber si es camping local o safari en África, la estimación
es inútil. ±400% es generoso - podría ser ±10,000%.

Pero si ya compraste vuelos, hotel, y tienes itinerario, puedes
estimar con ±10%."
```

**Tips:**
- Dibuja el cono con la mano si tienes pizarra virtual
- Enfatiza que el cono NO se estrecha solo - requiere APRENDER
- Menciona que veremos el gráfico visual en el siguiente slide

---

### **Slide 6: Las 5 Fases del Cono** (10 min)

**Contenido:**
Tabla con 5 fases:
1. **Concepto Inicial**: ±400% (×0.25 a ×4)
2. **Requisitos Aprobados**: ±100% (×0.5 a ×2)
3. **Diseño de UI Completo**: ±50% (×0.67 a ×1.5)
4. **Diseño Detallado**: ±25% (×0.8 a ×1.25)
5. **Código Completo**: ±10% (×0.9 a ×1.1)

**Puntos clave:**
1. Cada fase reduce incertidumbre SI aprendes
2. Saltar fases NO reduce el cono - solo lo oculta
3. Los números son PROMEDIOS de cientos de proyectos

**Script sugerido:**
```
"Veamos las 5 fases en detalle:

FASE 1 - Concepto Inicial: 'Queremos una app de e-commerce.'
¿Con catálogo de 10 productos o 10 millones? ¿Con pagos o solo
carrito? ±400% es RAZONABLE aquí.

FASE 2 - Requisitos Aprobados: Ya sabemos QUÉ, no HOW.
'E-commerce con 1000 productos, pagos con tarjeta, envíos.'
Incertidumbre baja a ±100%. Todavía puede duplicarse o reducirse
a la mitad.

FASE 3 - Diseño UI Completo: Mockups, flujos, pantallas.
Ahora ±50%. Claramente más acotado.

FASE 4 - Diseño Detallado: Arquitectura, base de datos, APIs.
±25% - Ya casi no hay sorpresas.

FASE 5 - Código Completo: Solo falta testing final.
±10% - Casi certeza."
```

**Pregunta crítica para el grupo:**
> "Si al INICIO la incertidumbre es ±400%, ¿tiene sentido exigir
> una fecha fija de entrega en esa fase?"

(Deja que procesen - algunos dirán "no" inmediatamente)

**Ejemplo práctico:**
```
"Es como si te pidieran estimar cuánto costará 'construir una casa.'
Sin saber si es 50m² o 500m², 1 piso o 3, materiales económicos
o premium... ¿cómo respondes?

La mayoría diría: 'Necesito más información.'
Pero en software decimos: '$200,000 y 6 meses' y luego nos
sorprendemos cuando falla."
```

**Tips:**
- Enfatiza que estas cifras vienen de DATOS (McConnell estudió 600+ proyectos)
- No son arbitrarias o pesimistas
- Menciona que el siguiente slide mostrará esto VISUALMENTE

---

### **Slide 7: Gráfico del Cono de Incertidumbre (SVG)** (15 min)

**Contenido:**
- Gráfico SVG interactivo
- Eje X: 5 fases del proyecto
- Eje Y: Variabilidad (×0.25 a ×4)
- Zona verde (optimista) y roja (pesimista)
- Línea amarilla central (estimación)

**Puntos clave:**
1. **El cono es ASIMÉTRICO** - puede explotar más que comprimirse
2. **Converge si y solo si APRENDES** activamente
3. **NO es automático** - proyectos mal gestionados mantienen alta incertidumbre

**Script sugerido:**
```
"Aquí está el famoso Cono de Incertidumbre visualizado.

El eje X muestra las 5 fases: Concepto → Requisitos → Diseño →
Desarrollo → Entrega.

El eje Y muestra la variabilidad. Al inicio, la zona VERDE (optimista)
llega hasta ×4 arriba. La zona ROJA (pesimista) baja hasta ×0.25.

Esa línea amarilla punteada es tu 'estimación central.' Pero nota
que el CONO es mucho más ancho arriba que abajo. ¿Por qué?

Porque los proyectos tienden a EXPLOTAR más que a comprimirse.
Es más común que algo tome 4× más de lo estimado, que 4× menos."
```

**Momento "Aha!" a buscar:**
```
"Miren la diferencia entre el inicio y el final. Al inicio, el
cono es ENORME. Al final, es una línea casi recta.

Esto significa que PEDIR una estimación precisa al inicio es
pedirle a alguien que MIENTA. La incertidumbre es real. No es
incompetencia."
```

**Pregunta para discusión:**
> "¿Qué pasa si un proyecto salta de Concepto directo a Código,
> sin pasar por Requisitos ni Diseño?"

**Respuesta esperada:**
"El cono NO se estrecha. La incertidumbre sigue ahí, oculta.
Aparece como 'bugs' o 'cambios de requisitos' tardíos."

**Conexión con realidad:**
```
"Esto explica por qué los proyectos 'Waterfall puro' a menudo
fallan desastrosamente. Asumen que la estimación inicial (±400%)
es válida como plan fijo. Matemáticamente, es imposible.

Y también explica por qué Agile funciona mejor: iteraciones
CORTAS estrechan el cono RÁPIDO. Cada sprint aprende y ajusta."
```

**Tips:**
- Pasa al menos 5 min en este slide - es el más importante de la clase
- Usa puntero/mouse para señalar partes específicas del gráfico
- Si alguien pregunta "¿cómo estrechar más rápido?", responde: "Aprender más rápido - prototipos, MVPs, iteraciones"
- Asegúrate que todos vean la asimetría (más arriba que abajo)

---

### **Slide 7b: Factores que Afectan la Estimación** (10 min)

**Contenido:**
Clasificación de 16 factores en 3 categorías:

**📐 Factores Técnicos (5):**
- Complejidad (algoritmos, integraciones, arquitectura)
- Tecnología (nueva vs conocida, madurez)
- Tamaño (LOC, componentes)
- Calidad requerida (testing, performance, seguridad)
- Restricciones (hardware, software, regulatorias)

**👥 Factores Humanos (5):**
- Experiencia del equipo
- Disponibilidad (dedicación, multitasking)
- Comunicación (claridad de requisitos)
- Motivación (compromiso del equipo)
- Rotación (cambios en personal)

**⚠️ Factores de Entorno (6):**
- Volatilidad requisitos, Dependencias externas
- Procesos, Herramientas, Presión temporal, Stakeholders

**Puntos clave:**
1. Estimaciones NO dependen solo de la tarea - dependen del CONTEXTO
2. Misma tarea, diferentes factores = estimación MUY diferente
3. Ignorar factores humanos/entorno es la causa #1 de error

**Script sugerido:**
```
"Ahora que entendemos el Cono, hablemos de QUÉ afecta la estimación.

La mayoría piensa solo en FACTORES TÉCNICOS: complejidad del código,
tecnología, tamaño. Esos importan, pero son solo 5 de 16.

Los FACTORES HUMANOS son igualmente críticos: un equipo senior
con 5 años juntos estimará MUY diferente que un equipo junior recién
formado. La misma feature puede tomar 2 semanas o 8 semanas.

Y los FACTORES DE ENTORNO son los que más se ignoran: si los
requisitos cambian cada semana (volatilidad), tu estimación original
es basura. Si dependes de una API externa que tarda 2 días en
responder consultas, tu timeline explota."
```

**Ejemplo práctico por categoría:**

**Técnico:**
```
"'Agregar login con email/password' suena simple. Pero:
- ¿Con MFA? (complejidad +200%)
- ¿Usando nueva librería de auth que nadie conoce? (tecnología +150%)
- ¿Con requisitos GDPR/CCPA de seguridad? (calidad +100%)"
```

**Humano:**
```
"Si tu mejor dev (experiencia) está en 3 proyectos simultáneos
(disponibilidad), y el Product Owner responde emails cada 3 días
(comunicación), tu estimación de '1 sprint' se convierte en 3."
```

**Entorno:**
```
"Si el stakeholder cambia de opinión cada semana (volatilidad),
y el proyecto depende de un sistema legacy sin documentación
(dependencias externas), y estás obligado a usar un proceso de
deploy manual que toma 1 día (herramientas)... ¿importa cuánto
estimaste el desarrollo puro? No."
```

**Actividad mental para el grupo:**
> "Piensen en un proyecto que estimaron mal recientemente.
> ¿Cuál de estos 16 factores fue el culpable? Escriban en el chat."

(Lee algunos - probablemente verás: "volatilidad requisitos", "experiencia", "dependencias externas")

**Tips:**
- No intentes memorizar los 16 - los slides los tienen
- Enfoca en la IDEA: estimación = tarea × contexto
- Menciona que usaremos estos factores en Clase 2 para estimación ágil

---

### **Slide 7c: Clasificación de Riesgos** (10 min)

**Contenido:**
Tabla con 7 riesgos clasificados por:
- **Categoría**: Crítico / Importante / Menor
- **Probabilidad**: Alta / Media / Baja
- **Impacto**: Alto / Medio / Bajo
- **Estrategia**: Mitigación específica

**7 Riesgos ejemplo:**
1. Cambios de alcance no controlados (CRÍTICO)
2. Dependencia de recurso único (CRÍTICO)
3. Tecnología no probada (CRÍTICO)
4. Requisitos ambiguos (IMPORTANTE)
5. Integraciones legacy (IMPORTANTE)
6. Cambios UI/UX (MENOR)
7. Disponibilidad ambiente testing (MENOR)

**Puntos clave:**
1. **Riesgo ≠ Problema**: Riesgo es PROBABILIDAD × IMPACTO
2. **No todos los riesgos son iguales**: Priorizar críticos
3. **Cada riesgo necesita ESTRATEGIA**: No solo identificar, ACTUAR

**Script sugerido:**
```
"Ahora que conocemos los 16 factores, hablemos de RIESGOS.

Un riesgo NO es un problema que ya ocurrió. Es algo que PUEDE
ocurrir, con cierta probabilidad e impacto.

Esta tabla muestra 7 riesgos comunes clasificados en 3 niveles:

CRÍTICOS (🔴): Alta probabilidad + Alto impacto, o Media + Alto.
Estos pueden MATAR el proyecto. Requieren acción inmediata.

Ejemplo: 'Dependencia de recurso único' - Si María es la ÚNICA
que sabe cómo funciona el módulo de pagos, y se enferma... el
proyecto se detiene. Probabilidad ALTA (gente se enferma),
Impacto ALTO (proyecto bloqueado).

IMPORTANTES (🟡): Combinación Media/Media. Hay que gestionarlos.

MENORES (🟢): Bajo impacto o baja probabilidad. Monitorear."
```

**Desglose de un riesgo crítico:**
```
"Veamos 'Cambios de alcance no controlados':

Probabilidad: ALTA - En proyectos sin gestión de cambios formal,
stakeholders piden 'pequeños ajustes' constantemente.

Impacto: ALTO - Cada cambio rompe estimaciones, retrasa entrega,
desmoraliza equipo.

Estrategia: Gestión de cambios FORMAL. Todo cambio va a comité,
se estima, se aprueba, se re-prioriza. No hay 'pequeños ajustes.'

Sin esta estrategia, el proyecto está condenado."
```

**Conexión con factores:**
```
"Nota que estos riesgos mapean directamente a los 16 factores:
- 'Requisitos ambiguos' = Factor Humano (comunicación)
- 'Tecnología no probada' = Factor Técnico (tecnología)
- 'Dependencias externas' = Factor de Entorno

Los factores son las CAUSAS. Los riesgos son las CONSECUENCIAS."
```

**Pregunta para el grupo:**
> "¿Cuál de estos 7 riesgos han experimentado en sus proyectos?
> ¿Cuál fue el más doloroso?"

(Probablemente: "Cambios de alcance" será el más mencionado)

**Tips:**
- Enfatiza que la columna "Estrategia" es la MÁS importante
- No basta identificar riesgos - hay que MITIGARLOS
- Menciona que el siguiente slide mostrará esto VISUALMENTE en matriz

---

### **Slide 7d: Matriz de Riesgos Visual (SVG)** (10 min)

**Contenido:**
- Gráfico SVG Probabilidad (X) vs Impacto (Y)
- Grid 3×3: Baja/Media/Alta × Bajo/Medio/Alto
- Zonas coloreadas: Verde/Amarillo/Rojo
- 5 riesgos ejemplo posicionados:
  - "UI Changes" (Verde: Baja/Bajo)
  - "Tech no probada" (Amarillo: Alta/Bajo)
  - "Legacy Integration" (Amarillo: Media/Medio)
  - "Recurso Único" (Rojo: Alta/Medio)
  - "Scope Creep" (Rojo: Alta/Alto)

**Puntos clave:**
1. **Zona Roja = Acción INMEDIATA**: No negociable
2. **Zona Amarilla = Plan de mitigación**: Documentar y monitorear
3. **Zona Verde = Monitorear**: Revisión periódica, no panic

**Script sugerido:**
```
"Esta matriz visualiza la tabla anterior.

Eje X = Probabilidad (Baja → Media → Alta)
Eje Y = Impacto (Bajo → Medio → Alto)

Los 9 cuadrados se colorean según severidad:

ZONA VERDE (abajo izquierda): Baja probabilidad + Bajo impacto.
Ejemplo: 'Cambios en UI/UX' - Puede pasar, pero no mata el proyecto.
Estrategia: Monitorear. No requiere acción preventiva.

ZONA AMARILLA (diagonal central): Combinaciones Media/Media.
Ejemplo: 'Integraciones con legacy' - Puede ser complejo, pero
manejable con plan.
Estrategia: Plan de mitigación documentado. Buffer de tiempo.

ZONA ROJA (arriba derecha): Alta probabilidad + Alto impacto.
Ejemplo: 'Scope Creep' - VA a pasar si no tienes proceso, y
MATARÁ el proyecto si pasa.
Estrategia: Acción INMEDIATA. Gestión de cambios formal. No esperar."
```

**Caso práctico - "Recurso Único":**
```
"Vean 'Recurso Único' en la zona roja (Alta prob, Medio impacto).

¿Por qué Alta probabilidad? Porque la gente se enferma, renuncia,
se va de vacaciones. Es INEVITABLE que ocurra.

¿Por qué Medio impacto? Si tenemos backup, el proyecto se retrasa
pero no muere. Si NO tenemos backup, es Alto.

Estrategia: Documentación + Pair programming + Rotación de tareas.
NO esperar a que María renuncie para empezar a documentar."
```

**Actividad mental:**
```
"Miren la posición de 'Tech no probada' (amarillo, Alta/Bajo).
Alta probabilidad de problemas, pero Bajo impacto si:
- Haces proof of concept TEMPRANO (antes de comprometerte)
- Tienes plan B (fallback a tech conocida)

Sin eso, se mueve a zona ROJA."
```

**Pregunta para discusión:**
> "¿Cuál es el riesgo #1 que enfrentan en sus proyectos actuales?
> ¿En qué zona de esta matriz está?"

(Pide que 2-3 personas compartan - usa chat si grupo es grande)

**Tips:**
- Mueve el puntero por el gráfico para mostrar las zonas
- Enfatiza que los riesgos MIGRAN entre zonas según acciones
- Menciona que en Clase 3 veremos cómo CCPM gestiona riesgos con buffers
- Asegúrate que entiendan: NO se trata de eliminar riesgos, sino GESTIONARLOS

---

### **Slide 8: Investigación del Desafío del Malvavisco** (10 min)

**Contenido:**
- Estudio de Tom Wujec (2010) con 70+ equipos
- Tabla comparativa de resultados:
  - **MBAs/Ejecutivos**: 25 cm (Planificaron >15 min, malvavisco al final)
  - **Abogados**: 38 cm (Similar a MBAs, mucha negociación)
  - **Niños de jardín**: 66 cm (Iteraron, probaron malvavisco desde min 1)

**Puntos clave:**
1. **No es sobre inteligencia** - MBAs son más inteligentes que niños
2. **Es sobre MÉTODO** - Planificar primero vs Probar primero
3. **La experiencia puede ser ENEMIGA** - Si aprendiste mal método

**Script sugerido:**
```
"Ahora vamos a ver uno de los experimentos más reveladores sobre
estimación: El Desafío del Malvavisco.

Tom Wujec, investigador de diseño, dio a 70+ equipos el mismo
reto: construir la torre más alta con 20 espaguetis, 1m de cinta,
1m de hilo, y 1 malvavisco. El malvavisco DEBE estar en la cima.
Tiempo: 18 minutos.

Lo fascinante no es QUIÉN ganó, sino POR QUÉ ganaron.

Miren esta tabla de resultados:

MBAs y ejecutivos - personas con MÁS educación y experiencia -
promediaron 25 cm. Muchos COLAPSARON completamente.

Niños de jardín - 5 años de edad - promediaron 66 cm. ¡Casi 3×!

¿Cómo es posible?"
```

**Análisis del resultado:**
```
"No es sobre inteligencia. Es sobre MÉTODO.

MBAs hacen lo que les enseñaron: PLANIFICAR → EJECUTAR.
Pasan 10-15 minutos discutiendo diseño, negociando roles,
dibujando en papel. Minuto 16, empiezan a construir. Minuto 18,
ponen el malvavisco... y TODO COLAPSA.

¿Por qué? Porque asumieron que el malvavisco era ligero. Nunca
lo PROBARON hasta el final. No tenían tiempo para iterar.

Niños NO saben planificar. Minuto 1: ponen malvavisco. Colapso.
Minuto 3: segunda versión. Mejor. Minuto 6: tercera versión.
Minuto 18: versión 5-6, optimizada por prueba/error."
```

**Conexión con software:**
```
"Esto es EXACTAMENTE lo que pasa en proyectos Waterfall:

6 meses planificando (como MBAs).
6 meses construyendo.
Mes 12: integramos componentes (como el malvavisco).
COLAPSO TOTAL.
No hay tiempo para iterar.

Agile/Scrum es el método de los niños:
Sprint 1: prototipo que colapsa.
Sprint 2: mejor.
Sprint 3-10: refinamiento continuo.
Release: producto TESTEADO, no teoría."
```

**El malvavisco = La INCERTIDUMBRE OCULTA:**
```
"El malvavisco representa las SUPOSICIONES que no validaste.

En software:
- 'El API externo responde en <200ms' (¿probaste?)
- 'La base de datos soporta 1M registros' (¿probaste?)
- 'Los usuarios entienden esta UI' (¿probaste?)

Cada suposición no validada es un malvavisco que pondrás al FINAL.
Y probablemente colapse todo."
```

**Pregunta para el grupo:**
> "¿Han estado en un proyecto donde descubrieron un problema CRÍTICO
> en los últimos días antes de la entrega, cuando ya no había tiempo
> de arreglarlo?"

(Espera respuestas - esta es experiencia universal)

**Tips:**
- Este estudio es GOLD - tómate el tiempo para explicarlo bien
- La metáfora del malvavisco = suposición oculta es poderosa
- Menciona que Tom Wujec tiene un TED Talk sobre esto (pueden buscarlo)
- Conecta explícitamente con el Cono: MBAs asumen cono estrecho, niños asumen cono ancho

---

### **Slide 9: Análisis de Comportamiento** (10 min)

**Contenido:**
Comparativa lado a lado:

**Patrón de Fracaso (MBAs):**
1. Min 0-10: Planificación y diseño en papel
2. Min 10-15: Discusión sobre el mejor enfoque
3. Min 15-17: Construcción frenética
4. Min 18: Colocan malvavisco → COLAPSO
- Resultado: No tienen tiempo para iterar

**Patrón de Éxito (Niños):**
1. Min 1: Ponen malvavisco inmediatamente
2. Min 2-5: Primera versión colapsa
3. Min 6-10: Prueban 2da variante
4. Min 11-18: Iteran y mejoran progresivamente
- Resultado: Múltiples ciclos de feedback

**Puntos clave:**
1. **Tiempo es CONSTANTE** (18 min para ambos)
2. **Diferencia es CUÁNDO aprendes**: Temprano vs Tarde
3. **Falla temprana = Oportunidad de corregir**
4. **Falla tardía = Desastre**

**Script sugerido:**
```
"Analicemos el COMPORTAMIENTO minuto a minuto.

PATRÓN MBA (Fracaso):
Minutos 0-10: Planificación exhaustiva. Discuten diseño óptimo.
'Si ponemos la base así, y usamos triangulación...'
Todo en PAPEL. Malvavisco en la mesa, sin tocar.

Minutos 10-15: Debate. 'No, yo creo que deberíamos...'
Negociación, consenso. Como buen MBA, todo debe estar acordado.

Minutos 15-17: PÁNICO. 'Tenemos 3 minutos!' Construcción frenética.
Los espaguetis se rompen. La cinta no pega bien. Improvisación.

Minuto 18: Con 10 segundos, ponen el malvavisco en la torre.
La torre tambalea... y COLAPSA. 25 cm (si sobrevive), 0 cm (si no).

¿Cuántos ciclos de aprendizaje? UNO. Al final. Cuando no hay tiempo.
"
```

```
"PATRÓN NIÑOS (Éxito):
Minuto 1: '¡Pongamos el malvavisco!' Lo ponen. COLAPSO inmediato.
Risas. 'Ok, eso no funcionó.'

Minutos 2-5: Segunda versión. Usan más base. Colapso más lento.
'Mejor, pero todavía cae.'

Minutos 6-10: Tercera versión. Descubren que la cinta funciona
mejor si la doblan. Torre dura 30 segundos antes de colapsar.
'¡Estamos mejorando!'

Minutos 11-18: Versiones 4, 5, 6. Cada una incorpora lo aprendido.
La final es ESTABLE. 66 cm. No es bonita, pero FUNCIONA.

¿Cuántos ciclos de aprendizaje? 5-6. Todos con el malvavisco incluido.
Cada falla enseñó algo REAL."
```

**La diferencia crítica:**
```
"La diferencia NO es el tiempo total. Ambos tienen 18 minutos.

La diferencia es CUÁNDO aprenden:

MBAs: Aprenden en el minuto 18. No hay tiempo para corregir.
Niños: Aprenden en los minutos 1, 3, 6, 9, 12, 15. Cada vez mejoran.

¿Por qué MBAs hacen esto? Porque les enseñaron:
1. Planificar
2. Ejecutar
3. Validar

En ese orden. Y en proyectos de 18 minutos (o 18 meses), el paso
3 llega cuando YA NO HAY TIEMPO."
```

**Pregunta retórica poderosa:**
> "¿Preferirían fallar 5 veces en los primeros 10 minutos y tener
> 8 minutos para perfeccionar, o planificar perfecto durante 15
> minutos y fallar 1 vez en el minuto 18?"

(La respuesta es obvia cuando se plantea así)

**Tips:**
- Actúa/dramatiza un poco los comportamientos (especialmente el pánico MBA)
- Enfatiza: falla TEMPRANA es BARATA, falla TARDÍA es CARA
- Menciona "fail fast" como mantra de startups - viene de aquí
- Conecta con Agile: sprints cortos = muchos "malvaviscos" tempranos

---

### **Slide 10: Lecciones para Gestión de Proyectos** (10 min)

**Contenido:**
- El Malvavisco = INCERTIDUMBRE OCULTA en proyectos
- Mapeo a fases de proyecto:
  - MBAs planearon todo = Fase de requisitos de 6 meses
  - Pusieron malvavisco al final = Integración/testing al final
  - Suposición falsa = "Sabemos cuánto pesa"
  - Resultado = Descubren problemas cuando NO HAY TIEMPO

**Lección central:**
> Los niños NO son más inteligentes, simplemente NO TIENEN el mal
> hábito de "planificar primero, ejecutar después"

**Puntos clave:**
1. **Probar suposiciones TEMPRANO** es más valioso que planificar perfecto
2. **Tiempo de feedback** es el recurso más valioso
3. **Experiencia puede ser ENEMIGA** si te enseñó método malo

**Script sugerido:**
```
"Ahora la lección CRÍTICA para proyectos reales:

El malvavisco representa la INCERTIDUMBRE OCULTA.

En el experimento: 'No sabemos cuánto pesa el malvavisco.'
En tu proyecto: 'No sabemos si la API responde en tiempo, si la
arquitectura escala, si los usuarios entienden la UI...'

Los MBAs ASUMEN que sus suposiciones son correctas. Planifican
6 meses basados en '200ms de latencia.' Construyen 6 meses.
Mes 12: integran... y la latencia es 2000ms. Proyecto muerto.

Los niños NO asumen nada. Prueban inmediatamente. Si el malvavisco
pesa mucho, lo descubren en 60 segundos, no en 18 minutos.

Traducido a software: Si el API es lento, lo descubres en Sprint 1
(proof of concept), no en Sprint 12 (integración final)."
```

**La lección más incómoda:**
```
"Aquí está la parte incómoda:

Los MBAs tienen más educación, más experiencia, mejores salarios.
Los niños tienen... 5 años.

Pero los NIÑOS ganaron porque NO les enseñaron el método INCORRECTO.

No tienen el hábito de 'analizar exhaustivamente antes de actuar.'
No se sienten mal por fallar públicamente.
No necesitan 'el mejor plan' - necesitan 'un plan que FUNCIONE.'

La experiencia los hizo PEORES, no mejores, porque aprendieron
un método que ignora la incertidumbre."
```

**Conexión con el Cono:**
```
"Recuerdan el Cono de Incertidumbre?

MBAs asumen que están en Fase 4 (±25%) cuando están en Fase 1 (±400%).
Planifican como si supieran todo. Por eso colapsan.

Niños asumen que NO saben nada. Prueban para APRENDER. Por eso
estrechan el cono RÁPIDO, con cada iteración.

El método ágil (Scrum, Kanban) es literalmente 'imitar a los niños':
- Incrementos pequeños
- Feedback rápido
- Aprender haciendo, no planificando"
```

**Pregunta final para reflexión:**
> "¿En qué se parece su proceso actual a los MBAs? ¿En qué a los niños?
> ¿Qué UN CAMBIO podrían hacer para 'poner el malvavisco' más temprano?"

(Deja 30 segundos de silencio para que procesen)

**Tips:**
- Esta es la lección MÁS importante de Clase 1
- Si solo recuerdan UNA cosa: "Prueba suposiciones críticas INMEDIATAMENTE"
- Valida que todos captaron el concepto antes de continuar
- Menciona que post-break veremos OTRO factor psicológico (Parkinson)

---

### **Slide 11: Break** (15 min)

**Contenido:**
- ☕ Break - 15 minutos
- Próximo: Factores Psicológicos (Parkinson y Estudiante)

**Script sugerido:**
```
"Perfecto, es momento del break. 15 minutos.

Hemos visto:
✅ Por qué el 70% de proyectos falla
✅ El Cono de Incertidumbre y sus 5 fases
✅ 16 factores que afectan estimación
✅ Clasificación y matriz de riesgos
✅ La investigación del Malvavisco

Después del break, hablaremos de factores PSICOLÓGICOS que sabotean
estimaciones: la Ley de Parkinson y el Síndrome del Estudiante.
Veremos estudios de Microsoft y MIT que confirman estos patrones.

Nos vemos en 15 minutos. Dejen cámaras apagadas y micrófonos en
mute para descansar."
```

**Durante el break (profesor):**
- Estira, toma agua, descansa ojos
- Revisa chat si hay preguntas acumuladas
- Prepara ejemplos de Parkinson si tienes alguno propio
- Regresa 2 min antes para estar listo

**Al regresar:**
```
"¡Bienvenidos de vuelta! Vamos a retomar con factores psicológicos.
Estos son... incómodos, porque nos aplican a TODOS nosotros.

Pero entenderlos es crucial para estimar mejor."
```

---

## 🎯 Resumen de la Primera Mitad (Pre-Break)

**Conceptos cubiertos:**
1. ✅ 70% de fracaso en estimaciones (problema sistémico)
2. ✅ Estimación ≠ Compromiso (distinción crítica)
3. ✅ Cono de Incertidumbre (±400% → ±10%)
4. ✅ 5 Fases del proyecto (Concepto → Entrega)
5. ✅ Gráfico visual del Cono (asimetría, convergencia)
6. ✅ 16 Factores: Técnicos, Humanos, Entorno
7. ✅ 7 Riesgos clasificados (Crítico/Importante/Menor)
8. ✅ Matriz de Riesgos (Probabilidad × Impacto)
9. ✅ Desafío Malvavisco (MBAs 25cm vs Niños 66cm)
10. ✅ Lección: Probar suposiciones TEMPRANO

**Tiempo usado:** ~90 minutos

**Próximo bloque:** Factores Psicológicos + Estudios Empíricos (85 min)

---

(Continuará en la próxima parte con la segunda mitad de Clase 1...)

## 📌 Notas para el Profesor

### Puntos Críticos de la Primera Mitad:
1. **Slide 7 (Gráfico Cono)** - Pasar mínimo 10 min aquí
2. **Slides 8-10 (Malvavisco)** - Esta es la analogía GOLD del curso
3. **Slide 7d (Matriz Riesgos)** - Herramienta práctica para proyectos reales

### Errores Comunes a Evitar:
- ❌ Culpar a roles específicos (PMs, devs, clientes)
- ❌ Presentar el Cono como "opinión" (son DATOS de 600+ proyectos)
- ❌ Saltar la distinción Estimación vs Plan (todo se confunde después)
- ❌ Apurar el experimento del Malvavisco (es el momento "aha!")

### Si te Quedas Sin Tiempo:
- Prioridad 1: Slides 7, 8-10 (Cono + Malvavisco) - NO NEGOCIABLES
- Prioridad 2: Slides 7b-7d (Factores y Riesgos) - Importantes
- Puedes acortar: Slides 3-4 (Intro, todos conocen el problema)

### Engagement Remoto:
- Pide que usen chat activamente
- Cada 10-15 min, una pregunta al grupo
- Si alguien comparte ejemplo propio, RECONÓCELO verbalmente
- "Gracias María, excelente ejemplo de scope creep"

---

**Próximo documento:** `GUIA_PROFESOR_CLASE1_PARTE2.md` (segunda mitad de Clase 1)
