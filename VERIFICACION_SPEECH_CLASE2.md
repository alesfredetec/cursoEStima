# Verificación de Speech Scripts - Clase 2

**Fecha:** 2025-01-01
**Archivo:** clase2_profesor.html
**Total Slides HTML:** 24
**Total Speech Scripts:** 18

---

## 🔍 Resumen Ejecutivo

**Estado:** ⚠️ **REQUIERE CORRECCIONES SIGNIFICATIVAS**

**Problemas Críticos Encontrados:**
1. ❌ **6 slides sin speech scripts** (25%)
2. ❌ **Desorden en slides 7-10** (scripts no corresponden)
3. ❌ **Mega-script en slide13** (debe dividirse en 5)
4. ⚠️ **Desalineación en slides finales** (21-24)

**Cobertura Actual:**
- ✅ Coincidencias perfectas: 7/24 (29%)
- ⚠️ Coincidencias parciales: 5/24 (21%)
- ❌ Desajustes: 6/24 (25%)
- ❌ Sin script: 6/24 (25%)

---

## 📊 Tabla de Mapeo Detallada

| # | Título Slide HTML | Key Script | Título Script | Estado | Problema |
|---|-------------------|------------|---------------|--------|----------|
| 1 | Portada | slide1 | Portada | ✅ | - |
| 2 | Agenda | slide2 | Agenda | ✅ | - |
| 3 | PERT: Estimación 3 Puntos | slide3 | Introducción a PERT | ✅ | - |
| 4 | Fórmulas PERT | slide4 | Fórmula PERT | ✅ | - |
| 5 | Ejemplo Práctico PERT | slide5 | PERT en Proyectos Complejos | ✅ | - |
| 6 | CPM: Critical Path Method | slide6 | CPM - Critical Path Method | ✅ | - |
| **7** | **Estimación Ágil: Cambio Paradigma** | **slide7** | **Combinando PERT y CPM** | ❌ | **DESAJUSTE TOTAL** |
| **8** | **T-Shirt Sizing** | **slide8** | **Introducción a Estimación Ágil** | ❌ | **DESAJUSTE ORDEN** |
| 9 | Story Points | slide9 | Story Points y Escala Fibonacci | ✅ | - |
| **10** | **La Secuencia de Fibonacci** | **slide10** | **T-Shirt Sizing** | ❌ | **INTERCAMBIADO** |
| 11 | Break (Preguntas) | - | - | ⚠️ | Sin script (aceptable) |
| 12 | Planning Poker Intro | slide11 | Planning Poker - Marco Teórico | ✅ | - |
| 13 | Caso: Backlog Autenticación | slide12 | Caso de Estudio - Backlog | ✅ | - |
| **14** | **Proceso Planning Poker** | **slide13** | **Demostración HU-3** | ⚠️ | Script largo cubre 14-17 |
| **15** | **La Discusión: Corazón Taller** | **(slide13)** | **(Demostración HU-3)** | ⚠️ | Cubierto por slide13 |
| **16** | **Re-votación y Consenso** | **(slide13)** | **(Demostración HU-3)** | ⚠️ | Cubierto por slide13 |
| **17** | **Debriefing: Lecciones** | **(slide13)** | **(Demostración HU-3)** | ⚠️ | Cubierto por slide13 |
| 18 | Velocidad: Points → Forecasting | slide14 | Velocidad - Concepto y Cálculo | ✅ | - |
| 19 | Flujo Refinamiento Progresivo | slide15 | Forecasting con Velocidad | ⚠️ | Temas relacionados pero diferentes |
| 20 | Cuadro Comparativo Métodos | slide16 | Cuadro Comparativo | ✅ | - |
| **21** | **¿Cuándo Usar Cada Método?** | **-** | **-** | ❌ | **SIN SCRIPT** |
| 22 | La Pregunta Crítica (Reprise) | slide17 | Síntesis de Clase 2 | ⚠️ | Offset, contenido diferente |
| **23** | **Resumen de la Clase 2** | **-** | **-** | ❌ | **SIN SCRIPT** |
| 24 | Fin | slide18 | Cierre y Preview Clase 3 | ⚠️ | Relacionado pero offset |

---

## ❌ Problema Crítico #1: Desorden Slides 7-10

### Situación Actual (INCORRECTA)

**HTML Slide 7:** "Estimación Ágil: El Cambio de Paradigma"
- Contenido visual: Introducción a métodos ágiles, diferencias con métodos tradicionales

**Speech slide7:** "Combinando PERT y CPM"
- Contenido narrado: Cómo usar PERT y CPM juntos, ejemplo con 6 tareas

❌ **RESULTADO:** Profesor lee sobre PERT/CPM mientras la pantalla muestra introducción a Ágil

---

**HTML Slide 8:** "T-Shirt Sizing"
- Contenido visual: XS, S, M, L, XL - tallas para estimar

**Speech slide8:** "Introducción a Estimación Ágil"
- Contenido narrado: Story Points vs horas, por qué Ágil cambia el paradigma

❌ **RESULTADO:** Profesor introduce Ágil mientras la pantalla muestra T-Shirt Sizing

---

**HTML Slide 10:** "La Secuencia de Fibonacci"
- Contenido visual: 0, 1, 2, 3, 5, 8, 13, 21... explicación matemática

**Speech slide10:** "T-Shirt Sizing"
- Contenido narrado: XS/S/M/L/XL, cuándo usar, mapeo a Fibonacci

❌ **RESULTADO:** Profesor habla de T-Shirt mientras pantalla muestra Fibonacci

---

### Corrección Necesaria

**Reordenar scripts:**

1. **slide6:** Mantener CPM (correcto)
2. **slide7 (nuevo):** Mover contenido de slide8 actual → "Introducción a Estimación Ágil"
3. **slide8 (nuevo):** Mover contenido de slide10 actual → "T-Shirt Sizing"
4. **slide9:** Mantener Story Points (correcto)
5. **slide10 (nuevo):** Crear script para Fibonacci (actualmente mal ubicado)

**O alternativa:** Mover script actual de slide7 (PERT+CPM) a final de slide6 como extensión.

---

## ❌ Problema Crítico #2: Mega-Script slide13

### Situación Actual

**slide13:** "Demostración - Historia HU-3 (Password Reset)"
- **Duración:** 15 minutos
- **Longitud:** 340+ líneas de script
- **Contenido:** Cubre TODO el proceso de Planning Poker:
  - Presentación de historia HU-3
  - Primera votación (2 vs 13)
  - Discusión de extremos (Ana explica 2, Pedro explica 13)
  - Revelación de suposiciones ocultas
  - Re-votación
  - Consenso final (5+3 dividido)
  - Debriefing y lecciones

### Problema

Este script intenta cubrir **5 slides HTML** (13-17) con una sola narración.

**Slides HTML afectados:**
- Slide 13: Caso de Estudio - Backlog de Autenticación
- Slide 14: Proceso de Planning Poker (Paso a Paso)
- Slide 15: La Discusión: El Corazón del Taller
- Slide 16: Re-votación y Consenso
- Slide 17: Debriefing: Lecciones del Planning Poker

### Impacto

- ✅ **Bueno:** El profesor tiene script completo para narrar toda la demo
- ❌ **Malo:** Sidebar no actualiza al cambiar slides 14, 15, 16, 17
- ❌ **Malo:** Timing incorrecto (15 min total, pero 5 slides individuales)
- ❌ **Malo:** Profesor no sabe cuándo avanzar slide (no hay marcadores visuales)

### Corrección Necesaria

**Dividir mega-script en 5 partes:**

**slide13** (3 min): Presentación del caso
```
- Backlog de autenticación (5 historias)
- Contexto del equipo
- Focus en HU-3: Password Reset
- Votación inicial
```

**slide14** (3 min): Primera ronda
```
- Mostrar cartas: 2, 3, 5, 8, 13
- Identificar extremos (Ana: 2, Pedro: 13)
- [TRANSICIÓN a discusión]
```

**slide15** (4 min): La discusión
```
- Ana explica su 2 (asume OAuth existente)
- Pedro explica su 13 (asume construir desde cero)
- Revelación: suposiciones diferentes
- Equipo alinea contexto
```

**slide16** (3 min): Re-votación
```
- Segunda ronda con contexto alineado
- Nuevos votos: 5, 5, 5, 8, 8
- Convergencia visible
- Decisión: dividir historia
```

**slide17** (2 min): Debriefing
```
- Lecciones: Planning Poker expone suposiciones
- No es sobre "acertar" el número
- Es sobre alineación del equipo
- [TRANSICIÓN a Velocidad]
```

---

## ❌ Problema Crítico #3: Slides Finales Sin Scripts

### Slides Faltantes

**Slide 21:** "¿Cuándo Usar Cada Método?"
- **Contenido visual:** Tabla de decisión (Proyecto, Contexto → Método recomendado)
- **Script actual:** ❌ No existe
- **Importancia:** 🔴 ALTA - Es el cierre conceptual, framework de decisión
- **Duración sugerida:** 8 min

**Slide 23:** "Resumen de la Clase 2"
- **Contenido visual:** Lista de conceptos clave aprendidos
- **Script actual:** ❌ No existe
- **Importancia:** 🔴 ALTA - Síntesis final, refuerza aprendizajes
- **Duración sugerida:** 5 min

### Impacto Pedagógico

Sin estos scripts:
- ❌ Clase termina abrupta (no hay cierre)
- ❌ Alumnos no reciben síntesis de 3 horas de contenido
- ❌ No hay framework práctico para aplicar lo aprendido
- ❌ Conexión con Clase 3 es débil

### Corrección Necesaria

**Crear slide21 script:** (Inspirado en slide 21 HTML)
```
Tema: Framework de decisión
Contenido:
- PERT/CPM: Proyectos con fases claras, pocas interdependencias
- Ágil: Productos con cambio frecuente, equipos auto-organizados
- CCPM: Proyectos con recursos compartidos, alta interdependencia
- Tabla de decisión con ejemplos
```

**Crear slide23 script:**
```
Tema: Síntesis Clase 2
Contenido:
- 3 métodos, 3 contextos
- PERT: Cuantifica incertidumbre (O-M-P)
- CPM: Identifica ruta crítica (pero ignora recursos)
- Ágil: Story Points + Velocidad (complejidad relativa)
- Planning Poker: Alineación > precisión
- Preview Clase 3: Critical CHAIN (no Path)
```

---

## ⚠️ Problema #4: Desalineación Slides 19, 22, 24

### Slide 19: Flujo de Refinamiento Progresivo

**HTML Slide 19:** "Flujo de Refinamiento Progresivo"
- Contenido visual: Diagrama de refinamiento (Epic → Historias → Estimadas → Sprint)

**Speech slide15:** "Forecasting con Velocidad"
- Contenido narrado: Cómo usar velocidad para forecast de fechas

⚠️ **Problema:** Temas relacionados pero NO idénticos
- slide15 habla de forecasting
- slide19 visual muestra refinamiento progresivo

**Corrección:**
- Renombrar slide15 → "Velocidad y Forecasting"
- Crear slide16 nuevo → "Flujo de Refinamiento Progresivo"
- Ajustar numeración posterior

---

### Slide 22: La Pregunta Crítica (Reprise)

**HTML Slide 22:** "La Pregunta Crítica (Reprise)"
- Contenido visual: Retoma pregunta de Clase 1 sobre buffers

**Speech slide17:** "Síntesis de Clase 2"
- Contenido narrado: Resumen de métodos aprendidos

⚠️ **Problema:** Contenidos completamente diferentes
- slide17 speech = síntesis general
- slide22 visual = gancho específico para Clase 3

**Corrección:**
- Mover contenido de slide17 speech a slide23 speech (Resumen Clase 2)
- Crear slide22 speech nuevo → Gancho Clase 3 con pregunta de buffers

---

### Slide 24: Fin

**HTML Slide 24:** "Fin"
- Contenido visual: Agradecimientos, "Nos vemos en Clase 3"

**Speech slide18:** "Cierre y Preview Clase 3"
- Contenido narrado: Cierre + preview de CCPM

⚠️ **Problema:** Offset de 2 slides (debería ser slide24, no slide18)

**Corrección:** Renumerar slide18 → slide24

---

## 📋 Plan de Corrección Recomendado

### Fase 1: Correcciones Críticas (Prioridad ALTA)

1. **Reordenar scripts 7-10**
   - [ ] Mover slide7 actual (PERT+CPM) → final de slide6 o crear slide6b
   - [ ] Mover slide8 actual (Intro Ágil) → slide7
   - [ ] Crear slide8 nuevo para T-Shirt Sizing (parte de slide10 actual)
   - [ ] Mantener slide9 (Story Points) - ya correcto
   - [ ] Crear slide10 nuevo para Fibonacci (explicación matemática)

2. **Dividir mega-script slide13**
   - [ ] slide13 (3 min): Presentación caso + votación inicial
   - [ ] slide14 (3 min): Primera ronda y extremos
   - [ ] slide15 (4 min): Discusión y suposiciones
   - [ ] slide16 (3 min): Re-votación y convergencia
   - [ ] slide17 (2 min): Debriefing y lecciones

3. **Crear scripts faltantes**
   - [ ] slide21: ¿Cuándo usar cada método? (8 min)
   - [ ] slide23: Resumen de la Clase 2 (5 min)

### Fase 2: Ajustes de Alineación (Prioridad MEDIA)

4. **Ajustar slides 19, 22, 24**
   - [ ] Renombrar slide15 → "Velocidad y Forecasting"
   - [ ] Crear slide19: Flujo de Refinamiento Progresivo
   - [ ] Mover slide17 contenido → slide23
   - [ ] Crear slide22: Gancho Clase 3
   - [ ] Renumerar slide18 → slide24

### Fase 3: Validación (Prioridad MEDIA)

5. **Testing completo**
   - [ ] Navegar los 24 slides verificando speech corresponde
   - [ ] Verificar timing total (objetivo: ~180 min)
   - [ ] Verificar transiciones entre slides
   - [ ] Verificar que markers ([PAUSA], [ÉNFASIS]) estén presentes

---

## 📊 Estadísticas Actuales vs Objetivo

### Estado Actual

| Métrica | Actual | Objetivo | Gap |
|---------|--------|----------|-----|
| **Slides con script correcto** | 7/24 (29%) | 24/24 (100%) | -17 |
| **Scripts alineados** | 7/18 (39%) | 24/24 (100%) | -17 |
| **Cobertura completa** | 18/24 (75%) | 24/24 (100%) | -6 |
| **Scripts bien ubicados** | 12/18 (67%) | 24/24 (100%) | -12 |

### Estado Post-Corrección (Estimado)

| Métrica | Proyectado |
|---------|------------|
| **Slides con script correcto** | 24/24 (100%) ✅ |
| **Scripts alineados** | 24/24 (100%) ✅ |
| **Cobertura completa** | 24/24 (100%) ✅ |
| **Scripts bien ubicados** | 24/24 (100%) ✅ |

---

## 🎯 Comparación con Clase 1

| Aspecto | Clase 1 | Clase 2 | Evaluación |
|---------|---------|---------|------------|
| **Slides HTML** | 24 (21 + 3 visuales) | 24 | ✅ Igual |
| **Speech scripts** | 21 | 18 | ❌ Clase 2 tiene menos |
| **Cobertura** | 100% | 75% | ❌ Clase 2 incompleta |
| **Alineación** | 100% | 29% | ❌ Clase 2 desalineada |
| **Scripts correctos** | 21/21 | 7/24 | ❌ Clase 2 problemática |

**Conclusión:** Clase 2 requiere el mismo nivel de atención que se le dio a Clase 1 durante la sincronización.

---

## 🔧 Fuentes de Referencia

Para crear/corregir los scripts faltantes, usar:

**Archivo fuente:** `C:\tmp\cursoEStima\materiales_facilitador\SPEECH_SCRIPTS_CLASE2_COMPLETO.md`

**Secciones existentes en MD:**
- ✅ Slides 1-12: Ya mapeados correctamente
- ⚠️ Slide 13: Mega-script que debe dividirse
- ❌ Slides 14-17: Crear desde sección de slide 13 (dividir)
- ❌ Slide 19: Crear script "Refinamiento Progresivo"
- ❌ Slide 21: Crear script "¿Cuándo usar qué?"
- ❌ Slide 23: Crear script "Resumen Clase 2"

---

## ✅ Checklist de Verificación Post-Corrección

Al completar las correcciones, verificar:

- [ ] Cada slide HTML (1-24) tiene un speech script correspondiente
- [ ] Títulos de speech scripts coinciden con títulos de slides HTML
- [ ] Contenido de speech scripts es relevante al contenido visual
- [ ] Duraciones suman ~180 minutos (3 horas de clase)
- [ ] No hay scripts "huérfanos" sin slide correspondiente
- [ ] Numeración es secuencial (slide1, slide2, ..., slide24)
- [ ] Markers pedagógicos presentes ([PAUSA], [ÉNFASIS], [TRANSICIÓN])
- [ ] Archivo carga sin errores JavaScript
- [ ] TTS puede leer todos los scripts
- [ ] Sidebar actualiza correctamente al cambiar slides

---

## 🎓 Conclusión

**Estado Actual:** ⚠️ Clase 2 tiene problemas significativos de sincronización speech ↔ slides.

**Impacto en Enseñanza:**
- 🔴 CRÍTICO: Slides 7-10 confundirán al profesor y alumnos
- 🔴 CRÍTICO: Slides 21, 23 sin guía pedagógica (falta cierre)
- 🟡 MEDIO: Slides 14-17 funcionan pero sidebar no actualiza
- 🟡 MEDIO: Timing impreciso por scripts faltantes

**Esfuerzo de Corrección:**
- Tiempo estimado: 3-4 horas
- Complejidad: Media (requiere reorganización, no creación masiva)
- Fuente disponible: Sí (SPEECH_SCRIPTS_CLASE2_COMPLETO.md)

**Prioridad:** 🔴 **ALTA** - Debe corregirse antes de usar en producción.

---

**Reporte creado:** 2025-01-01
**Próximo paso:** Ejecutar Plan de Corrección (Fase 1 → Fase 2 → Fase 3)
