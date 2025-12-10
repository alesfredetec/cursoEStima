#!/usr/bin/env python3
"""
Script para reorganizar speeches de clase2_profesor.html
Mapea speeches actuales a la numeración correcta según slides HTML
"""

# Mapeo: speech_actual -> speech_nuevo
# Basado en el análisis de slides HTML vs speeches actuales

MAPEO = {
    # 1-11 ya están OK (T-Shirt y Story Points intercambiados manualmente)
    # Solo necesitamos reorganizar del 12 en adelante

    # slide12: Planning Poker Intro - ya está OK en slide12
    12: 12,  # "Planning Poker - Introducción" → mantener

    # slide13 HTML: "Caso de Estudio: Backlog"
    # Actualmente no hay speech específico para esto, el slide13 actual es "Demo HU-3"
    # La demo HU-3 debería ir en slide15 (La Discusión)
    # Por ahora, reusar slide13 actual pero actualizar título
    13: 13,  # Mantener pero renombrar título

    # slide14-24: todos corren normalmente
    14: 14,  # "Proceso Planning Poker"
    15: 15,  # "La Discusión"
    16: 16,  # "Re-votación"
    17: 17,  # "Debriefing"
    18: 18,  # "Velocidad"
    19: 19,  # "Flujo de Refinamiento"
    20: 20,  # "Cuadro Comparativo"
    21: 21,  # "¿Cuándo Usar Cada Método?"
    22: 22,  # "La Pregunta Crítica"
    23: 23,  # "Resumen"
    24: 24,  # "Fin"
}

print("Mapeo de speeches para reorganización:")
print("=" * 50)
for actual, nuevo in sorted(MAPEO.items()):
    if actual == nuevo:
        print(f"slide{actual} → slide{nuevo} (sin cambio)")
    else:
        print(f"slide{actual} → slide{nuevo} (MOVER)")
