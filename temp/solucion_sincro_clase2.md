# SOLUCIÓN SINCRONIZACIÓN CLASE2_PROFESOR.HTML

## CAMBIOS PROPUESTOS

### OPCIÓN RECOMENDADA: Fusionar speeches 4 y 5, eliminar speech 7

#### Cambio 1: slide4 - Mantener solo fórmulas

**Slide HTML 4**: "🧮 Fórmulas PERT"
- Muestra las fórmulas μ y σ

**Speech slide4 actual**: Incluye fórmula + ejemplo autenticación

**Speech slide4 NUEVO**: Solo fórmula y explicación teórica (mover ejemplo a slide5)

#### Cambio 2: slide5 - Fusionar ejemplo + proyectos complejos

**Slide HTML 5**: "💡 Ejemplo Práctico PERT"
- Muestra ejemplo concreto: migración DB (O=5, M=10, P=25)

**Speech slide5 actual**: "PERT en Proyectos Complejos" (concepto de sumar varianzas)

**Speech slide5 NUEVO**:
1. Ejemplo práctico de migración DB (del slide HTML)
2. Transición a proyectos complejos
3. Contenido del speech5 actual (sumar varianzas)
4. Contenido del speech7 actual (tabla de 6 tareas, rutas)

#### Cambio 3: Eliminar slide7 speech

**Speech slide7 actual**: "Combinando PERT y CPM"

**Acción**: Fusionar contenido con slide5 o slide6

#### Cambio 4: Re-numerar speeches del 8 en adelante

Después de eliminar slide7, todos los speeches del 8 al 24 bajan un número:
- slide8 → slide7
- slide9 → slide8
- ...
- slide24 → slide23

### RESULTADO FINAL

- **23 Slides HTML** (sin cambios)
- **23 Speeches** (eliminando slide7 y re-numerando)
- **Sincronización perfecta**

## IMPLEMENTACIÓN

### Paso 1: Actualizar speech slide4

Reducir el speech para que NO incluya ejemplo de autenticación (moverlo a slide5).

### Paso 2: Actualizar speech slide5

Crear un speech largo que cubra:
1. Ejemplo práctico migración DB (del HTML)
2. Concepto de PERT en proyectos complejos (del speech5 actual)
3. Ejemplo de 6 tareas con rutas (del speech7 actual)

### Paso 3: Eliminar speech slide7

Borrar completamente la entrada "slide7" del objeto speechDataClase2.

### Paso 4: Re-numerar del slide8 al slide24

Renombrar todas las keys:
- "slide8" → "slide7"
- "slide9" → "slide8"
- "slide10" → "slide9"
- ...
- "slide24" → "slide23"

### Paso 5: Verificar JavaScript de navegación

Asegurar que el código que genera el slideKey sea:
```javascript
const slideKey = `slide${currentSlide + 1}`;
```

Esto mapea:
- currentSlide = 0 → slide1
- currentSlide = 1 → slide2
- ...
- currentSlide = 22 → slide23

## ALTERNATIVA MÁS SIMPLE

Si no querés re-numerar todo, otra opción es:

### Dejar slide7 como placeholder

Convertir speech slide7 en un speech MUY CORTO que diga:

```javascript
"slide7": {
    "title": "Transición",
    "duration": "30 seg",
    "script": "[Transición entre conceptos - avanzar al siguiente slide]"
},
```

Y ajustar el HTML para agregar un slide de transición en la posición 7.

**PERO ESTO NO ES RECOMENDADO** porque agrega un slide innecesario.

## DECISIÓN FINAL

**Recomiendo la OPCIÓN 1**: Fusionar contenidos y re-numerar.

Es más trabajo inicial pero deja el código limpio y mantenible.

¿Procedo con la implementación?
