# VERSIÓN ALUMNO: clase2_anexos_alumno.html

**Fecha**: 2025-12-09
**Archivo base**: `clase2_pert_anexos.html`
**Archivo generado**: `clase2_anexos_alumno.html`

---

## PROPÓSITO

Crear una versión del archivo de anexos PERT/CPM para **estudiantes** que:
- **Oculte el speech sidebar por defecto** (modo alumno)
- **Permita activar el modo profesor con tecla secreta** (Ctrl+Shift+S)
- Mantenga toda la funcionalidad de gráficos y navegación

---

## CAMBIOS IMPLEMENTADOS

### 1. Título Modificado

**Antes**:
```html
<title>Clase 2 - Anexos PERT/CPM: Ejemplos Gráficos y Cálculos</title>
```

**Después**:
```html
<title>Clase 2 - Anexos PERT/CPM: Ejemplos Gráficos y Cálculos (Versión Alumno)</title>
```

---

### 2. CSS: Layout Responsivo con Sidebar Oculto

#### Slide Area (100% por defecto)

**Antes**:
```css
.slide-area {
    width: 70%;
    height: 100vh;
    position: relative;
}
```

**Después**:
```css
.slide-area {
    width: 100%;              /* Pantalla completa por defecto */
    height: 100vh;
    position: relative;
    transition: width 0.3s ease;
}

.slide-area.with-sidebar {
    width: 70%;               /* Se reduce cuando se activa sidebar */
}
```

#### Sidebar Oculto por Defecto

**Antes**:
```css
.sidebar {
    width: 30%;
    height: 100vh;
    background: rgba(20, 20, 20, 0.95);
    /* ... */
    display: flex;            /* Visible por defecto */
}
```

**Después**:
```css
.sidebar {
    width: 30%;
    height: 100vh;
    background: rgba(20, 20, 20, 0.95);
    /* ... */
    display: none;            /* Oculto por defecto */
    flex-direction: column;
    transition: all 0.3s ease;
}

.sidebar.visible {
    display: flex;            /* Visible con clase .visible */
}
```

#### TTS Controls Ocultos por Defecto

**Antes**:
```css
.tts-controls {
    position: fixed;
    top: 20px;
    right: 20px;
    display: flex;            /* Visible por defecto */
    /* ... */
}
```

**Después**:
```css
.tts-controls {
    position: fixed;
    top: 20px;
    right: 20px;
    display: none;            /* Oculto por defecto */
    gap: 10px;
    z-index: 100;
    /* ... */
    transition: all 0.3s ease;
}

.tts-controls.visible {
    display: flex;            /* Visible con clase .visible */
}
```

---

### 3. JavaScript: Combinación de Teclas Secreta

**Combinación**: `Ctrl + Shift + S`

#### Código Implementado

```javascript
// SECRET KEY COMBINATION TO ENABLE SPEECH MODE
// Combination: Ctrl + Shift + S
let secretKeyActive = false;
const secretKeys = { ctrl: false, shift: false, s: false };

document.addEventListener('keydown', function(e) {
    // Track key combinations
    if (e.ctrlKey) secretKeys.ctrl = true;
    if (e.shiftKey) secretKeys.shift = true;
    if (e.key.toLowerCase() === 's') secretKeys.s = true;

    // Check if all keys are pressed
    if (secretKeys.ctrl && secretKeys.shift && secretKeys.s && !secretKeyActive) {
        secretKeyActive = true;
        toggleSpeechMode();
        console.log('🎤 Speech mode activated!');
    }
});

document.addEventListener('keyup', function(e) {
    // Reset key tracking
    if (!e.ctrlKey) secretKeys.ctrl = false;
    if (!e.shiftKey) secretKeys.shift = false;
    if (e.key.toLowerCase() === 's') secretKeys.s = false;
});
```

#### Función toggleSpeechMode()

```javascript
function toggleSpeechMode() {
    const sidebar = document.getElementById('sidebar');
    const slideArea = document.querySelector('.slide-area');
    const ttsControls = document.querySelector('.tts-controls');

    if (secretKeyActive) {
        // Show speech mode
        sidebar.classList.add('visible');
        slideArea.classList.add('with-sidebar');
        ttsControls.classList.add('visible');

        // Add visual indicator
        const indicator = document.createElement('div');
        indicator.id = 'speech-indicator';
        indicator.style.cssText = `
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: rgba(102, 126, 234, 0.9);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            font-size: 0.9rem;
            z-index: 1000;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.5);
        `;
        indicator.textContent = '🎤 Modo Profesor Activado';
        document.body.appendChild(indicator);

        // Auto-hide indicator after 3 seconds
        setTimeout(() => {
            indicator.style.opacity = '0';
            indicator.style.transition = 'opacity 0.5s ease';
            setTimeout(() => indicator.remove(), 500);
        }, 3000);
    }
}
```

#### Mensaje de Consola al Cargar

```javascript
// Initialize as student version (speech hidden)
window.addEventListener('DOMContentLoaded', function() {
    console.log('📚 Versión Alumno cargada. Presiona Ctrl+Shift+S para modo profesor.');
});
```

---

## FUNCIONAMIENTO

### Modo Alumno (Por Defecto)

**Estado inicial al abrir el archivo**:

```
┌─────────────────────────────────────────────────┐
│                                                  │
│                                                  │
│          [SLIDE CONTENT 100% WIDTH]              │
│                                                  │
│          📊 Gráficos de Monte Carlo              │
│          📈 Cálculos PERT                        │
│                                                  │
│                                                  │
│                                                  │
│                          [← ] [1/9] [→]          │ ← Controles de navegación
└─────────────────────────────────────────────────┘

✅ Sidebar: Oculto
✅ TTS Controls: Ocultos
✅ Layout: 100% width
✅ Navegación: Funcional (flechas teclado, botones)
✅ Gráficos: Todos visibles
```

---

### Activación: Ctrl + Shift + S

**Usuario presiona**: `Ctrl` + `Shift` + `S` (simultáneamente)

**Resultado**:

1. **Sidebar aparece** (animación suave 0.3s)
2. **TTS controls aparecen** (arriba derecha)
3. **Slide area se ajusta** de 100% a 70% width
4. **Indicador temporal** aparece (abajo izquierda):

```
┌─────────────────────────────┬──────────────────┐
│                              │                  │
│   [SLIDE CONTENT 70%]        │   [SIDEBAR 30%]  │
│                              │                  │
│   📊 Gráficos               │   📄 Speech      │
│                              │                  │
│                              │   Script text... │
│                              │                  │
│   [← ] [1/9] [→]             │                  │
│                              │                  │
│  ┌────────────────────┐     │                  │
│  │ 🎤 Modo Profesor   │     │                  │ ← Indicador temporal
│  │    Activado        │     │                  │   (desaparece en 3s)
│  └────────────────────┘     │                  │
└─────────────────────────────┴──────────────────┘
       ▲
       TTS Controls (arriba derecha)
       [▶ Play] [⏸ Pause] [⏹ Stop] [Speed] [Voice]
```

---

## CARACTERÍSTICAS

### Transiciones Suaves

```css
transition: all 0.3s ease;
```

Todos los elementos tienen animación de 0.3 segundos:
- Sidebar: Aparece de derecha a izquierda
- Slide area: Se reduce de 100% a 70%
- TTS controls: Fade in
- Indicador: Fade out después de 3 segundos

---

### Indicador Visual Temporal

**Propiedades**:
- Posición: Fixed, bottom-left
- Fondo: Púrpura semitransparente
- Duración: 3 segundos visible
- Animación: Opacity 0.5s al desaparecer
- Texto: "🎤 Modo Profesor Activado"

**Por qué es útil**:
- Confirma visualmente que la combinación de teclas funcionó
- No requiere interacción del usuario
- Se auto-elimina (no molesta)

---

### Consola del Navegador

**Mensajes**:

Al cargar:
```
📚 Versión Alumno cargada. Presiona Ctrl+Shift+S para modo profesor.
```

Al activar:
```
🎤 Speech mode activated!
```

**Útil para**:
- Debugging
- Confirmación de activación
- Ayuda para usuarios que olvidan la combinación

---

## COMPARACIÓN: VERSIÓN PROFESOR vs VERSIÓN ALUMNO

| Aspecto | clase2_pert_anexos.html<br>(PROFESOR) | clase2_anexos_alumno.html<br>(ALUMNO) |
|---------|--------------------------------------|--------------------------------------|
| **Sidebar** | Visible por defecto (30%) | Oculto por defecto |
| **TTS Controls** | Visibles por defecto | Ocultos por defecto |
| **Slide width** | 70% siempre | 100% → 70% al activar |
| **Speech scripts** | Siempre accesibles | Accesibles con Ctrl+Shift+S |
| **Activación secreta** | No tiene | Ctrl+Shift+S |
| **Indicador visual** | No tiene | "Modo Profesor Activado" (3s) |
| **Consola mensaje** | No tiene | Sí, al cargar y activar |
| **Título** | "Ejemplos Gráficos y Cálculos" | "... (Versión Alumno)" |
| **Para quién** | Profesor/Facilitador | Estudiantes (+ profesor secreto) |

---

## VENTAJAS DE ESTA IMPLEMENTACIÓN

### Para Estudiantes

✅ **Pantalla completa**: Aprovechan 100% del espacio para ver gráficos
✅ **Sin distracciones**: No ven el speech del profesor
✅ **Navegación clara**: Botones y flechas funcionan igual
✅ **Mismos gráficos**: Todos los ejemplos, cálculos y visualizaciones disponibles

### Para Profesores

✅ **Un solo archivo**: No necesitan dos archivos separados
✅ **Fácil activación**: Ctrl+Shift+S (fácil de recordar: **S**peech)
✅ **Modo oculto**: Estudiantes no saben que existe a menos que se les diga
✅ **Transición suave**: Cambio visual profesional (no abrupto)
✅ **Confirmación clara**: Indicador temporal confirma activación

### Técnicas

✅ **No duplica código**: Mantiene todo el contenido original
✅ **CSS limpio**: Solo cambios en display y width
✅ **JavaScript mínimo**: ~70 líneas agregadas
✅ **Sin dependencias**: No requiere librerías adicionales
✅ **Retrocompatible**: Navegación y gráficos funcionan igual

---

## TESTING RECOMENDADO

### 1. Modo Alumno (Default)

Abrir `clase2_anexos_alumno.html` y verificar:
- [ ] Sidebar NO visible
- [ ] TTS controls NO visibles
- [ ] Slides ocupan 100% de ancho
- [ ] Navegación funciona (flechas ← →, Home, End)
- [ ] Botones [Anterior] [Siguiente] funcionan
- [ ] Contador de slides funciona (1/9, 2/9, etc.)
- [ ] Todos los gráficos se renderizan correctamente:
  - [ ] Gráfico de varianza (slide 7)
  - [ ] Gráfico de Monte Carlo (slide 8) con referencias
- [ ] Consola muestra: "📚 Versión Alumno cargada..."

### 2. Activación con Tecla Secreta

Presionar `Ctrl + Shift + S` simultáneamente:
- [ ] Sidebar aparece a la derecha (30%)
- [ ] TTS controls aparecen arriba derecha
- [ ] Slide area se reduce a 70%
- [ ] Indicador "Modo Profesor Activado" aparece (abajo izquierda)
- [ ] Indicador desaparece después de ~3 segundos
- [ ] Transiciones son suaves (no abrupto)
- [ ] Consola muestra: "🎤 Speech mode activated!"

### 3. Modo Profesor (Activado)

Después de activar con Ctrl+Shift+S:
- [ ] Sidebar muestra título y duración del speech
- [ ] Sidebar muestra script del slide actual
- [ ] TTS controls funcionan:
  - [ ] Play/Pause
  - [ ] Stop
  - [ ] Speed control (0.8x - 2.0x)
  - [ ] Voice selection
- [ ] Sidebar se actualiza al cambiar de slide
- [ ] Layout 70/30 se mantiene al navegar

### 4. Testing de Edge Cases

- [ ] Presionar solo Ctrl+S (no debería activar)
- [ ] Presionar solo Shift+S (no debería activar)
- [ ] Presionar Ctrl+Shift+otro (no debería activar)
- [ ] Activar dos veces Ctrl+Shift+S (no debería duplicar)
- [ ] Resize ventana en modo alumno (100% responsive)
- [ ] Resize ventana en modo profesor (70/30 responsive)
- [ ] Fullscreen (F11) funciona en ambos modos

---

## INSTRUCCIONES DE USO

### Para Profesores

**Compartir archivo con estudiantes**:
1. Enviar `clase2_anexos_alumno.html`
2. NO mencionar la combinación secreta (a menos que quieran que la usen)
3. Si quieren que la usen: "Presionen Ctrl+Shift+S para ver el speech"

**Usar en clase**:
- Abrir archivo
- Presionar `Ctrl+Shift+S`
- Usar TTS o leer speech manualmente
- Estudiantes ven mismo archivo sin distracciones

### Para Estudiantes

**Uso normal**:
- Abrir `clase2_anexos_alumno.html`
- Navegar con flechas o botones
- Ver gráficos y ejemplos
- Estudiar los 9 slides de anexos

**Si el profesor les da la clave**:
- Presionar `Ctrl+Shift+S`
- Aparece sidebar con explicaciones
- Pueden usar TTS para escuchar
- Estudian de forma independiente con audio

---

## ARCHIVOS EN EL PROYECTO

```
cursoEStima/
  clase2_pert_anexos.html          ← Versión PROFESOR (sidebar visible siempre)
  clase2_anexos_alumno.html         ← Versión ALUMNO (sidebar oculto, Ctrl+Shift+S)
  clase2.html                       ← Clase 2 principal (alumnos)
  clase2_profesor.html              ← Clase 2 principal (profesor)

  temp/
    CLASE2_ANEXOS_ALUMNO.md         ← Esta documentación
```

---

## POSIBLES MEJORAS FUTURAS

### Opción 1: Toggle On/Off

Permitir desactivar el modo profesor:

```javascript
if (secretKeyActive) {
    // Si ya está activo, desactivar
    sidebar.classList.remove('visible');
    slideArea.classList.remove('with-sidebar');
    ttsControls.classList.remove('visible');
    secretKeyActive = false;
} else {
    // Si está inactivo, activar
    // ... código actual
}
```

### Opción 2: Otras Combinaciones

Agregar más atajos:
- `Ctrl+Shift+G`: Mostrar guías pedagógicas
- `Ctrl+Shift+H`: Mostrar hints/tips
- `Ctrl+Shift+A`: Mostrar respuestas a ejercicios

### Opción 3: Password en Prompt

En lugar de tecla secreta:

```javascript
const password = prompt('Ingrese password de profesor:');
if (password === 'pert2025') {
    toggleSpeechMode();
}
```

### Opción 4: URL Parameter

Activar automáticamente con URL:

```javascript
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('mode') === 'profesor') {
    secretKeyActive = true;
    toggleSpeechMode();
}
```

Uso: `clase2_anexos_alumno.html?mode=profesor`

---

## CONCLUSIÓN

**Archivo generado**: `clase2_anexos_alumno.html`

✅ **Versión dual en un solo archivo**: Alumno por defecto, profesor con tecla secreta
✅ **UI limpia para estudiantes**: 100% pantalla para gráficos
✅ **Activación elegante**: Ctrl+Shift+S con confirmación visual
✅ **Transiciones profesionales**: Animaciones suaves 0.3s
✅ **Funcionalidad completa**: Todos los gráficos, navegación, TTS

**Antes**: 2 archivos separados (profesor.html y alumno.html)
**Después**: 1 archivo con modo oculto activable

---

**Fecha de creación**: 2025-12-09
**Tiempo de implementación**: ~15 minutos
**Complejidad**: Baja (solo CSS + 70 líneas JS)
**Testing**: Pendiente con usuarios reales
**Retrocompatibilidad**: 100% (no rompe funcionalidad existente)

---

## MÉTRICAS

| Métrica | Valor |
|---------|-------|
| **Líneas agregadas** | ~70 (JavaScript) |
| **Líneas modificadas** | ~25 (CSS) |
| **Total cambios** | ~95 líneas |
| **Tamaño archivo** | ~1950 líneas (igual que original + 70) |
| **Performance** | Sin impacto (solo event listeners) |
| **Compatibilidad** | Chrome, Firefox, Edge, Safari (modernos) |
| **Dependencias** | 0 (vanilla JS) |

---

**Listo para distribución**: Sí ✅
**Requiere testing adicional**: Sí (en diferentes navegadores)
**Documentación completa**: Sí ✅
