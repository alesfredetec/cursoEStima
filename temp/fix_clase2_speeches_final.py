#!/usr/bin/env python3
"""
Fix clase2_profesor.html speeches synchronization (slides 12-18)
"""

import re
import shutil

# Backup original file
shutil.copy('C:/tmp/cursoEStima/clase2_profesor.html',
            'C:/tmp/cursoEStima/clase2_profesor.html.backup_before_fix')

# Read file
with open('C:/tmp/cursoEStima/clase2_profesor.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Corrected speeches for slides 12-18
corrected_speeches = {
    "slide12": {
        "title": "Planning Poker - Introducción y Marco Teórico",
        "duration": "12 min",
        "script": """Bienvenidos de vuelta.

Ahora: **Planning Poker**.

[PAUSA]

Planning Poker es el método COLABORATIVO por excelencia para asignar Story Points.

[VER SLIDE - Objetivo Central]

El objetivo NO es obtener un número exacto.

Es generar **CONSENSO** basado en **DISCUSIÓN** y exposición de **SUPOSICIONES OCULTAS**.

[ELEMENTOS en slide]

**Elementos Clave del Proceso:**

1. **Votación simultánea y anónima** (evita anclaje)
2. **Discusión de estimaciones extremas** (identifica riesgos)
3. **Re-votación hasta consenso** (alineación del equipo)
4. **Compromiso compartido** (ownership distribuido)

[PAUSA]

¿Por qué votación anónima?

Porque previene el **efecto ancla**.

Si el arquitecto senior dice '8' primero, todos dicen 8.

Con cartas boca abajo, cada uno piensa independientemente.

[EJEMPLO]

Si en una sala hay 5 personas y todas votan diferente: 2, 3, 5, 8, 13...

¿Están mal 4 de ellas?

[PAUSA]

NO. Cada una tiene **suposiciones diferentes**.

Y esas suposiciones necesitan salir a la luz.

[TRANSICIÓN]

Veamos un caso real..."""
    },

    "slide13": {
        "title": "Caso de Estudio - Backlog de Autenticación",
        "duration": "10 min",
        "script": """Aquí está nuestro caso: **Sistema de Autenticación**.

[LEER TABLA en pantalla]

Tenemos 5 Historias de Usuario (HU):

**HU-1: Login básico** - Ya estimado: **2 puntos**
**HU-2: Registro de usuarios** - Ya estimado: **3 puntos** ← BASELINE
**HU-3: Password reset** - **SIN ESTIMAR ← Este lo haremos**
**HU-4: Reporte de usuarios** - Sin estimar
**HU-5: Pago con tarjeta** - Sin estimar

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

Veamos el proceso paso a paso..."""
    },

    "slide14": {
        "title": "Proceso Planning Poker - Paso a Paso",
        "duration": "8 min",
        "script": """OK, el equipo está listo para estimar HU-3 (Password Reset).

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

Veamos qué pasó..."""
    },

    "slide15": {
        "title": "La Discusión - El Corazón del Taller",
        "duration": "10 min",
        "script": """Todos revelan cartas simultáneamente.

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

Segunda ronda..."""
    },

    "slide16": {
        "title": "Re-votación y Consenso",
        "duration": "7 min",
        "script": """Después de la discusión, el facilitador dice:

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

Veamos las lecciones clave..."""
    },

    "slide17": {
        "title": "Debriefing - Lecciones del Planning Poker",
        "duration": "8 min",
        "script": """Debriefing: ¿Qué aprendimos?

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

Veamos..."""
    },

    "slide18": {
        "title": "Velocidad - De Points a Forecasting",
        "duration": "12 min",
        "script": """Una vez que el equipo estima en Story Points, puede calcular su **VELOCIDAD**.

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

Veamos un flujo de refinamiento progresivo..."""
    }
}

print("Reemplazando speeches 12-18...")
print("="*80)

# Function to escape special regex characters
def escape_for_regex(text):
    # Escape special regex chars but keep newlines
    special_chars = ['.', '^', '$', '*', '+', '?', '{', '}', '[', ']', '(', ')', '|', '\\']
    for char in special_chars:
        text = text.replace(char, '\\' + char)
    return text

# Replace each speech
for slide_key in ["slide12", "slide13", "slide14", "slide15", "slide16", "slide17", "slide18"]:
    print(f"\nProcessing {slide_key}...")

    # Find the current speech block
    pattern = rf'"{slide_key}":\s*\{{\s*"title":\s*"[^"]+",\s*"duration":\s*"[^"]+",\s*"script":\s*"[^"]*?"(?:[^"\\]|\\.)*?"\s*\}}'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        old_block = match.group(0)

        # Create new block
        new_speech = corrected_speeches[slide_key]
        # Escape script content for JSON
        script_escaped = new_speech['script'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

        new_block = f'"{slide_key}": {{\n                        "title": "{new_speech["title"]}",\n                        "duration": "{new_speech["duration"]}",\n                        "script": "{script_escaped}"\n            }}'

        # Replace in content
        content = content.replace(old_block, new_block, 1)
        print(f"  OK Replaced {slide_key}: {new_speech['title']}")
    else:
        print(f"  ERROR Could not find {slide_key}")

# Write corrected file
with open('C:/tmp/cursoEStima/clase2_profesor.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "="*80)
print("OK Archivo actualizado: clase2_profesor.html")
print("OK Backup creado: clase2_profesor.html.backup_before_fix")
print("\nVerificando...")

# Verify
speeches_check = re.findall(r'"(slide1[2-8])":\s*\{\s*"title":\s*"([^"]+)"', content)
print("\nSPEECHES ACTUALIZADOS:")
for num, title in speeches_check:
    print(f"  {num}: {title}")

print("\nOK Proceso completado!")
