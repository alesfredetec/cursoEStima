# Material de Estudio - Clase 1: La Crisis de la Estimación

**Curso:** Estimación de Proyectos
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Duración:** 3 horas
**Versión:** 2.0 - Formato Remoto - Enero 2025

---

## 📋 Índice

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Objetivos de Aprendizaje](#objetivos-de-aprendizaje)
3. [Conceptos Clave](#conceptos-clave)
4. [El Cono de Incertidumbre](#el-cono-de-incertidumbre)
5. [Factores que Afectan la Estimación](#factores-que-afectan-la-estimación)
6. [Clasificación de Riesgos](#clasificación-de-riesgos)
7. [Factores Psicológicos](#factores-psicológicos)
8. [Estudios Empíricos](#estudios-empíricos)
9. [Ejercicios y Actividades](#ejercicios-y-actividades)
10. [Lecturas Complementarias](#lecturas-complementarias)
11. [Preguntas de Autoevaluación](#preguntas-de-autoevaluación)

---

## 📝 Resumen Ejecutivo

### ¿De qué trata esta clase?

La Clase 1 **diagnostica el problema** de por qué las estimaciones en proyectos de software fallan sistemáticamente.

**Pregunta central:** ¿Por qué 64% de los proyectos fallan (Standish CHAOS Report)?

**Respuesta:** No es un problema técnico aislado. Es un problema **sistémico** que combina:
- Factores técnicos (complejidad, tecnología, tamaño)
- Factores humanos (experiencia, comunicación, disponibilidad)
- Factores psicológicos (**Ley de Parkinson**, **Síndrome del Estudiante**)
- Incertidumbre inherente (Cono de Incertidumbre: ±400% al inicio)

### Mensaje principal

**NO existe la "estimación perfecta".**

La incertidumbre es **inherente** a proyectos complejos.

El secreto NO es eliminar la incertidumbre, sino **gestionarla** adecuadamente.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, serás capaz de:

✅ Explicar por qué las estimaciones tradicionales fallan sistemáticamente
✅ Aplicar el Cono de Incertidumbre para adaptar el enfoque según la fase del proyecto
✅ Identificar los 16 factores que afectan la estimación (técnicos, humanos, entorno)
✅ Clasificar riesgos usando matriz Probabilidad × Impacto
✅ Reconocer y mitigar factores psicológicos: Ley de Parkinson y Síndrome del Estudiante
✅ Citar evidencia empírica de estudios reales (Tom Wujec, Microsoft, Dan Ariely)
✅ Comprender que la estimación es un problema sistémico, no solo técnico

---

## 💡 Conceptos Clave

### 1. La Crisis de la Estimación

**Definición:**
Fenómeno por el cual la mayoría de los proyectos de software:
- Se retrasan (promedio: 45%)
- Exceden presupuesto (promedio: 55%)
- Entregan menos funcionalidad de la planificada (promedio: 70%)

**Estadísticas (Standish CHAOS Report 2020):**
- ✅ **29%** de proyectos exitosos (on-time, on-budget, con todas las features)
- ⚠️ **52%** de proyectos desafiados (retrasos, sobrecostos, features reducidas)
- ❌ **19%** de proyectos cancelados o fallidos

**Por qué importa:**
- Pérdida de millones de dólares
- Frustración de equipos
- Pérdida de confianza con clientes
- Competidores nos pasan

---

### 2. El Cono de Incertidumbre

**Concepto:**
Modelo que muestra cómo la **variabilidad de la estimación** disminuye a medida que avanza el proyecto.

**Visualización:**

```
    ×4.0 ─────────────┐
                      │ Zona Optimista
    ×2.0 ─────┐       │
              │  \    │
    ×1.5 ──┐  │    \  │
           │  │      \│
    ±1.0 ──┼──┼───────●────── Estimación Central
           │  │      /│
    ×0.67──┘  │    /  │
              │  /    │
    ×0.5 ─────┘       │ Zona Pesimista
                      │
    ×0.25 ────────────┘

    Concepto  Requisitos  Diseño  Desarrollo  Entrega
```

**Fases y Variabilidad:**

| Fase | Variabilidad | Explicación |
|------|--------------|-------------|
| **Concepto Inicial** | ×0.25 a ×4.0 | ±400% de error posible |
| **Requisitos Aprobados** | ×0.5 a ×2.0 | ±200% de error |
| **Diseño UI/UX Completo** | ×0.67 a ×1.5 | ±50% de error |
| **Código Completo** | ×0.8 a ×1.25 | ±25% de error |
| **Entrega** | ×0.9 a ×1.1 | ±10% de error |

**Ejemplo Práctico:**

```
Estimación inicial en fase de Concepto: "6 meses"

Rango real:
- Optimista (×0.25): 1.5 meses
- Pesimista (×4.0): 24 meses

Estimación en fase de Diseño: "8 meses" (más información)

Rango real:
- Optimista (×0.67): 5.3 meses
- Pesimista (×1.5): 12 meses
```

**Implicación para Gestión:**

⚠️ **NO comprometas fechas fijas en fase de Concepto**

✅ **Usa rangos amplios al inicio, afina progresivamente**

✅ **Re-estima periódicamente a medida que avanzas**

---

### 3. Factores que Afectan la Estimación

Existen **16 factores principales** clasificados en 3 categorías:

#### **📐 Factores Técnicos (5 factores)**

1. **Complejidad**
   - Algoritmos complejos vs lógica simple
   - Integraciones con sistemas externos
   - Arquitectura distribuida vs monolítica
   - **Ejemplo:** Sistema de ML con 50 features vs CRUD básico

2. **Tecnología**
   - Nueva vs conocida por el equipo
   - Madura vs experimental
   - **Ejemplo:** React (conocido) vs Framework X recién lanzado

3. **Tamaño**
   - Líneas de código
   - Cantidad de componentes/módulos
   - **Ejemplo:** 5 pantallas vs 50 pantallas

4. **Calidad Requerida**
   - Nivel de testing (unitario, integración, E2E)
   - Requisitos de performance (milisegundos de respuesta)
   - Requisitos de seguridad (GDPR, PCI-DSS)
   - **Ejemplo:** Prototipo vs Sistema bancario

5. **Restricciones**
   - Hardware (debe correr en servidor X específico)
   - Software (debe usar librería Y legacy)
   - Regulatorias (cumplir con normativa Z)
   - **Ejemplo:** App móvil vs App móvil que funciona offline

---

#### **👥 Factores Humanos (5 factores)**

6. **Experiencia del Equipo**
   - Años en la tecnología
   - Proyectos similares previos
   - **Impacto:** Dev senior 3-10x más productivo que junior

7. **Disponibilidad**
   - % de dedicación al proyecto (100% vs 25%)
   - Multitarea (1 proyecto vs 5 proyectos simultáneos)
   - **Impacto:** 20-40% pérdida por cambio de contexto

8. **Comunicación**
   - Claridad de requisitos
   - Frecuencia de feedback
   - Acceso a stakeholders
   - **Ejemplo:** PO disponible diariamente vs mensajes asíncronos semanales

9. **Motivación**
   - Compromiso con el proyecto
   - Alineación con objetivos personales
   - **Impacto:** Equipo motivado 2x más productivo

10. **Rotación de Personal**
    - Salida de miembros clave
    - Onboarding de nuevos
    - **Impacto:** 3-6 meses para que nuevo miembro sea 100% productivo

---

#### **⚠️ Factores de Entorno (6 factores)**

11. **Volatilidad de Requisitos**
    - Frecuencia de cambios
    - Magnitud de cambios
    - **Estadística:** Proyectos con >25% cambio de req tienen 85% falla

12. **Dependencias Externas**
    - APIs de terceros
    - Proveedores (cloud, servicios)
    - Equipos externos
    - **Ejemplo:** "Depende de que equipo X entregue servicio Y"

13. **Procesos y Governance**
    - Burocracia organizacional
    - Aprobaciones requeridas
    - **Impacto:** Cada nivel de aprobación agrega 15-20% overhead

14. **Herramientas**
    - Calidad del IDE
    - Pipeline CI/CD automático vs manual
    - **Impacto:** DevOps maduro 2-3x más rápido en deploys

15. **Presión Temporal**
    - Deadlines irrealistas
    - Crunch mode prolongado
    - **Impacto:** Presión extrema reduce calidad 40%, aumenta bugs 60%

16. **Stakeholders**
    - Cantidad de stakeholders
    - Alineación entre ellos
    - **Ejemplo:** 1 Product Owner vs 5 gerentes con visiones diferentes

---

### 4. Clasificación de Riesgos

**Matriz Probabilidad × Impacto:**

```
           │ BAJO      │ MEDIO     │ ALTO
───────────┼───────────┼───────────┼──────────
  ALTA     │ 🟡 Medio  │ 🔴 Alto   │ 🔴 Crítico
           │ Plan      │ Acción    │ Inmediato
───────────┼───────────┼───────────┼──────────
  MEDIA    │ 🟢 Bajo   │ 🟡 Medio  │ 🔴 Alto
           │ Monitor   │ Plan      │ Acción
───────────┼───────────┼───────────┼──────────
  BAJA     │ 🟢 Bajo   │ 🟢 Bajo   │ 🟡 Medio
           │ Aceptar   │ Monitor   │ Plan
───────────┴───────────┴───────────┴──────────
                    IMPACTO
```

#### **Riesgos Críticos (🔴 Acción Inmediata)**

| Riesgo | Probabilidad | Impacto | Estrategia de Mitigación |
|--------|--------------|---------|--------------------------|
| **Cambios masivos de alcance** | Alta | Alto | - Implementar change control estricto<br>- Re-estimar después de cada cambio mayor<br>- Comunicar impacto en timeline |
| **Recurso único no disponible** | Alta | Alto | - Identificar backup/suplente<br>- Documentar conocimiento crítico<br>- Pair programming |
| **Tecnología no probada en producción** | Media | Alto | - Spike/POC antes de comprometer<br>- Tener plan B con tecnología conocida<br>- Aumentar buffer |

#### **Riesgos Importantes (🟡 Planificar Mitigación)**

| Riesgo | Probabilidad | Impacto | Estrategia |
|--------|--------------|---------|------------|
| **Requisitos ambiguos** | Alta | Medio | - Incrementar frecuencia de reviews<br>- Prototipos tempranos<br>- User Stories con criterios claros |
| **Integraciones con sistemas legacy** | Media | Medio | - Identificar puntos de integración temprano<br>- Testing de integración en ambiente similar<br>- Buffer adicional en tareas de integración |
| **Dependencia de API externa inestable** | Media | Medio | - Mock/simulador para desarrollo<br>- Monitoreo proactivo<br>- Plan de contingencia |

#### **Riesgos Menores (🟢 Monitorear)**

| Riesgo | Probabilidad | Impacto | Estrategia |
|--------|--------------|---------|------------|
| **Cambios cosméticos UI/UX** | Alta | Bajo | - Aceptar como parte normal<br>- Timeboxear revisiones de diseño |
| **Disponibilidad intermitente de ambientes** | Media | Bajo | - Ambiente local robusto<br>- Dockerización |

---

## 🧠 Factores Psicológicos

### Ley de Parkinson (1955)

**Enunciado:**

> "El trabajo se expande hasta llenar el tiempo disponible para que se termine"

**Origen:**
- Cyril Northcote Parkinson
- Artículo en The Economist (1955)
- Libro "Parkinson's Law: The Pursuit of Progress"

**Mecanismos psicológicos:**

1. **Perfeccionismo innecesario**
   - "Tengo tiempo, voy a hacer esto PERFECTO"
   - Over-engineering
   - Refactoring excesivo

2. **Exploración desenfocada**
   - "Voy a probar 5 librerías diferentes para elegir la mejor"
   - Analysis paralysis

3. **Procrastinación inicial**
   - "Tengo 10 días, puedo empezar pasado mañana"
   - Inicio tardío

4. **Expansión del alcance autoimpuesta**
   - "Ya que estoy, agrego esta feature extra"
   - Scope creep interno

**Ejemplo Clásico:**

```
Tarea: Implementar endpoint de login

Estimación con padding: 5 días (2 días reales + 3 días colchón)

¿Qué pasa?

Día 1: "Voy a investigar todas las librerías de auth disponibles"
Día 2: "Voy a hacer un diagrama detallado de arquitectura"
Día 3: "Empiezo a codear, pero voy a hacerlo MUY bien diseñado"
Día 4: "Refactorizo todo porque encontré un patrón mejor"
Día 5: "Termino justo a tiempo" ✅

Tiempo REAL necesario: 2 días
Tiempo CONSUMIDO: 5 días
Colchón DESPERDICIADO: 3 días
```

**Implicación para Estimación:**

❌ **Dar más tiempo NO mejora la calidad proporcionalmente**

❌ **El padding oculto en cada tarea se desperdicia**

✅ **Usar estimaciones agresivas + buffer agregado visible (CCPM)**

---

### Síndrome del Estudiante

**Enunciado:**

> "Las personas tienden a comenzar a trabajar seriamente en una tarea solo cuando se acerca el deadline"

**Origen:**
- Observación de comportamiento académico
- Estudiantes que empiezan trabajos/estudian el día anterior al examen
- Dan Ariely (MIT) hizo estudio formal en 2002

**Mecanismos psicológicos:**

1. **Descuento hiperbólico**
   - Humanos valoran más recompensas inmediatas que futuras
   - "El deadline está lejos, puedo hacerlo después"

2. **Optimismo injustificado**
   - "Voy a hacerlo rápido cuando empiece"
   - Subestimación de complejidad

3. **Priorización por urgencia**
   - Tareas con deadline cercano tienen prioridad
   - Tareas con deadline lejano se postergan

**Ejemplo Clásico:**

```
Tarea: Escribir documentación técnica

Deadline: 15 días

¿Qué pasa?

Día 1-10: "Tengo tiempo, primero termino otras cosas urgentes"
Día 11-13: "Bueno, ya debería empezar... mañana empiezo"
Día 14: "Mierda, es mañana. Voy a hacer un rush" (pánico)
Día 15: Entrega algo apurado, incompleto, con errores

Resultado: Calidad baja, estrés alto, mismo tiempo consumido
```

**Combinación Parkinson + Estudiante:**

```
Tarea con 15 días de deadline:

Parkinson dice: "Voy a usar los 15 días"
Estudiante dice: "Voy a empezar en día 13"

Resultado:
- Días 1-12: Procrastinación
- Días 13-15: Rush intenso, bajo colchón de Parkinson
- Entrega día 15: Justo a tiempo, calidad cuestionable
```

**Implicación para Estimación:**

❌ **Más tiempo NO significa inicio temprano**

❌ **El colchón se desperdicia en procrastinación, no se usa para contingencias**

✅ **Usar deadlines intermedios (milestones)**

✅ **Estimaciones agresivas fuerzan inicio inmediato**

---

## 📊 Estudios Empíricos

### 1. Desafío del Malvavisco (Tom Wujec, 2010)

**Experimento:**
- 70+ equipos de 4 personas
- 18 minutos para construir estructura autoportante más alta
- Materiales: 20 espaguetis, 1m cinta, 1m hilo, 1 malvavisco
- Malvavisco debe estar en la cima

**Grupos evaluados:**
- Estudiantes de MBA (prestigiosas escuelas de negocios)
- Niños de jardín de infantes (5-6 años)
- Ingenieros, arquitectos, etc.

**Resultados:**

| Grupo | Altura Promedio | Tasa de Éxito |
|-------|-----------------|---------------|
| **Niños** | 66 cm | 85% |
| **MBAs** | 25 cm | 35% |
| **Ingenieros** | 78 cm | 90% |
| **Abogados** | 20 cm | 30% |

**¿Por qué los niños ganan?**

**MBAs (Patrón de Fracaso):**
```
Minuto 1-15: Planifican exhaustivamente
            - "¿Qué diseño es óptimo?"
            - "¿Quién hace qué?"
            - "¿Cuál es la estrategia?"
Minuto 16:   Empiezan a construir
Minuto 17:   Ponen malvavisco... COLAPSA
Minuto 18:   Pánico, no hay tiempo para iterar
Resultado:   Estructura baja o caída
```

**Niños (Patrón de Éxito):**
```
Minuto 1:    Ponen malvavisco INMEDIATAMENTE
            ↳ Estructura colapsa
Minuto 2:    Ajustan, prueban otra configuración
            ↳ Malvavisco otra vez
Minuto 3-18: Iteran rápidamente
            ↳ Prueban 5-10 configuraciones
            ↳ Aprenden qué funciona
Resultado:   Estructura alta y estable
```

**Lecciones para Gestión de Proyectos:**

✅ **Iteración rápida > Planificación exhaustiva**

✅ **Probar suposiciones temprano** (el malvavisco = incertidumbre oculta)

✅ **Feedback loops cortos** (cada 2 min vs cada 17 min)

✅ **Fallar barato y rápido** (prototipo en sprint 1, no en sprint 10)

---

### 2. Microsoft Research: Impacto de Deadlines (2009)

**Estudio:**
- Mismo equipo, misma feature
- **Grupo A:** 6 semanas de deadline
- **Grupo B:** 2 semanas de deadline

**Hipótesis del experimento:**
- Si Parkinson es real → Grupo A usará 6 semanas, Grupo B usará 2 semanas
- Si calidad depende de tiempo → Grupo A tendrá mejor calidad

**Resultados:**

| Métrica | Grupo A (6 sem) | Grupo B (2 sem) | Diferencia |
|---------|-----------------|-----------------|------------|
| **Tiempo consumido** | 5.8 semanas | 2.1 semanas | **176% más** |
| **Features completadas** | 100% | 98% | Similar |
| **Bugs en producción** | 12 bugs | 14 bugs | Similar |
| **Calidad de código** | 7.2/10 | 7.5/10 | **B ligeramente mejor** |

**Conclusión:**

✅ **Ley de Parkinson confirmada:** Grupo A usó TODO el tiempo disponible

✅ **Más tiempo ≠ Mejor calidad:** De hecho, Grupo B tuvo código ligeramente mejor

✅ **Presión razonable mejora foco:** Grupo B se enfocó en lo esencial

**Implicación:**
- Deadlines ajustados (pero no imposibles) mejoran productividad
- Deadlines holgados invitan a Parkinson y desperdicio

---

### 3. Standish CHAOS Report (2020)

**Estudio más citado en industria de software:**
- 50,000+ proyectos evaluados desde 1994
- Actualización anual

**Hallazgos 2020:**

**1. Tasa de Éxito:**
- ✅ 29% de proyectos on-time, on-budget, con todas las features
- ⚠️ 52% de proyectos desafiados (retrasos, sobrecostos, features reducidas)
- ❌ 19% de proyectos cancelados

**2. Promedio de Sobrecosto/Retraso:**
- Costo: 55% por encima del estimado
- Tiempo: 45% más tiempo del estimado
- Features: Solo entregan 70% de funcionalidad prometida

**3. Factores de Éxito:**

| Factor | Proyectos Exitosos | Proyectos Fallidos |
|--------|--------------------|--------------------|
| Ejecutivo Sponsor | 95% | 30% |
| Emotional Maturity | 90% | 25% |
| User Involvement | 85% | 40% |
| Clear Requirements | 80% | 35% |
| Agile Process | 75% | 45% |

**4. Impacto del Tamaño:**

| Tamaño | Tasa de Éxito | Tasa de Falla |
|--------|---------------|---------------|
| Pequeño (<$1M, <6 meses) | 62% | 8% |
| Mediano ($1M-10M, 6-12 meses) | 27% | 18% |
| Grande (>$10M, >12 meses) | 9% | 42% |

**Lección:** Proyectos grandes fallan 5x más que proyectos pequeños

**5. Estimación con Buffer:**
- Proyectos que agregan 30% buffer: 45% siguen retrasándose
- ¿Por qué? Porque el buffer se CONSUME (Parkinson) antes de que ocurran imprevistos reales

**Implicación para Estimación:**

❌ **Agregar buffer NO resuelve el problema**

✅ **Necesitamos cambiar CÓMO gestionamos la incertidumbre** (CCPM en Clase 3)

---

### 4. Dan Ariely MIT Study: Deadlines (2002)

**Experimento:**
- 3 grupos de estudiantes
- Mismo trabajo: 3 ensayos durante semestre (14 semanas)
- Diferentes políticas de deadlines

**Grupo 1: Deadlines Autoimpuestos**
- "Entreguen deadlines para cada ensayo en Semana 1"
- No pueden cambiarlos después
- Penalización por entregar tarde

**Grupo 2: Deadlines Distribuidos (Impuestos)**
- Ensayo 1: Semana 5
- Ensayo 2: Semana 9
- Ensayo 3: Semana 14

**Grupo 3: Sin Deadlines Intermedios**
- "Entreguen los 3 ensayos en Semana 14"
- Total libertad

**Resultados:**

| Métrica | Grupo 1 (Auto) | Grupo 2 (Distribuido) | Grupo 3 (Libre) |
|---------|----------------|------------------------|-----------------|
| **Calificación Promedio** | 8.2/10 | **8.7/10** ✅ | 6.9/10 |
| **% Entregado a Tiempo** | 85% | **95%** ✅ | 60% |
| **Procrastinación (días)** | 12 días | **3 días** ✅ | 28 días |

**Conclusión:**

🥇 **Deadlines distribuidos (impuestos) = Mejor rendimiento**

🥈 **Deadlines autoimpuestos = Rendimiento intermedio**

🥉 **Sin deadlines intermedios = Peor rendimiento** (Síndrome del Estudiante máximo)

**Implicación para Proyectos:**

✅ **Usar milestones intermedios frecuentes** (sprints de 2 semanas en Ágil)

✅ **No dar "deadlines lejanos únicos"** (invitan a procrastinación)

✅ **Imponer estructura** (los equipos NO se auto-disciplinan naturalmente)

---

## 🎮 Ejercicios y Actividades

### Ejercicio 1: Demostración de Parkinson (Realizado en Clase)

**Ver:** `EJERCICIO_PARKINSON_SOPA_LETRAS.md` o `EJERCICIO_PARKINSON_VACACIONES.md`

**Objetivo:** Experimentar cómo el tiempo asignado dicta el tiempo consumido

**Reflexión personal:**
1. ¿Qué grupo tuviste? (15 min o 3 min)
2. ¿Cómo te sentiste durante el ejercicio?
3. ¿Completaste la tarea?
4. ¿En qué otras áreas de tu vida actúa Parkinson?

---

### Ejercicio 2: Identificar Factores en Tu Proyecto

**Instrucciones:**

Piensa en un proyecto real en el que estés trabajando (o trabajaste recientemente).

**Evalúa cada factor (1-5):**
- 1 = Factor no presente o impacto mínimo
- 5 = Factor muy presente o impacto crítico

| Factor | Puntaje (1-5) | Comentario |
|--------|---------------|------------|
| **Técnicos** | | |
| Complejidad | | |
| Tecnología nueva | | |
| Tamaño | | |
| Calidad requerida | | |
| Restricciones | | |
| **Humanos** | | |
| Experiencia | | |
| Disponibilidad | | |
| Comunicación | | |
| Motivación | | |
| Rotación | | |
| **Entorno** | | |
| Volatilidad requisitos | | |
| Dependencias externas | | |
| Procesos/governance | | |
| Herramientas | | |
| Presión temporal | | |
| Stakeholders | | |

**Análisis:**
- Suma total: ____
- Factores con puntaje ≥4: ____ (estos son tus riesgos principales)
- ¿Qué acciones puedes tomar para mitigar los top 3?

---

### Ejercicio 3: Matriz de Riesgos de Tu Proyecto

**Instrucciones:**

Lista 5 riesgos de tu proyecto actual:

**Riesgo 1:**
- Descripción: ___________________________________
- Probabilidad (Alta/Media/Baja): _______________
- Impacto (Alto/Medio/Bajo): ___________________
- Estrategia de mitigación: _____________________

**Riesgo 2:**
- ...

(Repetir para 5 riesgos)

**Ubica cada riesgo en la matriz 3×3**

```
           │ BAJO      │ MEDIO     │ ALTO
───────────┼───────────┼───────────┼──────────
  ALTA     │           │           │
───────────┼───────────┼───────────┼──────────
  MEDIA    │           │           │
───────────┼───────────┼───────────┼──────────
  BAJA     │           │           │
───────────┴───────────┴───────────┴──────────
```

**Reflexión:**
- ¿Cuántos riesgos están en zona ROJA? (requieren acción inmediata)
- ¿Estás tomando acciones proactivas o solo reactivas?

---

## 📚 Lecturas Complementarias

### Libros Recomendados

1. **"The Mythical Man-Month" - Frederick Brooks (1975)**
   - Clásico sobre por qué proyectos de software fallan
   - Ley de Brooks: "Agregar gente a un proyecto atrasado lo retrasa más"
   - Lectura esencial para todo PM

2. **"Software Estimation: Demystifying the Black Art" - Steve McConnell (2006)**
   - Técnicas de estimación profundas
   - Casos de estudio
   - Métricas y datos empíricos

3. **"The Phoenix Project" - Gene Kim (2013)**
   - Novela sobre DevOps y gestión de TI
   - Muestra cómo cuellos de botella matan proyectos
   - Fácil de leer, muy educativo

### Papers Académicos

1. **"Parkinson's Law" - Cyril Northcote Parkinson (1955)**
   - Artículo original en The Economist
   - Disponible online

2. **"The Cone of Uncertainty" - Barry Boehm (1981)**
   - Paper seminal sobre variabilidad en estimación
   - Base para metodologías actuales

3. **"Why Software Projects Fail" - IEEE Software (2009)**
   - Meta-análisis de estudios
   - Factores de éxito y fracaso

### Recursos Online

1. **Standish CHAOS Report**
   - www.standishgroup.com
   - Reporte anual (requiere compra, pero resúmenes disponibles gratis)

2. **Tom Wujec: Marshmallow Challenge**
   - TED Talk: "Build a Tower, Build a Team"
   - www.youtube.com/watch?v=H0_yKBitO8M

3. **Dan Ariely: Procrastination**
   - Múltiples charlas y papers
   - www.danariely.com

---

## 🧪 Preguntas de Autoevaluación

### Nivel 1: Recordar/Comprender

1. ¿Qué porcentaje de proyectos son exitosos según CHAOS Report 2020?
   <details><summary>Respuesta</summary>29%</details>

2. ¿Qué es el Cono de Incertidumbre?
   <details><summary>Respuesta</summary>Modelo que muestra cómo la variabilidad de estimación disminuye desde ±400% (concepto) hasta ±10% (entrega)</details>

3. Enuncia la Ley de Parkinson.
   <details><summary>Respuesta</summary>"El trabajo se expande hasta llenar el tiempo disponible para que se termine"</details>

4. ¿Cuáles son las 3 categorías de factores que afectan estimación?
   <details><summary>Respuesta</summary>Técnicos, Humanos, Entorno</details>

### Nivel 2: Aplicar/Analizar

5. Un proyecto está en fase de Diseño UI/UX. La estimación es "6 meses". ¿Cuál es el rango real según Cono de Incertidumbre?
   <details><summary>Respuesta</summary>×0.67 a ×1.5 → 4 a 9 meses</details>

6. Tienes un riesgo: "Tecnología X no probada" con Probabilidad ALTA e Impacto ALTO. ¿Qué color en matriz y qué acción?
   <details><summary>Respuesta</summary>🔴 Rojo, Acción Inmediata (ej: hacer POC, plan B)</details>

7. En el estudio de Microsoft (2009), ¿qué grupo fue más productivo: 6 semanas o 2 semanas?
   <details><summary>Respuesta</summary>2 semanas (176% más rápido, calidad similar)</details>

### Nivel 3: Evaluar/Crear

8. Un PM dice: "Voy a agregar 50% de buffer a cada tarea para estar seguro". ¿Qué problema tiene esta estrategia?
   <details><summary>Respuesta</summary>Padding distribuido es vulnerable a Parkinson. El buffer se GASTARÁ antes de que ocurran imprevistos reales. Mejor: estimaciones agresivas + buffer agregado visible (CCPM).</details>

9. ¿Por qué los niños ganaron en el Marshmallow Challenge?
   <details><summary>Respuesta</summary>Iteraron rápidamente probando suposiciones (pusieron malvavisco desde minuto 1). MBAs planificaron 15 min y probaron recién al final (sin tiempo para iterar).</details>

10. Diseña una estrategia para combatir Síndrome del Estudiante en tu equipo.
    <details><summary>Respuesta Ejemplo</summary>
    - Sprints cortos (2 semanas, no 3 meses)
    - Daily standups (accountability diaria)
    - Milestones intermedios con demos
    - Estimaciones agresivas (sin padding oculto)
    - Buffer agregado al final (visible, gestionado por PM)
    </details>

---

## 🎯 Para la Próxima Clase

**Clase 2: Métodos de Estimación**

Temas:
- PERT (3 puntos: Optimista, Más Probable, Pesimista)
- CPM (Ruta Crítica)
- Estimación Ágil (Story Points, Planning Poker, Velocidad)

**Preparación recomendada:**
- Revisar este material
- Pensar en proyecto actual: ¿Qué método de estimación usan?
- Traer ejemplos de historias de usuario para Planning Poker

---

**Curso:** Estimación de Proyectos
**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 2.0 - Formato Remoto - Enero 2025
