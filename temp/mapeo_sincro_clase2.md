# SINCRONIZACIÓN CLASE2_PROFESOR.HTML

## DIAGNÓSTICO

**23 slides HTML** pero **24 speeches** → Desbalance de 1 speech extra

## MAPEO COMPLETO

| # | Slide HTML (h2) | Speech Title | Sincronizado? |
|---|-----------------|--------------|---------------|
| 1 | Tradicionales y Ágiles | Portada | ✓ OK (mismo contenido) |
| 2 | Agenda de la Clase | Agenda | ✓ OK |
| 3 | PERT: Estimación de 3 Puntos | Introducción a PERT | ✓ OK |
| 4 | Fórmulas PERT | Fórmula PERT | ✓ OK |
| 5 | Ejemplo Práctico PERT | PERT en Proyectos Complejos | ⚠️ PROBLEMA |
| 6 | CPM: Critical Path Method | CPM - Critical Path Method | ⚠️ CORRIDO |
| 7 | Estimación Ágil: El Cambio de Paradigma | Combinando PERT y CPM | ✗ CORRIDO |
| 8 | Técnica 1: T-Shirt Sizing | Introducción a Estimación Ágil | ✗ CORRIDO |
| 9 | Técnica 2: Story Points | Story Points y Escala Fibonacci | ✗ CORRIDO |
| 10 | La Secuencia de Fibonacci | T-Shirt Sizing | ✗ CORRIDO |
| 11 | Preguntas ? (break) | Break - Preguntas y Transición | ✓ OK |
| 12 | Planning Poker | Planning Poker - Introducción y Marco Teórico | ✓ OK |
| 13 | Caso de Estudio: Backlog de Autenticación | Demostración - Historia HU-3 (Password Reset) | ✗ CORRIDO |
| 14 | Proceso de Planning Poker (Paso a Paso) | Proceso Planning Poker - Paso a Paso | ✓ OK |
| 15 | La Discusión: El Corazón del Taller | La Discusión - El Corazón del Taller | ✓ OK |
| 16 | Re-votación y Consenso | Re-votación y Consenso | ✓ OK |
| 17 | Debriefing: Lecciones del Planning Poker | Debriefing - Lecciones del Planning Poker | ✓ OK |
| 18 | Velocidad: De Points a Forecasting | Velocidad - De Points a Forecasting | ✓ OK |
| 19 | Flujo de Refinamiento Progresivo | Flujo de Refinamiento Progresivo | ✓ OK |
| 20 | Cuadro Comparativo de Métodos | Cuadro Comparativo de Métodos | ✓ OK |
| 21 | ¿Cuándo Usar Cada Método? | ¿Cuándo Usar Cada Método? | ✓ OK |
| 22 | La Pregunta Crítica (Reprise) | La Pregunta Crítica (Reprise) | ✓ OK |
| 23 | Resumen de la Clase 2 | Resumen de la Clase 2 | ✓ OK |
| 24 | ¡Fin de la Clase 2! | Fin de la Clase 2 | ⚠️ Slide existe pero no tiene speech asignado |

## PROBLEMAS IDENTIFICADOS

### Problema Principal: Slide 5

**Slide HTML #5**: "💡 Ejemplo Práctico PERT"
- Debería tener un speech sobre un ejemplo práctico de PERT

**Speech slide5**: "PERT en Proyectos Complejos"
- Este contenido parece ser DISTINTO a "Ejemplo Práctico"

**Speech slide7**: "Combinando PERT y CPM"
- Este speech NO tiene slide HTML correspondiente

### Hipótesis:

Parece que **falta el slide HTML** entre slide 4 y 6, o que los speeches 5-7 están mal organizados.

**Opciones:**

1. **Crear slide HTML nuevo** entre slide 4 y 5 para "PERT en Proyectos Complejos"
2. **Eliminar speech slide7** "Combinando PERT y CPM" si no es necesario
3. **Re-organizar speeches** para que coincidan con los slides existentes

### Problema Secundario: Slides 7-10

Están completamente descorrados porque el problema del slide 5 empuja todo.

### Problema Terciario: Slide 13

**Slide HTML #13**: "Caso de Estudio: Backlog de Autenticación"
**Speech slide13**: "Demostración - Historia HU-3 (Password Reset)"

Estos son DIFERENTES momentos:
- Slide 13 HTML debería presentar el backlog completo
- Speech slide13 habla de una historia específica (HU-3)

Parece que falta un slide HTML para el backlog.

## SOLUCIÓN PROPUESTA

### Opción A: Agregar Slides HTML Faltantes

Agregar 2 slides HTML:
1. Entre slide 4 y 5: "PERT en Proyectos Complejos"
2. Entre slide 5 y 6: "Combinando PERT y CPM"

Esto balancea a 25 slides HTML y 24 speeches.

### Opción B: Reorganizar Speeches (RECOMENDADO)

Fusionar contenido de speeches para que coincida con los 23 slides existentes:

- slide5: Combinar "PERT en Proyectos Complejos" + "Combinando PERT y CPM" en un solo speech "Ejemplo Práctico PERT"
- slide13: Agregar introducción del backlog al speech de HU-3

Esto mantiene 23 slides HTML y ajusta a 23 speeches.

### Opción C: Eliminar Speech Extra

Eliminar slide7 "Combinando PERT y CPM" y ajustar el resto.

## RECOMENDACIÓN

**Opción B** es la más limpia porque:
1. No requiere modificar HTML (más estable)
2. Solo ajusta speeches (más fácil)
3. Mantiene la estructura del curso intacta
