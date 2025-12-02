# CursoEStima - Comprehensive Guide for Claude Instances

**Project Type**: Educational Course - Project Estimation & Risk Management
**Duration**: 9 hours (3 classes x 3 hours)
**Version**: 2.1 (December 2025)
**Instructor**: Alejandro Sfrede

---

## QUICK SUMMARY

This is a complete, remote-ready 9-hour course teaching professionals to replace "inflated" estimation with systematic approaches (PERT, Agile, CCPM) that explicitly manage uncertainty and psychology.

**Three Classes**:
- Class 1: Why estimates fail (Uncertainty Cone, Parkinson's Law)
- Class 2: How to estimate (PERT, Story Points, Planning Poker)
- Class 3: Critical Chain CCPM (Resource-aware scheduling with buffers)

**Two Versions Available**:
- **clase#.html** - Student version (slides only)
- **clase#_profesor.html** - Professor version (slides + TTS narration)

---

## MUST-READ FILES

1. **RESUMEN_CURSO.md** - Course structure
2. **MEJORAS_REALIZADAS.md** - V2.0 changes
3. **materiales_facilitador/GUIA_FACILITADOR_TALLERES.md** - How to teach (1086 lines)
4. **INSTRUCCIONES_USO.md** - How to use
5. **SEGURIDAD_API_KEYS.md** - Security setup for TTS
6. **This file (CLAUDE.md)** - Overview

---

## NEW IN V2.1: PROFESOR FILES WITH TTS

### What's New (December 2025)

Added **profesor** versions of all 3 classes with Text-to-Speech functionality:

#### Files:
- `clase1_profesor.html` - 24 slides with synchronized speech scripts
- `clase2_profesor.html` - 24 slides with synchronized speech scripts
- `clase3_profesor.html` - 22 slides with synchronized speech scripts

#### TTS Features:
- **Dual Mode**: Browser TTS (free) + OpenAI TTS (professional quality)
- **6 OpenAI Voices**: nova, shimmer, alloy, echo, fable, onyx
- **Browser Voices**: Spanish (España, México, Argentina)
- **Controls**: Play/Pause, Speed (0.8x - 2x), Voice selection
- **Navigation**: Arrow keys, Home/End, slide counter
- **Synchronized Scripts**: Speech content matches each slide exactly

#### TTS Usage:
1. **Without config.js**: Browser TTS works immediately (Spanish voices)
2. **With config.js**: OpenAI TTS available (better quality)

### Security: API Keys Externalized

**IMPORTANT**: API keys are NOT in git repository.

**Setup for new users**:
```bash
# 1. Copy template
cp config.example.js config.js

# 2. Edit and add your OpenAI API key
notepad config.js  # Windows
nano config.js     # Linux/Mac

# 3. Open profesor files in browser
```

**Files**:
- `config.js` - Contains real API key (ignored by git)
- `config.example.js` - Template with placeholder (in git)
- `.gitignore` - Excludes config.js

**Read**: `SEGURIDAD_API_KEYS.md` for complete security documentation.

---

## THE CORE INSIGHT: A-B-C-D CASE

**Setup**: 4-task project where Ana must do both task B and D

**Discovery Flow**:
- CPM says: 25 days (ignores Ana conflict - WRONG)
- Reality says: 35 days (Ana can't multitask - REAL)
- CCPM says: 27 days (aggressive + buffers - ACHIEVABLE)

This case teaches that CPM fails because it ignores resources - CCPM fixes this.

---

## DIRECTORY STRUCTURE

```
cursoEStima/
  # Student versions (slides only)
  clase1.html (1170 lines)
  clase2.html (1133 lines)
  clase3.html (1671 lines)
  index.html

  # Professor versions (slides + TTS)
  clase1_profesor.html (2900 lines) ← NEW
  clase2_profesor.html (1900 lines) ← NEW
  clase3_profesor.html (2100 lines) ← NEW

  # Configuration (for TTS)
  config.js (ignored by git) ← NEW
  config.example.js (template) ← NEW

  # Documentation
  RESUMEN_CURSO.md
  INSTRUCCIONES_USO.md
  MEJORAS_REALIZADAS.md
  SEGURIDAD_API_KEYS.md ← NEW
  CLAUDE.md (this file)

  materiales_facilitador/
    GUIA_FACILITADOR_TALLERES.md (1086 lines - CRITICAL)
    GUIA_PROFESOR_CLASE*.md
    SPEECH_SCRIPTS_COMPLETO.md (all speeches)

  materiales_alumnos/
    MATERIAL_ESTUDIO_CLASE*.md
    EJERCICIO_PARKINSON_*.md

  doc/
    adminpro/ (40 reference PDFs)
    guiasyejemplos/ (templates)

  temp/ ← NEW
    # Auxiliary scripts (verification, fixes)
    # Old documentation (completed tasks)
    # 29 files: *.py, *.md, *.txt, *.js
```

---

## THE THREE CLASSES OVERVIEW

### CLASS 1: La Crisis (3 hours)
**24 slides total**
- Uncertainty Cone (±400% start to ±10% end)
- Parkinson's Law (work expands to fill time)
- Student Syndrome (procrastination)
- 16 Factors Affecting Estimation (5 tech + 5 human + 6 environment)
- Risk Matrix (7 categories: CRÍTICOS, IMPORTANTES, MENORES)
- Research analysis (Tom Wujec, Microsoft, Ariely studies)

**TTS Duration**: ~180 min (3 hours)

### CLASS 2: Métodos (3 hours)
**24 slides total**
- PERT: (O + 4M + P) / 6
- CPM: Identifies long sequence (but ignores resources)
- Agile: T-Shirt sizing, Story Points (Fibonacci), Planning Poker
- Case: Authentication backlog with 5 user stories
- Planning Poker demonstration (HU-3: Password Reset)
- Velocity and Forecasting

**TTS Duration**: ~184 min (3h 4min)
**Note**: Slide 13 needs manual review (complex format)

### CLASS 3: Solución (3 hours)
**22 slides total**
- Critical Chain = CPM + Resources (THE FIX)
- 3 Buffer Types: Project, Feeding, Resource
- Fever Chart monitoring
- A-B-C-D walkthrough showing CPM fails, CCPM wins
- Resource conflict resolution

**TTS Duration**: ~180 min (3 hours)

---

## KEY FORMULAS

```
PERT: (O + 4M + P) / 6
PERT SD: (P - O) / 6
CCPM Buffer: 50% of Total Time Cut
Story Points: Fibonacci (0,1,2,3,5,8,13,21) - relative, NOT hours
Velocity: Story Points Completed / Sprint
Forecast: Total Points / Velocity = Number of Sprints
```

---

## VERSION HISTORY

### V2.1 (December 2025) - Professor Files + TTS
- Added clase#_profesor.html with dual TTS (browser + OpenAI)
- Externalized API keys to config.js (security)
- Synchronized 70 speech scripts across 3 classes
- Added fallback for missing config.js
- Fixed slide 7b (16 factors), 7c (risk table), 7d (risk matrix SVG)
- Documentation: SEGURIDAD_API_KEYS.md, GIT_PUSH_SUCCESS.md

### V2.0 (January 2025) - Remote Adaptation
- Marshmallow Challenge → Theoretical case study
- Parkinson Experiment → Real data analysis
- Planning Poker workshop → Guided walkthrough
- Physical CCPM calc → On-screen step-by-step
- Added 5 SVG graphics
- UI fixes for long content

### V1.0 (2024) - Original In-Person Course
- 3 HTML slide decks
- Interactive workshops
- Physical exercises

---

## FOR CLAUDE INSTANCES

### When Working on This Project:

1. **Read Context First**:
   - MEJORAS_REALIZADAS.md for V2.0 changes
   - SEGURIDAD_API_KEYS.md for security setup
   - This file for overview

2. **Testing**:
   - Test HTML files in browser
   - Verify keyboard navigation (arrows, Home, End)
   - Test TTS functionality (both browser and OpenAI if key available)
   - Check speech synchronization with slides

3. **Code Changes**:
   - NEVER hardcode API keys in files
   - Use CONFIG.OPENAI_API_KEY for external keys
   - Include fallback for missing config.js
   - Document changes in appropriate MD files

4. **Speech Synchronization**:
   - Each slide# must have corresponding speech in speechDataClase#
   - clase1: Uses slideToSpeechMap array (has slides 7, 7b, 7c, 7d)
   - clase2: Uses formula `slide${currentSlide + 1}` (sequential)
   - clase3: Uses formula `slide${currentSlide + 1}` (sequential)

5. **Git Practices**:
   - NEVER commit config.js (ignored by .gitignore)
   - ALWAYS commit config.example.js (template)
   - Run security checks before push (no API keys in files)
   - Use force push carefully (only for security fixes)

### Common Tasks:

#### Adding a New Speech:
```javascript
// In speechDataClaseX object:
"slideN": {
    "title": "Slide Title",
    "duration": "X min",
    "script": "Speech content here..."
}
```

#### Updating Speech Synchronization:
1. Check HTML slide number/title
2. Verify speech title matches
3. Test navigation in browser
4. Use verification scripts in temp/ folder

#### Testing Without OpenAI Key:
1. Open clase#_profesor.html in browser
2. Browser TTS works automatically
3. Console shows: "config.js not found - OpenAI TTS disabled"
4. All functionality works except OpenAI voices

---

## FACILITATION QUICK START

### Before Class:
1. Open `clase#_profesor.html` in browser
2. Read GUIA_FACILITADOR_TALLERES.md for timing
3. Choose TTS mode (browser or OpenAI)
4. Test audio levels
5. Have visible timer ready

### During Class:
1. Project HTML slides fullscreen
2. Use TTS or narrate manually
3. Follow facilitator guide scripts
4. Stop for debriefing (where learning happens)
5. Emphasize connections to real projects
6. Use arrow keys for navigation

### TTS Controls:
- **Play/Pause**: Click play button or use toggle
- **Speed**: Adjust 0.8x - 2x (default 1.2x for teaching)
- **Voice**: Select from dropdown (browser or OpenAI)
- **Navigation**: Speeches auto-sync with slide changes

### After Class:
- Share HTML files (student versions)
- Share study materials (materiales_alumnos/)
- Get feedback on timing
- Note: Don't share profesor files (contain speeches)

---

## SUCCESS CRITERIA

Participants understand:
- ✅ Why traditional estimates fail (Cone, Parkinson)
- ✅ How Uncertainty Cone works (±400% → ±10%)
- ✅ Parkinson's Law destroys padding
- ✅ 16 factors affecting estimation
- ✅ PERT formula and when to use it
- ✅ Story Points vs Hours (relative complexity)
- ✅ Planning Poker exposes hidden assumptions
- ✅ Velocity enables empirical forecasting
- ✅ Critical Chain (not Path) matters
- ✅ Buffers managed at project level, not task level
- ✅ A-B-C-D case: CPM fails, CCPM wins

---

## TECHNICAL STACK

### Student Files (clase#.html):
- HTML5 (self-contained)
- CSS3 (dark theme, responsive)
- JavaScript (navigation only)
- SVG (inline graphics)
- ~1200 lines each
- No external dependencies

### Professor Files (clase#_profesor.html):
- HTML5 + CSS3 + JavaScript
- Speech data embedded (JSON-like objects)
- Dual TTS system:
  - Browser: Web Speech API (Spanish voices)
  - OpenAI: Fetch API to OpenAI TTS endpoint
- Synchronized sidebar with speech scripts
- ~2500 lines each
- External dependency: config.js (optional)

### Configuration:
- `config.js`: Plain JavaScript object with API key
- Loaded via `<script src="config.js">` with error handler
- Fallback to empty CONFIG object if missing

Works offline (browser TTS), requires internet for OpenAI TTS.

---

## TROUBLESHOOTING

### "Cannot access 'isSpeaking' before initialization"
**Solution**: Update to latest version with config.js fallback (v2.1+)

### OpenAI TTS not working
**Check**:
1. config.js exists? `ls config.js`
2. API key valid? Check OpenAI dashboard
3. Console errors? Open browser DevTools

### Speeches out of sync
**Check**:
1. HTML slide number matches speech key
2. For clase1: Verify slideToSpeechMap array
3. For clase2/3: Formula is `slide${currentSlide + 1}`
4. Run verification scripts in temp/ folder

### API key security
**Remember**:
- NEVER commit config.js
- ALWAYS use config.example.js as template
- Run `git diff --cached | grep "sk-"` before commit
- Read SEGURIDAD_API_KEYS.md for complete guide

---

## USEFUL COMMANDS

```bash
# Setup
cp config.example.js config.js
nano config.js  # Add your API key

# Test in browser
start clase1_profesor.html  # Windows
open clase1_profesor.html   # Mac
xdg-open clase1_profesor.html  # Linux

# Security check before commit
git diff --cached | grep -E "sk-proj|sk-svcacct"

# Verify speeches
python temp/verify_clase2.py

# Backup before changes
cp clase2_profesor.html clase2_profesor.html.backup
```

---

## FILES TO IGNORE IN GIT

Already in `.gitignore`:
- `config.js` (contains API key)
- `*.backup` (backup files)
- `temp/*.py` (verification scripts)
- `*.log` (logs)

---

## CONTACTS & RESOURCES

**Instructor**: Alejandro Sfrede
**Organization**: Área de Arquitectura
**OpenAI TTS**: https://platform.openai.com/docs/guides/text-to-speech
**Web Speech API**: https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API

---

**Last Updated**: December 2, 2025
**Version**: 2.1
**Created For**: Future Claude Instances
**Main Goal**: Estimate realistically by managing uncertainty, psychology, and resources
**New Goal**: Enable remote teaching with professional TTS narration
