# Plan: HTML para Profesor con Speech Scripts y TTS

**Fecha:** 2025-01-01
**Objetivo:** Crear versiones HTML para el profesor con speech scripts en barra lateral y opción TTS

---

## 📋 ANÁLISIS COMPLETADO

### Estructura Actual de los HTML

**Archivos existentes:**
- `clase1.html` - 23 slides - La Crisis de la Estimación
- `clase2.html` - 24 slides - Métodos de Estimación
- `clase3.html` - 32 slides - Cadena Crítica (CCPM)

**Características técnicas:**
- ✅ Dark theme profesional (gradiente púrpura)
- ✅ Sistema de navegación con teclado (flechas, Home, End, Space)
- ✅ Touch/swipe support para móviles
- ✅ Progress bar visual
- ✅ Slide counter (ej: "1 / 23")
- ✅ Botones prev/next
- ✅ Responsive design (breakpoint 768px)
- ✅ Scroll interno en slides con mucho contenido
- ✅ Animaciones fadeIn suaves
- ✅ Self-contained (CSS inline, sin dependencias externas)

**Estructura JavaScript:**
```javascript
- currentSlide = 0
- showSlide(n) - Cambia slide, actualiza UI
- changeSlide(direction) - +1 o -1
- Event listeners: keyboard, touch, buttons
```

### Speech Scripts Disponibles

**Clase 1:** ✅ COMPLETO
- Archivo: `materiales_facilitador/SPEECH_SCRIPTS_COMPLETO.md`
- 21 slides con scripts detallados
- Markers: [PAUSA], [ÉNFASIS], [TRANSICIÓN], [LEER slide], [ANALOGÍA]
- Timing: cada slide tiene duración sugerida

**Clase 2:** ✅ COMPLETO
- Archivo: `materiales_facilitador/SPEECH_SCRIPTS_CLASE2_COMPLETO.md`
- 18 slides con scripts conversacionales
- Caso completo de Planning Poker (HU-3 Password Reset)
- Timing: 180 minutos totales

**Clase 3:** ❌ PENDIENTE
- Archivo: Necesita crearse
- 32 slides sobre CCPM, buffers, Fever Chart
- Incluye caso A-B-C-D (el "aha! moment")

---

## 🎯 DISEÑO PROPUESTO

### Layout: Pantalla Dividida

```
┌─────────────────────────────────────────────────────────┐
│ Progress Bar                                             │
├────────────────────────────┬────────────────────────────┤
│                            │  📝 SPEECH PANEL          │
│                            │  ┌──────────────────────┐ │
│    SLIDE CONTENT           │  │ Slide 1: Portada     │ │
│    (70% width)             │  │ Duración: 2 min      │ │
│                            │  ├──────────────────────┤ │
│                            │  │ "Hola a todos..."    │ │
│                            │  │                      │ │
│    [Existing slide]        │  │ [PAUSA]              │ │
│                            │  │                      │ │
│                            │  │ [Scrollable]         │ │
│                            │  │                      │ │
│                            │  ├──────────────────────┤ │
│                            │  │ 🔊 TTS Controls      │ │
│                            │  │ ▶️ Play | ⏸️ Pause   │ │
│                            │  │ 🔇 Mute | ⚙️ Speed   │ │
│                            │  └──────────────────────┘ │
├────────────────────────────┴────────────────────────────┤
│ ◀️ Prev  |  Controls  |  Next ▶️  |  Slide 1/23       │
└─────────────────────────────────────────────────────────┘
```

### Características del Speech Panel

**Header:**
- Título del slide actual (ej: "Slide 3: El Problema Fundamental")
- Duración sugerida (ej: "5 min")
- Toggle button para mostrar/ocultar panel

**Body (scrollable):**
- Speech script completo del slide actual
- Formatting:
  - [PAUSA] → ⏸️ icon + énfasis visual
  - [ÉNFASIS] → 💪 icon + bold
  - [TRANSICIÓN] → 🔄 icon + italic
  - [PREGUNTA] → ❓ icon + color diferente
- Line height amplio para legibilidad

**Footer - TTS Controls:**
- ▶️ Play / ⏸️ Pause
- Speed: 0.8x, 1.0x, 1.2x, 1.5x
- Voice selection (si disponible)
- Mute/Unmute
- Auto-play toggle (leer script al cambiar slide)

**Responsive:**
- Desktop (>1024px): Sidebar 30% width, siempre visible
- Tablet (768-1024px): Sidebar colapsable, botón toggle
- Mobile (<768px): Speech panel en modal overlay

---

## 🛠️ IMPLEMENTACIÓN TÉCNICA

### Fase 1: Estructura de Datos

**Formato JSON embebido:**
```javascript
const speechData = {
  "slide1": {
    "title": "Portada",
    "duration": "2 min",
    "script": "Hola a todos, bienvenidos...",
    "markers": [
      {"type": "PAUSA", "position": 45},
      {"type": "ÉNFASIS", "position": 120}
    ]
  },
  "slide2": {...}
};
```

### Fase 2: CSS Additions

**Nuevo CSS para sidebar:**
```css
.professor-layout {
  display: flex;
  height: 100vh;
}

.slide-area {
  flex: 0 0 70%;
  /* Mantiene estructura existente */
}

.speech-sidebar {
  flex: 0 0 30%;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  border-left: 1px solid rgba(255,255,255,0.1);
  overflow-y: auto;
  padding: 20px;
}

.speech-header {
  position: sticky;
  top: 0;
  background: rgba(102, 126, 234, 0.2);
  padding: 15px;
  border-radius: 10px;
  margin-bottom: 15px;
}

.speech-body {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #e0e0e0;
}

.marker-pause::before {
  content: "⏸️ ";
  margin-right: 5px;
}

.marker-emphasis {
  font-weight: bold;
  color: #667eea;
}

.tts-controls {
  position: sticky;
  bottom: 0;
  background: rgba(0,0,0,0.9);
  padding: 15px;
  border-radius: 10px;
  margin-top: 20px;
}
```

### Fase 3: JavaScript Enhancements

**Sincronización con slides:**
```javascript
function showSlide(n) {
  // ... código existente ...

  // Update speech panel
  updateSpeechPanel(n);

  // Stop TTS if playing
  if (ttsPlaying) {
    speechSynthesis.cancel();
  }

  // Auto-play if enabled
  if (autoPlayTTS) {
    playTTS(speechData[`slide${n+1}`].script);
  }
}
```

**Web Speech API (TTS):**
```javascript
function playTTS(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'es-ES';
  utterance.rate = ttsSpeed;
  utterance.pitch = 1.0;
  utterance.volume = ttsVolume;

  speechSynthesis.speak(utterance);
}

function pauseTTS() {
  speechSynthesis.pause();
}

function stopTTS() {
  speechSynthesis.cancel();
}
```

**Keyboard shortcuts adicionales:**
- `S` - Toggle speech sidebar
- `T` - Play/Pause TTS
- `[` - Decrease speed
- `]` - Increase speed

### Fase 4: Conversión de Markdown a JSON

**Script de conversión (realizar manualmente):**

1. Parsear `SPEECH_SCRIPTS_COMPLETO.md`
2. Extraer cada slide (## Slide N:)
3. Identificar markers ([PAUSA], [ÉNFASIS], etc.)
4. Generar JSON estructurado
5. Embeber en HTML como `<script>const speechData = {...}</script>`

---

## 📦 ENTREGABLES

### Archivos a Generar:

1. **clase1_profesor.html** (Prioridad 1)
   - HTML completo con sidebar
   - Speech scripts de 21 slides embebidos
   - TTS funcional
   - ~2500 líneas

2. **clase2_profesor.html** (Prioridad 2)
   - HTML completo con sidebar
   - Speech scripts de 18 slides embebidos
   - TTS funcional
   - ~2200 líneas

3. **clase3_profesor.html** (Prioridad 3)
   - **REQUIERE:** Completar speech scripts primero
   - HTML completo con sidebar
   - Speech scripts de 32 slides (por crear)
   - TTS funcional
   - ~3000 líneas

### Testing Checklist:

✅ Navegación con teclado (flechas, Home, End, Space)
✅ Sincronización slide ↔ speech panel
✅ TTS play/pause/stop
✅ TTS speed control (0.8x, 1.0x, 1.2x, 1.5x)
✅ Sidebar toggle (S key)
✅ Responsive behavior (desktop/tablet/mobile)
✅ Scroll independiente (slide content vs speech panel)
✅ Progress bar actualizado
✅ Slide counter correcto
✅ Touch/swipe funcional
✅ Botones prev/next sincronizados

---

## 🚀 PLAN DE EJECUCIÓN

### Paso 1: Preparar Speech Data (30 min)
- [x] Leer `SPEECH_SCRIPTS_COMPLETO.md` (Clase 1)
- [x] Leer `SPEECH_SCRIPTS_CLASE2_COMPLETO.md` (Clase 2)
- [ ] Extraer scripts por slide
- [ ] Convertir a JSON estructurado
- [ ] Identificar markers y posiciones

### Paso 2: Crear Template Base (20 min)
- [ ] Clonar estructura de `clase1.html`
- [ ] Añadir CSS para sidebar
- [ ] Añadir HTML structure para speech panel
- [ ] Añadir TTS controls

### Paso 3: JavaScript Integration (30 min)
- [ ] Función `updateSpeechPanel(slideIndex)`
- [ ] Función `playTTS(text)`
- [ ] Event listeners para TTS controls
- [ ] Keyboard shortcuts (S, T, [, ])
- [ ] Auto-play toggle logic

### Paso 4: Generar clase1_profesor.html (40 min)
- [ ] Copiar todos los slides de `clase1.html`
- [ ] Embeber `speechDataClase1` JSON
- [ ] Conectar navigation con speech sync
- [ ] Testing completo

### Paso 5: Generar clase2_profesor.html (40 min)
- [ ] Copiar todos los slides de `clase2.html`
- [ ] Embeber `speechDataClase2` JSON
- [ ] Conectar navigation con speech sync
- [ ] Testing completo

### Paso 6: Completar Clase 3 Speech Scripts (60-90 min)
- [ ] Leer `materiales_facilitador/GUIA_PROFESOR_CLASE3.md`
- [ ] Generar scripts para 32 slides
- [ ] Crear `SPEECH_SCRIPTS_CLASE3_COMPLETO.md`
- [ ] Validar timing (180 minutos totales)

### Paso 7: Generar clase3_profesor.html (40 min)
- [ ] Copiar todos los slides de `clase3.html`
- [ ] Embeber `speechDataClase3` JSON
- [ ] Conectar navigation con speech sync
- [ ] Testing completo

**Total estimado:** 4-5 horas

---

## 💡 MEJORAS OPCIONALES (Futuro)

### V2 Features:
- 📊 Timer visible con cuenta regresiva por slide
- 📝 Notas del facilitador (tips pedagógicos) en tab separado
- 🎨 Highlight text-to-speech sincronizado (palabra actual en amarillo)
- 💾 Save/restore state (localStorage con slide actual)
- 📱 Remote control via WebSocket (controlar desde celular)
- 🎤 Voice commands (navegar con "siguiente", "anterior")
- 📊 Analytics (tiempo real en cada slide)
- 🔗 Deep links (compartir URL de slide específico)

### Accessibility:
- ♿ ARIA labels completos
- ⌨️ Focus management
- 🔊 Screen reader optimized
- 🎨 High contrast mode toggle
- 📏 Font size adjustment

---

## 🎯 DECISIONES DE DISEÑO

### Por qué Sidebar (no modal)?
- ✅ Siempre visible = menos clicks
- ✅ Profesor puede leer script mientras muestra slide
- ✅ No obstruye contenido principal
- ✅ Más profesional que overlay

### Por qué Web Speech API?
- ✅ Nativo del browser (Chrome, Edge, Safari)
- ✅ Sin dependencias externas
- ✅ Funciona offline (voces locales)
- ✅ Control completo (rate, pitch, volume)
- ❌ Limitación: Voces varían por browser/OS
- ❌ Limitación: Calidad no es Google Cloud TTS

### Por qué JSON embebido (no fetch)?
- ✅ Self-contained (funciona offline, doble-click para abrir)
- ✅ No requiere servidor HTTP
- ✅ Más rápido (no network request)
- ✅ Más simple (un solo archivo)
- ❌ Limitación: Archivos más grandes (~200KB extra)

---

## 📋 NOTAS TÉCNICAS

### Browser Support:
- **Chrome/Edge:** ✅ Excelente (Web Speech API completo)
- **Firefox:** ⚠️ Limitado (TTS sin voces premium)
- **Safari:** ✅ Bueno (voces iOS/macOS nativas)
- **Mobile:** ✅ Chrome/Safari móvil soportan TTS

### Performance:
- **Tamaño HTML:** ~500KB (con JSON embebido)
- **Load time:** <1 segundo (local file)
- **Memory:** ~50MB (razonable para HTML+JS)
- **CPU:** Bajo (solo TTS usa recursos)

### Fallbacks:
- Si Web Speech API no disponible → Mostrar warning, deshabilitar TTS
- Si sidebar muy angosto (<1024px) → Colapsar por defecto
- Si touch no soportado → Solo keyboard/buttons

---

## ✅ CRITERIOS DE ÉXITO

**Funcionalidad:**
- [ ] Profesor puede navegar slides normalmente
- [ ] Speech script visible para slide actual
- [ ] TTS lee script correctamente en español
- [ ] Speed control funciona (0.8x - 1.5x)
- [ ] Sidebar toggleable con teclado (S)
- [ ] Sincronización perfecta (cambio slide → update speech)
- [ ] Funciona offline (doble-click en archivo)

**UX:**
- [ ] UI clara, profesional, no distractora
- [ ] Legible desde 2 metros de distancia (proyector)
- [ ] No requiere tutorial (intuitivo)
- [ ] Responsive (desktop/tablet)
- [ ] Performance fluida (no lag)

**Calidad:**
- [ ] Código limpio, comentado
- [ ] Sin errores de consola
- [ ] Cross-browser tested (Chrome, Edge, Firefox, Safari)
- [ ] Cumple timing de facilitador guide

---

**Conclusión:** Plan completo, técnicamente viable, UX optimizada para profesor.

**Próximo paso:** Comenzar implementación con `clase1_profesor.html`.
