# Anexo 3: Plantillas y Herramientas Prácticas

**Curso:** Estimación de Proyectos
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 1.0 - Enero 2025

---

## 📋 Índice de Contenidos

1. [Plantillas PERT](#plantillas-pert)
2. [Plantillas Planning Poker](#plantillas-poker)
3. [Plantillas CCPM y Fever Chart](#plantillas-ccpm)
4. [Herramientas Online Recomendadas](#herramientas-online)
5. [Checklists y Guías Rápidas](#checklists)

---

## 📊 Plantillas PERT {#plantillas-pert}

### Plantilla 1: Hoja de Cálculo PERT (Excel/Sheets)

**Instrucciones de uso:**

1. Copia esta estructura a Excel o Google Sheets
2. Completa las columnas O, M, P para cada tarea
3. Las fórmulas calcularán automáticamente μ y σ

**Estructura de la tabla:**

```
| Tarea | Descripción | O (días) | M (días) | P (días) | μ (días) | σ (días) | Notas |
|-------|-------------|----------|----------|----------|----------|----------|-------|
| A | Análisis requisitos | 3 | 5 | 10 | =FÓRMULA | =FÓRMULA | |
| B | Diseño arquitectura | 5 | 8 | 15 | =FÓRMULA | =FÓRMULA | |
| C | Desarrollo backend | 10 | 15 | 25 | =FÓRMULA | =FÓRMULA | |
```

**Fórmulas de Excel:**

```excel
Celda F2 (μ para tarea A):
=(C2 + 4*D2 + E2) / 6

Celda G2 (σ para tarea A):
=(E2 - C2) / 6
```

**Fórmula para suma de duraciones esperadas:**
```excel
Celda F_total:
=SUM(F2:F10)  // Suma de todos los μ
```

**Fórmula para desviación estándar total (asumiendo independencia):**
```excel
Celda G_total:
=SQRT(SUMSQ(G2:G10))  // √(σ₁² + σ₂² + ... + σₙ²)
```

---

### Plantilla 2: Informe PERT Completo

```markdown
# Estimación PERT: [Nombre del Proyecto]

**Fecha:** [DD/MM/YYYY]
**Estimador(es):** [Nombres]
**Revisado por:** [Nombre del PM/Líder]

---

## Resumen Ejecutivo

**Duración Total Esperada:** [X] días
**Rango de Confianza (68%):** [X-σ] a [X+σ] días
**Rango de Confianza (95%):** [X-2σ] a [X+2σ] días

---

## Detalle por Tarea

### Tarea 1: [Nombre]

| Escenario | Días | Probabilidad | Justificación |
|-----------|------|--------------|---------------|
| **Optimista** | X | ~1% | [Descripción del mejor caso] |
| **Más Probable** | Y | ~Modal | [Descripción del caso realista] |
| **Pesimista** | Z | ~1% | [Descripción del peor caso] |

**Estimación PERT:**
- μ = (X + 4Y + Z) / 6 = [resultado] días
- σ = (Z - X) / 6 = [resultado] días

**Riesgos identificados:**
- [Riesgo 1]
- [Riesgo 2]

**Mitigaciones propuestas:**
- [Acción 1]
- [Acción 2]

---

[Repetir para cada tarea]

---

## Análisis de Ruta Crítica

**Tareas en secuencia:**
1. Tarea A → Tarea B → Tarea C

**Duración total de ruta crítica:**
- μ_total = [suma de μ] días
- σ_total = √(σ_A² + σ_B² + ...) = [resultado] días

---

## Recomendaciones

1. [Recomendación basada en análisis de incertidumbre]
2. [Consideraciones de riesgo]
3. [Propuesta de fases o paralelismo si aplicable]

---

## Anexos

- Supuestos técnicos
- Dependencias externas
- Recursos requeridos
```

---

### Plantilla 3: Checklist de Validación PERT

Antes de presentar tu estimación PERT, verifica:

```
VALIDACIÓN DE ESTIMACIONES PERT

□ Cada tarea tiene justificación escrita para O, M, P
□ Optimista (O) es REALMENTE optimista (~1% probabilidad)
□ Pesimista (P) es REALMENTE pesimista (~99% probabilidad)
□ No hay "olvidos" obvios (testing, documentación, reuniones)
□ Dependencias están documentadas
□ Recursos necesarios están identificados
□ Riesgos principales están listados
□ Desviación estándar alta (σ > 30% de μ) tiene plan de mitigación

REVISIÓN DE SUPUESTOS

□ Supuestos técnicos documentados
□ Disponibilidad de recursos confirmada
□ Dependencias externas identificadas
□ Aprobaciones necesarias listadas
□ Ventanas de mantenimiento consideradas (si aplican)

COMUNICACIÓN

□ Stakeholders entienden que μ NO es promesa fija
□ Rango de confianza (68% y 95%) está comunicado
□ Plan de contingencia para peor caso existe
```

---

## 🎴 Plantillas Planning Poker {#plantillas-poker}

### Plantilla 4: Backlog de Historias de Usuario para Planning Poker

```markdown
# Backlog: [Nombre del Sprint/Release]

**Fecha de estimación:** [DD/MM/YYYY]
**Equipo:** [Nombres de participantes]
**Product Owner:** [Nombre]
**Facilitador:** [Nombre]

---

## Historia de Referencia (Baseline)

**ID:** HU-REF
**Historia:** [Descripción completa]
**Story Points asignados:** X puntos
**Justificación:** Esta historia fue completada en sprint anterior y tomó [Y] días de trabajo efectivo.

---

## Historias a Estimar

### HU-[Número]: [Título corto]

**Como** [tipo de usuario]
**Quiero** [acción/funcionalidad]
**Para** [beneficio/objetivo]

**Criterios de Aceptación:**
1. [Criterio 1 - medible y verificable]
2. [Criterio 2]
3. [Criterio 3]

**Notas técnicas:**
- [Detalles de implementación conocidos]
- [Dependencias con otras historias]
- [Restricciones técnicas]

**Mockups/Referencias:** [Link o "Ver anexo"]

**Preguntas frecuentes:**
- **P:** [Pregunta típica]
- **R:** [Respuesta del PO]

---

**ESTIMACIÓN:**

Primera votación: [Anotar votos]
Discusión: [Resumen de puntos clave discutidos]
Segunda votación (si necesario): [Anotar votos]
**Consenso final: [ ] Story Points**

---

[Repetir para cada historia]

---

## Resumen del Sprint

| ID | Historia | Story Points | Prioridad |
|----|----------|--------------|-----------|
| HU-X | [Título] | X pts | Alta |
| HU-Y | [Título] | Y pts | Media |
| ... | ... | ... | ... |

**Total Story Points:** [Suma]
**Velocity del equipo:** [Puntos/sprint basado en histórico]
**Capacidad este sprint:** [Puntos considerando vacaciones, feriados, etc.]
**Compromiso:** [Puntos a comprometer basado en capacidad]

---

## Decisiones y Acciones

- [Decisión 1: ej. "HU-15 necesita spike técnico"]
- [Acción 1: ej. "Carlos investigará API de proveedor antes del sprint"]
```

---

### Plantilla 5: Acta de Sesión de Planning Poker

```markdown
# Acta de Planning Poker

**Proyecto:** [Nombre]
**Sprint:** [Número]
**Fecha:** [DD/MM/YYYY]
**Duración:** [HH:MM] (de XX:XX a YY:YY)

---

## Participantes

| Rol | Nombre | Presente |
|-----|--------|----------|
| Product Owner | [Nombre] | ✅ |
| Scrum Master / Facilitador | [Nombre] | ✅ |
| Developer 1 | [Nombre] | ✅ |
| Developer 2 | [Nombre] | ❌ (ausente) |
| ... | ... | ... |

---

## Historia de Referencia

**HU-REF:** [Breve descripción] = **X Story Points**

---

## Historias Estimadas

### HU-101: [Título]

**Descripción:** [1-2 líneas]

**Votación 1:**
| Dev A | Dev B | Dev C | Dev D | Dev E |
|-------|-------|-------|-------|-------|
| 5 | 5 | 8 | 13 | 5 |

**Dispersión:** 5 a 13 (ratio 2.6x) → Requiere discusión

**Discusión clave:**
- Dev D (13): "Veo complejidad en [X] que otros no mencionaron"
- Dev A (5): "Ah, no había considerado [X]"
- Aclaración del PO: [Respuesta a dudas]

**Votación 2:**
| Dev A | Dev B | Dev C | Dev D | Dev E |
|-------|-------|-------|-------|-------|
| 8 | 8 | 8 | 8 | 8 |

**Consenso:** ✅ **8 Story Points**

---

[Repetir para cada historia]

---

## Historias que Requieren Más Trabajo

| ID | Razón | Acción Siguiente | Responsable | Deadline |
|----|-------|------------------|-------------|----------|
| HU-105 | Mockups incompletos | PO completará diseño | [Nombre PO] | [Fecha] |
| HU-108 | Dependencia técnica incierta | Spike de 2 días | [Dev] | [Fecha] |

---

## Métricas de la Sesión

- **Historias estimadas:** [Número]
- **Tiempo promedio por historia:** [Minutos]
- **Historias que requirieron re-votación:** [Número] ([X]%)
- **Historias diferidas por falta de info:** [Número]

---

## Decisiones y Acuerdos

1. [Decisión 1]
2. [Decisión 2]

---

## Próximos Pasos

- [ ] [Acción 1] - [Responsable] - [Fecha]
- [ ] [Acción 2] - [Responsable] - [Fecha]

---

**Acta preparada por:** [Nombre del Facilitador]
**Aprobada por:** [Nombre del PO]
```

---

### Plantilla 6: Cartas de Planning Poker (Para Imprimir)

Si quieres crear cartas físicas, usa este template:

```
INSTRUCCIONES DE IMPRESIÓN:

1. Imprime en cartulina (200-300 gsm)
2. Tamaño sugerido: 8.5 cm × 5.5 cm (tamaño póker estándar)
3. Plastifica o usa fundas de cartas (opcional)
4. Crea 1 mazo por participante

CONTENIDO DEL MAZO (13 cartas por persona):

Frente de cada carta:
- Número grande centrado
- Fondo con gradiente sutil

Reverso:
- Logo del equipo o empresa
- Texto: "Planning Poker - [Nombre del Equipo]"

VALORES (secuencia Fibonacci):
0, ½, 1, 2, 3, 5, 8, 13, 21, 40, 100, ?, ☕

SIGNIFICADO DE CARTAS ESPECIALES:

? (Interrogación) = "No puedo estimar, necesito más información"
☕ (Taza de café) = "Estoy cansado, hagamos un break"
0 (Cero) = "Esta historia ya está hecha" o "Es trivial (< 1 hora)"
½ (Medio) = "Muy pequeña pero no cero (1-2 horas)"
100 = "Esta historia es ENORME, debe splitarse"
```

**Archivo para diseñador:**
```
Especificaciones técnicas:

Tamaño: 8.5cm × 5.5cm (con 3mm de sangrado)
Resolución: 300 DPI
Formato: CMYK para impresión
Tipografía: Sans-serif bold, mínimo 48pt para el número
Colores sugeridos:
  - 0-3: Verde (#51cf66)
  - 5-8: Azul (#667eea)
  - 13-21: Amarillo (#ffc107)
  - 40-100: Rojo (#ff6b6b)
  - ?, ☕: Gris (#a0a0a0)
```

---

## ⛓️ Plantillas CCPM y Fever Chart {#plantillas-ccpm}

### Plantilla 7: Hoja de Cálculo CCPM Completa

**Estructura en Excel/Sheets:**

**HOJA 1: Definición de Proyecto**

```
| Tarea | Descripción | Predecesora | Duración Tradicional | Duración Agresiva (50%) | Recurso | Tipo |
|-------|-------------|-------------|---------------------|------------------------|---------|------|
| A | Análisis | - | 10 días | 5 días | Juan | CC |
| B | Diseño | A | 8 días | 4 días | Ana | CC |
| C | Frontend | B | 12 días | 6 días | Pedro | NC |
| D | Backend | B | 10 días | 5 días | Ana | CC |
| E | Testing | C, D | 8 días | 4 días | María | CC |

Leyenda:
CC = Cadena Crítica
NC = No Crítica (alimenta a CC)
```

**HOJA 2: Cálculo de Cadena Crítica**

```
IDENTIFICACIÓN DE CADENA CRÍTICA (considerando recursos):

Ruta 1: A → B → D → E = 5+4+5+4 = 18 días
Ruta 2: A → B → C → E = 5+4+6+4 = 19 días

Restricción de recursos:
- Ana hace B y D → NO pueden ir en paralelo
- C y D van en paralelo SOLO si recursos diferentes

CADENA CRÍTICA FINAL: A → B → D → E = 18 días

Rutas que alimentan (No Críticas):
- C (Frontend): 6 días → alimenta a E
```

**HOJA 3: Dimensionamiento de Buffers**

```
CÁLCULO DE PROJECT BUFFER:

Método 1 - Corte del 50%:
Tarea A: 10 → 5 (cortado 5)
Tarea B: 8 → 4 (cortado 4)
Tarea D: 10 → 5 (cortado 5)
Tarea E: 8 → 4 (cortado 4)

Total cortado en CC: 18 días
Project Buffer = 50% × 18 = 9 días

Método 2 - SSQ (Sum of Squares):
PB = √(5² + 4² + 5² + 4²) = √(25+16+25+16) = √82 ≈ 9 días

RESULTADO: Project Buffer = 9 días

---

CÁLCULO DE FEEDING BUFFER:

Tarea C (Frontend, no crítica):
Tradicional: 12 días
Agresiva: 6 días
Cortado: 6 días

Feeding Buffer (C→E) = 50% × 6 = 3 días

---

TIMELINE FINAL:

Cadena Crítica: 18 días
Project Buffer: 9 días
TOTAL: 27 días

vs Enfoque Tradicional: 10+8+max(12,10)+8 = 38 días
AHORRO: 29% del tiempo tradicional
```

**HOJA 4: Fever Chart (Tracker)**

```
| Semana | Fecha | % CC Completado | Días CC usados | % Buffer Consumido | Días Buffer usados | Zona | Notas |
|--------|-------|-----------------|----------------|-------------------|-------------------|------|-------|
| 1 | 01/02 | 15% | 2.7 / 18 | 0% | 0 / 9 | 🟢 | Inicio normal |
| 2 | 08/02 | 30% | 5.4 / 18 | 5% | 0.5 / 9 | 🟢 | Pequeño delay en A |
| 3 | 15/02 | 50% | 9 / 18 | 15% | 1.5 / 9 | 🟢 | Recuperado |
| 4 | 22/02 | 70% | 12.6 / 18 | 35% | 3.5 / 9 | 🟡 | Testing encontró bugs |
| 5 | 01/03 | 90% | 16.2 / 18 | 50% | 4.5 / 9 | 🟢 | Bugs resueltos |
| 6 | 08/03 | 100% | 18 / 18 | 60% | 5.5 / 9 | ✅ | Completado, 3.5 días buffer sobrante |

INTERPRETACIÓN:

Zona Verde (🟢): % Buffer < % CC → Todo bien
Zona Amarilla (🟡): % Buffer ≈ % CC → Monitorear de cerca
Zona Roja (🔴): % Buffer > % CC → Acción inmediata

Proyecto terminó usando 60% del buffer (5.5 de 9 días).
40% del buffer quedó sin usar → Buena señal (protección funcionó sin desperdicio).
```

---

### Plantilla 8: Fever Chart Visual (Excel con Gráfico)

**Instrucciones para crear en Excel:**

1. **Preparar datos:**
```
Columna A: % CC Completado (0%, 10%, 20%, ..., 100%)
Columna B: % Buffer Consumido (datos reales del proyecto)
Columna C: Línea Ideal (0%, 10%, 20%, ..., 100%) [mismos valores que Columna A]
```

2. **Crear gráfico de dispersión:**
- Seleccionar datos (Columnas A, B, C)
- Insertar → Gráfico de Dispersión con Líneas
- Eje X: % CC Completado
- Eje Y: % Buffer Consumido

3. **Agregar zonas de color:**
- Zona Verde: Área bajo línea ideal
- Zona Amarilla: Banda alrededor de línea ideal (±15%)
- Zona Roja: Área sobre línea ideal

**Fórmulas de alertas automáticas:**

```excel
Celda "Zona actual":
=IF(B2 < A2*0.85, "🟢 VERDE", IF(B2 < A2*1.15, "🟡 AMARILLA", "🔴 ROJA"))

Celda "Proyección final":
=SI(A2>0, B2/A2*100, "N/A") & "% buffer total proyectado"

Celda "Alerta":
=SI(Zona="🔴 ROJA", "⚠️ ACCIÓN INMEDIATA REQUERIDA",
    SI(Zona="🟡 AMARILLA", "⚠️ Monitorear de cerca",
    "✅ En buen estado"))
```

---

### Plantilla 9: Informe Semanal CCPM

```markdown
# Informe Semanal CCPM - Semana [#]

**Proyecto:** [Nombre]
**PM:** [Nombre]
**Fecha:** [DD/MM/YYYY]
**Periodo:** [Fecha inicio] a [Fecha fin]

---

## 📊 Estado del Proyecto

### Métricas Clave

| Métrica | Valor | Cambio vs Semana Anterior |
|---------|-------|---------------------------|
| **% Cadena Crítica Completada** | X% | +Y% |
| **% Project Buffer Consumido** | X% | +Y% |
| **Días CC usados / Total** | X / Y días | +Z días |
| **Días Buffer usados / Total** | X / Y días | +Z días |
| **Zona actual** | 🟢/🟡/🔴 | [Cambio] |

### Fever Chart

[Insertar gráfico actualizado]

**Interpretación:**
- [Análisis del estado actual]
- [Tendencia observada]
- [Proyección si continúa tendencia actual]

---

## ✅ Logros de la Semana

1. [Tarea completada 1] - [Responsable]
2. [Tarea completada 2] - [Responsable]

**Hitos alcanzados:**
- [Hito 1]

---

## 🚧 En Progreso

| Tarea | Responsable | % Completado | Estimado Fin | Bloqueadores |
|-------|-------------|--------------|--------------|--------------|
| [Tarea A] | [Nombre] | 60% | [Fecha] | Ninguno |
| [Tarea B] | [Nombre] | 30% | [Fecha] | [Bloqueador si aplica] |

---

## ⚠️ Riesgos y Issues

### Riesgos Activos

| # | Riesgo | Probabilidad | Impacto | Mitigación | Owner |
|---|--------|--------------|---------|------------|-------|
| R1 | [Descripción] | Alta/Media/Baja | Alto/Medio/Bajo | [Acción] | [Nombre] |

### Issues Abiertos

| # | Issue | Prioridad | Status | Acción Requerida | Owner | Deadline |
|---|-------|-----------|--------|------------------|-------|----------|
| I1 | [Descripción] | Alta | Bloqueante | [Acción] | [Nombre] | [Fecha] |

---

## 📈 Consumo de Buffers

### Project Buffer

- **Capacidad total:** 9 días
- **Consumido:** X días (Y%)
- **Restante:** Z días
- **Proyección:** [¿Alcanza? ¿Sobra? ¿Falta?]

### Feeding Buffers

| Ruta No Crítica | Buffer Total | Consumido | Restante | Estado |
|-----------------|--------------|-----------|----------|--------|
| Frontend → Testing | 3 días | 1 día | 2 días | ✅ OK |

---

## 🎯 Acciones Correctivas (si aplican)

| # | Acción | Razón | Responsable | Deadline | Status |
|---|--------|-------|-------------|----------|--------|
| A1 | [Descripción] | [Justificación] | [Nombre] | [Fecha] | [Status] |

---

## 📅 Plan para Próxima Semana

### Objetivos

1. [Objetivo 1]
2. [Objetivo 2]

### Tareas Críticas

- [ ] [Tarea en cadena crítica 1] - [Responsable]
- [ ] [Tarea en cadena crítica 2] - [Responsable]

### Recursos Críticos

- [Recurso X] necesario para [Tarea Y] - **Resource Buffer Alert:** [Fecha]

---

## 💬 Comentarios del PM

[Observaciones, preocupaciones, éxitos destacados]

---

**Próxima revisión:** [Fecha]
**Distribución:** [Lista de stakeholders]
```

---

## 🌐 Herramientas Online Recomendadas {#herramientas-online}

### Herramientas para Planning Poker

#### 1. **Planning Poker Online** (planningpokeronline.com)

**Características:**
- ✅ Gratis
- ✅ No requiere registro
- ✅ Crea salas privadas con código
- ✅ Cartas Fibonacci estándar
- ✅ Revela votos simultáneamente

**Uso:**
1. Crear sala
2. Compartir link con equipo
3. Facilitador controla reveal de votos

---

#### 2. **Scrum Poker for Jira** (Atlassian Marketplace)

**Características:**
- ✅ Integrado con Jira
- ✅ Estimaciones se guardan directo en el ticket
- ✅ Historial de sesiones
- ❌ De pago

---

#### 3. **Planit Poker** (planitpoker.com)

**Características:**
- ✅ Gratis
- ✅ Exporta resultados a CSV
- ✅ Permite cartas personalizadas
- ✅ Timer incorporado

---

### Herramientas para CCPM y Fever Chart

#### 1. **MS Project con ProChain** (plugin de pago)

**Características:**
- ✅ Cálculo automático de buffers
- ✅ Fever Chart integrado
- ✅ Resource leveling con CCPM
- ❌ Costo: ~$500/licencia

---

#### 2. **Excel Template (Gratis)**

Ver Plantilla 7 y 8 de este anexo.

---

#### 3. **Aurora CCPM** (software especializado)

**Características:**
- ✅ Diseñado específicamente para CCPM
- ✅ Multi-proyecto
- ✅ Fever Chart automático
- ❌ Costo: ~$2,000/año

---

#### 4. **Google Sheets Template con Apps Script**

Crea tu propio Fever Chart automatizado:

**Script básico para alertas:**

```javascript
function checkFeverChartZone() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Fever Chart");

  var ccCompleted = sheet.getRange("B2").getValue(); // % CC
  var bufferConsumed = sheet.getRange("C2").getValue(); // % Buffer

  var zone;
  if (bufferConsumed < ccCompleted * 0.85) {
    zone = "🟢 VERDE - Proyecto en buen estado";
  } else if (bufferConsumed < ccCompleted * 1.15) {
    zone = "🟡 AMARILLA - Monitorear de cerca";
  } else {
    zone = "🔴 ROJA - Acción inmediata requerida";
  }

  sheet.getRange("D2").setValue(zone);

  // Enviar email si zona roja
  if (zone.includes("ROJA")) {
    MailApp.sendEmail({
      to: "pm@company.com",
      subject: "⚠️ ALERTA: Proyecto en Zona Roja",
      body: "El proyecto ha entrado en zona roja del Fever Chart. Acción inmediata requerida."
    });
  }
}
```

---

### Herramientas para Seguimiento de Velocidad (Agile)

#### 1. **Jira Software**

- ✅ Burndown charts automáticos
- ✅ Velocity tracking
- ✅ Sprint planning integrado

---

#### 2. **Azure DevOps**

- ✅ Similar a Jira
- ✅ Integración con Microsoft ecosystem

---

#### 3. **Trello + Power-Up "Scrum for Trello"**

- ✅ Más simple que Jira
- ✅ Story points manuales
- ✅ Burndown básico

---

## ✅ Checklists y Guías Rápidas {#checklists}

### Checklist 1: Pre-Planning Poker

**24 horas antes de la sesión:**

```
PREPARACIÓN DEL PRODUCT OWNER:
□ Todas las historias tienen descripción completa
□ Criterios de Aceptación escritos
□ Mockups disponibles (si aplican)
□ Dependencias técnicas identificadas
□ Respuestas a preguntas frecuentes preparadas

PREPARACIÓN DEL FACILITADOR:
□ Sala de reunión reservada (física o virtual)
□ Cartas de Planning Poker disponibles (físicas o digitales)
□ Timer configurado
□ Plantilla de notas preparada
□ Historia de referencia comunicada al equipo

PREPARACIÓN DEL EQUIPO:
□ Todos revisaron el backlog ANTES de la sesión
□ Dudas técnicas básicas ya resueltas (no esperan a la reunión)
□ Tiempo bloqueado en calendario (sin interrupciones)
```

---

### Checklist 2: Durante Planning Poker

```
INICIO DE SESIÓN (5 min):
□ Confirmar asistencia completa
□ Recordar historia de referencia (baseline)
□ Explicar proceso (para nuevos integrantes)
□ Establecer time-box (max 10 min por historia)

POR CADA HISTORIA (10 min):
□ PO lee historia completa
□ PO aclara criterios de aceptación
□ Equipo hace preguntas (max 3 min)
□ Votación simultánea
□ Si dispersión >2x → Discutir extremos (max 4 min)
□ Re-votación si necesario
□ Consenso y anotar puntos

CIERRE DE SESIÓN (10 min):
□ Resumen de historias estimadas
□ Total de story points
□ Comparar con velocity del equipo
□ Identificar historias que necesitan más trabajo
□ Asignar acciones pendientes
```

---

### Checklist 3: Implementación de CCPM en Nuevo Proyecto

```
FASE 1: PREPARACIÓN (Semana -2 antes de inicio)

□ Buy-in de stakeholders clave (sponsor, ejecutivos)
□ Training de equipo completo (4 horas mínimo)
□ Explicar por qué CCPM (no imponer sin contexto)
□ Establecer cultura de "estimación agresiva = honestidad, no riesgo"

FASE 2: PLANNING (Semana -1)

□ Descomponer proyecto en tareas
□ Identificar dependencias (diagrama de red)
□ Asignar recursos a cada tarea
□ Estimar duración tradicional (con padding)
□ Estimar duración agresiva (50% probabilidad)
□ Calcular tiempo cortado por tarea

FASE 3: IDENTIFICAR CADENA CRÍTICA (Semana -1)

□ Identificar ruta más larga (considerando recursos)
□ Marcar tareas críticas
□ Identificar tareas no críticas que alimentan a CC
□ Validar restricciones de recursos (especialmente recursos compartidos)

FASE 4: DIMENSIONAR BUFFERS (Semana -1)

□ Calcular Project Buffer (50% o SSQ)
□ Calcular Feeding Buffers para rutas no críticas
□ Colocar Resource Buffers (alertas) 3-5 días antes de tareas críticas
□ Documentar todos los buffers

FASE 5: SETUP DE MONITOREO (Día 1 de proyecto)

□ Crear Fever Chart en Excel/herramienta
□ Establecer frecuencia de actualización (semanal recomendado)
□ Definir quién actualiza (PM o líder de proyecto)
□ Definir reunión de revisión semanal (15 min)
□ Establecer protocolo de escalamiento (zona amarilla → monitoreo, zona roja → acción)

FASE 6: EJECUCIÓN (Durante el proyecto)

□ Prohibir multitarea mala (enfoque finish-to-finish)
□ Actualizar Fever Chart semanalmente
□ Responder a Resource Buffer alerts con anticipación
□ Consumir Feeding Buffers cuando rutas no críticas se atrasen
□ Consumir Project Buffer SOLO cuando cadena crítica se atrase
□ Reunión semanal de 15 min para revisar estado

FASE 7: CIERRE Y RETROSPECTIVA (Al finalizar proyecto)

□ Documentar % de buffer usado (ideal: 60-80%)
□ Identificar qué funcionó bien
□ Identificar qué mejorar para próximo proyecto CCPM
□ Calcular ROI (tiempo ahorrado vs tradicional)
□ Compartir aprendizajes con organización
```

---

### Guía Rápida: Cuándo Usar Qué Método

```
┌─────────────────────────────────────────────────────────────────┐
│  DIAGRAMA DE DECISIÓN: ¿QUÉ MÉTODO DE ESTIMACIÓN USAR?          │
└─────────────────────────────────────────────────────────────────┘

¿Cuán incierto es el proyecto?

    │
    ├─ BAJA incertidumbre (tareas bien conocidas)
    │   │
    │   ├─ Proyecto pequeño (1-4 semanas)
    │   │   → ESTIMACIÓN EXPERTA (analogía, juicio)
    │   │
    │   └─ Proyecto mediano/grande
    │       │
    │       ├─ Muchas dependencias
    │       │   → PERT + CPM
    │       │
    │       └─ Recursos compartidos / múltiples proyectos
    │           → CCPM
    │
    ├─ MEDIA incertidumbre (requisitos emergentes)
    │   │
    │   ├─ Equipo ágil con sprints
    │   │   → PLANNING POKER + VELOCITY
    │   │
    │   └─ Equipo tradicional
    │       → PERT (con buffers altos)
    │
    └─ ALTA incertidumbre (R&D, innovación)
        │
        ├─ Puedes hacer experimentos rápidos
        │   → SPIKE + ITERACIÓN ÁGIL
        │
        └─ No puedes experimentar
            → NO ESTIMES. Usa FASES con GO/NO-GO decisions.

┌─────────────────────────────────────────────────────────────────┐
│  COMBINACIONES COMUNES QUE FUNCIONAN:                            │
└─────────────────────────────────────────────────────────────────┘

✅ PERT + Planning Poker:
   Usa PERT para tareas técnicas conocidas.
   Usa Poker para features nuevas.

✅ Planning Poker + CCPM:
   Estima con Poker (story points).
   Gestiona múltiples sprints con CCPM (buffers entre sprints).

✅ Estimación Experta + CCPM:
   En proyectos pequeños, PM estima rápido.
   CCPM protege el timeline con buffers.

❌ COMBINACIONES QUE NO FUNCIONAN:

❌ CPM + Estimación Optimista:
   CPM asume recursos ilimitados.
   Estimación optimista ignora incertidumbre.
   Resultado: Guaranteed failure.

❌ Planning Poker + Multitarea Masiva:
   Poker expone complejidad.
   Multitarea la ignora.
   Desperdicia el esfuerzo de estimar.
```

---

## 📚 Recursos Adicionales

### Libros Recomendados

1. **"Software Estimation: Demystifying the Black Art"** - Steve McConnell (2006)
   - Cono de Incertidumbre, PERT, mejores prácticas

2. **"Agile Estimating and Planning"** - Mike Cohn (2005)
   - Story Points, Planning Poker, Velocity

3. **"Critical Chain"** - Eliyahu Goldratt (1997)
   - CCPM, Teoría de Restricciones (TOC)

4. **"The Mythical Man-Month"** - Fred Brooks (1975)
   - Clásico sobre estimación y proyectos de software

---

### Artículos y Papers

- **"The Cone of Uncertainty"** - Steve McConnell (IEEE Software, 2005)
- **"Planning Poker: An Agile Estimating and Planning Technique"** - Mike Cohn (Mountain Goat Software)
- **"Critical Chain Project Management"** - Larry Leach (PM Network, 1999)

---

### Comunidades y Foros

- **Project Management Institute (PMI)** - pmi.org
- **Scrum Alliance** - scrumalliance.org
- **TOC International Certification Organization** - tocico.org

---

## 📞 Soporte

**Instructor:** Alejandro Sfrede
**Área:** Arquitectura
**Email:** [tu_email_aquí]

**Repositorio del curso:**
`C:\tmp\cursoEStima\`

---

**Fin del Anexo 3**

**Versión:** 1.0
**Última actualización:** Enero 2025

---

## 🎓 Próximos Pasos

Con estas plantillas y herramientas, estás listo para:

1. ✅ Realizar sesiones de Planning Poker profesionales
2. ✅ Calcular estimaciones PERT correctamente
3. ✅ Implementar CCPM en tus proyectos
4. ✅ Monitorear progreso con Fever Chart
5. ✅ Tomar decisiones basadas en datos, no intuición

**¡Éxito en tus proyectos!** 🚀
