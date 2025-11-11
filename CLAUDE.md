# CursoEStima - Comprehensive Guide for Claude Instances

**Project Type**: Educational Course - Project Estimation & Risk Management  
**Duration**: 9 hours (3 classes x 3 hours)  
**Version**: 2.0 (January 2025)  
**Instructor**: Alejandro Sfrede

---

## QUICK SUMMARY

This is a complete, remote-ready 9-hour course teaching professionals to replace "inflated" estimation with systematic approaches (PERT, Agile, CCPM) that explicitly manage uncertainty and psychology.

**Three Classes**:
- Class 1: Why estimates fail (Uncertainty Cone, Parkinson's Law)
- Class 2: How to estimate (PERT, Story Points, Planning Poker)  
- Class 3: Critical Chain CCPM (Resource-aware scheduling with buffers)

---

## MUST-READ FILES

1. RESUMEN_CURSO.md - Course structure
2. MEJORAS_REALIZADAS.md - V2.0 changes
3. materiales_facilitador/GUIA_FACILITADOR_TALLERES.md - How to teach (1086 lines)
4. INSTRUCCIONES_USO.md - How to use
5. This file (CLAUDE.md) for overview

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
  clase1.html (1170 lines)
  clase2.html (1133 lines)
  clase3.html (1671 lines)
  index.html
  
  RESUMEN_CURSO.md
  INSTRUCCIONES_USO.md
  MEJORAS_REALIZADAS.md
  CLAUDE.md
  
  materiales_facilitador/
    GUIA_FACILITADOR_TALLERES.md (1086 lines - CRITICAL)
    GUIA_PROFESOR_CLASE*.md
    
  materiales_alumnos/
    MATERIAL_ESTUDIO_CLASE*.md
    EJERCICIO_PARKINSON_*.md
    
  doc/
    adminpro/ (40 reference PDFs)
    guiasyejemplos/ (templates)
```

---

## THE THREE CLASSES OVERVIEW

### CLASS 1: La Crisis (3 hours)
- Uncertainty Cone (±400% start to ±10% end)
- Parkinson's Law (work expands to fill time)
- Student Syndrome (procrastination)
- Workshops replaced with research analysis (Tom Wujec, Microsoft, Ariely studies)

### CLASS 2: Métodos (3 hours)
- PERT: (O + 4M + P) / 6
- CPM: Identifies long sequence (but ignores resources)
- Agile: T-Shirt sizing, Story Points (Fibonacci), Planning Poker
- Case: Authentication backlog with 5 user stories

### CLASS 3: Solución (3 hours)
- Critical Chain = CPM + Resources (THE FIX)
- 3 Buffer Types: Project, Feeding, Resource
- Fever Chart monitoring
- A-B-C-D walkthrough showing CPM fails, CCPM wins

---

## KEY FORMULAS

PERT: (O + 4M + P) / 6
CCPM Buffer: 50% of Total Time Cut
Story Points: Fibonacci (0,1,2,3,5,8,13,21) - relative, NOT hours

---

## VERSION 2.0 CHANGES

Adapted from in-person to remote:
- Marshmallow Challenge → Theoretical case study analysis
- Parkinson Experiment → Real data (Microsoft, Dan Ariely)
- Planning Poker workshop → Walkthrough + case analysis
- Physical CCPM calc → Guided step-by-step on screen

Added:
- 5 SVG graphics (Cone, Risk Matrix, Buffers, Fever Chart)
- UI fixes (scrolling for long content)
- 4 new theory slides

---

## FOR CLAUDE INSTANCES

When working on this project:
1. Read MEJORAS_REALIZADAS.md for context
2. Understand why V2.0 went remote
3. Check GUIA_FACILITADOR_TALLERES.md for teaching methodology
4. Test HTML files in browser
5. Verify keyboard navigation (arrows, Home, End)
6. Document changes in MEJORAS_REALIZADAS.md

---

## FACILITATION QUICK START

**Before Class**:
- Open clase#.html
- Read GUIA_FACILITADOR_TALLERES.md for timing
- Have visible timer ready

**During Class**:
- Project HTML slides
- Follow facilitator guide scripts
- Stop for debriefing (this is where learning happens)
- Emphasize connections to real projects

**After Class**:
- Share HTML files + study materials
- Get feedback on timing

---

## SUCCESS CRITERIA

Participants understand:
- Why traditional estimates fail
- How Uncertainty Cone works
- Parkinson's Law destroys padding
- PERT, Story Points, Planning Poker are tools
- Critical Chain (not Path) matters
- Buffers managed at project level, not task level
- A-B-C-D case shows why CPM fails, CCPM works

---

## TECHNICAL STACK

- HTML5 (self-contained)
- CSS3 (dark theme, responsive)
- JavaScript (navigation only)
- SVG (4 inline graphics)
- ~4000 lines total
- No external dependencies

Works offline, runs locally or via HTTP server.

---

**Last Updated**: January 2025  
**Created For**: Future Claude Instances  
**Main Goal**: Estimate realistically by managing uncertainty, psychology, and resources
