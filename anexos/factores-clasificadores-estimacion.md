# Factores Clasificadores y Porcentajes para Estimación de Software
## Guía de Referencia Rápida

**Versión:** 2.0  
**Última actualización:** Noviembre 2025

---

## 📋 Índice

1. [Introducción y Metodología](#1-introducción-y-metodología)
2. [Matriz de Factores de Riesgo](#2-matriz-de-factores-de-riesgo)
3. [Factores de Equipo](#3-factores-de-equipo)
4. [Factores de Aplicación](#4-factores-de-aplicación)
5. [Factores de Cliente](#5-factores-de-cliente)
6. [Factores de Contexto](#6-factores-de-contexto)
7. [Cálculo del Factor Compuesto](#7-cálculo-del-factor-compuesto)
8. [Buffers y Contingencias](#8-buffers-y-contingencias)
9. [Tablas de Referencia Rápida](#9-tablas-de-referencia-rápida)
10. [Casos de Aplicación](#10-casos-de-aplicación)

---

## 1. Introducción y Metodología

### 1.1 Cómo Usar Esta Guía

```
PASO 1: Obtener estimación base
├─ Usar Puntos Función, Casos de Uso, o Descomposición
└─ Resultado: Horas Base (HB)

PASO 2: Evaluar cada factor de riesgo
├─ Ubicar nivel (Muy Bajo, Bajo, Nominal, Alto, Muy Alto, Extra Alto)
└─ Obtener multiplicador

PASO 3: Calcular Factor Compuesto (FC)
└─ FC = Factor1 × Factor2 × Factor3 × ... × FactorN

PASO 4: Calcular Esfuerzo Ajustado
└─ Esfuerzo Ajustado = HB × FC

PASO 5: Agregar Buffer de Contingencia
└─ Esfuerzo Final = Esfuerzo Ajustado × (1 + %Buffer)
```

### 1.2 Principios Fundamentales

**⚠️ CRÍTICO: Los factores se MULTIPLICAN, NO se suman**

```
❌ INCORRECTO:
Factor1 = 1.5, Factor2 = 1.5
Factor Total = 1.5 + 1.5 = 3.0

✅ CORRECTO:
Factor1 = 1.5, Factor2 = 1.5
Factor Total = 1.5 × 1.5 = 2.25
```

**Rangos de Factores:**
- **Reducen esfuerzo**: 0.50 - 0.99 (factores positivos como experiencia alta)
- **Neutral**: 1.00 (sin impacto)
- **Aumentan esfuerzo**: 1.01 - 4.00 (factores de riesgo)

---

## 2. Matriz de Factores de Riesgo

### 2.1 Vista General de Factores

| ID | Factor | Categoría | Riesgo | Rango Multiplicador |
|----|--------|-----------|--------|---------------------|
| **E1** | Tamaño del Equipo | Equipo | 🟡 Medio | 1.00 - 1.60 |
| **E2** | Experiencia Técnica | Equipo | 🟡 Medio | 0.70 - 2.00 |
| **E3** | Experiencia Funcional | Equipo | 🟡 Medio | 0.85 - 1.40 |
| **E4** | Experiencia en Procesos | Equipo | 🟡 Medio | 0.70 - 2.00 |
| **E5** | Dedicación al Proyecto | Equipo | 🔴 Alto | 1.00 - 2.50 |
| **E6** | Rotación de Personal | Equipo | 🔴 Alto | 1.00 - 1.50 |
| **E7** | Conocimiento del Stack | Equipo | 🔴 Alto | 0.80 - 4.00 |
| **A1** | Complejidad de la Aplicación | Aplicación | 🔴 Alto | 1.00 - 4.00 |
| **A2** | Criticidad del Sistema | Aplicación | 🔴 Alto | 1.00 - 3.00 |
| **A3** | Complejidad de Base de Datos | Aplicación | 🔴 Alto | 1.00 - 3.50 |
| **A4** | Complejidad de Pruebas | Aplicación | 🟡 Medio | 1.00 - 1.80 |
| **A5** | Volumen de Información | Aplicación | 🟡 Medio | 1.00 - 2.50 |
| **A6** | Integraciones Externas | Aplicación | 🔴 Alto | 1.00 - 2.50 |
| **C1** | Disponibilidad del Cliente | Cliente | 🔴 Alto | 1.00 - 1.50 |
| **C2** | Conocimiento del Negocio | Cliente | 🟡 Medio | 0.90 - 1.40 |
| **C3** | Claridad de Requerimientos | Cliente | 🔴 Alto | 1.00 - 1.80 |
| **C4** | Volatilidad de Requerimientos | Cliente | 🔴 Alto | 1.00 - 2.00 |
| **X1** | Requerimientos de Compliance | Contexto | 🟡 Medio | 1.00 - 1.70 |
| **X2** | Deadline Impuesto | Contexto | 🔴 Alto | 1.00 - 1.80 |
| **X3** | Equipos Distribuidos | Contexto | 🟡 Medio | 1.00 - 1.50 |
| **X4** | Calidad de Infraestructura | Contexto | 🟡 Medio | 0.90 - 1.30 |
| **X5** | Restricciones de Hardware | Contexto | 🟡 Medio | 1.00 - 1.50 |
| **X6** | Documentación Existente | Contexto | 🟢 Bajo | 0.90 - 1.30 |

**Leyenda de Riesgo:**
- 🔴 **Alto**: Factor crítico, puede duplicar o triplicar el esfuerzo
- 🟡 **Medio**: Impacto moderado, aumenta esfuerzo 20-50%
- 🟢 **Bajo**: Impacto menor, variación <20%

---

## 3. Factores de Equipo

### E1: Tamaño del Equipo

**Concepto:** Overhead de comunicación y coordinación

**Clasificación:**

| Nivel | Tamaño Equipo | Canales Comunicación | Multiplicador | Descripción |
|-------|---------------|----------------------|---------------|-------------|
| **Óptimo** | 2-5 personas | 1-10 canales | **×1.00** | Squad pequeño, comunicación directa |
| **Bueno** | 6-8 personas | 15-28 canales | **×1.10** | Equipo mediano, coordinación manejable |
| **Nominal** | 9-12 personas | 36-66 canales | **×1.20** | Equipo grande, overhead moderado |
| **Alto** | 13-20 personas | 78-190 canales | **×1.35** | Equipo muy grande, coordinación compleja |
| **Muy Alto** | 21+ personas | 210+ canales | **×1.50** | Múltiples equipos, overhead significativo |

**Fórmula:** `Canales = n(n-1)/2`

**Mitigaciones:**
- Dividir en squads de 5-7 personas
- Arquitectura modular con interfaces claras
- Definir ownership por módulos
- Usar Scrum of Scrums para coordinación

---

### E2: Experiencia Técnica del Equipo

**Concepto:** Nivel de seniority y conocimiento técnico general

**Clasificación:**

| Nivel | Experiencia | Productividad | Multiplicador | Características |
|-------|-------------|---------------|---------------|-----------------|
| **Expert** | 10+ años | 150-200% | **×0.70** | Arquitectos, referentes técnicos, mentores |
| **Senior** | 5-10 años | 110-150% | **×0.85** | Autónomos, diseñan soluciones, anticipan problemas |
| **Semi-Senior** | 2-5 años | 80-100% | **×1.00** | Base de referencia, trabajan autónomamente |
| **Junior** | 1-2 años | 50-70% | **×1.50** | Requieren supervisión, curva de aprendizaje |
| **Trainee** | <1 año | 30-50% | **×2.00** | Necesitan mentoría constante, errores frecuentes |

**Cálculo para Equipos Mixtos:**

```
Ejemplo: Equipo de 10 developers
- 2 Seniors (20%)
- 5 Semi-Seniors (50%)
- 3 Juniors (30%)

Factor Ponderado = (0.20 × 0.85) + (0.50 × 1.00) + (0.30 × 1.50)
Factor Ponderado = 0.17 + 0.50 + 0.45 = 1.12
```

**Consideraciones por Tarea:**

| Tipo de Tarea | Junior vs Senior |
|---------------|------------------|
| **Feature CRUD simple** | Junior: 8h, Senior: 4h (2x) |
| **Feature con lógica compleja** | Junior: 24h, Senior: 8h (3x) |
| **Arquitectura/Diseño** | Junior: No puede, Senior: 12h (∞) |
| **Bug fixing crítico** | Junior: 12h, Senior: 2h (6x) |
| **Code review** | Junior: No efectivo, Senior: 1h |
| **Integración compleja** | Junior: 40h, Senior: 12h (3.3x) |

---

### E3: Experiencia Funcional (Conocimiento del Negocio)

**Concepto:** Cuánto conoce el equipo el dominio del problema

**Clasificación:**

| Nivel | Conocimiento | Multiplicador | Impacto |
|-------|--------------|---------------|---------|
| **Experto en Dominio** | 5+ años en industria | **×0.85** | Anticipa requerimientos, casos borde conocidos |
| **Con Experiencia** | 2-5 años en industria | **×1.00** | Conoce el negocio, curva mínima |
| **Conocimiento Básico** | <2 años, dominio similar | **×1.15** | Necesita explicaciones, algunos conceptos claros |
| **Sin Conocimiento** | Primera vez en industria | **×1.40** | Curva de aprendizaje del negocio, muchas preguntas |

**Ejemplo Fintech:**

| Developer | Background | Tarea: API de Pagos | Estimación |
|-----------|------------|---------------------|------------|
| Dev A | 5 años en fintech | Conoce flujos, PSP, clearing, reversión | 40h × 0.85 = **34h** |
| Dev B | 2 años en e-commerce | Conoce pagos básicos, no clearing | 40h × 1.00 = **40h** |
| Dev C | Viene de gaming | No conoce terminología fintech | 40h × 1.40 = **56h** |

---

### E4: Experiencia en Procesos de Desarrollo

**Concepto:** Madurez del equipo en metodologías y DevOps

**Clasificación (Basado en CMMI):**

| Nivel | Descripción | Multiplicador | Características |
|-------|-------------|---------------|-----------------|
| **Nivel 5: Optimizado** | DevOps avanzado | **×0.70** | CI/CD completo, métricas, mejora continua, chaos eng |
| **Nivel 4: Gestionado** | Procesos medidos | **×0.85** | Métricas de calidad, SonarQube, APM, postmortems |
| **Nivel 3: Definido** | Proceso estándar | **×1.00** | SCRUM/Kanban, CI/CD básico, code review, testing auto |
| **Nivel 2: Repetible** | Proceso básico | **×1.40** | Proceso documentado, testing manual, deploy semi-auto |
| **Nivel 1: Ad-Hoc** | Caos | **×2.00** | Sin proceso, cada quien trabaja diferente, deploy manual |

**Checklist para Clasificación:**

```
Nivel 5 (×0.70):
☑ Deploy a producción en <30 minutos
☑ Rollback automático ante errores
☑ Feature flags / Canary deployments
☑ Chaos engineering (testing en prod)
☑ Métricas de DORA (deployment frequency, lead time, MTTR, change fail rate)
☑ Postmortems blameless de todos los incidentes
☑ Infrastructure as Code completo

Nivel 4 (×0.85):
☑ CI/CD con pipeline completo
☑ Code coverage >80%
☑ SonarQube u herramienta de calidad
☑ APM (Application Performance Monitoring)
☑ Métricas de velocidad del equipo
☐ Chaos engineering

Nivel 3 (×1.00):
☑ Metodología ágil (SCRUM/Kanban)
☑ CI/CD básico (build + test automático)
☑ Code review obligatorio
☑ Testing automatizado (unit + integration)
☑ Definition of Done clara
☐ Métricas de calidad

Nivel 2 (×1.40):
☑ Proceso documentado
☑ Testing manual estructurado
☑ Code review opcional
☑ Deploy semi-automático
☐ Testing automatizado

Nivel 1 (×2.00):
☐ Proceso definido
☐ Testing estructurado
☐ Code review
☐ CI/CD
```

---

### E5: Dedicación al Proyecto

**Concepto:** Porcentaje de tiempo efectivo dedicado al proyecto

**Clasificación:**

| Nivel | Dedicación | Productividad Real | Multiplicador | Contexto |
|-------|------------|-------------------|---------------|----------|
| **Full-Time** | 100% | 100% | **×1.00** | Único proyecto, enfoque completo |
| **Alta** | 80-90% | 75-85% | **×1.20** | 1-2 proyectos, cambio mínimo de contexto |
| **Media** | 60-70% | 50-60% | **×1.50** | 2-3 proyectos, cambio frecuente |
| **Baja** | 40-50% | 35-45% | **×2.00** | 3+ proyectos, multitasking excesivo |
| **Muy Baja** | <40% | <30% | **×2.50** | Muchos proyectos + soporte + operaciones |

**Impacto del Multitasking:**

```
Productividad Real = Dedicación Nominal × Factor de Context Switching

Factor Context Switching:
- 1 proyecto: 1.00
- 2 proyectos: 0.85 (15% pérdida)
- 3 proyectos: 0.65 (35% pérdida)
- 4+ proyectos: 0.50 (50% pérdida)
```

**Ejemplo:**

```
Developer con 40% en Proyecto A, 35% en B, 25% en C:

Tiempo nominal: 8h/día
Horas productivas: 8 × 0.50 (context switching) = 4h/día
Horas en Proyecto A: 4 × 0.40 = 1.6h/día

Tarea de 40h en Proyecto A:
Con 100% dedicación: 40 / 8 = 5 días
Con distribución real: 40 / 1.6 = 25 días
Factor: ×5.0 en duración calendario
```

---

### E6: Rotación de Personal

**Concepto:** Pérdida de conocimiento por salidas del equipo

**Clasificación:**

| Nivel | Rotación Anual | Multiplicador | Impacto |
|-------|----------------|---------------|---------|
| **Muy Baja** | 0-5% | **×1.00** | Equipo estable, conocimiento consolidado |
| **Baja** | 5-10% | **×1.05** | Rotación saludable, renovación controlada |
| **Media** | 10-20% | **×1.15** | Pérdida de conocimiento moderada |
| **Alta** | 20-30% | **×1.30** | Impacto en continuidad, re-onboarding frecuente |
| **Muy Alta** | 30%+ | **×1.50** | Crisis de equipo, pérdida masiva de conocimiento |

**Costo por Persona que se va:**

```
FASE 1: Pre-salida (2-4 semanas)
- Productividad: 60%
- Pérdida: 40% × 2.5 semanas = 1 semana

FASE 2: Transición (1-2 semanas)
- Documentación + transferencia: 60h
- Pérdida: 1.5 semanas

FASE 3: Vacancia (variable)
- Sin recurso: 100%
- Redistribución carga al equipo: overhead 20%

FASE 4: Onboarding reemplazo (4-8 semanas)
- Productividad progresiva: 40% → 80%
- Pérdida equivalente: 3-4 semanas

TOTAL: 6-10 semanas de productividad perdida
```

**Ejemplo de Proyecto:**

```
Proyecto de 12 meses, equipo de 10 personas

Escenario A: Rotación 5% (0.5 personas/año)
- Pérdida: 2 meses-persona
- Impacto: 12 × 1.05 = 12.6 meses

Escenario B: Rotación 25% (2.5 personas/año)
- Pérdida: 10 meses-persona
- Impacto: 12 × 1.30 = 15.6 meses
```

---

### E7: Conocimiento del Stack Tecnológico

**Concepto:** Experiencia del equipo en tecnologías específicas del proyecto

**Clasificación:**

| Nivel | Experiencia en Stack | Multiplicador | Curva de Aprendizaje |
|-------|---------------------|---------------|---------------------|
| **Experto** | 3+ años en stack | **×0.80** | N/A - Ya es experto |
| **Avanzado** | 1-3 años en stack | **×1.00** | Productividad completa |
| **Intermedio** | 6-12 meses en stack | **×1.30** | 2-3 meses para 100% |
| **Básico** | 1-6 meses en stack | **×1.70** | 4-6 meses para 100% |
| **Principiante** | <1 mes en stack | **×2.50** | 6-8 meses para 100% |
| **Nuevo Total** | Nunca usó stack | **×4.00** | 8-12 meses para 100% |

**Curva de Productividad para Nuevo en Stack:**

| Mes | Productividad | Factor | Actividad Típica |
|-----|---------------|--------|------------------|
| **1** | 25% | ×4.00 | Setup, hello world, tutoriales |
| **2** | 40% | ×2.50 | Features simples, muchas dudas |
| **3** | 55% | ×1.80 | Features moderadas, debugging lento |
| **4** | 70% | ×1.40 | Independencia parcial |
| **5** | 80% | ×1.25 | Casi autónomo |
| **6** | 90% | ×1.10 | Productividad cercana a normal |
| **7-8** | 95% | ×1.05 | Refinando conocimiento |
| **9+** | 100% | ×1.00 | Productividad completa |

**Ejemplo: Equipo migrando a .NET Core 8 + Azure AKS + Microservicios**

```
Equipo de 8 developers:
- 2 con 2 años en stack (×1.00)
- 3 con 6 meses en stack (×1.30)
- 3 nuevos en stack (mes 1: ×4.00, mes 6: ×1.10)

Mes 1:
Factor Ponderado = (2×1.00 + 3×1.30 + 3×4.00) / 8 = 2.24

Mes 6:
Factor Ponderado = (2×1.00 + 3×1.30 + 3×1.10) / 8 = 1.16

Proyecto 10 meses:
Factor Promedio ≈ 1.50
```

**Stack Específicos - Curva de Aprendizaje:**

| Stack | Complejidad | Tiempo para Productividad 80% |
|-------|-------------|-------------------------------|
| **.NET Core + SQL Server** | Media | 3-4 meses |
| **.NET Core + Microservicios + K8s** | Alta | 6-8 meses |
| **React/Angular** | Media | 2-3 meses |
| **React Native** | Alta | 4-6 meses |
| **Azure Cloud (básico)** | Media | 3-4 meses |
| **Azure AKS + DevOps** | Muy Alta | 6-9 meses |
| **RabbitMQ + MassTransit** | Media | 2-3 meses |
| **Redis (básico)** | Baja | 1-2 meses |
| **Redis (avanzado: cluster, patterns)** | Media | 3-4 meses |

---

## 4. Factores de Aplicación

### A1: Complejidad de la Aplicación

**Concepto:** Complejidad técnica y de negocio de la solución

**Clasificación:**

| Nivel | Multiplicador | Características | Ejemplo |
|-------|---------------|-----------------|---------|
| **Muy Baja** | **×1.00** | CRUD puro, sin lógica, sin integraciones | Backoffice administración catálogo |
| **Baja** | **×1.30** | Lógica simple, 1 integración, validaciones básicas | Sistema de tickets interno |
| **Media** | **×1.80** | Lógica moderada, 2-3 integraciones, workflows | Sistema de reservas online |
| **Alta** | **×2.50** | Lógica compleja, 4-6 integraciones, transacciones distribuidas | Plataforma e-commerce |
| **Muy Alta** | **×3.50** | Misión crítica, tiempo real, múltiples integraciones críticas | Core bancario |
| **Extrema** | **×4.00** | Sistemas ultra-críticos, >10 integraciones, compliance estricto | PSP, Trading platform |

**Matriz de Dimensiones:**

| Dimensión | Muy Baja | Baja | Media | Alta | Muy Alta |
|-----------|----------|------|-------|------|----------|
| **Lógica de Negocio** | Lineal | Condicionales | Workflows | State Machines | Event Sourcing |
| **Integraciones** | 0 | 1 | 2-3 | 4-6 | 7+ |
| **Concurrencia (TPS)** | <10 | 10-50 | 50-500 | 500-5K | 5K+ |
| **Latencia** | >5s | 1-5s | 500ms-1s | 100-500ms | <100ms |
| **Disponibilidad** | 95% | 98% | 99% | 99.9% | 99.99%+ |
| **Volumen Datos** | MB | GB | Cientos GB | TB | PB |

**Checklist de Complejidad:**

```
Complejidad ALTA/MUY ALTA incluye:
☑ Transacciones distribuidas (Saga, 2PC)
☑ Event sourcing
☑ CQRS
☑ State machines complejos
☑ Algoritmos complejos (ML, optimización)
☑ Procesamiento en tiempo real
☑ Circuit breakers + Retry policies
☑ Idempotencia obligatoria
☑ Consistency models complejos
☑ Sharding / Partitioning
☑ Multi-tenancy
☑ Compliance estricto (PCI DSS, SOX)
```

---

### A2: Criticidad del Sistema

**Concepto:** Impacto de fallas en el negocio

**Clasificación:**

| Nivel | Multiplicador | Uptime | RTO | RPO | Impacto Downtime |
|-------|---------------|--------|-----|-----|------------------|
| **Baja** | **×1.00** | 95-98% | 24h | 24h | Molestia interna |
| **Media** | **×1.40** | 99% | 4h | 4h | Afecta operaciones |
| **Alta** | **×2.00** | 99.9% | 1h | 1h | Pérdida revenue |
| **Muy Alta** | **×2.50** | 99.95% | 15min | 15min | Pérdida masiva + reputación |
| **Crítica** | **×3.00** | 99.99%+ | 5min | 5min | Regulatorio + pérdidas críticas |

**RTO:** Recovery Time Objective (tiempo máximo de downtime)  
**RPO:** Recovery Point Objective (pérdida máxima de datos)

**Overhead por Nivel de Criticidad:**

```
Criticidad Baja (×1.00):
- Error handling: básico
- Testing: 60% coverage
- Monitoring: logs básicos
- Deploy: manual ok
- DR: backup diario

Criticidad Alta (×2.00):
- Error handling: exhaustivo + circuit breakers
- Testing: 85% coverage + e2e
- Monitoring: APM + alerting proactivo
- Deploy: blue-green + rollback
- DR: backup cada hora + standby

Criticidad Crítica (×3.00):
- Error handling: redundante + retry + fallback
- Testing: 95% coverage + chaos engineering
- Monitoring: APM detallado + SLO tracking
- Deploy: canary + automatic rollback
- DR: replicación sincrónica + activo-activo multi-region
```

**Ejemplo Comparativo - Feature: API Endpoint**

```
Criticidad Baja (sistema interno):
- Feature base: 20h
- Testing básico: +8h
- Total: 28h (×1.4)

Criticidad Crítica (PSP):
- Feature base: 20h
- Error handling exhaustivo: +10h
- Circuit breakers: +8h
- Idempotencia: +6h
- Monitoring detallado: +5h
- Testing >95%: +20h
- Security review: +8h
- Chaos testing: +10h
- Documentación compliance: +8h
Total: 95h (×4.75)
```

---

### A3: Complejidad de Base de Datos

**Concepto:** Complejidad del modelo de datos y volumen

**Clasificación:**

| Nivel | Multiplicador | Tablas | Volumen | Características |
|-------|---------------|--------|---------|-----------------|
| **Simple** | **×1.00** | <10 | <100K reg | Relaciones simples, sin optimización |
| **Media** | **×1.40** | 10-50 | 100K-10M | Relaciones N:M, índices compuestos |
| **Alta** | **×2.20** | 50-150 | 10M-1B | Particionamiento, múltiples esquemas |
| **Muy Alta** | **×3.00** | 150-300 | 1B-100B | Sharding, event sourcing, CQRS |
| **Extrema** | **×3.50** | 300+ | >100B | Polyglot persistence, arquitectura distribuida |

**Características por Nivel:**

```
SIMPLE (×1.00):
- Queries directos
- Sin índices especializados
- Sin particionamiento
- Sin read replicas

MEDIA (×1.40):
- Índices compuestos
- Queries optimizados necesarios
- Stored procedures moderados
- 1-2 read replicas

ALTA (×2.20):
- Particionamiento horizontal
- Índices especializados (full-text, spatial)
- Múltiples read replicas (3-5)
- Queries muy optimizados
- Archiving strategy

MUY ALTA (×3.00):
- Sharding por criterio de negocio
- Event sourcing
- CQRS (write DB ≠ read DB)
- Cache distribuido (Redis cluster)
- Multiple databases (SQL + NoSQL)

EXTREMA (×3.50):
- Polyglot persistence (SQL + NoSQL + Graph + Time-series)
- Distributed transactions
- Eventual consistency patterns
- Data lake integration
- Real-time analytics
```

**Ejemplo Query - Sistema Financiero:**

```
Query Simple (sistema pequeño):
SELECT * FROM Transactions WHERE UserId = @id
Tiempo desarrollo: 1h

Query en Sistema PSP (300 tablas, 500M transacciones):
- Análisis plan ejecución: 3h
- Diseño índices columnar: 5h
- Partitioning strategy: 4h
- Implementación: 3h
- Testing con volumen real: 6h
- Optimización performance: 5h
- Validación en read-replica: 3h
- Documentación: 2h
Total: 31h (×31)
```

---

### A4: Complejidad de Pruebas

**Concepto:** Esfuerzo de testing necesario

**Clasificación:**

| Nivel | Multiplicador | Testing Requerido | Coverage |
|-------|---------------|-------------------|----------|
| **Baja** | **×1.00** | Unit tests básicos | 50-60% |
| **Media** | **×1.30** | Unit + Integration | 70-80% |
| **Alta** | **×1.60** | Unit + Integration + E2E + Performance | 85-90% |
| **Muy Alta** | **×1.80** | Full suite + Security + Load + Chaos | 95%+ |

**Overhead de Testing por Nivel:**

```
Nivel Bajo (×1.00):
Desarrollo: 40h
Testing: 20h (50% del desarrollo)
Total: 60h

Nivel Alto (×1.60):
Desarrollo: 40h
Testing: 64h (160% del desarrollo)
- Unit: 16h
- Integration: 20h
- E2E: 15h
- Performance: 8h
- Security scan: 5h
Total: 104h
```

---

### A5: Volumen de Información a Procesar

**Concepto:** Cantidad de datos que maneja la aplicación

**Clasificación:**

| Nivel | Multiplicador | Registros | Datos | Overhead |
|-------|---------------|-----------|-------|----------|
| **Muy Bajo** | **×1.00** | <1K | <10MB | Sin optimización necesaria |
| **Bajo** | **×1.10** | 1K-100K | 10MB-1GB | Índices básicos |
| **Medio** | **×1.30** | 100K-10M | 1GB-100GB | Índices + paginación + cache |
| **Alto** | **×1.80** | 10M-1B | 100GB-10TB | Particionamiento + optimización agresiva |
| **Muy Alto** | **×2.50** | >1B | >10TB | Big Data, arquitectura especializada |

**Ejemplo - Reporte de Transacciones:**

```
Volumen Bajo (1,000 registros):
- Query simple: 2h
- Paginación básica: 1h
Total: 3h

Volumen Alto (50M registros):
- Análisis de rendimiento: 4h
- Particionamiento de tablas: 8h
- Índices especializados: 6h
- Query optimization: 8h
- Caching strategy: 5h
- Testing performance: 6h
Total: 37h (×12.3)
```

---

### A6: Cantidad y Complejidad de Integraciones

**Concepto:** Dependencias con sistemas externos

**Clasificación:**

| Nivel | Multiplicador | # Integraciones | Características |
|-------|---------------|-----------------|-----------------|
| **Ninguna** | **×1.00** | 0 | Sistema standalone |
| **Baja** | **×1.20** | 1-2 | APIs REST simples, bien documentadas |
| **Media** | **×1.50** | 3-4 | Mix de protocolos, documentación media |
| **Alta** | **×2.00** | 5-7 | Legacy, SOAP, sin docs, diferentes vendors |
| **Muy Alta** | **×2.50** | 8+ | Múltiples vendors, protocolos legacy, críticas |

**Overhead por Integración:**

```
INTEGRACIÓN SIMPLE (×1.0 baseline):
- Análisis API docs: 2h
- Implementación: 6h
- Testing: 3h
- Error handling: 2h
Total por integración: 13h

INTEGRACIÓN COMPLEJA (×2.5):
- Reverse engineering (sin docs): 8h
- Implementación: 12h
- Testing: 8h
- Error handling + retry: 6h
- Circuit breaker: 4h
- Mocking para tests: 4h
Total por integración: 42h
```

**Ejemplo: Sistema de Pagos**

```
Integraciones requeridas:
1. Visa (API moderna, docs buenas): 15h
2. Mastercard (API moderna, docs buenas): 15h
3. Coelsa (API legacy, docs medias): 30h
4. BCRA (API legacy, docs pobres): 45h
5. Banco X (sin API, FTP): 60h
6. Sistema de Fraude (webhook): 20h

Sin complejidad: 6 × 13h = 78h
Con complejidad real: 185h
Factor: ×2.37
```

---

## 5. Factores de Cliente

### C1: Disponibilidad del Cliente/PO

**Concepto:** Velocidad de respuesta del cliente para dudas y decisiones

**Clasificación:**

| Nivel | Multiplicador | Tiempo Respuesta | Impacto |
|-------|---------------|------------------|---------|
| **Excelente** | **×0.95** | Mismo día (daily) | Decisiones instantáneas, progreso fluido |
| **Buena** | **×1.00** | 1-2 días | Bloqueos mínimos |
| **Media** | **×1.15** | 3-5 días | Bloqueos ocasionales |
| **Baja** | **×1.35** | 1-2 semanas | Bloqueos frecuentes, supuestos erróneos |
| **Muy Baja** | **×1.50** | >2 semanas | Proyecto bloqueado, muchos re-trabajos |

**Impacto en Sprint:**

```
Sprint 2 semanas, 5 dudas críticas:

Cliente Disponible (mismo día):
- 0 días bloqueados
- Factor: ×1.0

Cliente Responde en 5 días:
- 25 días bloqueados acumulados
- 1.25 sprints perdidos
- Factor: ×1.25

Cliente Responde en 2 semanas:
- 70 días bloqueados
- 3.5 sprints perdidos
- Factor: ×1.75
```

---

### C2: Conocimiento del Equipo sobre el Cliente/Negocio

**Concepto:** Cuánto conoce el equipo sobre el dominio del cliente

**Clasificación:**

| Nivel | Multiplicador | Descripción | Impacto |
|-------|---------------|-------------|---------|
| **Experto** | **×0.90** | Trabajó 3+ años en dominio, anticipa necesidades | Menos dudas, casos borde conocidos |
| **Alto** | **×1.00** | Trabajó 1-3 años, conoce bien el negocio | Curva mínima |
| **Medio** | **×1.15** | Conocimiento básico, dominio similar | Algunas dudas, conceptos a aprender |
| **Bajo** | **×1.30** | Primera vez, necesita capacitación | Muchas reuniones, curva pronunciada |
| **Nulo** | **×1.40** | Dominio completamente desconocido | Re-trabajos por malentendidos |

---

### C3: Claridad y Completitud de Requerimientos

**Concepto:** Calidad de la especificación inicial

**Clasificación:**

| Nivel | Multiplicador | Descripción |
|-------|---------------|-------------|
| **Excelente** | **×0.95** | Requerimientos completos, detallados, con criterios de aceptación |
| **Buena** | **×1.00** | Requerimientos claros, algunos detalles a definir |
| **Media** | **×1.20** | Requerimientos ambiguos, muchos detalles faltantes |
| **Baja** | **×1.50** | Requerimientos vagos, solo ideas generales |
| **Muy Baja** | **×1.80** | Sin requerimientos, "queremos algo como X" |

---

### C4: Volatilidad de Requerimientos

**Concepto:** Frecuencia de cambios en requerimientos

**Clasificación:**

| Nivel | Multiplicador | Cambios | Descripción |
|-------|---------------|---------|-------------|
| **Muy Baja** | **×1.00** | <5% | Requerimientos estables, cambios mínimos |
| **Baja** | **×1.10** | 5-15% | Algunos ajustes, manejables |
| **Media** | **×1.30** | 15-30% | Cambios frecuentes, re-trabajo moderado |
| **Alta** | **×1.60** | 30-50% | Cambios constantes, mucho re-trabajo |
| **Muy Alta** | **×2.00** | >50% | Requerimientos en constante cambio, caos |

**Impacto de Cambios Tardíos:**

```
Costo relativo de cambio por fase:

Requerimientos: ×1 (baseline)
Diseño: ×2-3
Desarrollo: ×5-10
Testing: ×10-15
Post-Deploy: ×30-100
```

---

## 6. Factores de Contexto

### X1: Requerimientos de Compliance y Regulatorios

**Concepto:** Overhead por regulaciones y normativas

**Clasificación:**

| Nivel | Multiplicador | Regulaciones | Overhead |
|-------|---------------|--------------|----------|
| **Ninguno** | **×1.00** | Sin regulaciones | Desarrollo estándar |
| **Básico** | **×1.15** | GDPR básico | Consentimientos, privacy |
| **Medio** | **×1.30** | GDPR completo | Privacy by design, auditoría |
| **Alto** | **×1.50** | PCI DSS o equivalente | Tokenización, cifrado, penetration testing |
| **Muy Alto** | **×1.70** | PCI DSS + SOX + Regulación Local | Múltiples auditorías, documentación exhaustiva |

**Overhead por Tipo de Compliance:**

```
GDPR (×1.15):
- Consentimiento explícito: +5%
- Right to be forgotten: +5%
- Data portability: +5%

PCI DSS (×1.50):
- Tokenización (no guardar PAN): +15%
- Cifrado E2E: +10%
- Logging auditable: +8%
- Penetration testing: +12%
- Documentación: +5%

BCRA (Argentina - ×1.35):
- Reportes regulatorios: +10%
- Validaciones específicas: +8%
- Auditoría BCRA: +12%
- Documentación: +5%

SOX (×1.25):
- Controles internos: +10%
- Segregación de funciones: +8%
- Auditoría financiera: +7%
```

---

### X2: Deadline Impuesto (Presión Temporal)

**Concepto:** Impacto de fechas límites inflexibles

**Clasificación:**

| Nivel | Multiplicador | Situación | Impacto |
|-------|---------------|-----------|---------|
| **Sin Deadline** | **×0.95** | Tiempo flexible | Calidad óptima, refactoring permitido |
| **Holgado** | **×1.00** | +30% sobre estimación | Sin presión |
| **Ajustado** | **×1.10** | Igual a estimación | Presión moderada |
| **Agresivo** | **×1.30** | -20% sobre estimación | Overtime, calidad sufre |
| **Imposible** | **×1.60** | -40%+ sobre estimación | Deuda técnica alta, burnout, fallas |

**Relación Deadline vs Calidad:**

```
Tiempo vs Calidad:

+50% tiempo: 110% calidad (refactoring, mejoras)
+25% tiempo: 105% calidad (polish)
Tiempo ideal: 100% calidad
-10% tiempo: 95% calidad (atajos menores)
-20% tiempo: 85% calidad (deuda técnica)
-30% tiempo: 70% calidad (deuda técnica significativa)
-40% tiempo: 50% calidad (sistema frágil)
```

**Estrategias ante Deadline Imposible:**

```
OPCIÓN A: Reducir Scope (MVP)
- Entregar 60-70% funcionalidad
- Roadmap post-lanzamiento
- Factor: ×1.15 (presión moderada)

OPCIÓN B: Aumentar Equipo
- Ley de Brooks: +overhead 20-30%
- Onboarding: 1-2 meses
- Raramente funciona

OPCIÓN C: Aceptar Deuda Técnica
- Factor: ×1.30
- Plan de pago de deuda post-deadline
- Riesgo de mantenibilidad

OPCIÓN D: Negociar Deadline
- Mejor opción cuando posible
- Presentar datos, riesgos, alternativas
```

---

### X3: Equipos Distribuidos / Ubicación Geográfica

**Concepto:** Overhead por distribución física del equipo

**Clasificación:**

| Nivel | Multiplicador | Ubicación | Overlap | Impacto |
|-------|---------------|-----------|---------|---------|
| **Co-ubicado** | **×1.00** | Mismo edificio | 8h | Comunicación instantánea |
| **Cercano** | **×1.05** | Mismo edificio, pisos diferentes | 8h | Mínimo friction |
| **Ciudad** | **×1.15** | Ciudad diferente, mismo huso | 8h | Requiere videollamadas |
| **Nacional** | **×1.25** | País diferente, 4-6h overlap | 4-6h | Coordinación horarios |
| **Internacional** | **×1.40** | País diferente, 2-3h overlap | 2-3h | Trabajo mayormente asíncrono |
| **Global** | **×1.50** | Sin overlap significativo | <2h | Muy difícil sincronización |

**Dependencias Externas:**

```
Factor adicional por dependencias de otros equipos:

Equipo disponible inmediatamente: +0%
Equipo responde en 1 día: +15%
Equipo responde en 3 días: +30%
Equipo responde en 1 semana: +50%
```

---

### X4: Calidad de Infraestructura de Desarrollo

**Concepto:** Calidad de herramientas y entornos

**Clasificación:**

| Nivel | Multiplicador | Descripción |
|-------|---------------|-------------|
| **Excelente** | **×0.90** | Infra moderna, automatizada, rápida, estable |
| **Buena** | **×1.00** | Herramientas estándar, funciona bien |
| **Media** | **×1.15** | Herramientas desactualizadas, ocasionales problemas |
| **Baja** | **×1.30** | Herramientas lentas, caídas frecuentes |
| **Muy Baja** | **×1.50** | Sin herramientas, todo manual, muy inestable |

**Impacto por Herramienta:**

```
Build lentos (>10min): +10-15%
Tests lentos (>30min suite completa): +15-20%
Deploy manual (>2h): +25-30%
Ambientes inestables (caídas diarias): +20-25%
Sin CI/CD: +40-50%
```

---

### X5: Restricciones de Hardware / Recursos

**Concepto:** Limitaciones de recursos computacionales

**Clasificación:**

| Nivel | Multiplicador | Descripción |
|-------|---------------|-------------|
| **Sin Restricciones** | **×1.00** | Cloud elástico, recursos ilimitados |
| **Restricciones Leves** | **×1.15** | Budget cloud moderado, require optimización |
| **Restricciones Moderadas** | **×1.30** | Hardware limitado, optimización necesaria |
| **Restricciones Severas** | **×1.50** | Hardware muy limitado, optimización agresiva |

**Ejemplo:**

```
API debe correr en contenedor 256MB RAM:

Sin restricción: 30h desarrollo

Con restricción severa:
- Profiling de memoria: 8h
- Optimización algoritmos: 12h
- Caching agresivo: 8h
- Testing de stress: 6h
- Documentación optimizaciones: 3h
Total: 67h (×2.23)
```

---

### X6: Calidad de Documentación Existente

**Concepto:** Documentación disponible de sistemas existentes

**Clasificación:**

| Nivel | Multiplicador | Descripción |
|-------|---------------|-------------|
| **Excelente** | **×0.90** | Docs actualizadas, completas, ejemplos, arquitectura clara |
| **Buena** | **×1.00** | Docs estándar, la mayoría actualizada |
| **Media** | **×1.15** | Docs parciales, algo desactualizadas |
| **Baja** | **×1.30** | Docs obsoletas, incompletas, falta arquitectura |
| **Nula** | **×1.50** | Sin documentación, reverse engineering necesario |

---

## 7. Cálculo del Factor Compuesto

### 7.1 Metodología de Cálculo

**Fórmula General:**

```
Factor Compuesto (FC) = FE × FA × FC × FX

Donde:
FE = Factor de Equipo
FA = Factor de Aplicación
FC = Factor de Cliente
FX = Factor de Contexto

Cada factor categoría:
FE = E1 × E2 × E3 × E4 × E5 × E6 × E7
FA = A1 × A2 × A3 × A4 × A5 × A6
FC = C1 × C2 × C3 × C4
FX = X1 × X2 × X3 × X4 × X5 × X6
```

### 7.2 Rangos Típicos por Categoría

| Categoría | Rango Típico | Extremos |
|-----------|--------------|----------|
| **Factor Equipo (FE)** | 0.8 - 2.5 | 0.5 - 4.0 |
| **Factor Aplicación (FA)** | 1.0 - 3.5 | 1.0 - 8.0 |
| **Factor Cliente (FC)** | 0.9 - 1.8 | 0.8 - 2.5 |
| **Factor Contexto (FX)** | 0.9 - 2.0 | 0.8 - 2.5 |
| **Factor Compuesto Total (FC)** | 1.5 - 6.0 | 1.0 - 20.0 |

### 7.3 Ejemplo de Cálculo Completo

**Proyecto:** Sistema de Wallet Digital

**Factores de Equipo:**
- E1 (Tamaño): 10 personas → **×1.20**
- E2 (Experiencia técnica): Mix semi-senior/junior → **×1.25**
- E3 (Experiencia funcional): Conocen fintech → **×1.00**
- E4 (Procesos): SCRUM + CI/CD → **×1.00**
- E5 (Dedicación): 90% → **×1.10**
- E6 (Rotación): 15% anual → **×1.10**
- E7 (Conocimiento stack): 3 nuevos en .NET Core → **×1.30**

```
FE = 1.20 × 1.25 × 1.00 × 1.00 × 1.10 × 1.10 × 1.30 = 2.31
```

**Factores de Aplicación:**
- A1 (Complejidad): Alta (integraciones, QR EMV) → **×2.50**
- A2 (Criticidad): Alta (99.9% uptime) → **×2.00**
- A3 (BD): Media-Alta (50 tablas, volumen medio) → **×1.60**
- A4 (Pruebas): Alta → **×1.60**
- A5 (Volumen): Medio → **×1.30**
- A6 (Integraciones): 5 integraciones → **×2.00**

```
FA = 2.50 × 2.00 × 1.60 × 1.60 × 1.30 × 2.00 = 26.62

⚠️ ALERTA: Factor muy alto
Revisar si aplicamos complejidad dos veces

Corrección: A1 ya incluye integraciones, no multiplicar A6
FA = 2.50 × 2.00 × 1.60 × 1.60 × 1.30 = 13.31

Aún muy alto, revisar...

Corrección realista:
A1 (Complejidad sin duplicar): ×1.50
FA = 1.50 × 2.00 × 1.60 × 1.60 × 1.30 = 7.99
```

**Factores de Cliente:**
- C1 (Disponibilidad): PO disponible 80% → **×1.05**
- C2 (Conocimiento): Medio → **×1.10**
- C3 (Claridad reqs): Media → **×1.20**
- C4 (Volatilidad): Baja-Media → **×1.15**

```
FC = 1.05 × 1.10 × 1.20 × 1.15 = 1.59
```

**Factores de Contexto:**
- X1 (Compliance): PCI DSS → **×1.50**
- X2 (Deadline): Agresivo → **×1.30**
- X3 (Distribución): Co-ubicado → **×1.00**
- X4 (Infraestructura): Buena → **×1.00**
- X5 (Hardware): Sin restricción → **×1.00**
- X6 (Documentación): Media → **×1.15**

```
FX = 1.50 × 1.30 × 1.00 × 1.00 × 1.00 × 1.15 = 2.24
```

**Factor Compuesto Total:**

```
FC Total = FE × FA × FC × FX
FC Total = 2.31 × 7.99 × 1.59 × 2.24
FC Total = 65.6

⚠️ CRÍTICO: Factor extremadamente alto (>20 es excepcional)

Esto indica:
1. Proyecto de altísima complejidad
2. O estamos aplicando factores incorrectamente (duplicación)

Revisión: Evitar duplicar complejidad
Si A2 (criticidad) ya incluye overhead de testing/calidad,
no aplicar A4 (complejidad pruebas) por separado.

Factor Corregido:
FA = 1.50 × 2.00 × 1.60 × 1.30 = 6.24
FC Total = 2.31 × 6.24 × 1.59 × 2.24 = 51.6

Aún muy alto. Última corrección realista:
Aplicar solo los factores más críticos sin duplicación.

Factor Realista Final:
FC = 2.31 (equipo) × 2.00 (criticidad) × 1.50 (compliance) × 1.30 (deadline)
FC = 9.01
```

---

## 8. Buffers y Contingencias

### 8.1 Buffer por Nivel de Incertidumbre

**Aplicar DESPUÉS del Factor Compuesto:**

```
Esfuerzo Final = Esfuerzo Ajustado × (1 + %Buffer)
```

| Tipo Proyecto | Buffer | Cuándo Aplicar |
|---------------|--------|----------------|
| **Mantenimiento** | +5-10% | Sistema conocido, cambios menores |
| **Proyecto Conocido** | +10-15% | Stack conocido, dominio conocido, similar a proyectos pasados |
| **Proyecto Estándar** | +15-20% | Stack conocido, dominio nuevo |
| **Proyecto con Incertidumbre** | +20-30% | Stack o dominio nuevo |
| **Proyecto Innovador** | +30-50% | Stack nuevo + dominio nuevo + tecnología emergente |
| **I+D / Investigación** | +50-100% | Alta experimentación, muchas incógnitas |

### 8.2 Cone of Uncertainty

**Precisión de Estimación por Fase:**

| Fase | Rango de Error | Buffer Sugerido |
|------|----------------|-----------------|
| **Idea Inicial** | ±100% (0.5x - 2x) | +80-100% |
| **Requerimientos Iniciales** | ±75% (0.7x - 1.75x) | +60-75% |
| **Requerimientos Completos** | ±50% (0.75x - 1.5x) | +40-50% |
| **Diseño Arquitectónico** | ±30% (0.85x - 1.3x) | +25-30% |
| **Diseño Detallado** | ±20% (0.9x - 1.2x) | +15-20% |
| **Desarrollo Iniciado** | ±10% (0.95x - 1.1x) | +10% |

### 8.3 Buffer por Tamaño de Proyecto

| Tamaño | Duración | Buffer Adicional | Razón |
|--------|----------|------------------|-------|
| **Muy Pequeño** | <1 mes | +5% | Riesgo bajo, poco margen error |
| **Pequeño** | 1-3 meses | +10% | Gestión sencilla |
| **Mediano** | 3-6 meses | +15% | Riesgos moderados |
| **Grande** | 6-12 meses | +20% | Mayor incertidumbre acumulada |
| **Muy Grande** | 12-24 meses | +30% | Muchos riesgos, cambios probables |
| **Mega Proyecto** | >24 meses | +40-50% | Casi seguro habrá cambios mayores |

---

## 9. Tablas de Referencia Rápida

### 9.1 Hoja de Cálculo Rápida

**Plantilla de Estimación:**

```
┌────────────────────────────────────────────────────────────┐
│              PLANTILLA DE ESTIMACIÓN RÁPIDA                 │
└────────────────────────────────────────────────────────────┘

1. ESTIMACIÓN BASE
   Método: [Puntos Función / Casos Uso / Descomposición]
   Horas Base (HB): _________ h

2. FACTORES DE EQUIPO (FE)
   E1 - Tamaño equipo:           ×_____
   E2 - Experiencia técnica:     ×_____
   E3 - Experiencia funcional:   ×_____
   E4 - Experiencia procesos:    ×_____
   E5 - Dedicación:              ×_____
   E6 - Rotación:                ×_____
   E7 - Conocimiento stack:      ×_____
   
   FE Total = ×_____

3. FACTORES DE APLICACIÓN (FA)
   A1 - Complejidad aplicación:  ×_____
   A2 - Criticidad:              ×_____
   A3 - Complejidad BD:          ×_____
   A4 - Complejidad pruebas:     ×_____
   A5 - Volumen información:     ×_____
   A6 - Integraciones:           ×_____
   
   FA Total = ×_____

4. FACTORES DE CLIENTE (FC)
   C1 - Disponibilidad:          ×_____
   C2 - Conocimiento negocio:    ×_____
   C3 - Claridad requerimientos: ×_____
   C4 - Volatilidad:             ×_____
   
   FC Total = ×_____

5. FACTORES DE CONTEXTO (FX)
   X1 - Compliance:              ×_____
   X2 - Deadline:                ×_____
   X3 - Distribución:            ×_____
   X4 - Infraestructura:         ×_____
   X5 - Hardware:                ×_____
   X6 - Documentación:           ×_____
   
   FX Total = ×_____

6. CÁLCULO FINAL
   Factor Compuesto (FC):
   FE × FA × FC × FX = _____ × _____ × _____ × _____ = ×_____
   
   Esfuerzo Ajustado:
   HB × FC = _____ × _____ = _________ h
   
   Buffer ([10/15/20/30]%): +_____% 
   
   Esfuerzo Final:
   EA × (1 + Buffer) = _____ × _____ = _________ h

7. CONVERSIÓN A CALENDARIO
   Recursos disponibles: _____ FTE
   Horas productivas/mes: _____ h (típico: 140h)
   
   Duración = Esfuerzo Final / (FTE × h/mes)
   Duración = _____ / (_____ × _____) = _____ meses

8. RANGO DE CONFIANZA
   Mejor caso (-15%): _____ meses
   Esperado (nominal): _____ meses
   Peor caso (+25%): _____ meses
```

---

### 9.2 Checklist de Validación

**Señales de Alerta en Estimación:**

```
🚨 FACTOR COMPUESTO >10
→ Proyecto de altísima complejidad
→ Validar que no hay duplicación de factores
→ Considerar re-scoping

🚨 FACTOR COMPUESTO <0.8
→ Probablemente subestimación
→ Validar factores aplicados
→ Considerar riesgos no contemplados

🚨 DURACIÓN >18 MESES
→ Riesgo alto de cambios en contexto
→ Considerar entregas iterativas
→ Re-evaluar MVP

🚨 EQUIPO >15 PERSONAS
→ Overhead de coordinación alto
→ Considerar división en sub-equipos
→ Aplicar factor E1 correctamente

🚨 FACTOR INDIVIDUAL >2.5
→ Factor extremo, posible show-stopper
→ Evaluar mitigaciones
→ Considerar inviabilidad del proyecto

🚨 MÚLTIPLES FACTORES >2.0
→ Riesgo compuesto muy alto
→ Proyecto probablemente subestimado
→ Revisar cada factor críticamente
```

---

### 9.3 Tabla de Conversión Rápida

**Horas a Persona-Mes (PM):**

| Horas | PM (140h/mes) | PM (160h/mes) |
|-------|---------------|---------------|
| 100 | 0.7 | 0.6 |
| 200 | 1.4 | 1.3 |
| 500 | 3.6 | 3.1 |
| 1,000 | 7.1 | 6.3 |
| 2,000 | 14.3 | 12.5 |
| 5,000 | 35.7 | 31.3 |
| 10,000 | 71.4 | 62.5 |

**Duración con Diferentes Tamaños de Equipo:**

| Esfuerzo (PM) | 1 FTE | 3 FTE | 5 FTE | 10 FTE | 15 FTE |
|---------------|-------|-------|-------|--------|--------|
| 12 PM | 12 m | 4 m | 2.4 m | 1.2 m | 0.8 m |
| 24 PM | 24 m | 8 m | 4.8 m | 2.4 m | 1.6 m |
| 48 PM | 48 m | 16 m | 9.6 m | 4.8 m | 3.2 m |
| 96 PM | 96 m | 32 m | 19.2 m | 9.6 m | 6.4 m |
| 192 PM | 192 m | 64 m | 38.4 m | 19.2 m | 12.8 m |

**Nota:** Los tiempos son teóricos. Aplicar factor de overhead de coordinación (E1).

---

## 10. Casos de Aplicación

### Caso 1: CRUD Simple

**Proyecto:** Backoffice de Administración de Productos

**Contexto:**
- Equipo: 2 developers semi-senior, conocen .NET
- Aplicación: CRUD puro, 10 tablas, sin integraciones
- Cliente: Disponible, requerimientos claros
- Contexto: Sin compliance, sin deadline estricto

**Estimación Base:** 400 horas (Puntos Función)

**Factores:**
- E2 (Experiencia): ×1.00
- E4 (Procesos): SCRUM básico ×1.00
- E7 (Stack): Conocen stack ×1.00
- A1 (Complejidad): Muy baja ×1.00
- A2 (Criticidad): Baja ×1.00
- A3 (BD): Simple ×1.00
- C1 (Disponibilidad): Buena ×1.00
- C3 (Claridad): Buena ×1.00

**Factor Compuesto:** 1.0 × 1.0 × 1.0 = **1.0**

**Esfuerzo Ajustado:** 400h × 1.0 = **400h**

**Buffer:** Proyecto conocido +10% = **440h**

**Duración:** 440h / (2 FTE × 140h/mes) = **1.6 meses**

---

### Caso 2: Sistema Empresarial Mediano

**Proyecto:** Sistema de Gestión de Inventarios

**Contexto:**
- Equipo: 6 developers (4 semi-senior, 2 junior), conocen stack
- Aplicación: Lógica moderada, 40 tablas, 2 integraciones (ERP, WMS)
- Cliente: PO disponible 70%, requerimientos medianamente claros
- Contexto: Sin compliance especial, deadline ajustado

**Estimación Base:** 2,500 horas

**Factores Aplicados:**
```
EQUIPO:
- E1 (Tamaño 6): ×1.10
- E2 (Mix): (0.67×1.00 + 0.33×1.50) = ×1.17
- E5 (Dedicación 90%): ×1.10
- E7 (Stack conocido): ×1.00
FE = 1.10 × 1.17 × 1.10 × 1.00 = 1.41

APLICACIÓN:
- A1 (Complejidad media): ×1.80
- A2 (Criticidad media): ×1.40
- A3 (BD media): ×1.40
- A6 (2 integraciones): ×1.30
FA = 1.80 × 1.40 × 1.40 × 1.30 = 4.57

CLIENTE:
- C1 (Disponibilidad 70%): ×1.15
- C3 (Claridad media): ×1.20
FC = 1.15 × 1.20 = 1.38

CONTEXTO:
- X2 (Deadline ajustado): ×1.10
FX = 1.10
```

**Factor Compuesto:** 1.41 × 4.57 × 1.38 × 1.10 = **9.76**

**Esfuerzo Ajustado:** 2,500 × 9.76 = **24,400h**

**Buffer:** +20% = **29,280h** (209 PM)

**Duración:** 29,280 / (6 × 140) = **34.9 meses**

**CONCLUSIÓN:** Proyecto inviable en plazo estimado original.

**Opciones:**
1. Reducir scope 50% → 17.5 meses
2. Aumentar equipo a 12 developers → 18 meses (con overhead)
3. Re-planificar en fases

---

### Caso 3: Sistema de Misión Crítica (Fintech)

**Proyecto:** PSP - Procesador de Pagos

**Contexto:**
- Equipo: 12 developers (6 senior, 4 semi-senior, 2 junior), 2 nuevos en stack
- Aplicación: Muy compleja, 150 tablas, 8 integraciones críticas, tiempo real
- Cliente: PO disponible, dominio complejo
- Contexto: PCI DSS, deadline regulatorio 10 meses

**Estimación Base:** 8,000 horas

**Factores Aplicados:**
```
EQUIPO:
- E1 (12 personas): ×1.25
- E2 (Mix): (0.5×0.85 + 0.33×1.0 + 0.17×1.5) = ×1.01
- E5 (Dedicación 85%): ×1.15
- E6 (Rotación 15%): ×1.10
- E7 (2 nuevos, curva aprendizaje): ×1.20
FE = 1.25 × 1.01 × 1.15 × 1.10 × 1.20 = 1.92

APLICACIÓN:
- A1 (Muy alta complejidad): ×3.50
- A2 (Criticidad crítica): ×3.00
- A3 (BD muy compleja): ×2.50
- A6 (8 integraciones críticas): ×2.50
FA = 3.50 × 3.00 × 2.50 × 2.50 = 65.6

⚠️ FACTOR DEMASIADO ALTO - REVISAR

Corrección: Evitar duplicación
A1 ya incluye criticidad e integraciones
FA corregido = 3.50 (complejidad integral) × 2.50 (BD) = 8.75

CLIENTE:
- C1 (Disponibilidad buena): ×1.00
- C2 (Conocimiento medio): ×1.15
- C3 (Claridad alta): ×1.00
- C4 (Volatilidad baja): ×1.10
FC = 1.00 × 1.15 × 1.00 × 1.10 = 1.27

CONTEXTO:
- X1 (PCI DSS): ×1.50
- X2 (Deadline agresivo 10m vs estimado): ×1.30
FX = 1.50 × 1.30 = 1.95
```

**Factor Compuesto:** 1.92 × 8.75 × 1.27 × 1.95 = **41.5**

**Esfuerzo Ajustado:** 8,000 × 41.5 = **332,000h** (2,371 PM)

**ESTO ES CLARAMENTE INCORRECTO**

**Revisión Metodológica:**

El error está en aplicar complejidad dos veces. En proyectos muy complejos:
- La estimación base (8,000h) ya debe considerar complejidad
- Los factores ajustan desviaciones del baseline, no multiplican todo

**Re-estimación Correcta:**

```
Estimación Base ya considera:
- Complejidad alta del PSP
- Criticidad

Factores de Ajuste (solo desviaciones):
- Equipo (mix, aprendizaje): ×1.92
- Compliance adicional (PCI): ×1.40
- Deadline presión: ×1.25

Factor Corregido: 1.92 × 1.40 × 1.25 = 3.36
```

**Esfuerzo Ajustado:** 8,000 × 3.36 = **26,880h** (192 PM)

**Buffer:** +25% = **33,600h** (240 PM)

**Duración:** 33,600 / (12 × 140) = **20 meses**

**CONCLUSIÓN:** No viable en 10 meses. 

**Estrategia:** MVP en 10 meses con 70% funcionalidad, roadmap post-regulatorio.

---

## 📝 Conclusión

### Principios Clave

1. **Los factores multiplican, no suman**
2. **Evitar duplicación de complejidad**
3. **Estimar base con método (PF, Casos Uso)**
4. **Aplicar factores sistemáticamente**
5. **Siempre agregar buffer de contingencia**
6. **Validar con sentido común**
7. **Presentar rangos, no números únicos**
8. **Documentar supuestos**
9. **Re-estimar cuando cambien supuestos**
10. **Aprender de cada proyecto (histórico)**

### Rangos de Sensatez

```
✅ Factor Compuesto: 1.0 - 8.0 (típico)
⚠️  Factor Compuesto: 8.0 - 15.0 (revisar)
🚨 Factor Compuesto: >15.0 (error en aplicación)

✅ Duración: 1-18 meses (manejable)
⚠️  Duración: 18-36 meses (riesgoso)
🚨 Duración: >36 meses (replantear estrategia)
```

### Última Recomendación

**Esta guía es una herramienta, no una ley absoluta.** 

Usa el juicio profesional, combina con otras técnicas (Delphi, datos históricos), y siempre comunica transparentemente los riesgos y supuestos.

---

**Versión:** 2.0  
**Fecha:** Noviembre 2025  
**Licencia:** Uso educativo y profesional libre
