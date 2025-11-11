# Curso de Estimación de Proyectos
## Resumen Ejecutivo

**Instructor**: Alejandro Sfrede - Área de Arquitectura
**Duración Total**: 9 horas (3 clases × 3 horas)
**Formato**: Teórico-Práctico-Interactivo

---

## Objetivo General

Capacitar a los participantes para abandonar la estimación tradicional "inflada" y adoptar un enfoque sistémico para **estimar de forma real**, gestionando explícitamente:
- Incertidumbre mediante el Cono de Incertidumbre
- Factores humanos (Parkinson, Síndrome del Estudiante)
- Riesgos y componentes de estimación
- Buffers estratégicos con CCPM

---

## Estructura del Curso

### **CLASE 1: La Crisis de la Estimación - Incertidumbre y Factores Humanos** (3 horas)

**Objetivos:**
- Comprender por qué las estimaciones tradicionales fallan sistemáticamente
- Internalizar el Cono de Incertidumbre como modelo fundamental
- Identificar y diagnosticar factores psicológicos destructivos (Parkinson, Estudiante)
- Experimentar estos conceptos mediante talleres interactivos

**Contenido:**

1. **Introducción al Problema de la Estimación** (30 min)
   - Teoría: Diferencia entre "estimación" y "plan"
   - El fracaso de las estimaciones como compromisos fijos
   - Casos de la industria: proyectos fallidos por mala estimación

2. **El Cono de Incertidumbre** (45 min)
   - Teoría: Definición y fases del cono
   - Gráfico: Variabilidad del ±400% al inicio vs ±10% al final
   - Error del enfoque tradicional (cascada)
   - Solución Ágil: "planifica poco, ponte a hacer"
   - **Interactivo**: Discusión grupal sobre proyectos fallidos

3. **🎮 TALLER 1: El Desafío del Malvavisco** (60 min)
   - Materiales: 20 espaguetis, cinta, hilo, 1 malvavisco por equipo
   - Objetivo: Experimentar el Cono de Incertidumbre
   - 18 minutos de construcción
   - **Debriefing crítico**: Conexión con teoría (iteración vs cascada)

4. **BREAK** (15 min)

5. **Factores Psicológicos: Los Enemigos Ocultos** (30 min)
   - Teoría: Ley de Parkinson - "El trabajo se expande hasta llenar el tiempo"
   - Teoría: Síndrome del Estudiante - Procrastinación sistemática
   - Teoría: Multitarea mala y cambio de contexto
   - El ciclo vicioso del padding: PM pide → Ejecutor infla → PM corta → Proyecto falla

6. **🎮 TALLER 2: Demostración de Parkinson** (30 min)
   - Dividir clase en Grupo A (15 min) y Grupo B (3 min)
   - Misma tarea, diferentes tiempos
   - **Debriefing**: El tiempo asignado dicta el tiempo consumido
   - Pregunta gancho para Clase 2: "¿Dónde ponemos entonces la seguridad?"

---

### **CLASE 2: Métodos de Estimación Tradicionales y Ágiles** (3 horas)

**Objetivos:**
- Calcular estimaciones con PERT (3 puntos) y entender CPM
- Dominar la estimación relativa vs absoluta
- Aplicar Story Points y Planning Poker
- Comprender cuándo usar cada método

**Contenido:**

1. **Métodos Clásicos: PERT y CPM** (45 min)
   - Teoría: PERT - Estimación de 3 Puntos (O, M, P)
   - **Fórmulas**:
     - Duración Esperada = `(O + 4M + P) / 6`
     - Desviación Estándar = `(P - O) / 6`
   - Teoría: CPM - Método de Ruta Crítica
   - Holgura (Slack) y su vulnerabilidad a factores psicológicos
   - **Defecto crítico**: CPM ignora recursos
   - **Ejercicio rápido**: Calcular duración esperada de 3 tareas

2. **Estimación Ágil: El Cambio de Paradigma** (45 min)
   - Teoría: Estimación Absoluta (horas) vs Relativa (comparación)
   - **Técnica 1: T-Shirt Sizing** (XS, S, M, L, XL)
     - Uso: Roadmaps trimestrales, Epics
     - Ventaja: Rápido, intuitivo, multidimensional
   - **Técnica 2: Story Points**
     - Secuencia Fibonacci: 0, 1, 2, 3, 5, 8, 13, 21
     - Combina: Esfuerzo + Complejidad + Incertidumbre
     - ¿Por qué Fibonacci? Refleja la incertidumbre creciente
   - **Flujo de refinamiento**: T-Shirt (trimestre) → Story Points (sprint)

3. **BREAK** (15 min)

4. **🎮 TALLER 3: Planning Poker - Simulación Completa** (90 min)
   - Materiales: Cartas Fibonacci por participante
   - Backlog de muestra: 5 historias de usuario
     - HU-1: Registro de usuario
     - HU-2: Login (referencia = 3 puntos)
     - HU-3: Reseteo de contraseña
     - HU-4: Reporte administrativo
     - HU-5: Pago con tarjeta

   **Proceso detallado:**
   - Product Owner presenta historia
   - Equipo hace preguntas
   - Votación simultánea (anónima)
   - Los extremos justifican (¡el corazón del taller!)
   - Re-votación → Consenso

   **Debriefing**: El valor está en la conversación, no en el número
   - Votación anónima previene anclaje
   - Exposición de suposiciones ocultas
   - Identificación de riesgos temprana

5. **Cierre Clase 2: Comparativa de Métodos** (15 min)
   - Tabla: PERT vs Agile (T-Shirt) vs Agile (Story Points)
   - Cuándo usar cada uno
   - Gancho para Clase 3: "Pero ¿cómo gestionamos la seguridad del proyecto?"

---

### **CLASE 3: La Solución de la Cadena Crítica (CCPM)** (3 horas)

**Objetivos:**
- Diferenciar CPM (Ruta Crítica) vs CCPM (Cadena Crítica)
- Entender y aplicar la gestión de Buffers (Proyecto, Alimentación, Recursos)
- Calcular una Cadena Crítica real y dimensionar buffers
- Aplicar CCPM a un caso práctico completo

**Contenido:**

1. **Introducción a CCPM y Teoría de Restricciones** (45 min)
   - Teoría: Eliyahu Goldratt y la Teoría de Restricciones (TOC)
   - Premisa: "Una cadena no es más fuerte que su eslabón más débil"
   - El problema que Goldratt vio: CPM ignora los **recursos**
   - **Definición de Cadena Crítica**: Ruta más larga considerando tareas Y recursos

   **Los 3 Principios de CCPM:**
   1. Eliminar padding de tareas → Estimaciones agresivas (50% probabilidad)
   2. Agregar seguridad como buffers → En puntos estratégicos
   3. Prohibir multitarea mala → "Focus and Finish"

2. **Gestión de Buffers: El Corazón de CCPM** (45 min)
   - **Cambio de paradigma**: Holgura (pasiva, invisible) → Buffer (activo, visible)

   **Los 3 Tipos de Buffers:**

   a) **Buffer de Proyecto (PB)**: Al final de la cadena crítica
      - Protege la fecha de entrega
      - Es propiedad del proyecto, no de la tarea

   b) **Buffer de Alimentación (FB)**: Donde cadenas no críticas alimentan la crítica
      - Protege la cadena crítica de retrasos externos
      - Evita que lo "no importante" retrase lo "crítico"

   c) **Buffer de Recursos (RB)**: NO es tiempo, es una alarma
      - Señal antes de tarea crítica que requiere recurso clave
      - Asegura disponibilidad del recurso a tiempo

   **Dimensionamiento de Buffers:**
   - Método 1: Corte del 50% (C&PM)
     - Buffer = 50% del tiempo total cortado
   - Método 2: Raíz Cuadrada de Suma de Cuadrados (SSQ)
     - Método estadísticamente robusto

   **Monitoreo: Gráfico de Fiebre**
   - Eje X: % Cadena Crítica completada
   - Eje Y: % Buffer consumido
   - Zonas: Verde (bien) → Amarilla (alerta) → Roja (acción)

3. **BREAK** (15 min)

4. **🎮 TALLER 4: Caso de Estudio CCPM Completo** (75 min)

   **Paso 1: Calcular Ruta Crítica (CPM)**
   - Proyecto con 2 rutas:
     - Ruta 1: A (10d) → B (10d) = 20 días
     - Ruta 2: A (10d) → C (5d) → D (10d) = 25 días
   - Ruta Crítica = A-C-D (25 días)

   **Paso 2: Introducir Restricción de Recursos**
   - Revelación: B y D las hace ANA (mismo recurso)
   - ¿El plan de 25 días sigue válido? **NO**
   - Ana no puede hacer multitarea

   **Paso 3: Identificar Cadena Crítica**
   - Re-planificar con recursos nivelados
   - Nueva secuencia: A → C → D → B (Ana debe terminar D antes de B)
   - Cadena Crítica = 35 días (¡más larga que Ruta Crítica!)
   - **Momento "Aha!"**: CPM dio 25 días imposibles de cumplir

   **Paso 4: Aplicar CCPM**
   - Cortar 50% del padding:
     - A: 10d → 5d
     - B: 10d → 5d
     - C: 5d → 3d
     - D: 10d → 5d
   - Nueva Cadena Crítica agresiva = 18 días
   - Tiempo cortado total = 17 días
   - Buffer de Proyecto = 50% × 17 = 9 días

   **Paso 5: Resultado Final**
   - Plan CPM (ingenuo): 25 días (incorrecto)
   - Plan Tradicional inflado: 35 días (lento, desperdiciado)
   - **Plan CCPM**: 18d + 9d buffer = **27 días** (realista y robusto)

   **Debriefing**: CCPM es más rápido que el plan inflado, pero más realista que CPM

5. **Síntesis Final y Cuadro Comparativo** (15 min)

   **Tabla Comparativa:**

   | Característica | CPM | Agile (Scrum) | CCPM |
   |---------------|-----|---------------|------|
   | **Foco** | Secuencia de tareas | Valor y adaptabilidad | Flujo y recursos |
   | **Incertidumbre** | Holgura distribuida | Iteración (re-plan) | Buffers agregados |
   | **Factores Psicológicos** | Muy vulnerable | Media vulnerabilidad | Baja (eliminada) |
   | **Recursos** | Asume ilimitados | Equipo dedicado | Central |
   | **Ideal para** | Proyectos predecibles | Requisitos emergentes | Recursos compartidos |

   **¿Cuándo usar cada método?**
   - CPM: Construcción simple, pocas restricciones de recursos
   - Agile: Software, I+D, requisitos cambiantes
   - CCPM: Manufactura, ingeniería, recursos limitados

   **Hibridación Agile-CCPM:**
   - CCPM a nivel proyecto/portfolio (plan general, buffers)
   - Agile a nivel ejecución (sprints dentro de la cadena)

6. **Cierre del Curso** (15 min)
   - Resumen de los 3 módulos
   - La estimación real es gestionar flujo y buffers visibles, no padding oculto
   - Entrega de certificados (opcional)
   - Q&A final

---

## Materiales Requeridos

### Por Clase

**Clase 1:**
- [ ] Proyector para slides
- [ ] Kits Marshmallow Challenge (por equipo de 4-5):
  - 20 espaguetis crudos
  - 1 metro cinta adhesiva
  - 1 metro hilo/cuerda
  - 1 malvavisco estándar
- [ ] Cronómetro visible
- [ ] Ejercicios Parkinson (2 versiones: 15min y 3min)
- [ ] Hojas de trabajo para discusiones

**Clase 2:**
- [ ] Proyector para slides
- [ ] Cartas Planning Poker (Fibonacci: 0,1,2,3,5,8,13,21) por participante
  - Alternativa: Herramienta online (planningpokeronline.com)
- [ ] Backlog impreso con 5 historias de usuario
- [ ] Calculadoras para ejercicios PERT
- [ ] Hojas de trabajo PERT

**Clase 3:**
- [ ] Proyector para slides
- [ ] Hojas de trabajo CCPM (caso A-B-C-D)
- [ ] Calculadoras
- [ ] Papel para diagrams de red
- [ ] Marcadores de colores
- [ ] Tabla comparativa impresa (CPM vs Agile vs CCPM)

### Documentación de Soporte

- Manual del Facilitador: `Diseño de Curso de Estimación de Proyectos.md`
- Referencia rápida CCPM: `doc/adminpro/09_Critical_Chain.pdf`
- Referencia Scrum: `doc/adminpro/Introduccion a SCRUM v1.pdf`
- Plantillas Excel: `EstimacionModuloContabilidad.xls`, `PlanillaEstimacion Workflow.xls`

---

## Evaluación y Seguimiento

### Durante el Curso
- Participación en talleres (cualitativa)
- Calidad de las discusiones en debriefings
- Precisión en ejercicios de cálculo (PERT, CCPM)

### Post-Curso (Opcional)
- Encuesta de satisfacción
- Ejercicio de aplicación: Estimar un proyecto real de la organización
- Seguimiento a 30 días: ¿Aplicaron las técnicas?

---

## Adaptaciones Recomendadas

### Para equipos de Software (IT)
- Enfatizar Clase 2 (Agile, Planning Poker)
- Clase 3: CCPM como introducción, no profundizar
- Agregar: Velocidad y forecasting

### Para equipos de Infraestructura/SRE
- Agregar módulo sobre capacidad y FinOps
- Usar caso Fintexa para ejemplos reales
- Enfatizar relación entre CCPM y planificación de capacidad

### Para Manufactura/Ingeniería
- Profundizar Clase 3 (CCPM)
- Usar Microsoft Project en taller
- Caso práctico adaptado a la industria

---

## Instructor: Alejandro Sfrede
**Área de Arquitectura**

Contacto para consultas post-curso y material adicional.

---

**Versión**: 1.0
**Fecha**: Enero 2025
**Basado en**: Material del repositorio cursoEStima
