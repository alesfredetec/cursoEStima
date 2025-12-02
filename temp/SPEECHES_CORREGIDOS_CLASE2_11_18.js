// SPEECHES CORREGIDOS para clase2_profesor.html
// Slides 11-18 sincronizados con HTML correcto

"slide11": {
    "title": "Break - Preguntas y Transición",
    "duration": "2 min",
    "script": `Tomemos un break de 15 minutos.

[PAUSA]

Si tienen preguntas sobre PERT, CPM, Story Points, o T-Shirt Sizing, ahora es el momento.

[PAUSA - responder preguntas si hay]

Cuando volvamos, vamos a hacer algo práctico:

**Taller de Planning Poker**.

Van a ver cómo un equipo REAL estima una historia.

Van a ver la DISCUSIÓN que genera consenso.

Van a ver cómo suposiciones ocultas salen a la luz.

[ÉNFASIS]

Este es el **corazón pedagógico** de Clase 2.

Nos vemos en 15 minutos.`
},

"slide12": {
    "title": "Planning Poker - Marco Teórico",
    "duration": "12 min",
    "script": `Bienvenidos de vuelta.

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

Al final comparamos.`
},

"slide13": {
    "title": "Caso de Estudio - Backlog de Autenticación",
    "duration": "10 min",
    "script": `Aquí está nuestro caso: **Sistema de Autenticación**.

[LEER TABLA en pantalla]

Tenemos 5 Historias de Usuario (HU):

**HU-1: Login básico** - Ya estimado: **2 puntos**
**HU-2: Registro de usuarios** - Ya estimado: **3 puntos** ← BASELINE
**HU-3: Password reset** - **SIN ESTIMAR ← Este lo haremos**
**HU-4: Reporte de usuarios registrados** - Sin estimar
**HU-5: Pago con tarjeta de crédito** - Sin estimar

[CONTEXTO]

El equipo ya completó HU-1 y HU-2 en sprint anterior.

Ahora en Sprint Planning están estimando las siguientes.

**HU-2 es el BASELINE:**

'Registro de usuarios' (form con nombre, email, password, validaciones, endpoint POST, hash, email confirmación) = **3 puntos**.

[ÉNFASIS]

Todos los miembros del equipo conocen HU-2 a fondo.
Lo completaron hace 5 días.
Tomó ~8 horas reales de trabajo (pero NO decimos 3pts = 8hs).

Es el **punto de comparación** para el resto.

[PAUSA]

Ahora van a estimar **HU-3: Password Reset**.

[LEER HU-3 completa]

**Como** usuario que olvidó su contraseña,
**Quiero** poder solicitar un enlace de reseteo por email,
**Para** recuperar el acceso.

[PAUSA - Dejar que procesen]

Antes de ver la estimación del equipo...

**Pregunta para ustedes:**

**¿Cuántos puntos asignarían?**

[DAR 30 SEGUNDOS]

Opciones: 1, 2, 3, 5, 8, 13...

Recuerden: HU-2 (Registro) = 3 puntos.

¿Password Reset es más simple, igual, o más complejo que Registro?

[TRANSICIÓN]

Veamos el proceso paso a paso...`
},

"slide14": {
    "title": "Proceso Planning Poker - Paso a Paso",
    "duration": "8 min",
    "script": `OK, el equipo está listo para estimar HU-3 (Password Reset).

[VER SLIDE con 4 pasos]

**Paso 1: Establecer Línea Base**

Product Owner dice:

'Recordemos: HU-2 (Login básico) fue 3 puntos.
Form, validaciones, endpoint, hash, email.
Todos lo completamos hace 5 días.
Eso es nuestro 3.'

Equipo asiente. Todos recuerdan HU-2.

[PAUSA]

**Paso 2: Presentar Historia**

PO lee HU-3:

'Como usuario que olvidó su contraseña,
Quiero solicitar enlace de reseteo por email,
Para recuperar el acceso.'

PO explica:
- Usuario hace click en 'Olvidé mi contraseña'
- Ingresa email
- Sistema envía email con enlace temporal
- Usuario resetea contraseña

[PAUSA]

**Paso 3: Clarificar Dudas**

Dev pregunta: '¿El enlace caduca?'
PO: 'Sí, 1 hora.'

Tester pregunta: '¿Se valida que el email existe?'
PO: 'Sí, pero NO decimos si existe o no (seguridad).'

Arquitecto pregunta: '¿Cuántos tokens simultáneos puede tener un usuario?'
PO: 'Mmm... buena pregunta. Supongo que 1. Si pide otro, invalida el anterior.'

[PAUSA]

**Paso 4: Votar Simultáneamente**

Facilitador (Scrum Master):

'OK, todos claros? Vamos a votar.

Piensen: ¿HU-3 es más simple, igual, o más complejo que HU-2 (3 pts)?

Elijan carta. Boca abajo.

[PAUSA]

Listos?

3... 2... 1...

**¡REVELAR!**'

[PAUSA DRAMÁTICA]

Veamos qué pasó...`
},

"slide15": {
    "title": "La Discusión - El Corazón del Taller",
    "duration": "10 min",
    "script": `Todos revelan cartas simultáneamente.

[VER SLIDE]

**Resultado:**

- 3
- 5
- 5
- 8
- 13

[REACCIÓN]

ENORME dispersión.

Diferencia de **4.3x** entre extremos (3 vs 13).

[PAUSA]

**Facilitador NO promedia.**

NO dice: 'OK, el promedio es 7, pongamos 8.'

[ÉNFASIS]

El facilitador pide a los **EXTREMOS** que justifiquen.

[LEER DIÁLOGO del slide]

**Facilitador al que votó 13 (rojo):**

'¿Qué riesgo o complejidad ve que los demás no vieron?'

**Respuesta (votó 13):**

'Esto implica:
- Enviar email
- Generar token ÚNICO
- Almacenar token en DB (tabla nueva?)
- Validar expiración
- Construir página de reseteo

Hay mucha incertidumbre. No sabemos si tenemos servicio de email configurado.
No sabemos cómo generar tokens seguros.
Token temporal significa tabla nueva o campo en users.

Por eso: **13 puntos**.'

[PAUSA LARGA]

**Facilitador al que votó 3 (verde):**

'¿Por qué piensa que es igual de simple que el login?'

**Respuesta (votó 3):**

'Ah... no había pensado en la generación del token.
Ni en el servicio de email.
Solo pensé en el formulario: ingresar email, validar, enviar.

Asumí que el backend ya tenía email y tokens.

[PAUSA]

Ahora que escucho al que votó 13... veo que hay más complejidad.'

[ÉNFASIS - LA MAGIA]

**Esto es lo VALIOSO.**

Las suposiciones ocultas salieron a la luz:
- Uno asumió infraestructura lista
- Otro vio todo lo que falta

Ahora **TODOS** entienden el alcance real.

[TRANSICIÓN]

Segunda ronda...`
},

"slide16": {
    "title": "Re-votación y Consenso",
    "duration": "7 min",
    "script": `Después de la discusión, el facilitador dice:

[VER SLIDE]

'OK, hemos **APRENDIDO** algo. Volvamos a votar.'

[PAUSA]

**Segunda ronda:**

Todos votan de nuevo, con nueva información.

[REVELAR]

**Resultado:**

- 5
- 5
- 5
- 8
- 8

[ANÁLISIS]

**¡Convergencia!**

Primera ronda: 3 a 13 (dispersión enorme)
Segunda ronda: 5 a 8 (rango aceptable: ±1 Fibonacci)

[DECISIÓN]

Facilitador:

'OK, tenemos 3 votos en 5, y 2 votos en 8.

¿Los que votaron 8, pueden aceptar 5?
¿O hay algo crítico que necesitamos considerar?'

**Respuesta (votó 8):**

'Mi 8 era por incertidumbre en email.
Pero si asumimos que el servicio de email está configurado, puedo aceptar 5.'

[CONSENSO]

**HU-3: Password Reset = 5 puntos**

[PAUSA]

**IMPORTANTE:**

El número (5) NO es lo más valioso.

Lo valioso fue:
1. **Exposición de suposiciones** (servicio de email, tokens)
2. **Identificación de riesgos** (tabla nueva, seguridad)
3. **Alineación del equipo** (todos entienden alcance)
4. **Decisión de qué investigar** (configurar email antes de sprint)

[ÉNFASIS]

El equipo ahora sabe que antes de HU-3, deben:
- Verificar servicio de email
- Decidir estrategia de tokens
- Diseñar tabla de reset_tokens

[TRANSICIÓN]

Veamos las lecciones clave...`
},

"slide17": {
    "title": "Debriefing - Lecciones del Planning Poker",
    "duration": "8 min",
    "script": `Debriefing: ¿Qué aprendimos?

[VER SLIDE]

[ÉNFASIS CENTRAL]

**El objetivo NO era el número (el 5).**

El objetivo era la **CONVERSACIÓN que ocurrió entre el 13 y el 3**.

[PAUSA LARGA]

Esa conversación expuso:
- Suposiciones ocultas
- Riesgos no considerados
- Complejidades técnicas
- Dependencias externas

[LEER LECCIONES del slide]

**¿Por qué funciona Planning Poker?**

**1. Votación anónima y simultánea:**
   - Previene anclaje
   - Junior no copia a senior
   - Todos piensan independientemente

**2. Exposición de suposiciones:**
   - El '13' vio el riesgo del token
   - El '3' asumió infraestructura lista
   - La discusión alineó entendimiento

**3. Identificación temprana de riesgos:**
   - Descubrimos complejidades ANTES de codear
   - Mejor momento para decidir: ¿dividir historia? ¿investigar primero?

**4. Construcción de consenso:**
   - TODO el equipo entiende
   - TODO el equipo acuerda
   - Ownership distribuido

**5. Aprendizaje colectivo:**
   - Conocimiento se distribuye
   - Junior aprende de senior
   - Tester aprende de dev, dev aprende de tester

[CONECTAR con Clase 1]

¿Recuerdan el Uncertainty Cone?

±400% al inicio, ±10% al final.

Planning Poker es **reducción activa de incertidumbre**:
- Primera votación: alta dispersión (incertidumbre)
- Discusión: reducción de incertidumbre
- Segunda votación: convergencia (certeza)

[ANALOGÍA]

Es como el Marshmallow Challenge:

Niños iteraban → construían → aprendían → ajustaban.

Planning Poker:
Estimaban → discutían → aprendían → re-estimaban.

**Ambos usan FEEDBACK para reducir incertidumbre.**

[PREGUNTA RETÓRICA]

'OK, tenemos Story Points. ¿Cómo los convertimos en FECHAS?'

[RESPUESTA]

Con **Velocidad**.

Veamos...`
},

"slide18": {
    "title": "Velocidad - De Points a Forecasting",
    "duration": "12 min",
    "script": `Una vez que el equipo estima en Story Points, puede calcular su **VELOCIDAD**.

[VER SLIDE]

**¿Qué es Velocidad?**

Cantidad de Story Points que el equipo **completa por Sprint**.

[EJEMPLO en slide]

Sprint 1: 23 puntos completados
Sprint 2: 27 puntos completados
Sprint 3: 25 puntos completados

**Velocidad promedio: 25 puntos/sprint**

[ÉNFASIS]

Velocidad NO es estimación. Es **MEDICIÓN**.

Es dato empírico: 'Este equipo, en este contexto, completa ~25 pts cada 2 semanas.'

[PAUSA]

**¿Por qué es importante?**

Porque ahora podemos hacer **FORECASTING**.

[EJEMPLO]

**Situación:**

Backlog tiene 120 Story Points.
Equipo tiene velocidad de 25 pts/sprint.
Sprints son de 2 semanas.

**Cálculo:**

120 pts ÷ 25 pts/sprint = **4.8 sprints**

≈ **5 sprints**

5 sprints × 2 semanas = **10 semanas**

[PAUSA]

**Respuesta al stakeholder:**

'Basado en velocidad histórica, estimamos ~10 semanas.'

[ÉNFASIS - HONESTIDAD]

NO decimos: 'Lo termino en 10 semanas.'

Decimos: 'Basado en datos, proyectamos 10 semanas ±20%.'

[BENEFICIOS de Velocidad]

**1. Forecast empírico:**
   - No adivinar
   - Usar datos reales

**2. Comunicación con stakeholders:**
   - Lenguaje compartido
   - Expectativas realistas

**3. Detección de anomalías:**
   - Si velocidad cae de 25 a 15: ¿qué pasó?
   - Impedimentos, ausentismo, deuda técnica

**4. Mejora continua:**
   - Velocidad aumenta → mejoras funcionan
   - Velocidad baja → investigar causas

[ADVERTENCIAS]

❌ **NO comparar velocidades entre equipos**
   - Equipo A: 40 pts/sprint
   - Equipo B: 25 pts/sprint
   - NO significa A es mejor. Cada equipo tiene su baseline.

❌ **NO usar velocidad como KPI de performance**
   - Presionar para aumentar velocidad → inflación de puntos
   - 'Ahora Login es 5 pts en vez de 3' (misma complejidad, diferente número)

❌ **NO calcular velocidad con menos de 3 sprints**
   - Sprint 1: 15 (aprendiendo)
   - Sprint 2: 28 (pico)
   - Sprint 3: 24 (estable)
   - Promedio estable después de 3-5 sprints

[TRANSICIÓN]

OK, ahora sabemos:
- PERT/CPM: estimación en tiempo
- Story Points: estimación en complejidad relativa
- Planning Poker: consenso colaborativo
- Velocidad: forecast empírico

¿Cómo estos métodos se relacionan?

Veamos un flujo de refinamiento progresivo...`
}
