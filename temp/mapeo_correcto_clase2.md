# MAPEO CORRECTO CLASE2_PROFESOR.HTML

## PROBLEMA ENCONTRADO

Los **comentarios HTML** están mal numerados desde el slide 8 (segundo) en adelante.

## ORDEN CORRECTO DE SLIDES HTML (por h2)

| # Real | Comentario HTML | h2 Title | Speech Title (actual) | Correcto? |
|--------|-----------------|----------|----------------------|-----------|
| 1 | Slide 1: Portada | Tradicionales y Ágiles | Portada | ✓ |
| 2 | Slide 2: Agenda | Agenda de la Clase | Agenda | ✓ |
| 3 | Slide 3: Intro PERT | PERT: Estimación de 3 Puntos | Introducción a PERT | ✓ |
| 4 | Slide 4: Fórmulas PERT | Fórmulas PERT | Fórmula PERT | ✓ |
| 5 | Slide 5: Ejemplo PERT | Ejemplo Práctico PERT | PERT en Proyectos Complejos | ⚠️ Revisar contenido |
| 6 | Slide 6: CPM Introducción | CPM: Critical Path Method | CPM - Critical Path Method | ✓ |
| 7 | Slide 7: Combinando PERT y CPM | Combinando PERT y CPM | Combinando PERT y CPM | ✓ NUEVO |
| 8 | Slide 8: Estimación Ágil Intro | Estimación Ágil: El Cambio | Introducción a Estimación Ágil | ✓ |
| 9 | **Slide 8** (ERROR): T-Shirt Sizing | Técnica 1: T-Shirt Sizing | **Story Points y Escala Fibonacci** | ✗ MAL |
| 10 | Slide 9: Story Points | Técnica 2: Story Points | **T-Shirt Sizing** | ✗ INVERTIDO |
| 11 | Slide 10: Fibonacci | La Secuencia de Fibonacci | **Break - Preguntas** | ✗ MAL |
| 12 | Slide 11: Break | Preguntas ? | **Planning Poker - Intro** | ✗ MAL |
| 13 | Slide 12: Planning Poker Intro | Planning Poker | **Demo HU-3** | ✗ MAL |
| 14 | Slide 13: Caso de Estudio | Caso de Estudio: Backlog | **Proceso Planning Poker** | ✗ MAL |
| 15 | Slide 14: Proceso Planning Poker | Proceso de Planning Poker | **La Discusión** | ✗ MAL |
| 16 | Slide 15: El Corazón del Taller | La Discusión: El Corazón | **Re-votación** | ✗ MAL |
| 17 | Slide 16: Re-votación | Re-votación y Consenso | **Debriefing** | ✗ MAL |
| 18 | Slide 17: Debriefing | Debriefing: Lecciones | **Velocidad** | ✗ MAL |
| 19 | Slide 18: Velocidad | Velocidad: De Points | **Flujo de Refinamiento** | ✗ MAL |
| 20 | Slide 19: Flujo de Refinamiento | Flujo de Refinamiento | **Cuadro Comparativo** | ✗ MAL |
| 21 | Slide 20: Tabla Comparativa | Cuadro Comparativo | **¿Cuándo Usar Cada Método?** | ✗ MAL |
| 22 | Slide 21: ¿Cuándo usar qué? | ¿Cuándo Usar Cada Método? | **La Pregunta Crítica** | ✗ MAL |
| 23 | Slide 22: Gancho Clase 3 | La Pregunta Crítica (Reprise) | **Resumen de la Clase 2** | ✗ MAL |
| 24 | Slide 23: Resumen Clase 2 | Resumen de la Clase 2 | **Fin de la Clase 2** | ✗ MAL |
| 25? | Slide 24: Fin | ¡Fin de la Clase 2! | (ninguno - slide24 tiene otro speech) | ✗ |

## ANÁLISIS

### Problema 1: Slides 9 y 10 invertidos

**HTML**:
- Slide 9: T-Shirt Sizing
- Slide 10: Story Points

**Speeches**:
- slide9: Story Points y Escala Fibonacci
- slide10: T-Shirt Sizing

**Solución**: Intercambiar speeches slide9 y slide10

### Problema 2: Todo descorrido desde slide 11

Todos los slides del 11 al 24 están corridos en 1 posición.

**Causa**: Hay 25 divs con class="slide" pero solo 24 speeches.

Déjame contar los divs exactos...

## VERIFICACIÓN NECESARIA

1. Contar exactamente cuántos `<div class="slide">` existen
2. Ver si el último slide (Fin) necesita speech
3. Reorganizar speeches para que coincidan con el orden HTML correcto

## SOLUCIÓN RECOMENDADA

### Paso 1: Corregir comentarios HTML
Los comentarios "Slide 8" duplicado debe ser "Slide 9", etc.

### Paso 2: Reorganizar speeches
Crear un nuevo orden de speeches que siga el orden HTML real:

```
slide9: T-Shirt Sizing (actualmente está en slide10)
slide10: Story Points y Fibonacci (actualmente está en slide9, fusionar con slide11)
slide11: Break (actualmente está en slide11)
slide12: Planning Poker Intro (actualmente está en slide12)
...
```

### Paso 3: Verificar slide final
Confirmar si slide 24 "Fin" necesita speech o no.
