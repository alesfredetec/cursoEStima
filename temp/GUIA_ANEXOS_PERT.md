# GUÍA DE USO: ANEXOS PERT/CPM

**Archivo**: `clase2_pert_anexos.html`
**Fecha**: 2025-12-09
**Versión**: 1.0

---

## RESUMEN EJECUTIVO

Archivo HTML complementario con **9 slides** de ejemplos gráficos y cálculos detallados de PERT, CPM, Desviación Estándar, Varianza y Monte Carlo.

**Propósito**: Reforzar conceptos de los slides 5, 6 y 7 de `clase2_profesor.html` con ejemplos paso a paso.

---

## CONTENIDO DE LOS SLIDES

### Slide 1: Portada
- Introducción a los anexos
- Lista de contenidos (slides 2-9)
- Prerequisitos (slides 3-7 de Clase 2)

### Slide 2: Ejemplo 1 Tarea - Cálculo μ (5 min)
**Tema**: Cálculo de duración esperada (μ) con PERT

**Caso**: Migración de base de datos PostgreSQL 12 → 15
- O = 5 días (optimista)
- M = 10 días (más probable)
- P = 25 días (pesimista)

**Cálculo paso a paso**:
1. μ = (O + 4M + P) / 6
2. μ = (5 + 4×10 + 25) / 6
3. μ = (5 + 40 + 25) / 6
4. μ = 70 / 6
5. **μ = 11.67 días ≈ 12 días**

**Pedagogía**: Muestra CADA paso algebraico con cajas de cálculo visuales.

---

### Slide 3: Ejemplo 1 Tarea - Cálculo σ (6 min)
**Tema**: Cálculo de desviación estándar (σ)

**Cálculo paso a paso**:
1. σ = (P - O) / 6
2. σ = (25 - 5) / 6
3. σ = 20 / 6
4. **σ = 3.33 días**

**Resultado final**: **12 ± 3.33 días**

**Rangos de confianza**:
- 68% (±1σ): 8.67 - 15.33 días
- 95% (±2σ): 5.34 - 18.66 días
- 99.7% (±3σ): 2 - 22 días

**Insight clave**: "Aunque μ = 12 días, hay 32% probabilidad de que tome más de 15 días"

---

### Slide 4: Ejemplo 100 Tareas - Contexto (5 min)
**Tema**: Proyecto real con 100 tareas

**Contexto**: Sistema e-commerce completo
- 25 tareas Frontend (React)
- 30 tareas Backend (Node.js)
- 20 tareas DB y APIs
- 15 tareas Testing/QA
- 10 tareas DevOps/Deploy

**Ruta crítica (CPM)**: 40 tareas identificadas

**Tabla parcial** con 5 tareas ejemplo:
| Tarea | O | M | P | μ | σ |
|-------|---|---|---|---|---|
| Setup & Arquitectura | 3 | 5 | 10 | 5.5 | 1.17 |
| Sistema de Auth | 5 | 10 | 20 | 10.83 | 2.5 |
| Catálogo de Productos | 8 | 15 | 30 | 16.33 | 3.67 |
| Carrito de Compras | 6 | 12 | 25 | 13.17 | 3.17 |
| Proceso de Checkout | 10 | 20 | 40 | 21.67 | 5.0 |

**Total (40 tareas)**: μ = 180 días, σ = ±15 días

---

### Slide 5: Ejemplo 100 Tareas - Resultados (7 min)
**Tema**: Resultados agregados y decisiones

**Métricas clave**:
- 100 tareas totales
- 40 en ruta crítica
- 60 con holgura

**Cálculo de σ total**:
```
σ²_total = σ₁² + σ₂² + ... + σ₄₀²
σ²_total = 225 días²
σ_total = √225 = 15 días
```

**Resultado**: **180 ± 15 días**

**Tabla de decisión**:
| Deadline | Probabilidad de Éxito | Riesgo | Recomendación |
|----------|----------------------|--------|---------------|
| 165 días | 16% | Muy Alto | ❌ No recomendado |
| 180 días (μ) | 50% | Alto | ⚠️ Solo si hay flexibilidad |
| **195 días (μ+1σ)** | **84%** | **Bajo** | **✅ Recomendado** |
| 210 días (μ+2σ) | 97.5% | Muy Bajo | ✅ Conservador |
| 225 días (μ+3σ) | 99.7% | Mínimo | ⚠️ Puede ser excesivo |

**Decisión recomendada**: **195 días** (μ + 1σ) para balance entre competitividad y realismo.

---

### Slide 6: Gráficos de Desviación Estándar (6 min)
**Tema**: Visualización de distribución normal

**Gráfico**: Curva de campana (distribución normal) con μ=180, σ=15
- Chart.js interactivo
- Áreas coloreadas: ±1σ (verde), ±2σ (amarillo), ±3σ (rojo)

**Coeficiente de Variación (CV)**:
```
CV = σ / μ × 100%
CV = 15 / 180 = 8.3%
```

**Interpretación de CV**:
- **CV < 10%**: Alta certeza ✅ (nuestro proyecto)
- **10% ≤ CV ≤ 25%**: Incertidumbre normal
- **CV > 25%**: Alta incertidumbre, considerar dividir tarea ⚠️

**Ejemplos contrastantes**:
- Tarea simple (cambiar texto UI): σ/μ = 23% → OK
- Integración legacy: σ/μ = 41% → DIVIDIR ⚠️

---

### Slide 7: Gráficos de Varianza (6 min)
**Tema**: Por qué sumamos varianzas y no desviaciones

**Fórmula clave**:
```
σ²_total = σ₁² + σ₂² + ... + σₙ²  ✅ CORRECTO
σ_total ≠ σ₁ + σ₂ + ... + σₙ      ❌ INCORRECTO
```

**Propiedad matemática**: La varianza es aditiva para variables independientes.

**Ejemplo numérico**:
| Tarea | σ (días) | σ² (días²) |
|-------|----------|-----------|
| A | 2 | 4 |
| B | 3 | 9 |
| C | 4 | 16 |
| **Total** | **√29 = 5.39** | **29** |

**Error común**:
- ❌ Incorrecto: σ_total = 2 + 3 + 4 = 9 días
- ✅ Correcto: σ_total = √(4 + 9 + 16) = √29 = 5.39 días

**Gráfico**: Barras mostrando acumulación de varianza en ruta crítica (Chart.js)

---

### Slide 8: Monte Carlo - Simulación (7 min)
**Tema**: Simulación de 10,000 iteraciones del proyecto

**Algoritmo**:
```
Para i = 1 hasta 10,000:
    Para cada tarea en ruta crítica:
        Generar duración aleatoria con distribución Beta(O, M, P)
    Sumar duraciones → duración_total[i]
    Guardar resultado
```

**Resultado**: Array con 10,000 posibles duraciones del proyecto

**Histograma (Chart.js)**:
- 20 bins de 5 días cada uno
- Distribución aproximadamente normal
- Pico en ~180 días

**Percentiles clave**:
- **P50 (Mediana)**: 180 días → 50% probabilidad
- **P85**: 195 días → 85% probabilidad
- **P95**: 208 días → 95% probabilidad

---

### Slide 9: Monte Carlo - Decisiones (8 min)
**Tema**: Validación PERT vs Monte Carlo y tabla de decisión

**Estadísticas de la simulación**:
| Métrica | Monte Carlo | PERT | Diferencia |
|---------|------------|------|------------|
| Media (μ) | 180.3 días | 180 días | 0.17% |
| Desv. Est. (σ) | 14.8 días | 15 días | 1.3% |
| Mediana | 179.8 días | - | - |
| Mínimo | 142 días | - | - |
| Máximo | 238 días | - | - |

**Validación**: Monte Carlo **confirma** los cálculos PERT con <2% diferencia.

**Tabla de decisión detallada**:
| Deadline | Prob. Éxito | Riesgo | Recomendación |
|----------|------------|--------|---------------|
| 165 días | 16% 🔴 | Muy Alto | ❌ No recomendado |
| 180 días (μ) | 50% 🟠 | Alto | ⚠️ Solo si flexibilidad |
| **195 días (μ+1σ)** | **84% 🟢** | **Bajo** | **✅ Recomendado** |
| 210 días (μ+2σ) | 97.5% 🟢 | Muy Bajo | ✅ Conservador |
| 225 días (μ+3σ) | 99.7% 🟢 | Mínimo | ⚠️ Excesivo |

**Mensaje al stakeholder**:
*"El proyecto tomará aproximadamente **6.5 meses (195 días)** con alta confianza de cumplimiento."*

---

## CARACTERÍSTICAS TÉCNICAS

### Layout
- **70/30 Split**: Slides a la izquierda, Sidebar con speeches a la derecha
- **Diseño responsive**: Se adapta a diferentes tamaños de pantalla
- **Dark theme**: Fondo oscuro con gradientes morados (#667eea, #764ba2)

### Gráficos Interactivos
- **Chart.js v4.4.0**: Librería para gráficos
- **3 gráficos**:
  1. Distribución Normal (Slide 6): Curva de campana
  2. Varianza Acumulada (Slide 7): Gráfico de barras
  3. Histograma Monte Carlo (Slide 8): Gráfico de barras (20 bins)

### TTS (Text-to-Speech)
- **Browser TTS**: Web Speech API (voces español España, México, Argentina)
- **Fallback**: Si config.js no existe, solo browser TTS disponible
- **9 speeches sincronizados**: Uno por cada slide
- **Controles**: Play/Pause, Stop, Speed (0.8x - 2.0x), Voice selection

### Navegación
- **Botones**: ← Anterior / Siguiente →
- **Teclado**: Flechas ← →, Home (primer slide), End (último slide)
- **Contador**: X / 9 slides
- **Deshabilitación automática**: Botones deshabilitados en extremos

---

## CÓMO USAR ESTE ARCHIVO

### Para el Profesor

1. **Abrir el archivo**:
   ```bash
   start clase2_pert_anexos.html  # Windows
   open clase2_pert_anexos.html   # Mac
   ```

2. **Cuándo usarlo**:
   - **Opción A**: Después de slides 5-7 de Clase 2 (PERT/CPM)
   - **Opción B**: Como material de refuerzo post-clase
   - **Opción C**: Para estudiantes que quieren profundizar

3. **Flujo sugerido**:
   - Mostrar slides 2-3 (ejemplo 1 tarea) para reforzar fórmulas
   - Mostrar slides 4-5 (ejemplo 100 tareas) para proyecto real
   - Mostrar slide 6-7 (σ y σ²) para aclarar conceptos
   - Mostrar slides 8-9 (Monte Carlo) para validación y decisiones

4. **Usar TTS**:
   - Click en **▶ Play** para narración automática
   - Ajustar velocidad (recomendado 1.2x para enseñanza)
   - Pausar cuando sea necesario para preguntas

5. **Interactuar con gráficos**:
   - Los gráficos Chart.js son interactivos
   - Hover sobre barras/líneas para ver valores exactos
   - Los gráficos se generan dinámicamente al cargar la página

### Para el Estudiante

1. **Uso independiente**:
   - Archivo standalone (no requiere servidor)
   - Navegar a tu propio ritmo
   - Usar TTS para narración automática

2. **Enfoque recomendado**:
   - Leer slide completo antes de usar TTS
   - Pausar en cálculos paso a paso
   - Intentar replicar cálculos en papel
   - Verificar con los resultados del slide

3. **Práctica**:
   - Usar los ejemplos como plantillas
   - Crear tus propios ejemplos con valores diferentes
   - Calcular μ y σ manualmente, verificar con fórmula

---

## INTEGRACIÓN CON CLASE 2

### Mapeo de Contenidos

**Clase 2 - Slide 5**: Ejemplo Práctico PERT
→ **Anexos - Slides 2-3**: Ejemplo 1 tarea con cálculo detallado

**Clase 2 - Slide 6**: CPM (Critical Path Method)
→ **Anexos - Slides 4-5**: Proyecto 100 tareas con ruta crítica identificada

**Clase 2 - Slide 7**: Combinando PERT y CPM
→ **Anexos - Slides 6-9**: Visualizaciones de σ, σ², y Monte Carlo

### Cuándo Mostrar los Anexos

**Escenario 1: Durante la Clase**
- Después de slide 7 de Clase 2
- Decir: "Ahora vamos a ver ejemplos detallados con cálculos paso a paso"
- Mostrar slides 2-3 (ejemplo simple)
- Mostrar slides 4-5 (proyecto real)
- Opcional: Slides 6-9 si hay tiempo

**Escenario 2: Post-Clase**
- Compartir archivo con estudiantes
- Decir: "Este material refuerza conceptos de PERT/CPM con ejemplos gráficos"
- Los estudiantes lo usan para estudio independiente

**Escenario 3: Talleres de Práctica**
- Usar slides 2-3 para que estudiantes repliquen cálculos
- Usar slides 4-5 para analizar proyecto real
- Usar slides 8-9 para discutir decisiones de management

---

## TESTING Y VERIFICACIÓN

### Checklist Pre-Uso

✅ **Navegación**:
- [ ] Botones ← → funcionan
- [ ] Flechas del teclado funcionan
- [ ] Home/End van a primer/último slide
- [ ] Contador muestra "X / 9" correctamente

✅ **Gráficos**:
- [ ] Slide 6: Gráfico de distribución normal se muestra
- [ ] Slide 7: Gráfico de varianza acumulada se muestra
- [ ] Slide 8: Histograma Monte Carlo se muestra
- [ ] Hover sobre gráficos muestra tooltips

✅ **TTS**:
- [ ] Click en Play inicia narración
- [ ] Speech se sincroniza con slide actual
- [ ] Sidebar muestra título y script correcto
- [ ] Cambiar de slide cambia speech automáticamente

✅ **Contenido**:
- [ ] Todas las fórmulas se muestran correctamente
- [ ] Tablas son legibles y bien formateadas
- [ ] Cajas de ejemplo (verde), warning (rojo), info (azul) se distinguen
- [ ] Stat cards muestran valores grandes correctamente

---

## TROUBLESHOOTING

### Problema: Gráficos no se muestran
**Causa**: Chart.js no cargó desde CDN
**Solución**: Verificar conexión a internet, o descargar Chart.js localmente

### Problema: TTS no funciona
**Causa**: Navegador no soporta Web Speech API
**Solución**: Usar Chrome, Edge, o Safari (soporte completo)

### Problema: Sidebar no se muestra
**Causa**: Resolución de pantalla muy pequeña
**Solución**: Usar pantalla ≥1024px de ancho, o zoom out

### Problema: Fórmulas se ven mal formateadas
**Causa**: Fuente monospace no disponible
**Solución**: CSS usa fallback a 'Courier New'

---

## EXTENSIONES FUTURAS (Opcionales)

### Ideas para V2.0
1. **Calculadora interactiva**: Input O-M-P → Output μ y σ
2. **Más ejemplos**: 5 tareas, 20 tareas, 50 tareas
3. **Gráfico CPM interactivo**: Visualizar ruta crítica con D3.js
4. **Monte Carlo en vivo**: Botón "Simular" ejecuta 10,000 iteraciones en tiempo real
5. **Exportar a PDF**: Generar reporte con todos los cálculos

---

## ARCHIVOS RELACIONADOS

- **clase2_profesor.html** - Clase principal (24 slides + TTS)
- **clase2.html** - Versión estudiante sin TTS (24 slides)
- **clase2_pert_anexos.html** - Este archivo (9 slides + TTS + gráficos)
- **config.js** - API keys para OpenAI TTS (opcional)
- **config.example.js** - Template de configuración

---

## MÉTRICAS DEL ARCHIVO

| Métrica | Valor |
|---------|-------|
| **Tamaño** | ~65 KB |
| **Líneas de código** | ~1,200 |
| **Slides** | 9 |
| **Speeches** | 9 (sincronizados) |
| **Gráficos Chart.js** | 3 |
| **Tablas** | 8 |
| **Fórmulas** | 15+ |
| **Ejemplos** | 2 (1 tarea, 100 tareas) |
| **Duración total** | ~52 min (con TTS) |

---

## CONCLUSIÓN

Este archivo es un **complemento pedagógico completo** para reforzar conceptos de PERT, CPM, Desviación Estándar, Varianza y Monte Carlo.

**Ventajas**:
- ✅ Ejemplos paso a paso con cálculos detallados
- ✅ Gráficos interactivos para visualización
- ✅ Sincronización perfecta con TTS
- ✅ Standalone (no requiere servidor)
- ✅ Responsive y accesible

**Uso recomendado**: Mostrar después de slides 5-7 de Clase 2, o compartir para estudio independiente.

---

**Fecha de creación**: 2025-12-09
**Versión**: 1.0
**Autor**: Claude Code (asistente)
**Para**: Curso de Estimación y Gestión de Proyectos
