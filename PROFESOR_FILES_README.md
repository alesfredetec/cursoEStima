# Profesor HTML Files - Generation Summary

## Generated Files

Two complete profesor HTML files have been successfully generated:

### 1. clase2_profesor.html
- **Title:** Clase 2: Métodos de Estimación (Versión Profesor)
- **File Size:** 116 KB (1,852 lines)
- **Slides:** 24 slides (from original clase2.html)
- **Speech Scripts:** 17 complete scripts embedded from SPEECH_SCRIPTS_CLASE2_COMPLETO.md
- **Features:**
  - 70/30 split layout (slides + speech sidebar)
  - Browser TTS (free, offline)
  - OpenAI TTS (professional quality)
  - Speed control: 1.0x, 1.2x (default), 1.5x, 2.0x
  - Keyboard shortcuts: S (toggle sidebar), T (toggle TTS), Arrows (navigate)
  - Complete speech scripts with markers ([PAUSA], [ÉNFASIS], etc.)
  - Self-contained, no external dependencies

### 2. clase3_profesor.html
- **Title:** Clase 3: Cadena Crítica (CCPM) (Versión Profesor)
- **File Size:** 192 KB (2,421 lines)
- **Slides:** 32 slides (from original clase3.html)
- **Speech Scripts:** 29 complete scripts embedded from SPEECH_SCRIPTS_CLASE3_COMPLETO.md
- **Features:**
  - Same complete TTS integration as clase2_profesor.html
  - Identical UI/UX with clase1_profesor.html template
  - All slides from original clase3.html preserved
  - Professional speech scripts with timing and markers

## Technical Details

### TTS System Features

**Two Modes:**
1. **Browser TTS (Default):**
   - Uses Web Speech API
   - Works offline
   - Free
   - Uses best available Spanish voice (es-ES, es-MX, es-US)

2. **OpenAI TTS (Professional):**
   - High-quality neural voices
   - Uses OpenAI TTS-1 model
   - Voice: nova (female, professional)
   - Requires API key (already embedded)
   - Automatic fallback to browser TTS on error

**Speed Control:**
- 1.0x (normal)
- 1.2x (default - recommended for teaching)
- 1.5x (fast review)
- 2.0x (very fast review)

**Controls:**
- ▶ Play/⏸ Pause: Start or pause current slide speech
- ⏹ Stop: Stop and reset playback
- Speed buttons: Change playback speed
- Mode toggle: Switch between Browser and OpenAI TTS

### Keyboard Shortcuts

- **Arrow keys:** Navigate slides
- **Space:** Next slide
- **Home:** First slide
- **End:** Last slide
- **S:** Toggle speech sidebar
- **T:** Toggle TTS playback

### Speech Script Format

Each slide has structured speech data:
```javascript
{
    title: "Slide Title",
    duration: "X min",
    script: `Complete speech script with
    [MARKERS] for delivery guidance`
}
```

**Markers in scripts:**
- `[PAUSA]` - Pause for emphasis
- `[ÉNFASIS]` - Emphasize this point
- `[TRANSICIÓN]` - Transition to next topic
- `[LEER ...]` - Read from slide
- `[PREGUNTAS]` - Ask audience

## Generation Process

Files were generated using `generate_profesor_files.py`:
1. Extract all slides from original HTML files (clase2.html, clase3.html)
2. Parse speech scripts from markdown files (SPEECH_SCRIPTS_CLASE2/3_COMPLETO.md)
3. Use clase1_profesor.html as template
4. Replace slides with correct ones
5. Replace speech data with correct scripts
6. Update all references to correct clase number

## Usage Instructions

### For Instructors:

1. **Open the profesor file** in any modern browser
2. **Select TTS mode:**
   - Browser (free, works offline)
   - OpenAI (professional, requires internet)
3. **Navigate** through slides with arrow keys or buttons
4. **Read speech script** in right sidebar
5. **Play TTS** to hear professional narration
6. **Adjust speed** for pacing (1.2x recommended)

### For Students:

- Share the regular files (clase2.html, clase3.html) without speech scripts
- Profesor versions are for instructor use only

## File Locations

```
C:\tmp\cursoEStima\
├── clase1_profesor.html (original template)
├── clase2_profesor.html (generated)
├── clase3_profesor.html (generated)
├── clase2.html (source slides)
├── clase3.html (source slides)
├── materiales_facilitador\
│   ├── SPEECH_SCRIPTS_CLASE2_COMPLETO.md (source scripts)
│   └── SPEECH_SCRIPTS_CLASE3_COMPLETO.md (source scripts)
└── generate_profesor_files.py (generation script)
```

## Verification

Both files have been validated:
- ✓ Correct number of slides embedded
- ✓ Speech scripts properly extracted and cleaned
- ✓ Quotes removed from script content
- ✓ Correct clase number in variable names (speechDataClase2/3)
- ✓ All references updated
- ✓ Self-contained HTML (no external dependencies)
- ✓ OpenAI API key embedded
- ✓ All TTS features functional

## Notes

- **API Key:** OpenAI API key is embedded in the files for convenience
- **Offline Mode:** Browser TTS works without internet
- **Browser Compatibility:** Works in Chrome, Firefox, Safari, Edge (modern versions)
- **Mobile:** Responsive design works on tablets and phones
- **Accessibility:** Keyboard navigation fully supported

## Regeneration

To regenerate files (if needed):
```bash
cd C:\tmp\cursoEStima
python generate_profesor_files.py
```

This will overwrite existing clase2_profesor.html and clase3_profesor.html.

---

**Generated:** January 2025
**Version:** 2.0 (Remote-ready format)
**Author:** Claude Code
**Instructor:** Alejandro Sfrede - Área de Arquitectura
