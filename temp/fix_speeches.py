#!/usr/bin/env python3
"""
Script para reorganizar speeches del 12 al 24
Inserta nuevo slide12 (Break) y mueve todos los demás +1
"""

import re
import sys

def main():
    with open('clase2_profesor.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Backup
    with open('clase2_profesor.html.before_speech_reorg', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Backup creado: clase2_profesor.html.before_speech_reorg")

    # Paso 1: Renombrar speeches del 24 al 13 (en orden inverso para evitar colisiones)
    # slide24 -> slide25 (temporal)
    # slide23 -> slide24
    # ...
    # slide12 -> slide13

    replacements = []
    for i in range(24, 11, -1):
        old_key = f'"slide{i}":'
        new_key = f'"slide{i+1}":'
        content = content.replace(old_key, new_key, 1)
        replacements.append(f"slide{i} -> slide{i+1}")

    print(f"\\nRenombrados {len(replacements)} speeches:")
    for r in replacements[:3]:
        print(f"  {r}")
    print(f"  ...")

    # Paso 2: Insertar nuevo slide12 (Break)
    new_slide12 = '''            "slide12": {
                        "title": "Break - Preguntas",
                        "duration": "2 min",
                        "script": "Tomemos un break de 15 minutos.\\n\\n[PAUSA]\\n\\nSi tienen preguntas sobre PERT, CPM, Story Points, Fibonacci, o T-Shirt Sizing, ahora es el momento.\\n\\n[PAUSA - responder preguntas si hay]\\n\\nCuando volvamos, vamos a hacer algo práctico:\\n\\n**Taller de Planning Poker**.\\n\\nVan a ver cómo un equipo REAL estima una historia.\\n\\nVan a ver la DISCUSIÓN que genera consenso.\\n\\nVan a ver cómo suposiciones ocultas salen a la luz.\\n\\n[ÉNFASIS]\\n\\nEste es el **corazón pedagógico** de Clase 2.\\n\\nNos vemos en 15 minutos.\\""
            },
'''

    # Buscar dónde insertar (después de slide11)
    pattern = r'("slide11":\s*\{[\s\S]*?\n\s+\},)'
    match = re.search(pattern, content)

    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + '\\n' + new_slide12 + content[insert_pos:]
        print("\\nInsertado nuevo slide12 (Break)")
    else:
        print("ERROR: No se encontró slide11 para insertar después")
        return 1

    # Paso 3: Eliminar slide25 (que antes era slide24 y ahora está duplicado)
    # En realidad no hay slide25, así que esto está OK

    # Guardar
    with open('clase2_profesor.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("\\nArchivo actualizado: clase2_profesor.html")
    print("\\nVerificar con: grep -c '\"slide[0-9]*\":' clase2_profesor.html")

    return 0

if __name__ == '__main__':
    sys.exit(main())
