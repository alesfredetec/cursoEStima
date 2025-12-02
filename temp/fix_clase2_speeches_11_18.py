import re
import json

# Read clase2_profesor.html
with open('C:/tmp/cursoEStima/clase2_profesor.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New corrected speeches for slides 11-18
corrected_speeches = {
    "slide11": {
        "title": "Break - Preguntas y Transición",
        "duration": "2 min",
        "script": """Tomemos un break de 15 minutos.

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

Nos vemos en 15 minutos."""
    },
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
    }
}

print("="*80)
print("FIX SPEECHES: clase2_profesor.html (slides 11-12)")
print("="*80)

# Find and replace slide11
# Look for the pattern: "slide11": { ... },
pattern_slide11 = r'("slide11":\s*\{[^}]+?"title":\s*"[^"]*",\s*"duration":\s*"[^"]*",\s*"script":\s*"(?:[^"\\]|\\.)*"\s*\})'

# Find current slide11
match11 = re.search(pattern_slide11, content, re.DOTALL)
if match11:
    old_speech11 = match11.group(1)
    print(f"\n✓ Found slide11 speech (length: {len(old_speech11)} chars)")

    # Create new speech11
    new_speech11 = f'"slide11": {{\n                        "title": "{corrected_speeches["slide11"]["title"]}",\n                        "duration": "{corrected_speeches["slide11"]["duration"]}",\n                        "script": "{corrected_speeches["slide11"]["script"]}"\n            }}'

    # Replace
    content = content.replace(old_speech11, new_speech11, 1)
    print("✓ Replaced slide11 with corrected version")
else:
    print("✗ Could not find slide11")

# Save corrected file
output_path = 'C:/tmp/cursoEStima/clase2_profesor_FIXED.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Saved corrected file to: {output_path}")
print("\nPlease review the file and if correct, rename it to clase2_profesor.html")
