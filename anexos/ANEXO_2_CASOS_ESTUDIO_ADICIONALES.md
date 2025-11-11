# Anexo 2: Casos de Estudio Adicionales

**Curso:** Estimación de Proyectos
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 1.0 - Enero 2025

---

## 📋 Índice de Contenidos

1. [Casos de Estimación PERT](#casos-pert)
2. [Casos de Planning Poker Reales](#casos-planning-poker)
3. [Casos de CCPM en Producción](#casos-ccpm)
4. [Casos de Fracaso Instructivos](#casos-fracaso)
5. [Análisis Comparativo Multi-Método](#analisis-comparativo)

---

## 📊 Casos de Estimación PERT {#casos-pert}

### Caso PERT-1: Migración de Base de Datos a la Nube

**Contexto:**
Una empresa de e-commerce necesita migrar su base de datos PostgreSQL on-premise (500GB) a AWS RDS.

**Equipo:**
- 1 DBA senior (María)
- 1 DevOps engineer (Carlos)
- 1 Backend developer (Luis)

**Restricciones:**
- Ventana de mantenimiento: Domingo 2AM-8AM
- Downtime máximo permitido: 4 horas
- No se puede hacer en fases (todo o nada)

---

#### Tarea 1: Backup completo y validación

**Estimaciones del equipo:**

| Miembro | Optimista (O) | Más Probable (M) | Pesimista (P) | Justificación |
|---------|--------------|-----------------|---------------|---------------|
| María (DBA) | 3 horas | 5 horas | 10 horas | "Con dump paralelo 3h, normal 5h, si hay corrupción y re-dump 10h" |
| Carlos (DevOps) | 4 horas | 5 horas | 8 horas | "Paralelo optimista 4h, normalizado 5h, si red lenta 8h" |
| Luis (Dev) | 5 horas | 6 horas | 12 horas | "Depende si el dump se corrompe" |

**Análisis de discrepancias:**

¿Por qué Luis es más pesimista?

```
Facilitador: "Luis, tu pesimista es 12h. María y Carlos dicen 10h y 8h.
             ¿Qué riesgo ves que ellos no?"

Luis: "He visto dumps corromperse en producción. Si pasa, hay que
      re-dumpear. Eso puede tomar otras 5h."

María: "Ah, buen punto. Yo consideré re-dump una vez (10h total).
       No consideré que podría pasar DOS veces."

Carlos: "También, si la red AWS está lenta (pasa los domingos de vez
        en cuando por mantenimiento), el upload puede tomar el doble."
```

**Estimación PERT consensuada:**

Toman el más conservador: O=3h, M=5h, P=12h

```
μ = (3 + 4×5 + 12) / 6 = (3 + 20 + 12) / 6 = 35 / 6 = 5.83 horas ≈ 6 horas

σ = (12 - 3) / 6 = 9 / 6 = 1.5 horas
```

**Resultado:**
- **Tiempo esperado:** 6 horas
- **Incertidumbre:** ±1.5 horas (68% probabilidad entre 4.5 y 7.5 horas)
- **Decisión:** NO cabe en ventana de 4 horas. Necesitan expandir ventana o partir en fases.

---

#### Tarea 2: Restore en AWS RDS

**Estimaciones:**

| O | M | P |
|---|---|---|
| 2h | 3h | 8h |

```
μ = (2 + 4×3 + 8) / 6 = 22 / 6 = 3.67 horas ≈ 4 horas
σ = (8 - 2) / 6 = 1 hora
```

---

#### Tarea 3: Validación de datos y smoke tests

**Estimaciones:**

| O | M | P |
|---|---|---|
| 1h | 2h | 6h |

```
μ = (1 + 4×2 + 6) / 6 = 15 / 6 = 2.5 horas
σ = (6 - 1) / 6 = 0.83 horas
```

---

#### Tarea 4: Switchover (cambiar DNS y aplicación)

**Estimaciones:**

| O | M | P |
|---|---|---|
| 0.5h | 1h | 3h |

```
μ = (0.5 + 4×1 + 3) / 6 = 7.5 / 6 = 1.25 horas
σ = (3 - 0.5) / 6 = 0.42 horas
```

---

### Análisis del Proyecto Completo

**Duración total esperada:**
- Tarea 1: 6h
- Tarea 2: 4h
- Tarea 3: 2.5h
- Tarea 4: 1.25h
- **Total: 13.75 horas ≈ 14 horas**

**Desviación estándar total (asumiendo independencia):**

```
σ_total = √(σ₁² + σ₂² + σ₃² + σ₄²)
σ_total = √(1.5² + 1² + 0.83² + 0.42²)
σ_total = √(2.25 + 1 + 0.69 + 0.18)
σ_total = √4.12 = 2.03 horas ≈ 2 horas
```

**Interpretación:**

Con 68% de confianza (1 desviación estándar):
- **Rango:** 12 a 16 horas

Con 95% de confianza (2 desviaciones estándar):
- **Rango:** 10 a 18 horas

**Decisión de proyecto:**

```
PM: "14 horas de trabajo esperado. Ventana original: 6 horas (2AM-8AM).

Opciones:
1. Ampliar ventana: Empezar viernes 10PM, terminar sábado 12PM
   - Downtime: 14 horas
   - Riesgo: Clientes afectados todo el sábado

2. Partir en fases:
   - Fase 1: Setup RDS en paralelo (sin downtime)
   - Fase 2: Replicación incremental
   - Fase 3: Switchover final (solo 2 horas downtime)
   - Riesgo: Más complejo técnicamente

3. Contratar consultor AWS para optimizar:
   - AWS DMS (Database Migration Service) puede reducir a 6 horas
   - Costo: $5,000
   - Riesgo: Tecnología nueva para el equipo

Decisión: Opción 2 (fases) - Mejor balance de riesgo/downtime."
```

**Lección clave:**

PERT no solo estima duración - **revela que el plan original es inviable** y fuerza replanteo estratégico.

---

### Caso PERT-2: Desarrollo de Feature con Dependencias Externas

**Contexto:**
Implementar integración con API de proveedor de pagos (Stripe).

#### Tarea crítica: "Esperar aprobación de Stripe para cuenta productiva"

**Problema:** Esta tarea NO está bajo control del equipo.

**Estimaciones del equipo:**

```
Optimista (O): 3 días (Stripe responde rápido)
Más Probable (M): 7 días (tiempo típico según documentación)
Pesimista (P): 30 días (si piden documentación adicional)
```

```
μ = (3 + 4×7 + 30) / 6 = (3 + 28 + 30) / 6 = 61 / 6 = 10.17 días ≈ 10 días

σ = (30 - 3) / 6 = 27 / 6 = 4.5 días
```

**Interpretación:**

La desviación estándar de 4.5 días es **ENORME** relativa a la media de 10 días.

Esto indica **altísima incertidumbre**.

**Análisis de riesgo:**

```
68% probabilidad: 5.5 a 14.5 días
95% probabilidad: 1 a 19 días

Peor caso (P): 30 días
```

**Estrategia de mitigación:**

1. **Paralelizar:** Hacer TODO el desarrollo con cuenta de test PRIMERO
2. **Aplicar ANTES:** Solicitar cuenta productiva DÍA 1 (no esperar a terminar dev)
3. **Plan B:** Tener Mercado Pago como alternativa (1 día de switcheo)

**Lección clave:**

Dependencias externas tienen varianza ALTA. PERT hace esto visible numéricamente (σ=4.5 días).

---

## 🎴 Casos de Planning Poker Reales {#casos-planning-poker}

### Caso PP-1: El "Simple CRUD" que No Lo Era

**Contexto:**
Startup de SaaS, equipo de 5 developers, primer sprint del MVP.

**Historia de Usuario:**

> **HU-12:** Como administrador, quiero poder crear, editar y eliminar usuarios,
> para gestionar quién tiene acceso al sistema.

**Primera impresión:** "Es un CRUD típico, 3 puntos."

---

#### Sesión de Planning Poker (transcripción real)

**Facilitador (Scrum Master):**
> "OK, HU-12: CRUD de usuarios. Product Owner, ¿puedes describirla?"

**PO:**
> "Sí, básicamente queremos que el admin pueda agregar usuarios, editarlos
> y borrarlos. Nada del otro mundo."

**Facilitador:**
> "Equipo, ¿preguntas?"

**Dev 1 (María - Backend):**
> "¿Qué campos tiene el usuario? ¿Solo nombre y email?"

**PO:**
> "Nombre, email, rol (admin/user/viewer), departamento, fecha de creación."

**Dev 2 (Carlos - Frontend):**
> "¿El form de edición es inline en la tabla o modal?"

**PO:**
> "Preferiría modal. Pero si es más fácil inline, OK."

**Dev 3 (Ana - Fullstack):**
> "Cuando decis 'eliminar', ¿es hard delete o soft delete?"

**PO:**
> "¿Cuál es la diferencia?"

**Ana:**
> "Hard delete = se borra de la base de datos para siempre.
> Soft delete = marcamos como 'inactivo' pero queda el registro."

**PO:**
> "Ah... hmm. Soft delete me parece mejor. ¿Qué pasa si borramos por error?"

**Dev 4 (Luis - Backend):**
> "OK entonces necesitamos campo 'deleted_at', lógica para filtrar users
> activos en todas las queries, y un endpoint para 'restaurar'."

**PO:**
> "Uh, sí, un endpoint para restaurar sería útil."

**Dev 5 (Pedro - Security):**
> "¿Cualquier admin puede borrar/editar cualquier usuario? ¿O solo superiores
> en jerarquía?"

**PO:**
> "Buena pregunta... Creo que solo admins deberían poder crear admins.
> Users normales no pueden crear nada."

**Pedro:**
> "Entonces necesitamos lógica de autorización. ¿Qué pasa si un admin
> intenta borrarse a sí mismo?"

**PO:**
> "Debería estar bloqueado."

**María:**
> "¿Y si es el ÚNICO admin y se borra por error? Necesitamos un
> 'super admin' que siempre exista."

**PO:**
> "Sí, mejor."

**Facilitador:**
> "OK, tenemos varias cosas nuevas. Recapitulemos:
>
> 1. Modelo User con 5 campos (no solo 2)
> 2. Modal de edición (componente nuevo)
> 3. Soft delete con 'deleted_at'
> 4. Endpoint de 'restore'
> 5. Lógica de autorización por rol
> 6. Prevención de auto-delete
> 7. Concepto de 'super admin' inmutable
>
> ¿Algo más?"

**Carlos:**
> "¿Validamos email único en frontend o solo en backend?"

**María:**
> "Backend siempre. Frontend opcional para UX."

**Carlos:**
> "Entonces necesito hacer la llamada async y manejar el error de duplicado."

**Facilitador:**
> "OK. Votemos. Recuerden que HU-2 (Login) fue 3 puntos."

---

#### Primera Votación

| Dev | Voto | Justificación |
|-----|------|---------------|
| María (Backend) | 8 | "Soft delete + authorization + super admin es más que login" |
| Carlos (Frontend) | 5 | "Modal + tabla + validación async, más de lo normal" |
| Ana (Fullstack) | 8 | "Estoy con María, hay mucho edge case" |
| Luis (Backend) | 5 | "No es TAN complejo, el modelo ya existe" |
| Pedro (Security) | 13 | "Authorization con roles es crítico, y hay casos edge (auto-delete, super admin)" |

**Dispersión:** 5 a 13 (2.6x diferencia)

---

#### Discusión de Extremos

**Facilitador a Pedro (13):**
> "Pedro, ¿por qué 13? Eso es más que Login (3) y casi tanto como Payment (13)."

**Pedro:**
> "Authorization es siempre complejo. Aquí tenemos:
> - Roles con permisos diferentes
> - Prevención de auto-delete
> - Super admin inmutable
> - Soft delete que afecta TODAS las queries
>
> Y ni hablamos de testing. Cada caso edge necesita test."

**María:**
> "Tiene razón. Yo voté 8 pero no consideré el impacto de soft delete
> en queries existentes. ¿Hay otras partes del sistema que consultan users?"

**PO:**
> "Sí, el dashboard muestra 'usuarios activos', auditoría muestra 'quién
> modificó qué', el módulo de permisos lista users..."

**Luis:**
> "OK, entonces soft delete no es solo 'agregar campo deleted_at'.
> Es refactorizar TODAS esas queries."

**Facilitador a Carlos y Luis (5):**
> "Carlos y Luis, ustedes votaron 5. ¿Cambian?"

**Carlos:**
> "Sí, ahora veo que es más. Yo solo estaba pensando en el CRUD básico."

**Luis:**
> "Yo también. No había pensado en el ripple effect del soft delete."

---

#### Segunda Votación

| Dev | Voto |
|-----|------|
| María | 8 |
| Carlos | 8 |
| Ana | 8 |
| Luis | 8 |
| Pedro | 13 |

**Facilitador:**
> "Estamos convergiendo en 8, pero Pedro sigue en 13. Pedro, ¿podemos
> separar algo?"

**Pedro:**
> "Sí. Propongo:
>
> **HU-12a:** CRUD básico con soft delete (sin restore, sin authorization compleja)
> → 8 puntos
>
> **HU-12b:** Authorization avanzada (prevención auto-delete, super admin, restore)
> → 5 puntos
>
> Total: 13, pero en 2 historias incrementales."

**PO:**
> "Me gusta. HU-12a ya nos da valor (poder gestionar users), y HU-12b
> agregamos robustez después."

**Consenso Final:**
- **HU-12a:** 8 puntos
- **HU-12b:** 5 puntos

---

### Lecciones del Caso PP-1

**1. "Simple CRUD" NO existe**
- Todo CRUD tiene edge cases
- Soft delete vs hard delete es decisión arquitectónica
- Authorization siempre es más complejo de lo que parece

**2. Planning Poker expuso suposiciones ocultas**
- Sin poker, tal vez hubieran estimado 3-5 puntos
- Con poker, Pedro forzó discusión que reveló complejidad
- Resultado: Estimación más realista (13) y split inteligente

**3. El valor NO está en el número (8+5)**
- El valor está en la CONVERSACIÓN
- Identificaron requisitos implícitos (super admin)
- Identificaron impacto sistémico (queries afectadas)

**4. El split fue mejor que consensuar en 10**
- 10 sería promedio de 8 y 13
- Pero el split en 8+5 da VALOR INCREMENTAL
- Pueden shippear HU-12a y diferir HU-12b si hay presión

---

### Caso PP-2: La Historia "Imposible de Estimar"

**Contexto:**
Empresa de fintech, migración de sistema legacy.

**Historia de Usuario:**

> **HU-99:** Como usuario, quiero que el nuevo sistema importe mis transacciones
> históricas del sistema viejo, para tener continuidad en mi historial.

---

#### Problema: Incertidumbre Extrema

**Votación:**

| Dev | Voto | Comentario |
|-----|------|-----------|
| Dev A | 21 | "El sistema viejo es un nightmare, ni documentación tiene" |
| Dev B | ? (carta interrogación) | "No sé ni por dónde empezar" |
| Dev C | 13 | "Si el export funciona bien, es manejable" |
| Dev D | ∞ (carta infinito) | "Esto podría tomar meses" |

**Dispersión:** Imposible de consensuar

---

#### Estrategia: Spike Story

**Facilitador:**
> "OK, esta historia tiene incertidumbre EXTREMA. No podemos estimarla
> porque no sabemos qué hay dentro.
>
> Propongo un **Spike**: una investigación time-boxed."

**Spike Story:**

> **SPIKE-99:** Investigar viabilidad de importación desde sistema legacy.
>
> **Time-box:** 3 días (1 developer)
>
> **Entregables:**
> 1. Documento describiendo formato de datos del sistema viejo
> 2. Script de prueba que extrae 100 transacciones de muestra
> 3. Lista de transformaciones necesarias
> 4. Estimación INFORMADA de HU-99 con 3 escenarios (best/mid/worst)

**Resultado del Spike (3 días después):**

```
Informe del Spike:

BUENA NOTICIA:
- El sistema viejo tiene export a CSV (encontrado en menú escondido)
- Formato es consistente
- Data quality es aceptable

MALA NOTICIA:
- 3 tipos diferentes de CSV según tipo de cuenta (personal/business/premium)
- Fechas en 2 formatos diferentes (antes y después de 2018)
- IDs no correlacionan directamente (necesitamos mapeo)

ESTIMACIÓN INFORMADA:

Escenario Optimista (si solo hacemos cuentas personal): 8 puntos
Escenario Realista (3 tipos de cuenta): 21 puntos
Escenario Pesimista (si hay data corrupta o formatos adicionales): 40+ puntos

RECOMENDACIÓN:
Hacer en fases:
- Fase 1: Cuentas personal (8 pts) → 80% de los usuarios
- Fase 2: Cuentas business (8 pts) → 15% de los usuarios
- Fase 3: Cuentas premium (5 pts) → 5% de los usuarios
```

**Decisión del PO:**

"Hagamos Fase 1 ahora (8 puntos). Las fases 2 y 3 van al backlog con prioridad baja."

---

### Lecciones del Caso PP-2

**1. Cuándo NO estimar**
- Si la dispersión de votos es >3x (ej: 5 a 21)
- Si múltiples personas votan "?" o "∞"
- Si la discusión no reduce incertidumbre

**2. Los Spikes son herramientas válidas**
- Time-boxed (días, no semanas)
- Objetivo: Reducir incertidumbre para estimar
- NO es "empezar a hacer la historia"

**3. Las estimaciones post-Spike son MÁS confiables**
- Basadas en datos reales, no suposiciones
- Pueden revelar opciones de split

**4. Es OK decir "No puedo estimar esto"**
- Honestidad > número inventado
- El Spike es admitir "necesito aprender primero"

---

## ⛓️ Casos de CCPM en Producción {#casos-ccpm}

### Caso CCPM-1: Implementación Real en Empresa de Software (50 personas)

**Contexto:**
- Empresa de desarrollo de software (outsourcing)
- 50 empleados, 8 proyectos simultáneos
- Problema: 60% de proyectos se entregan tarde (promedio 30% delay)
- Implementan CCPM en Enero 2024

---

#### Situación Antes de CCPM (2023)

**Proyecto típico: Sistema de gestión de inventario**

**Timeline tradicional con padding distribuido:**

| Fase | Tareas | Duración Estimada | Incluye Padding |
|------|--------|------------------|-----------------|
| Análisis y Diseño | Levantamiento requisitos, mockups | 15 días | Sí (~5 días padding) |
| Desarrollo Backend | APIs, base de datos | 25 días | Sí (~8 días padding) |
| Desarrollo Frontend | UI/UX, integración | 20 días | Sí (~6 días padding) |
| Testing | QA, corrección bugs | 15 días | Sí (~5 días padding) |
| Despliegue | Setup producción, migración | 5 días | Sí (~2 días padding) |

**Total estimado: 80 días**

**Total real promedio (2023): 105 días** (31% delay)

**¿Por qué el delay si había 26 días de padding?**

```
Análisis post-mortem típico:

Día 1-15: Análisis
- Parkinson: Usaron los 15 días completos
- Síndrome Estudiante: Empezaron con "calma"
- Padding consumido: 5 días

Día 16-40: Backend (25 días)
- Parkinson: Se expandió a 28 días
- "Refactorizamos para que quede mejor" (3 días extra)
- Padding consumido: 8 días, desperdiciados 3 días

Día 41-65: Frontend (20 días planificados)
- Multitarea mala: Backend entregó tarde, frontend esperó 3 días
- Luego tomó 23 días (Parkinson)
- Padding consumido: 6 días, desperdiciados 3 días más

Día 66-90: Testing (15 días)
- Bugs más complejos de lo esperado (código no óptimo del backend)
- Tomó 20 días reales
- Padding consumido: 5 días, INSUFICIENTE (+5 días delay)

Día 91-100: Despliegue (5 días)
- Problemas de configuración (backend no documentado correctamente)
- Tomó 10 días
- Padding consumido: 2 días, INSUFICIENTE (+5 días delay)

Total: 105 días (vs 80 planeados)
```

**Diagnóstico:**
- Padding distribuido fue consumido por Parkinson en fases tempranas
- Cuando llegaron problemas REALES (testing, despliegue), no había colchón
- Multitarea entre proyectos empeoró todo (recursos compartidos)

---

#### Implementación CCPM (Enero 2024)

**Cambios aplicados:**

1. **Estimaciones agresivas (50% probabilidad)**
   - Análisis: 15 días → 8 días
   - Backend: 25 días → 13 días
   - Frontend: 20 días → 10 días
   - Testing: 15 días → 8 días
   - Despliegue: 5 días → 3 días
   - **Total cadena crítica: 42 días**

2. **Buffers agregados**
   - Tiempo cortado: 80 - 42 = 38 días
   - Project Buffer: 50% × 38 = 19 días
   - **Timeline total: 42 + 19 = 61 días**

3. **Prohibición de multitarea mala**
   - Regla: Developer trabaja en 1 proyecto a la vez (no cambia hasta terminar su tarea)
   - Recursos compartidos (ej: DBA) tienen Resource Buffer (alertas anticipadas)

4. **Fever Chart semanal**
   - PM mide % completado de cadena crítica vs % buffer consumido
   - Reunión de 15 min cada lunes para revisar

---

#### Resultados Primer Proyecto con CCPM (Feb-Abril 2024)

**Proyecto: Sistema CRM para cliente retail**

**Timeline planificada CCPM: 55 días (cadena crítica 36 días + buffer 19 días)**

**Timeline real: 51 días** ✅

**Evolución del Fever Chart:**

| Semana | % Cadena Crítica | % Buffer Consumido | Zona | Acción |
|--------|-----------------|-------------------|------|--------|
| 1 | 15% | 5% | 🟢 Verde | Ninguna |
| 2 | 28% | 12% | 🟢 Verde | Ninguna |
| 3 | 38% | 25% | 🟢 Verde | Ninguna |
| 4 | 50% | 35% | 🟢 Verde | Ninguna |
| 5 | 58% | 52% | 🟡 Amarillo | Investigar: Testing encuentra bugs arquitectónicos |
| 6 | 68% | 68% | 🟡 Amarillo | **Acción:** Agregar 1 developer senior para ayudar con bugs |
| 7 | 85% | 75% | 🟢 Verde | Bugs resueltos, volviendo a zona verde |
| 8 | 100% | 79% | 🟢 Verde | **Proyecto completado con 21% de buffer restante** |

**Análisis:**

```
Semana 5-6: Proyecto entró en zona amarilla.

SIN Fever Chart:
- Nadie hubiera notado el problema hasta semana 7-8
- Para entonces, ya tarde para actuar

CON Fever Chart:
- Alerta temprana en semana 5
- Acción correctiva en semana 6 (agregar recurso)
- Problema resuelto, proyecto salvado

Timeline final: 51 días (vs 55 planeados)
→ 4 días ANTES del deadline
→ En enfoque tradicional (80 días), hubiera tomado ~105 días
→ CCPM fue 51% más rápido que tradicional
```

---

#### Resultados Empresa Completa (2024 full year)

**Métricas comparativas: 2023 (Tradicional) vs 2024 (CCPM)**

| Métrica | 2023 | 2024 | Mejora |
|---------|------|------|--------|
| **Proyectos on-time** | 40% | 82% | +105% |
| **Delay promedio (proyectos tarde)** | +31% | +8% | -74% |
| **Timeline promedio** | 84 días | 58 días | -31% |
| **Satisfacción cliente** | 6.8/10 | 8.9/10 | +31% |
| **Burnout equipo** | 38% reporte | 15% reporte | -61% |
| **Proyectos simultáneos manejados** | 8 | 12 | +50% |

**ROI calculado:**

```
Costo de implementar CCPM:
- Training (2 días): $8,000
- Herramienta Fever Chart: $2,000/año
- Total: $10,000

Beneficios (2024):
- 31% reducción timeline = 26 días promedio ahorrados por proyecto
- 12 proyectos/año × 26 días × $800/día tasa diaria = $249,600 ahorrados
- Menos re-work por bugs tardíos: ~$50,000 ahorrados
- Total: $299,600

ROI: ($299,600 - $10,000) / $10,000 = 2,896% (29x retorno)
```

---

### Lecciones del Caso CCPM-1

**1. CCPM requiere cambio cultural**
- Desarrolladores al principio resistieron ("50% probabilidad es imposible")
- Se requirió training y coaching
- A los 2 meses, adoptaron naturalmente

**2. Fever Chart es el hero oculto**
- Alerta temprana salvó 4 de 12 proyectos
- PM puede actuar con tiempo, no en crisis

**3. Eliminar multitarea mala es CRÍTICO**
- En 2023: Developers cambiaban entre 3 proyectos/semana
- En 2024: 1 proyecto hasta terminar su tarea
- Reducción de context switching = +25% productividad medida

**4. Buffers agregados NO se desperdician**
- En 2023: Padding distribuido (26 días) → consumido por Parkinson
- En 2024: Buffer agregado (19 días) → consumido solo por problemas reales
- Proyectos terminaron con 10-20% buffer restante en promedio

---

### Caso CCPM-2: Implementación en Construcción (Obra Residencial)

**Contexto:**
- Constructora mediana (10-15 obras simultáneas)
- Obra: Torre residencial de 8 pisos
- Implementan CCPM por primera vez en este proyecto

---

#### Proyecto: Torre "Los Pinos" (8 pisos, 32 departamentos)

**Timeline Tradicional (con padding distribuido):**

| Fase | Duración Planificada |
|------|---------------------|
| Excavación y fundaciones | 45 días |
| Estructura (8 pisos) | 160 días (20 días/piso) |
| Instalaciones (eléctricas, plomería, gas) | 80 días |
| Terminaciones (yeso, pintura, pisos) | 100 días |
| Espacios comunes (lobby, jardín) | 30 días |

**Total tradicional: 415 días (≈14 meses)**

**Problema histórico:**
- Obras similares habían tomado 18-22 meses reales
- Delays de 30-50% sobre estimación inicial
- Penalidades contractuales frecuentes

---

#### Aplicación de CCPM

**Paso 1: Identificar Cadena Crítica (con recursos)**

Recurso crítico: **Grúa torre** (solo 1 disponible, se usa para estructura Y para materiales)

Cadena crítica:
1. Excavación (con grúa para remoción de tierra)
2. Fundaciones (con grúa para hierros y encofrados)
3. Estructura (con grúa para columnas y losas)
4. Terminaciones en pisos altos (con grúa para materiales)

Otras tareas (instalaciones, espacios comunes) pueden ir en paralelo pero NO son críticas.

**Paso 2: Estimaciones agresivas**

| Fase | Tradicional | CCPM Agresivo (50%) |
|------|------------|---------------------|
| Excavación | 45 días | 25 días |
| Fundaciones | (parte de excavación) | (parte de excavación) |
| Estructura | 160 días | 100 días |
| Instalaciones | 80 días | 50 días |
| Terminaciones | 100 días | 60 días |
| Espacios comunes | 30 días | 18 días |

**Cadena crítica: 25 + 100 + 60 = 185 días**

**Tiempo cortado: 415 - 253 (suma agresiva sin buffers) = 162 días**

**Paso 3: Buffers**

**Project Buffer:** 50% × (185 días críticos cortados) = 45 días

**Feeding Buffer 1:** Instalaciones (50 días) alimenta a Terminaciones
- Buffer: 50% × (80-50) = 15 días

**Feeding Buffer 2:** Espacios comunes (18 días) alimenta a entrega final
- Buffer: 50% × (30-18) = 6 días

**Timeline total CCPM: 185 + 45 = 230 días (≈7.5 meses)**

vs Timeline tradicional: 415 días (14 meses)

**Reducción: 45% del timeline tradicional**

---

#### Ejecución Real (con Fever Chart)

**Mes 1-2 (Excavación + Fundaciones):**
- Zona 🟢 Verde
- Climaexcepcional, avance rápido
- Completado en 22 días (vs 25 planificados)
- Buffer: 0% consumido (ganaron 3 días)

**Mes 3-5 (Estructura pisos 1-5):**
- Zona 🟢 Verde
- Sin incidentes mayores
- Día 100: 50% de cadena crítica completada, 8% buffer consumido

**Mes 6 (Estructura pisos 6-8):**
- Día 120: Problema con proveedor de hormigón (huelga)
- Delay de 10 días
- Zona 🟡 Amarilla (65% completado, 30% buffer consumido)
- **Acción:** Contratar proveedor alternativo (más caro pero disponible)
- Resuelto en 5 días extras (vs 10 que hubiera sido)

**Mes 7-8 (Terminaciones):**
- Zona 🟢 Verde
- Feeding Buffer de instalaciones no fue necesario (terminaron a tiempo)
- Consumo total de buffer: 15 días de 45 disponibles

**Timeline final real: 200 días** (6.5 meses)

vs Timeline tradicional planificado: 415 días (14 meses)
vs Timeline tradicional real (histórico): 540-660 días (18-22 meses)

**Reducción real: 63-70% más rápido que proyectos históricos**

---

#### Impacto Económico

**Costos evitados:**

```
Ahorro en alquiler de grúa:
- Tradicional: 18 meses × $8,000/mes = $144,000
- CCPM: 6.5 meses × $8,000/mes = $52,000
- Ahorro: $92,000

Ahorro en costos fijos (oficina obra, seguridad):
- Tradicional: 18 meses × $12,000/mes = $216,000
- CCPM: 6.5 meses × $12,000/mes = $78,000
- Ahorro: $138,000

Penalidades contractuales evitadas:
- Contrato: $5,000/semana de delay después de mes 12
- Tradicionalmente: 6 meses delay = 26 semanas = $130,000 penalidad
- CCPM: Sin penalidad (entregado a los 6.5 meses)
- Ahorro: $130,000

Beneficio por entrega temprana:
- Cláusula bonus: $50,000 por entregar antes de mes 10
- CCPM entregó en mes 6.5 → Bonus obtenido: $50,000

Total beneficio económico: $410,000
Costo de implementar CCPM (training + consultor): $25,000
ROI: 1,540% (15x retorno)
```

---

### Lecciones del Caso CCPM-2 (Construcción)

**1. CCPM funciona fuera de software**
- Los principios son universales
- La grúa es el "recurso crítico" (como el DBA senior en software)
- Buffer protege contra clima, proveedores, permisos

**2. La velocidad genera valor exponencial**
- No solo ahorra costos directos (grúa, oficina)
- Evita penalidades contractuales
- Obtiene bonos por entrega temprana
- Libera equipo para siguiente proyecto antes

**3. Fever Chart adapta a construcción**
- Eje X: % de estructura completada (medible físicamente)
- Eje Y: % buffer consumido (días extras usados)
- Inspecciones semanales con ingeniero residente

**4. Cambio cultural en construcción es DURO**
- "Siempre lo hicimos así" es resistencia común
- Subcontratistas no entienden "estimación agresiva" al principio
- Se requirió tener reuniones explicativas con cada gremio

---

## ❌ Casos de Fracaso Instructivos {#casos-fracaso}

### Caso Fracaso-1: Planning Poker Sin Preparación

**Contexto:**
Startup early-stage, founders deciden "ser ágiles" después de leer blog.

**Qué hicieron mal:**

1. **Convocaron Planning Poker sin Product Owner claro**
   - 5 personas en la reunión
   - Nadie sabía quién tenía autoridad para decidir

2. **No establecieron historia de referencia**
   - Primera historia: "¿Cuánto es un punto?"
   - Nadie sabía, empezaron a adivinar

3. **No investigaron requisitos antes de estimar**
   - PO "improvisado" leía historias que él mismo no entendía
   - Preguntas del equipo: "No sé, averiguamos después"

4. **Discutieron cada estimación 20-30 minutos**
   - Sin facilitador entrenado
   - Conversaciones circulares
   - 5 historias tomaron 3 horas

**Resultado:**
- Estimaciones completamente inválidas
- Equipo frustrado ("esto es pérdida de tiempo")
- Abandonaron Planning Poker después de 2 sprints
- Volvieron a estimación individual arbitraria

**Lecciones:**

✅ **SÍ hacer:**
- Product Owner debe conocer historias ANTES de reunión
- Establecer historia de referencia en Sprint 0
- Tener facilitador entrenado
- Time-box de 5-10 min por historia (si se extiende, marcar como "necesita refinamiento")
- Preparar historias: AC, mockups, contexto

❌ **NO hacer:**
- Improvisar Planning Poker sin entender el proceso
- Estimar historias sin requisitos claros
- Permitir discusiones infinitas

---

### Caso Fracaso-2: CCPM Sin Compromiso de Liderazgo

**Contexto:**
Empresa mediana (200 empleados), PMO decide implementar CCPM en 5 proyectos.

**Qué hicieron mal:**

1. **No capacitaron a líderes ejecutivos**
   - VP de Operaciones no entendía CCPM
   - Seguía pidiendo estimaciones "conservadoras" a PMs
   - PMs estimaban agresivo (CCPM), VP les pedía "agregar seguridad"

2. **Conflicto con cultura existente**
   - Cultura de la empresa: "Prometer conservador, entregar antes = héroe"
   - CCPM: "Prometer agresivo, usar buffer si es necesario"
   - Desarrolladores tenían miedo de estimar agresivo

3. **Implementación parcial**
   - Usaron buffers, pero NO eliminaron multitarea
   - Resultado: Buffers se consumían igual (no atacaron Parkinson)

4. **Fever Chart sin consecuencias**
   - PMs reportaban Fever Chart, pero nadie actuaba
   - Proyectos en zona roja no recibían ayuda
   - "Es solo un gráfico más"

**Resultado:**
- 4 de 5 proyectos se retrasaron igual que antes
- 1 proyecto tuvo éxito (PM que sí aplicó CCPM 100%)
- Directivos concluyeron: "CCPM no funciona" (pero nunca lo implementaron bien)

**Lecciones:**

✅ **SÍ hacer:**
- Buy-in de ejecutivos ANTES de implementar
- Training para TODOS (no solo PMs)
- Implementar CCPM completo (no cherry-pick)
- Fever Chart debe tener consecuencias (acción cuando zona amarilla/roja)

❌ **NO hacer:**
- Implementar metodología sin cambiar cultura
- Dejar que viejos hábitos (multitarea, padding) continúen
- Ignorar señales de Fever Chart

---

### Caso Fracaso-3: PERT en Proyecto con Incertidumbre Extrema

**Contexto:**
Startup de AI/ML, producto innovador (no hay competencia directa).

**Historia:**

> "Vamos a usar PERT para estimar cuánto toma construir nuestro modelo de ML."

**Problema: PERT asume que PUEDES estimar O, M, P**

En este caso:
- **Optimista:** "Si el modelo converge en 1 semana de entrenamiento" (¿probabilidad?)
- **Más Probable:** "Tal vez 1 mes" (basado en ¿qué?)
- **Pesimista:** "Podría ser 6 meses si no converge" (o ¿infinito?)

**Resultado de PERT:**

```
O = 7 días
M = 30 días
P = 180 días

μ = (7 + 4×30 + 180) / 6 = 54 días
σ = (180 - 7) / 6 = 29 días

Interpretación: "Tomará 54 días ± 29 días"

Rango 1σ (68%): 25 a 83 días
Rango 2σ (95%): -4 a 112 días (¡negativo!)
```

**El número (54 días) es BASURA porque las estimaciones O, M, P eran ADIVINANZAS.**

**Qué hubieran debido hacer:**

```
"Este proyecto tiene incertidumbre EXTREMA. PERT no aplica.

Enfoque correcto:
1. Sprint 0 (2 semanas): Investigación, dataset, baseline model
2. Al final de Sprint 0: Re-evaluar si es viable
   - Si baseline funciona → Continuar con sprints iterativos
   - Si baseline falla → Pivotar o cancelar
3. Sprints de 2 semanas, iterando hasta convergencia
4. Forecast: 'Entre 2 y 6 meses, dependiendo de qué aprendamos'"
```

**Lecciones:**

✅ **PERT funciona cuando:**
- Hay experiencia previa en tareas similares
- Incertidumbre es moderada (no extrema)
- Puedes justificar O, M, P con datos

❌ **PERT NO funciona cuando:**
- Proyecto es R&D puro
- No hay precedentes
- Incertidumbre es "unknown unknowns"

En esos casos: **Agile iterativo** con forecasting empírico.

---

## 📊 Análisis Comparativo Multi-Método {#analisis-comparativo}

### Caso Comparativo Final: El Mismo Proyecto, 3 Enfoques

**Proyecto:** Migración de sistema monolítico a microservicios

**Equipo:** 8 developers, 1 architect, 1 PM

**Alcance:** Extraer 5 módulos del monolito a servicios independientes

---

#### Enfoque 1: Estimación Tradicional (Analogía + Juicio Experto)

**Proceso:**
1. Architect estima basado en experiencia: "Cada microservicio toma 3-4 semanas"
2. PM agrega 20% de buffer "por las dudas"
3. Total: 5 servicios × 4 semanas × 1.2 = 24 semanas

**Timeline resultante:** 36 semanas (50% delay)

**Qué salió mal:**
- Analogía no consideró complejidades específicas (un servicio tenía dependencias muy enredadas)
- Buffer distribuido se consumió por Parkinson
- Arquitecto solo estimó "happy path", no casos edge

---

#### Enfoque 2: PERT + CPM

**Proceso:**

Para cada microservicio, 3 estimaciones:

| Servicio | O | M | P | μ (PERT) |
|----------|---|---|---|----------|
| Auth | 2 sem | 3 sem | 6 sem | 3.3 sem |
| Payments | 3 sem | 5 sem | 10 sem | 5.5 sem |
| Catalog | 2 sem | 3 sem | 5 sem | 3.2 sem |
| Orders | 3 sem | 4 sem | 8 sem | 4.5 sem |
| Shipping | 2 sem | 3 sem | 6 sem | 3.3 sem |

**Total μ:** 19.8 semanas ≈ 20 semanas

**CPM (con dependencias):**
- Auth debe ir primero (otros dependen)
- Payments y Orders en paralelo después de Auth
- Catalog y Shipping en paralelo después de Orders

**Ruta Crítica:** Auth → Orders → Shipping = 3.3 + 4.5 + 3.3 = 11.1 semanas

**Timeline PERT+CPM:** 12 semanas (considerando paralelismo)

**Timeline resultante:** 15 semanas

**Ventajas sobre Tradicional:**
- Cálculo más preciso (PERT capturó incertidumbre)
- CPM identificó paralelismo (ahorró tiempo)

**Limitaciones:**
- No consideró recursos (developers compartidos)
- No protegió contra Parkinson

---

#### Enfoque 3: Planning Poker + CCPM

**Proceso:**

**Fase 1: Breakdown y Planning Poker**

Cada microservicio se descompuso en historias de usuario:

| Servicio | Historias | Total Story Points |
|----------|-----------|-------------------|
| Auth | 8 HUs | 42 puntos |
| Payments | 12 HUs | 68 puntos |
| Catalog | 6 HUs | 28 puntos |
| Orders | 10 HUs | 55 puntos |
| Shipping | 7 HUs | 35 puntos |

**Total: 228 Story Points**

**Velocidad del equipo (8 devs):** 32 puntos/semana

**Forecast inicial:** 228 / 32 = 7.1 semanas

**Fase 2: Identificar Cadena Crítica (con recursos)**

```
Recurso crítico: Architect (solo 1, necesario para diseñar cada servicio)

Cadena Crítica:
1. Architect diseña Auth (1 semana)
2. Team desarrolla Auth (1.5 semanas)
3. Architect diseña Payments (1 semana)
4. Team desarrolla Payments (2 semanas)
5. ... (secuencial para arquitectura)

vs

Planning Poker asumía paralelismo total (7 semanas)
CCPM revela: Necesitamos 12 semanas (por contención de Architect)
```

**Fase 3: Estimaciones Agresivas + Buffer**

Velocity agresiva (50% probabilidad): 40 puntos/semana (team enfocado sin multitask)

Timeline agresivo: 228 / 40 = 5.7 semanas de desarrollo
+ Arquitectura secuencial: 5 semanas
= **10.7 semanas cadena crítica**

**Project Buffer:** 50% × (contracción) ≈ 3 semanas

**Timeline total CCPM:** 10.7 + 3 = **13.7 semanas ≈ 14 semanas**

**Timeline resultante:** 13 semanas (1 semana antes del buffer)

---

### Comparación Final de los 3 Enfoques

| Enfoque | Timeline Planeada | Timeline Real | Precisión | Stress del Equipo |
|---------|------------------|--------------|-----------|-------------------|
| **Tradicional** | 24 sem | 36 sem | -50% | Alto (crunches frecuentes) |
| **PERT + CPM** | 12 sem | 15 sem | -25% | Medio (algunos crunches) |
| **Poker + CCPM** | 14 sem | 13 sem | +7% | Bajo (buffer absorbió variación) |

**Ventajas de cada método:**

**Tradicional:**
- ✅ Rápido de calcular (30 minutos)
- ❌ Menos preciso
- ❌ No identifica riesgos

**PERT + CPM:**
- ✅ Captura incertidumbre numéricamente
- ✅ Identifica ruta crítica
- ❌ Ignora recursos
- ❌ Vulnerable a Parkinson

**Planning Poker + CCPM:**
- ✅ Colaborativo (expone suposiciones)
- ✅ Considera recursos críticos
- ✅ Buffer protege contra variación real
- ✅ Fever Chart da visibilidad continua
- ❌ Requiere más tiempo de setup (2-3 horas de poker)
- ❌ Requiere cambio cultural

---

## 🎓 Conclusiones de los Casos de Estudio

### Cuándo Usar Cada Método

| Método | Mejor Para | Evitar Cuando |
|--------|-----------|---------------|
| **Estimación Experta** | Proyectos muy pequeños (1-2 semanas) | Proyectos complejos, equipos grandes |
| **PERT** | Proyectos con fases secuenciales claras, equipo pequeño | Alta incertidumbre, R&D |
| **CPM** | Proyectos con dependencias complejas, recursos ilimitados | Recursos compartidos, multitarea |
| **Planning Poker** | Equipos ágiles, backlog claro, necesidad de consenso | Requisitos muy inciertos (hacer spike primero) |
| **CCPM** | Múltiples proyectos simultáneos, recursos compartidos | Equipos muy pequeños (1-3 personas), proyectos muy cortos |

---

### Factores de Éxito Comunes

**Los casos exitosos tenían:**
1. ✅ Buy-in de liderazgo
2. ✅ Training del equipo completo
3. ✅ Implementación disciplinada (no cherry-picking)
4. ✅ Herramientas de visibilidad (Fever Chart, burndown, etc.)
5. ✅ Cultura de confianza (estimaciones honestas sin castigo)

**Los casos fallidos tenían:**
1. ❌ Resistencia de stakeholders
2. ❌ Implementación parcial ("probemos solo esta parte")
3. ❌ Falta de facilitación experta
4. ❌ Cultura tóxica (castigo por retrasos = inflación de estimaciones)

---

## 📞 Recursos Adicionales

**Para profundizar en los casos:**

- **PERT/CPM:** PMI Project Management Body of Knowledge (PMBOK), Capítulo 6
- **Planning Poker:** "Agile Estimating and Planning" - Mike Cohn (2005)
- **CCPM:** "Critical Chain" - Eliyahu Goldratt (1997)
- **Estudios de caso reales:** PM Network Magazine, Biblioteca del PMI

**Herramientas recomendadas:**

- **Planning Poker online:** PlanningPoker.com, Scrum Poker Online
- **Fever Chart:** Excel template (incluido en Anexo 3), MS Project con CCPM plugin
- **Gestión ágil:** Jira, Azure DevOps, Monday.com

---

**Fin del Anexo 2**

**Versión:** 1.0
**Última actualización:** Enero 2025
**Autor:** Alejandro Sfrede - Área de Arquitectura

---

¿Preguntas sobre estos casos? Contacto: [tu_email]
