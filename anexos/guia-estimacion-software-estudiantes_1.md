# Guía Completa de Estimación de Proyectos de Software
## Material Didáctico para Estudiantes

**Versión:** 1.0  
**Última actualización:** Noviembre 2025

---

## 📚 Índice

1. [Introducción a la Estimación de Software](#1-introducción-a-la-estimación-de-software)
2. [Métodos y Modelos de Estimación](#2-métodos-y-modelos-de-estimación)
3. [Factores de Riesgo en Estimación](#3-factores-de-riesgo-en-estimación)
4. [Aplicación Práctica](#4-aplicación-práctica)
5. [Ejercicios y Casos de Estudio](#5-ejercicios-y-casos-de-estudio)
6. [Referencias y Recursos](#6-referencias-y-recursos)

---

## 1. Introducción a la Estimación de Software

### 1.1 ¿Por qué es importante estimar?

La estimación de proyectos de software es una competencia crítica porque permite:

- **Planificar recursos**: Saber cuántas personas y cuánto tiempo necesitamos
- **Gestionar expectativas**: Comunicar plazos realistas a stakeholders
- **Controlar costos**: Presupuestar adecuadamente el proyecto
- **Tomar decisiones**: Evaluar viabilidad y priorizar funcionalidades
- **Mitigar riesgos**: Identificar factores que pueden afectar el proyecto

### 1.2 El Desafío de la Estimación

> **"Estimar software es como predecir el clima: podemos usar modelos científicos, pero siempre hay incertidumbre."**

**Razones de la dificultad:**
- Cada proyecto es único
- Los requerimientos cambian
- La tecnología evoluciona rápidamente
- El factor humano es impredecible
- Hay muchas variables interrelacionadas

### 1.3 Tipos de Estimación

#### Estimación por Analogía
Comparar con proyectos similares del pasado.
```
Ejemplo: "El módulo de reportes tomó 3 meses en el proyecto anterior, 
este será similar, estimamos 3 meses también."
```

#### Estimación Paramétrica
Usar modelos matemáticos basados en métricas.
```
Fórmula: Esfuerzo = A × (Tamaño)^B × Multiplicadores
```

#### Estimación por Descomposición
Dividir el proyecto en partes pequeñas y estimar cada una.
```
Sistema = Módulo A (20h) + Módulo B (35h) + Módulo C (15h) + Integración (10h)
```

#### Estimación por Juicio de Expertos
Consultar a personas con experiencia relevante (método Delphi).

### 1.4 Métricas Comunes

| Métrica | Descripción | Uso Típico |
|---------|-------------|------------|
| **LOC** (Lines of Code) | Líneas de código fuente | Proyectos con tecnología definida |
| **PF** (Puntos Función) | Funcionalidad desde perspectiva usuario | Proyectos en etapa de requerimientos |
| **PCU** (Puntos Caso de Uso) | Basado en casos de uso UML | Proyectos con diseño orientado a objetos |
| **Persona-Mes (PM)** | Esfuerzo de 1 persona en 1 mes | Planificación de recursos |
| **Story Points** | Complejidad relativa (Ágil) | Proyectos con metodologías ágiles |

---

## 2. Métodos y Modelos de Estimación

### 2.1 COCOMO II (Constructive Cost Model)

#### 📖 Descripción
Modelo paramétrico desarrollado por Barry Boehm en 1981 (COCOMO I) y actualizado en 2000 (COCOMO II). Es el modelo más conocido y estudiado académicamente.

#### 🎯 Cuándo Usar
- Proyectos medianos a grandes
- Cuando tienes datos históricos para calibrar
- En fases de diseño o post-arquitectura
- Para comparar alternativas de diseño

#### 📐 Fórmula Base

```
Esfuerzo (PM) = A × (Tamaño)^B × ∏(EMi)

Donde:
- PM = Persona-Mes (1 persona trabajando 1 mes)
- A = Constante (2.94 por defecto)
- Tamaño = KLOC o Puntos Función
- B = Exponente de escala (0.91 a 1.23)
- EMi = Multiplicadores de Esfuerzo (17 factores)
```

#### 🔢 Tres Niveles de COCOMO II

**1. Composición de Aplicación** (Prototipo inicial)
- Usa Puntos Objeto (screens, reports, components)
- Para estimaciones muy tempranas
- Precisión: ±75%

**2. Diseño Temprano** (Después de requerimientos)
- Usa Puntos Función o KLOC aproximado
- 7 multiplicadores de esfuerzo
- Precisión: ±50%

**3. Post-Arquitectura** (Diseño detallado)
- Usa KLOC o PF ajustados
- 17 multiplicadores de esfuerzo
- Precisión: ±25-30%

#### 📊 Multiplicadores de Esfuerzo (ejemplos)

| Factor | Muy Bajo | Bajo | Nominal | Alto | Muy Alto | Extra Alto |
|--------|----------|------|---------|------|----------|------------|
| RELY (Confiabilidad) | 0.82 | 0.92 | 1.00 | 1.10 | 1.26 | - |
| CPLX (Complejidad) | 0.73 | 0.87 | 1.00 | 1.17 | 1.34 | 1.74 |
| ACAP (Capacidad Analistas) | 1.42 | 1.19 | 1.00 | 0.85 | 0.71 | - |
| PCAP (Capacidad Programadores) | 1.34 | 1.15 | 1.00 | 0.88 | 0.76 | - |
| TOOL (Herramientas) | 1.17 | 1.09 | 1.00 | 0.90 | 0.78 | - |

**Interpretación:**
- Valores <1.0: Reducen el esfuerzo (factores positivos)
- Valores >1.0: Aumentan el esfuerzo (factores negativos)

#### 💡 Ejemplo Práctico

**Proyecto:** API REST para gestión de pagos

**Datos:**
- Tamaño estimado: 50 KLOC (50,000 líneas de código)
- Confiabilidad: Alta (sistema financiero) → 1.10
- Complejidad: Alta (integraciones bancarias) → 1.17
- Capacidad del equipo: Nominal → 1.00
- Herramientas: Muy buenas (IDE, CI/CD) → 0.78

**Cálculo:**
```
A = 2.94
B = 1.12 (proyecto semi-detached)
Tamaño = 50 KLOC

Esfuerzo = 2.94 × (50)^1.12 × (1.10 × 1.17 × 1.00 × 0.78)
Esfuerzo = 2.94 × 65.2 × 1.003
Esfuerzo ≈ 192 PM (Persona-Mes)

Con equipo de 10 personas: 192/10 = 19.2 meses
Con equipo de 15 personas: 192/15 = 12.8 meses
```

#### ✅ Ventajas
- Método científico y ampliamente validado
- Base de datos histórica de miles de proyectos
- Considera múltiples factores del proyecto
- Herramientas de software disponibles
- Estándar de la industria para proyectos grandes

#### ❌ Desventajas
- Requiere experiencia para calibrar multiplicadores
- Necesita conocer tamaño (LOC/PF) tempranamente
- Difícil de aplicar en proyectos ágiles iterativos
- Curva de aprendizaje pronunciada
- Puede sobreestimar proyectos pequeños

#### 🎓 Ejercicio
**Tu turno:** Estima un sistema de e-commerce con 30 KLOC, complejidad media (CPLX=1.00), equipo junior (PCAP=1.15), herramientas buenas (TOOL=0.90).

---

### 2.2 Puntos Función (Function Points)

#### 📖 Descripción
Métrica de tamaño funcional creada por Allan Albrecht (IBM) en 1979. Mide la funcionalidad entregada al usuario **independientemente de la tecnología**.

#### 🎯 Cuándo Usar
- Fase temprana (requerimientos funcionales)
- Para comparar proyectos en diferentes tecnologías
- Cuando no sabes cuántas líneas de código tendrás
- Proyectos con énfasis en funcionalidad de negocio
- Mantenimiento y evolución de sistemas

#### 📐 Método de Cálculo

**Paso 1: Identificar Componentes Funcionales**

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DE SOFTWARE                       │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           ENTRADA DE DATOS (EI)                     │   │
│  │  - Formularios, pantallas de captura               │   │
│  │  - APIs que reciben datos                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           SALIDAS PROCESADAS (EO)                   │   │
│  │  - Reportes con cálculos                            │   │
│  │  - Dashboards con agregaciones                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           CONSULTAS SIMPLES (EQ)                    │   │
│  │  - Búsquedas, listados sin procesamiento           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │    ARCHIVOS LÓGICOS INTERNOS (ILF)                  │   │
│  │  - Tablas/entidades que mantiene el sistema        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │    ARCHIVOS INTERFAZ EXTERNA (EIF)                  │   │
│  │  - Datos de otros sistemas que se usan             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Paso 2: Contar y Clasificar por Complejidad**

| Componente | Complejidad Baja | Media | Alta |
|------------|------------------|-------|------|
| **EI** (Entradas) | 3 PF | 4 PF | 6 PF |
| **EO** (Salidas) | 4 PF | 5 PF | 7 PF |
| **EQ** (Consultas) | 3 PF | 4 PF | 6 PF |
| **ILF** (Archivos Internos) | 7 PF | 10 PF | 15 PF |
| **EIF** (Archivos Externos) | 5 PF | 7 PF | 10 PF |

**Criterios de Complejidad:**

**Para EI (Entradas):**
- **Baja:** ≤4 campos, 1 archivo referenciado, lógica simple
- **Media:** 5-15 campos, 2-3 archivos, validaciones estándar
- **Alta:** >15 campos, >3 archivos, lógica compleja

**Para ILF (Archivos):**
- **Baja:** ≤19 campos, 1 relación
- **Media:** 20-50 campos, 2-5 relaciones
- **Alta:** >50 campos, >5 relaciones

#### 💡 Ejemplo Completo: Sistema de Gestión de Biblioteca

**Entradas (EI):**
1. **Registrar usuario**
   - Campos: nombre, apellido, email, teléfono, dirección (5 campos)
   - Archivos: Usuarios
   - Validaciones: email único, formato teléfono
   - **Complejidad: Media → 4 PF**

2. **Préstamo de libro**
   - Campos: usuario, libro, fecha préstamo, fecha devolución (4 campos)
   - Archivos: Préstamos, Usuarios, Libros
   - Validaciones: disponibilidad, límite de préstamos, multas pendientes
   - **Complejidad: Alta → 6 PF**

3. **Devolver libro**
   - Campos: código préstamo, fecha devolución (2 campos)
   - Archivos: Préstamos
   - Validaciones: calcular multas por retraso
   - **Complejidad: Media → 4 PF**

**Salidas (EO):**
1. **Reporte de préstamos por usuario**
   - Cálculos: total préstamos, multas acumuladas, estado
   - **Complejidad: Media → 5 PF**

2. **Listado de libros más prestados**
   - Cálculos: ranking, porcentajes, tendencias
   - **Complejidad: Alta → 7 PF**

**Consultas (EQ):**
1. **Buscar libro por título/autor**
   - Sin procesamiento complejo
   - **Complejidad: Baja → 3 PF**

2. **Consultar historial de usuario**
   - Listado simple sin cálculos
   - **Complejidad: Media → 4 PF**

**Archivos Internos (ILF):**
1. **Usuarios**
   - Campos: 10 (id, nombre, apellido, email, teléfono, dirección, etc.)
   - Relaciones: Préstamos
   - **Complejidad: Baja → 7 PF**

2. **Libros**
   - Campos: 15 (id, título, autor, ISBN, editorial, año, categoría, etc.)
   - Relaciones: Préstamos, Categorías, Autores
   - **Complejidad: Media → 10 PF**

3. **Préstamos**
   - Campos: 12 (id, usuario, libro, fecha_préstamo, fecha_devolución, etc.)
   - Relaciones: Usuarios, Libros, Multas
   - **Complejidad: Media → 10 PF**

**Archivos Externos (EIF):**
1. **Catálogo ISBN Global**
   - Datos externos para validar libros
   - **Complejidad: Baja → 5 PF**

**Total PFNA (Puntos Función No Ajustados):**
```
EI:  4 + 6 + 4 = 14 PF
EO:  5 + 7 = 12 PF
EQ:  3 + 4 = 7 PF
ILF: 7 + 10 + 10 = 27 PF
EIF: 5 = 5 PF

PFNA = 14 + 12 + 7 + 27 + 5 = 65 PF
```

**Paso 3: Factor de Ajuste (0.65 - 1.35)**

14 Características Generales del Sistema (cada una se puntúa 0-5):

1. Comunicación de datos (4 - Alta)
2. Procesamiento distribuido (2 - Bajo)
3. Performance (3 - Media)
4. Configuración muy usada (2 - Bajo)
5. Tasa de transacciones (2 - Bajo)
6. Entrada online (4 - Alta)
7. Eficiencia del usuario final (3 - Media)
8. Actualización online (4 - Alta)
9. Complejidad de procesamiento (3 - Media)
10. Reusabilidad (3 - Media)
11. Facilidad de instalación (4 - Alta)
12. Facilidad de operación (4 - Alta)
13. Múltiples sitios (1 - Muy bajo)
14. Facilidad de cambios (3 - Media)

**Suma:** 42 puntos

**Factor de Ajuste:** 0.65 + (0.01 × 42) = 1.07

**Paso 4: Puntos Función Ajustados**
```
PFA = PFNA × Factor de Ajuste
PFA = 65 × 1.07 = 69.55 ≈ 70 PF
```

**Paso 5: Estimar Esfuerzo**

Productividad típica por industria (horas por PF):

| Tipo de Sistema | Horas/PF |
|-----------------|----------|
| CRUD Simple | 5-8 h |
| Aplicación Empresarial | 10-15 h |
| Sistema Financiero | 15-20 h |
| Sistema de Misión Crítica | 20-30 h |

Para nuestra biblioteca (aplicación empresarial): **12 h/PF**

```
Esfuerzo = 70 PF × 12 h/PF = 840 horas
Con jornada de 8h/día: 840 / 8 = 105 días
Con 1 desarrollador: 105 / 20 días laborables = 5.25 meses
Con 2 desarrolladores: 2.6 meses
```

#### ✅ Ventajas
- Independiente de tecnología (permite comparar Java vs .NET)
- Aplicable muy temprano (solo necesita requerimientos)
- Estándar internacional (ISO/IEC 20926)
- Enfocado en valor para el usuario
- Útil para benchmarking entre proyectos

#### ❌ Desventajas
- Requiere entrenamiento (certificación IFPUG)
- Subjetividad al clasificar complejidad
- No considera arquitectura técnica (microservicios, cloud)
- Toma tiempo contar correctamente (2-8 horas por proyecto)
- Puede subestimar complejidad técnica

#### 🎓 Ejercicio
**Tu turno:** Calcula los PF para un módulo de facturación que tiene:
- 3 pantallas de entrada (alta, baja, modificación)
- 2 reportes (facturas del mes, facturas vencidas)
- 2 consultas (buscar factura, ver detalle)
- 2 tablas (Facturas con 20 campos, Clientes con 15 campos)

---

### 2.3 Puntos Caso de Uso (Use Case Points)

#### 📖 Descripción
Método creado por Gustav Karner (1993) basado en casos de uso UML. Variante simplificada de Puntos Función para proyectos orientados a objetos.

#### 🎯 Cuándo Usar
- Proyectos con casos de uso definidos
- Metodologías orientadas a objetos (RUP, UP)
- Cuando tienes diagramas de casos de uso
- Estimaciones tempranas con UML

#### 📐 Fórmula

```
1. UUCP = UAW + UUCW
   (Puntos sin ajustar = Peso Actores + Peso Casos de Uso)

2. TCF = Factor Técnico (13 factores)
3. ECF = Factor Ambiental (8 factores)

4. UCP = UUCP × TCF × ECF

5. Esfuerzo (horas) = UCP × 20 horas promedio
```

#### 📊 Clasificación de Actores

| Tipo | Descripción | Peso |
|------|-------------|------|
| **Simple** | Sistema externo vía API | 1 |
| **Medio** | Sistema vía protocolo o interfaz estándar | 2 |
| **Complejo** | Usuario humano con interfaz gráfica | 3 |

#### 📊 Clasificación de Casos de Uso

| Complejidad | Transacciones | Clases de Análisis | Peso |
|-------------|---------------|---------------------|------|
| **Simple** | ≤3 | 1-5 | 5 |
| **Medio** | 4-7 | 6-10 | 10 |
| **Complejo** | >7 | >10 | 20 |

**¿Qué es una transacción?**
- Un paso significativo en el caso de uso
- Una interacción entre actor y sistema
- Un cambio de estado o validación importante

#### 💡 Ejemplo: Sistema de Reservas de Hotel

**Actores:**
1. **Cliente** (interfaz web) → Complejo = 3 puntos
2. **Recepcionista** (interfaz desktop) → Complejo = 3 puntos
3. **Sistema de Pagos** (API externa) → Simple = 1 punto
4. **Sistema de Email** (SMTP) → Medio = 2 puntos

**UAW (Peso Actores)** = 3 + 3 + 1 + 2 = **9 puntos**

**Casos de Uso:**

1. **Login** (Simple - 5 puntos)
   - Transacciones: 2 (ingresar credenciales, validar)
   - Clases: 2 (Usuario, Sesión)

2. **Buscar Habitación Disponible** (Medio - 10 puntos)
   - Transacciones: 5 (ingresar fechas, seleccionar tipo, filtrar, mostrar resultados, ver detalle)
   - Clases: 6 (Habitación, Reserva, TipoHabitación, Disponibilidad, etc.)

3. **Realizar Reserva** (Complejo - 20 puntos)
   - Transacciones: 9 (seleccionar habitación, ingresar datos, validar disponibilidad, verificar cliente, calcular precio, aplicar descuentos, confirmar, procesar pago, enviar confirmación)
   - Clases: 12 (Reserva, Cliente, Habitación, Pago, Email, Descuento, etc.)

4. **Cancelar Reserva** (Medio - 10 puntos)
   - Transacciones: 6 (buscar reserva, validar política cancelación, calcular reembolso, procesar cancelación, liberar habitación, notificar)
   - Clases: 8 (Reserva, PoliticaCancelación, Reembolso, etc.)

5. **Check-in** (Medio - 10 puntos)
   - Transacciones: 5 (validar reserva, verificar pago, asignar habitación física, generar llave, registrar entrada)
   - Clases: 7 (Reserva, CheckIn, Habitación, Llave, etc.)

6. **Check-out** (Medio - 10 puntos)
   - Transacciones: 6 (calcular consumos, generar factura, procesar pago adicional, liberar habitación, entregar llave, cerrar estancia)
   - Clases: 8 (CheckOut, Factura, Consumo, Pago, etc.)

**UUCW (Peso Casos de Uso)** = 5 + 10 + 20 + 10 + 10 + 10 = **65 puntos**

**UUCP** = 9 + 65 = **74 puntos**

#### 🔧 Factores Técnicos (TCF)

13 factores técnicos, cada uno ponderado de 0 (irrelevante) a 5 (esencial):

| Factor | Descripción | Peso | Valor | Subtotal |
|--------|-------------|------|-------|----------|
| T1 | Sistema distribuido | 2 | 4 | 8 |
| T2 | Performance/tiempo respuesta | 1 | 5 | 5 |
| T3 | Eficiencia usuario final | 1 | 4 | 4 |
| T4 | Procesamiento interno complejo | 1 | 3 | 3 |
| T5 | Código reutilizable | 1 | 3 | 3 |
| T6 | Facilidad de instalación | 0.5 | 4 | 2 |
| T7 | Facilidad de uso | 0.5 | 5 | 2.5 |
| T8 | Portabilidad multiplataforma | 2 | 2 | 4 |
| T9 | Facilidad de cambios | 1 | 3 | 3 |
| T10 | Concurrencia (múltiples usuarios) | 1 | 5 | 5 |
| T11 | Seguridad | 1 | 5 | 5 |
| T12 | Acceso a terceros | 1 | 4 | 4 |
| T13 | Capacitación especial requerida | 1 | 2 | 2 |

**TFactor** = 0.6 + (0.01 × Suma) = 0.6 + (0.01 × 50.5) = **1.105**

#### 🧑‍💼 Factores Ambientales (ECF)

8 factores del equipo, ponderados -1.5 a +1.5 y valorados 0-5:

| Factor | Descripción | Peso | Valor | Subtotal |
|--------|-------------|------|-------|----------|
| E1 | Familiaridad con proceso desarrollo | 1.5 | 4 | 6.0 |
| E2 | Experiencia en aplicación | 0.5 | 3 | 1.5 |
| E3 | Experiencia OO | 1 | 4 | 4.0 |
| E4 | Capacidad del analista líder | 0.5 | 5 | 2.5 |
| E5 | Motivación del equipo | 1 | 4 | 4.0 |
| E6 | Estabilidad de requerimientos | 2 | 2 | 4.0 |
| E7 | Personal part-time | -1 | 1 | -1.0 |
| E8 | Dificultad lenguaje programación | -1 | 2 | -2.0 |

**EFactor** = 1.4 + (-0.03 × Suma) = 1.4 + (-0.03 × 19) = **0.83**

#### 🎯 Cálculo Final

```
UCP = UUCP × TCF × ECF
UCP = 74 × 1.105 × 0.83
UCP = 67.87 ≈ 68 UCP

Esfuerzo = UCP × 20 horas
Esfuerzo = 68 × 20 = 1,360 horas

Calendario:
- Con 1 desarrollador: 1,360 / 160h/mes = 8.5 meses
- Con 2 desarrolladores: 4.25 meses
- Con 4 desarrolladores: 2.1 meses
```

#### ✅ Ventajas
- Método estructurado y relativamente simple
- Basado en casos de uso (común en análisis)
- Considera factores técnicos y del equipo
- Buena precisión para proyectos OO
- Más rápido que Puntos Función

#### ❌ Desventajas
- Requiere casos de uso bien definidos
- Menos precisión que métodos paramétricos complejos
- Subjetividad al clasificar complejidad
- No es estándar ISO (menos aceptación)
- Puede fallar en arquitecturas no tradicionales

#### 🎓 Ejercicio
**Tu turno:** Calcula UCP para un sistema de gestión de gimnasio con:
- 3 actores: Cliente (web), Entrenador (app), Sistema de Pago (API)
- 5 casos de uso: Registrarse (simple), Reservar clase (medio), Pagar mensualidad (complejo), Ver rutinas (simple), Seguimiento progreso (medio)

---

### 2.4 Método Delphi

#### 📖 Descripción
Técnica de juicio de expertos estructurada para lograr consenso. Desarrollada por RAND Corporation en los años 1950.

#### 🎯 Cuándo Usar
- No hay datos históricos
- Proyectos innovadores o únicos
- Alta incertidumbre
- Necesitas múltiples perspectivas
- Para validar otras estimaciones

#### 📐 Proceso Paso a Paso

```
┌───────────────────────────────────────────────────────────┐
│                     MÉTODO DELPHI                         │
└───────────────────────────────────────────────────────────┘

PREPARACIÓN
├─ Seleccionar 3-7 expertos con diferentes perspectivas
├─ Definir el problema/proyecto claramente
└─ Preparar plantilla de estimación

RONDA 1 (Estimación Independiente)
├─ Cada experto estima ANÓNIMAMENTE
├─ Documentan supuestos y justificaciones
├─ Sin comunicación entre expertos
└─ Plazo: 2-3 días

ANÁLISIS 1
├─ Recopilar todas las estimaciones
├─ Calcular estadísticas (media, mediana, rango)
├─ Anonimizar y compilar justificaciones
└─ Identificar outliers

RONDA 2 (Revisión)
├─ Compartir resultados agregados anónimos
├─ Expertos revisan su estimación
├─ Pueden mantener o ajustar
├─ Nuevas justificaciones si cambian
└─ Plazo: 2-3 días

ANÁLISIS 2
├─ Recopilar estimaciones actualizadas
├─ Calcular nueva estadística
├─ Verificar convergencia
└─ ¿Consenso alcanzado? → Sí/No

RONDA 3 (Si necesario)
├─ Compartir nueva información
├─ Última oportunidad de ajuste
└─ Máximo 3 rondas (usualmente suficiente)

CONSOLIDACIÓN
├─ Presentar resultado final
├─ Usar promedio ponderado o mediana
├─ Documentar rango de incertidumbre
└─ Generar informe ejecutivo
```

#### 💡 Ejemplo Completo

**Proyecto:** Migrar sistema monolítico a microservicios

**Expertos Seleccionados:**
1. **Arquitecto de Software** (15 años experiencia)
2. **Tech Lead Backend** (8 años, conoce el sistema actual)
3. **DevOps Engineer** (10 años, experto en cloud)
4. **DBA Senior** (12 años, conoce la base de datos)
5. **QA Manager** (7 años, conoce testing del sistema)

---

**RONDA 1: Estimaciones Iniciales**

| Experto | Estimación | Justificación |
|---------|------------|---------------|
| Arquitecto | **24 meses** | "Refactorización compleja, 150K LOC, 12 módulos. Necesita rediseño completo de APIs, implementar event sourcing, testing exhaustivo. Riesgo de regresión alto." |
| Tech Lead | **15 meses** | "El equipo conoce bien el código, muchos componentes ya están desacoplados. Con inversión en automatización de tests, podemos ser ágiles. Estimo 5 microservicios principales." |
| DevOps | **30 meses** | "Incluyo setup completo de infraestructura: K8s, CI/CD, monitoring, logging. Migración de datos es compleja. Plan de rollback y fase de coexistencia monolito-microservicios añade tiempo." |
| DBA | **20 meses** | "La base de datos tiene 80 tablas con alta interdependencia. Necesitamos database-per-service, ETL, sincronización temporal. Riesgo en consistencia eventual." |
| QA Manager | **18 meses** | "Considerando que debemos mantener paridad funcional, cada microservicio necesita full testing. Tests de integración son críticos. Pero si vamos incremental, es manejable." |

**Análisis Ronda 1:**
- Rango: 15 - 30 meses (muy amplio)
- Media: 21.4 meses
- Mediana: 20 meses
- Outliers: DevOps (muy alto), Tech Lead (muy bajo)

---

**RONDA 2: Después de Compartir**

**Feedback Agregado Compartido:**
```
- Rango de estimaciones: 15-30 meses
- Media: 21.4 meses
- Preocupaciones comunes:
  * Complejidad de base de datos
  * Testing exhaustivo necesario
  * Infraestructura cloud
  * Fase de coexistencia monolito-micro
  
- Diferencias de opinión:
  * ¿Es posible rollout incremental?
  * ¿Cuánto pesa la infraestructura?
  * ¿Nivel de automatización disponible?
```

**Estimaciones Revisadas:**

| Experto | Nueva Estimación | Cambio | Justificación del Cambio |
|---------|------------------|--------|--------------------------|
| Arquitecto | **22 meses** | -2 | "Acepto que rollout incremental reduce riesgo. Si priorizamos 5 microservicios core, podemos ser más ágiles que refactorizar todo." |
| Tech Lead | **17 meses** | +2 | "Considerando puntos de QA y DBA sobre testing e integración de datos, necesito ser más conservador. Subestimé complejidad de consistencia eventual." |
| DevOps | **24 meses** | -6 | "Si infraestructura de K8s ya está lista (lo confirmo con el equipo), mi estimación baja. Pero mantengo buffer por migración gradual y monitoreo robusto." |
| DBA | **20 meses** | = | "Mantengo estimación. Los puntos del Arquitecto sobre priorización son válidos, pero la complejidad de datos no cambia." |
| QA Manager | **19 meses** | +1 | "Después de ver preocupaciones de DBA, añado tiempo para testing de consistencia de datos y escenarios de concurrencia distribuida." |

**Análisis Ronda 2:**
- Rango: 17 - 24 meses (convergió)
- Media: 20.4 meses
- Mediana: 20 meses
- Convergencia: ✅ Aceptable

---

**DECISIÓN FINAL:**

```
Estimación Consensuada: 20 meses
Rango de Confianza: 18 - 23 meses

Supuestos Clave Documentados:
1. Infraestructura Kubernetes ya disponible
2. Rollout incremental priorizando 5 microservicios core
3. Equipo de 8 developers dedicados full-time
4. Fase de coexistencia monolito-micro de 6 meses
5. Automatización de testing desde el inicio
6. Sin cambios mayores de requerimientos durante migración

Riesgos Identificados:
- Base de datos legacy compleja (mitigación: DBA dedicado)
- Consistencia eventual en transacciones (mitigación: saga pattern)
- Curva de aprendizaje del equipo (mitigación: capacitación)
```

#### ✅ Ventajas
- Aprovecha sabiduría colectiva
- Elimina sesgo de autoridad (anonimato)
- No requiere datos históricos
- Aplicable a proyectos únicos/innovadores
- Identifica supuestos y riesgos tempranamente
- Genera "buy-in" del equipo

#### ❌ Desventajas
- Consume tiempo (días/semanas)
- Requiere coordinación
- Calidad depende de los expertos seleccionados
- No es reproducible con exactitud
- Puede haber presión de grupo implícita
- Difícil con más de 10 expertos

#### 🎓 Ejercicio
**Tu turno:** Organiza una mini-Delphi con 3 compañeros para estimar: "Desarrollar una app móvil de fitness con tracking de ejercicios, planes nutricionales y red social". Documenta 2 rondas.

---

### 2.5 Otros Modelos (Resumen)

#### PUTMAN
- Basado en curva de Rayleigh
- Predice distribución de esfuerzo en el tiempo
- Útil para planificar contrataciones
- Fórmula: `E = (L³/P²) / (t⁴ₘ)`

#### TRW WOLVERTON
- Clasifica módulos por dificultad (fácil, medio, difícil, muy difícil)
- Asigna productividad diferente a cada nivel
- Ejemplo: Fácil 175 LOC/PM, Difícil 80 LOC/PM

#### WALSTON-FELIX (IBM)
- 29 variables del proyecto
- Fórmula base: `E = 5.2 × L^0.91`
- Ajustado por multiplicadores

#### BISAD
- Método de descomposición
- Dividir y estimar partes
- Agregar buffer de integración

---

## 3. Factores de Riesgo en Estimación

### 3.1 Introducción a los Factores

> **"Una estimación sin considerar riesgos es simplemente una esperanza."**

Los factores de riesgo son variables que pueden **aumentar o disminuir** el esfuerzo real respecto a la estimación base.

#### 🎯 Cómo Aplicar Factores

```
Esfuerzo Real = Esfuerzo Base × Factor Compuesto

Factor Compuesto = Factor1 × Factor2 × Factor3 × ... × FactorN

⚠️ IMPORTANTE: Los factores se MULTIPLICAN, no se suman.
```

**Ejemplo:**
```
Estimación base: 100 horas

Factores:
- Equipo junior (×1.5)
- Complejidad alta (×1.8)
- Sin documentación (×1.3)

Esfuerzo Real = 100 × 1.5 × 1.8 × 1.3 = 351 horas
```

### 3.2 Mapa de Factores

```
┌─────────────────────────────────────────────────────────────────┐
│                    FACTORES DE RIESGO                           │
│                   (Impacto en Estimación)                        │
└─────────────────────────────────────────────────────────────────┘

🔴 ALTO RIESGO (×1.5 - ×3.0)
├─ Criticidad del sistema (Factor 50)
├─ Complejidad aplicación (Factor 41)
├─ Complejidad base de datos (Factor 51)
├─ Experiencia en tecnología (Factor 52)
├─ Disponibilidad cliente (Factor 23)
├─ Deadline impuesto (Factor 69)
├─ Dedicación a otras tareas (Factor 5)
└─ Rotación de personal (Factor 6)

🟡 MEDIO RIESGO (×1.2 - ×1.5)
├─ Experiencia del equipo (Factores 2, 3, 4)
├─ Tamaño del equipo (Factor 1)
├─ Conocimiento del negocio (Factor 43)
├─ Complejidad de pruebas (Factor 42)
├─ Requerimientos legales (Factor 68)
├─ Dependencias externas (Factor 9)
└─ Volumen de datos (Factor 54)

🟢 BAJO RIESGO (×1.0 - ×1.2)
├─ Documentación (Factores 44, 45)
├─ Calidad de entornos (Factores 61, 62)
├─ Metodologías (Factor 24)
├─ Infraestructura estable (Factor 63)
└─ Comunicación (Factor 71)
```

---

### 3.3 Factores de Equipo de Trabajo

#### Factor 1: Tamaño del Equipo
**Riesgo:** 🟡 Medio

**Concepto:** Ley de Brooks + Overhead de Comunicación

La cantidad de canales de comunicación crece exponencialmente:

```
Canales = n(n-1)/2

Equipo de 3: 3 canales
Equipo de 5: 10 canales    (+233%)
Equipo de 10: 45 canales   (+350%)
Equipo de 20: 190 canales  (+322%)
```

**Factores de Ajuste:**

| Tamaño Equipo | Overhead Coordinación | Factor |
|---------------|------------------------|--------|
| 2-5 personas | 0-10% | ×1.0 - ×1.1 |
| 6-10 personas | 15-20% | ×1.15 - ×1.2 |
| 11-20 personas | 25-35% | ×1.25 - ×1.35 |
| 21+ personas | 40-60% | ×1.4 - ×1.6 |

**Ejemplo:**
```
Funcionalidad: Módulo de reportes = 80 horas

Escenario A: Squad de 4 developers
Overhead: 10%
Esfuerzo: 80 × 1.1 = 88 horas

Escenario B: Equipo de 15 developers
Overhead: 30%
Esfuerzo: 80 × 1.3 = 104 horas
```

**Mitigación:**
- Dividir en squads pequeños (5-7 personas)
- Definir interfaces claras entre equipos
- Usar domain-driven design para reducir acoplamiento
- Implementar ceremonias ágiles efectivas

---

#### Factor 2-4: Experiencia del Equipo
**Riesgo:** 🟡 Medio

**Factor 2: Experiencia Técnica**
**Factor 3: Experiencia Funcional (negocio)**
**Factor 4: Experiencia en Procesos**

**Clasificación de Niveles:**

```
┌─────────────────────────────────────────────────────────────┐
│              NIVELES DE EXPERIENCIA                          │
├─────────────────────────────────────────────────────────────┤
│ JUNIOR (<2 años)                                            │
│ - Necesita supervisión constante                            │
│ - Comete errores de concepto                                │
│ - Productividad: 50-70%                                     │
│ - Factor: ×1.5 - ×2.0                                       │
├─────────────────────────────────────────────────────────────┤
│ SEMI-SENIOR (2-5 años)                                      │
│ - Trabaja de manera autónoma                                │
│ - Conoce patrones estándar                                  │
│ - Productividad: 80-100%                                    │
│ - Factor: ×1.0 - ×1.2                                       │
├─────────────────────────────────────────────────────────────┤
│ SENIOR (5-10 años)                                          │
│ - Anticipa problemas                                        │
│ - Diseña soluciones elegantes                               │
│ - Productividad: 110-150%                                   │
│ - Factor: ×0.7 - ×0.9                                       │
├─────────────────────────────────────────────────────────────┤
│ EXPERT (10+ años)                                           │
│ - Arquitecta sistemas complejos                             │
│ - Mentorea al equipo                                        │
│ - Productividad: 150-200%                                   │
│ - Factor: ×0.5 - ×0.7                                       │
└─────────────────────────────────────────────────────────────┘
```

**Ejemplo Comparativo:**

**Tarea:** Implementar autenticación OAuth2 + JWT en .NET Core

| Nivel | Tiempo | Actividades |
|-------|--------|-------------|
| **Junior** | 24h | Investigar OAuth2 (8h), probar libraries (6h), implementar (5h), debuggear errores (5h) |
| **Semi-Senior** | 10h | Revisar docs (2h), implementar (6h), testing (2h) |
| **Senior** | 5h | Implementar con best practices, reutilizar código anterior |
| **Expert** | 3h | Implementar + arquitectura extensible + documentación |

**Factor de Equipo Mixto:**

Si tienes un equipo mixto, calcula el promedio ponderado:

```
Equipo de 10 developers:
- 2 Juniors (20%) → Factor 1.8
- 5 Semi-Seniors (50%) → Factor 1.1
- 3 Seniors (30%) → Factor 0.8

Factor Ponderado = (0.2 × 1.8) + (0.5 × 1.1) + (0.3 × 0.8)
Factor Ponderado = 0.36 + 0.55 + 0.24 = 1.15
```

**Curva de Aprendizaje:**

Cuando incorporas personal nuevo (aunque sean seniors en general, si no conocen tu stack):

```
Mes 1: 30% productividad
Mes 2: 50% productividad
Mes 3: 70% productividad
Mes 4: 85% productividad
Mes 5-6: 100% productividad
```

---

#### Factor 5: Dedicación a Otras Tareas
**Riesgo:** 🔴 Alto

**Concepto:** Costo del Cambio de Contexto

```
┌──────────────────────────────────────────────────────────┐
│         IMPACTO DEL MULTITASKING                         │
├──────────────────────────────────────────────────────────┤
│ 100% Dedicado → 100% Productividad                       │
│  90% Dedicado →  85% Productividad  (-15%)              │
│  75% Dedicado →  60% Productividad  (-40%)              │
│  50% Dedicado →  40% Productividad  (-60%)              │
│  25% Dedicado →  15% Productividad  (-85%)              │
└──────────────────────────────────────────────────────────┘

🧠 Razón: Cada cambio de contexto tiene costo cognitivo
- Recargar contexto: 15-30 minutos
- 3 proyectos = 6 cambios/día = 3+ horas perdidas
```

**Factores de Ajuste:**

| Dedicación | Productividad Real | Factor |
|------------|-------------------|--------|
| 100% | 100% | ×1.0 |
| 80-90% | 75-85% | ×1.2 |
| 60-70% | 50-60% | ×1.5 |
| 40-50% | 35-45% | ×2.0 |
| <40% | <30% | ×2.5+ |

**Ejemplo Real:**

```
Developer en 3 proyectos simultáneos:

Proyecto A: 40% tiempo (3.2h/día)
Proyecto B: 35% tiempo (2.8h/día)
Proyecto C: 25% tiempo (2h/día)

Horas nominales: 8h/día
Horas productivas: 8 × 0.4 ≈ 3.2h/día

Si tarea requiere 40h de trabajo enfocado:
Con 100% dedicación: 40h / 8h = 5 días
Con dedicación distribuida: 40h / 3.2h = 12.5 días
Factor: ×2.5
```

**Recomendación:**
- Mantener dedicación >80% al proyecto
- Limitar a máximo 2 proyectos activos simultáneos
- Usar time-boxing para minimizar cambios de contexto

---

#### Factor 6: Rotación de Personal
**Riesgo:** 🔴 Alto

**Costos de la Rotación:**

```
┌────────────────────────────────────────────────────────────┐
│        CICLO DE PÉRDIDA POR ROTACIÓN                       │
├────────────────────────────────────────────────────────────┤
│ FASE 1: Aviso de salida (2-4 semanas)                     │
│ - Persona se desvincula mentalmente                        │
│ - Productividad: 50-70%                                    │
│ - Pérdida: 30-50%                                          │
├────────────────────────────────────────────────────────────┤
│ FASE 2: Transición (1-2 semanas)                          │
│ - Documentar conocimiento                                  │
│ - Transferir tareas                                        │
│ - Costo: 40-80 horas                                       │
├────────────────────────────────────────────────────────────┤
│ FASE 3: Vacancia (0-4 semanas)                            │
│ - Sin recurso                                              │
│ - Redistribución de carga                                 │
│ - Pérdida: 100%                                            │
├────────────────────────────────────────────────────────────┤
│ FASE 4: Onboarding nuevo (4-8 semanas)                    │
│ - Setup, capacitación, curva aprendizaje                  │
│ - Productividad: 30-80% progresivo                         │
│ - Costo: 160-320 horas                                     │
├────────────────────────────────────────────────────────────┤
│ FASE 5: Productividad plena (8-16 semanas)                │
│ - Alcanza 100% productividad                               │
└────────────────────────────────────────────────────────────┘

📊 IMPACTO TOTAL: 3-6 meses de productividad reducida
💰 COSTO REAL: 25-35% del salario anual
```

**Factores por Tasa de Rotación:**

| Rotación Anual | Factor | Impacto |
|----------------|--------|---------|
| <5% (Excelente) | ×1.0 | Equipo estable |
| 5-10% (Bueno) | ×1.05 | Rotación saludable |
| 10-20% (Medio) | ×1.15 | Pérdida de conocimiento |
| 20-30% (Alto) | ×1.3 | Impacto significativo |
| >30% (Crítico) | ×1.5+ | Crisis de equipo |

**Ejemplo:**

```
Proyecto de 12 meses, equipo de 10 personas:

Escenario A: Rotación 10% (1 persona se va)
- Pérdida productividad: 4 meses-persona
- Factor: ×1.1

Escenario B: Rotación 30% (3 personas se van)
- Pérdida productividad: 12 meses-persona
- Factor: ×1.35
- Efecto cascada: Equipo se desmoraliza, más rotación
```

**Mitigación:**
- Documentación del código (no solo verbal)
- Pair programming (conocimiento distribuido)
- Code reviews (todos conocen todo)
- Retención de talento (compensación competitiva)

---

#### Factor 7-8: Conocimiento de Procesos y Herramientas
**Riesgo:** 🔴 Alto

**Factor 7: Proceso de Desarrollo**
**Factor 8: Herramientas de Software**

**Niveles de Madurez (CMMI adaptado):**

```
┌──────────────────────────────────────────────────────────────┐
│              NIVELES DE MADUREZ DE PROCESO                    │
├──────────────────────────────────────────────────────────────┤
│ NIVEL 1: AD-HOC (Caos)                            Factor: ×2.0│
│ - Sin proceso definido                                        │
│ - Cada quien trabaja diferente                                │
│ - No hay definition of done                                   │
│ - Deploy manual con errores frecuentes                        │
│ - No hay testing automatizado                                 │
│ - No hay code review                                          │
├──────────────────────────────────────────────────────────────┤
│ NIVEL 2: REPETIBLE (Básico)                      Factor: ×1.4│
│ - Procesos documentados pero no siempre seguidos              │
│ - Testing manual estructurado                                 │
│ - Code review opcional                                        │
│ - Deploy semi-automático                                      │
├──────────────────────────────────────────────────────────────┤
│ NIVEL 3: DEFINIDO (Estándar)                     Factor: ×1.0│
│ - SCRUM o Kanban establecido                                  │
│ - Testing automatizado (unit + integration)                   │
│ - Code review obligatorio                                     │
│ - CI/CD básico                                                │
│ - Documentación estándar                                      │
├──────────────────────────────────────────────────────────────┤
│ NIVEL 4: GESTIONADO (Métricas)                   Factor: ×0.9│
│ - Métricas de calidad monitoreadas                            │
│ - SonarQube, code coverage >80%                               │
│ - Performance monitoring                                      │
│ - Postmortems de incidentes                                   │
├──────────────────────────────────────────────────────────────┤
│ NIVEL 5: OPTIMIZADO (DevOps)                     Factor: ×0.7│
│ - CI/CD avanzado (deploy en minutos)                          │
│ - Feature flags, canary deployments                           │
│ - Chaos engineering                                           │
│ - Mejora continua basada en datos                             │
│ - Infrastructure as Code                                      │
└──────────────────────────────────────────────────────────────┘
```

**Ejemplo Comparativo:**

**Feature:** API de procesamiento de pagos

| Nivel | Tiempo Desarrollo | Tiempo Testing | Tiempo Deploy | Total |
|-------|------------------|----------------|---------------|-------|
| Ad-hoc | 40h | 30h (manual) | 10h (manual, errores) | **80h** |
| Repetible | 40h | 20h (semi-auto) | 6h | **66h** |
| Definido | 40h | 12h (auto) | 2h (CI/CD) | **54h** |
| Optimizado | 40h | 5h (auto + TDD) | 0.5h (auto) | **45.5h** |

**Factor Compuesto:**
```
Ad-hoc vs Optimizado: 80h / 45.5h = ×1.76
```

**Herramientas y su Impacto:**

| Categoría | Sin Herramienta | Con Herramienta | Factor |
|-----------|----------------|-----------------|--------|
| **IDE** | Notepad | Visual Studio / VS Code | ×0.6 |
| **Control Versiones** | Carpetas zip | Git + GitHub/Azure DevOps | ×0.5 |
| **Testing** | Manual | xUnit + Selenium | ×0.4 |
| **CI/CD** | Manual | Azure Pipelines / Jenkins | ×0.3 |
| **Debugging** | Console.WriteLine | Debugger + Logs | ×0.7 |
| **Docs** | Word disperso | Confluence / Notion | ×0.8 |

---

#### Factor 9: Equipos Distribuidos
**Riesgo:** 🟡 Medio

**Overhead por Ubicación:**

```
┌────────────────────────────────────────────────────────┐
│         IMPACTO DE LA DISTRIBUCIÓN                     │
├────────────────────────────────────────────────────────┤
│ Mismo edificio/piso                       Factor: ×1.0│
│ - Comunicación instantánea                            │
│ - Pair programming físico                             │
│ - Resolución rápida de dudas                          │
├────────────────────────────────────────────────────────┤
│ Mismo edificio, pisos diferentes          Factor: ×1.05│
│ - Requiere caminar, pero factible                     │
├────────────────────────────────────────────────────────┤
│ Ciudad diferente (mismo huso)             Factor: ×1.15│
│ - Videollamadas necesarias                            │
│ - Latencia en respuestas (minutos-horas)              │
├────────────────────────────────────────────────────────┤
│ País diferente (4-6h overlap)             Factor: ×1.25│
│ - Coordinación de horarios                            │
│ - Respuestas al día siguiente                         │
│ - Diferencias culturales menores                      │
├────────────────────────────────────────────────────────┤
│ País diferente (<3h overlap)              Factor: ×1.5│
│ - Muy poco tiempo sincrónico                          │
│ - Trabajo asíncrono obligatorio                       │
│ - Reuniones fuera de horario                          │
├────────────────────────────────────────────────────────┤
│ Equipos dependientes externos            Factor: +0.2│
│ - Esperas por aprobaciones                            │
│ - Bloqueos por dependencias                           │
└────────────────────────────────────────────────────────┘
```

**Ejemplo:**

```
Feature que requiere:
- Trabajo propio: 30h
- Integración con equipo Payments (otra ciudad): 10h
- Aprobación equipo Security (otro país, 2h overlap): 5h

Sin distribución: 30 + 10 + 5 = 45h

Con distribución:
- Trabajo propio: 30h
- Integración Payments: 10h × 1.15 = 11.5h
- Aprobación Security: 5h × 1.5 + esperas (5 días × 2h) = 17.5h
Total Real: 59h (×1.31 factor)
```

**Mitigación:**
- Documentación asíncrona excelente
- Over-communicate (Slack, confluence)
- Definir interfaces contract-first
- Automatizar lo máximo posible
- Daily overlap meetings

---

### 3.4 Factores de Aplicación

#### Factor 41: Complejidad de la Aplicación
**Riesgo:** 🔴 Alto

**Escala de Complejidad:**

```
┌────────────────────────────────────────────────────────────┐
│                NIVELES DE COMPLEJIDAD                       │
├────────────────────────────────────────────────────────────┤
│ BAJA (Factor: ×1.0)                                        │
│ ✓ CRUD básico sin lógica de negocio                        │
│ ✓ Operaciones simples (create, read, update, delete)       │
│ ✓ Sin integraciones externas                               │
│ ✓ Base de datos simple (<10 tablas)                        │
│ ✓ Sin concurrencia                                         │
│ Ejemplo: Backoffice de administración de catálogo          │
├────────────────────────────────────────────────────────────┤
│ MEDIA (Factor: ×1.5)                                       │
│ ✓ Lógica de negocio moderada                               │
│ ✓ 2-3 integraciones con sistemas conocidos                 │
│ ✓ Validaciones de negocio complejas                        │
│ ✓ Reporting con agregaciones                               │
│ ✓ Concurrencia moderada (100-500 usuarios)                 │
│ Ejemplo: Sistema de reservas online                        │
├────────────────────────────────────────────────────────────┤
│ ALTA (Factor: ×2.5)                                        │
│ ✓ Lógica de negocio compleja                               │
│ ✓ 4-6 integraciones heterogéneas                            │
│ ✓ Transacciones distribuidas                               │
│ ✓ Alta concurrencia (1,000-5,000 usuarios)                 │
│ ✓ Algoritmos complejos                                     │
│ ✓ Manejo de estados complejos (state machines)             │
│ Ejemplo: Plataforma de e-commerce multi-tenant             │
├────────────────────────────────────────────────────────────┤
│ MUY ALTA (Factor: ×4.0)                                    │
│ ✓ Sistemas de misión crítica                               │
│ ✓ Tiempo real (<100ms latencia)                            │
│ ✓ Muy alta concurrencia (10K+ TPS)                         │
│ ✓ Alta disponibilidad (99.99%+)                            │
│ ✓ Múltiples integraciones críticas                         │
│ ✓ Compliance estricto (PCI DSS, SOX)                       │
│ ✓ Procesamiento masivo de datos                            │
│ Ejemplo: Core bancario, PSP, Trading platform              │
└────────────────────────────────────────────────────────────┘
```

**Dimensiones de la Complejidad:**

| Dimensión | Bajo | Medio | Alto | Muy Alto |
|-----------|------|-------|------|----------|
| **Lógica de Negocio** | Lineal | Condicionales | Workflows | State Machines |
| **Integraciones** | 0-1 | 2-3 | 4-6 | 7+ |
| **Concurrencia (TPS)** | <10 | 10-100 | 100-1K | 1K+ |
| **Volumen Datos** | MB | GB | TB | PB |
| **Latencia Requerida** | >5s | 1-5s | 100ms-1s | <100ms |
| **Disponibilidad** | 95% | 99% | 99.9% | 99.99%+ |

**Ejemplo Aplicado al Sector Fintech:**

```
Feature: Procesar pago con tarjeta de crédito

CRUD Básico (Factor ×1.0):
- Guardar datos en DB: 5 horas

Complejidad Real PSP (Factor ×3.5):
- Tokenización PCI DSS: 10h
- Integración Visa/Mastercard: 15h
- Manejo 3D Secure: 12h
- Circuit breaker + retry: 8h
- Idempotencia: 6h
- Logging auditable: 5h
- Reversión transaccional: 10h
- Conciliación: 8h
- Testing exhaustivo: 20h
- Code review estricto: 5h
- Documentación compliance: 6h

Total: 5 × 3.5 ≈ 105 horas (vs 5h básicas)
```

---

#### Factor 50: Criticidad del Sistema
**Riesgo:** 🔴 Alto

**Niveles de Criticidad:**

```
┌──────────────────────────────────────────────────────────────┐
│              MATRIZ DE CRITICIDAD                            │
├──────────────────────────────────────────────────────────────┤
│ BAJA (Factor: ×1.0)                                          │
│ - Sistema interno, no crítico                                │
│ - Downtime tolerable (horas/días)                            │
│ - Pérdidas mínimas si falla                                  │
│ - Uptime: 95-98%                                             │
│ Ejemplo: Panel administrativo, reportes internos             │
├──────────────────────────────────────────────────────────────┤
│ MEDIA (Factor: ×1.4)                                         │
│ - Sistema de negocio importante                              │
│ - Downtime afecta operaciones                                │
│ - Pérdidas moderadas si falla                                │
│ - Uptime: 99%                                                │
│ Ejemplo: CRM, ERP interno                                    │
├──────────────────────────────────────────────────────────────┤
│ ALTA (Factor: ×2.0)                                          │
│ - Sistema core de negocio                                    │
│ - Downtime = pérdida directa de revenue                      │
│ - Impacto reputacional                                       │
│ - Uptime: 99.9% (8.76h downtime/año)                         │
│ Ejemplo: E-commerce principal, app móvil pública             │
├──────────────────────────────────────────────────────────────┤
│ CRÍTICA (Factor: ×3.0)                                       │
│ - Sistema financiero regulado                                │
│ - Cero tolerancia a errores                                  │
│ - Pérdidas masivas si falla                                  │
│ - Compliance estricto                                        │
│ - Uptime: 99.99%+ (52min downtime/año)                       │
│ Ejemplo: Core bancario, PSP, exchanges                       │
└──────────────────────────────────────────────────────────────┘
```

**Implicaciones por Nivel:**

| Aspecto | Baja | Alta | Crítica |
|---------|------|------|---------|
| **Error Handling** | Básico | Exhaustivo | Redundante |
| **Testing** | 60% coverage | 80% coverage | 95%+ coverage |
| **Monitoring** | Básico | Avanzado | APM completo |
| **Logging** | Errores | Auditoría | Auditoría + Compliance |
| **Code Review** | Opcional | Obligatorio | Doble review + Security |
| **Deployment** | Manual ok | Blue-Green | Canary + Rollback automático |
| **DR Plan** | No | Sí | Activo-Activo multi-region |

**Ejemplo:**

```
Feature básica: API endpoint = 20 horas

Sistema de criticidad baja:
20h × 1.0 = 20 horas

Sistema crítico (PSP):
- Feature base: 20h
- Error handling exhaustivo: +8h
- Circuit breakers: +6h
- Idempotencia: +5h
- Monitoring detallado: +4h
- Logging compliance: +4h
- Testing >95% coverage: +15h
- Security review: +6h
- Chaos testing: +8h
- Documentación: +6h
- Runbook operativo: +4h

Total: 20 × 3.3 = 86 horas
```

---

#### Factor 51: Complejidad de Base de Datos
**Riesgo:** 🔴 Alto

**Escala de Complejidad:**

```
┌────────────────────────────────────────────────────────────┐
│         COMPLEJIDAD DE BASE DE DATOS                        │
├────────────────────────────────────────────────────────────┤
│ SIMPLE (Factor: ×1.0)                                      │
│ • <10 tablas                                               │
│ • Relaciones 1:N simples                                   │
│ • Sin índices complejos                                    │
│ • Volumen: <100K registros                                 │
│ • Queries directos sin optimización                        │
├────────────────────────────────────────────────────────────┤
│ MEDIA (Factor: ×1.4)                                       │
│ • 10-50 tablas                                             │
│ • Relaciones N:M, herencia                                 │
│ • Índices compuestos                                       │
│ • Volumen: 100K-10M registros                              │
│ • Queries optimizados requeridos                           │
├────────────────────────────────────────────────────────────┤
│ ALTA (Factor: ×2.2)                                        │
│ • 50-150 tablas                                            │
│ • Múltiples esquemas                                       │
│ • Particionamiento horizontal                              │
│ • Volumen: 10M-1B registros                                │
│ • Índices especializados (full-text, spatial)              │
│ • Read replicas                                            │
├────────────────────────────────────────────────────────────┤
│ MUY ALTA (Factor: ×3.5)                                    │
│ • 150+ tablas                                              │
│ • Arquitectura distribuida                                 │
│ • Sharding                                                 │
│ • Volumen: >1B registros                                   │
│ • Multiple DBs (polyglot persistence)                      │
│ • Event sourcing                                           │
│ • CQRS                                                     │
└────────────────────────────────────────────────────────────┘
```

**Ejemplo Sistema Financiero:**

```
Sistema PSP - Transacciones:

Tablas Principales:
- Transacciones (500M registros)
- Movimientos (1B registros)
- Cuentas (10M registros)
- Usuarios (5M registros)
- [... 140 tablas más ...]

Complejidad:
✓ Particionamiento por mes
✓ Índices columnares para reportes
✓ Read replicas (6 réplicas)
✓ Sharding por país
✓ Consistencia eventual
✓ Event sourcing para auditoría

Query simple (sin optimización): 2 horas

Query en sistema real:
- Análisis plan de ejecución: 4h
- Diseño índices óptimos: 6h
- Testing con volumen real: 5h
- Optimización queries: 5h
- Testing performance (load test): 4h
- Documentación: 2h

Total: 2h × 13 = 26 horas (Factor ×13!)
```

---

#### Factor 52: Experiencia en Tecnología
**Riesgo:** 🔴 Alto

**Curva de Aprendizaje Tecnológico:**

```
┌────────────────────────────────────────────────────────────┐
│        PRODUCTIVIDAD POR EXPERIENCIA EN TECH                │
└────────────────────────────────────────────────────────────┘

100% │                                    ┌─────────────
     │                               ┌────┘
 80% │                          ┌────┘
     │                     ┌────┘
 60% │                ┌────┘
     │           ┌────┘
 40% │      ┌────┘
     │ ┌────┘
 20% │─┘
     │
  0% └─────┬────┬────┬────┬────┬────┬────┬────┬────┬────
          M1   M2   M3   M4   M5   M6   M7   M8   M9   M10
```

**Factores por Mes:**

| Mes | Productividad | Factor | Actividad Típica |
|-----|---------------|--------|------------------|
| **Mes 1** | 25% | ×4.0 | Setup, tutoriales básicos, "hello world" |
| **Mes 2** | 40% | ×2.5 | Primera feature simple, muchas dudas |
| **Mes 3** | 60% | ×1.7 | Features moderadas, menos errores |
| **Mes 4** | 75% | ×1.3 | Independencia parcial |
| **Mes 5-6** | 90% | ×1.1 | Casi autónomo |
| **Mes 7+** | 100% | ×1.0 | Productividad completa |
| **Año 2+** | 120% | ×0.8 | Experto, mentor |

**Ejemplo: Equipo nuevo en .NET Core + Azure + Microservicios**

```
Proyecto: 6 meses, equipo de 8 developers

Opción A: Equipo experto en stack
8 devs × 6 meses × 100% = 48 PM

Opción B: Equipo nuevo en stack
Mes 1-2: 8 × 2 × 30% = 4.8 PM
Mes 3-4: 8 × 2 × 60% = 9.6 PM
Mes 5-6: 8 × 2 × 85% = 13.6 PM
Total: 28 PM (vs 48 PM esperados)

Déficit: 20 PM
Proyecto se extiende: 6 → 10.3 meses
Factor real aplicado: ×1.72
```

**Estrategias de Mitigación:**
- Capacitación formal (bootcamp) antes del proyecto
- Pair programming con experto
- Prototipo/spike inicial
- Mentoring continuo
- Code reviews educativas

---

### 3.5 Factores de Contexto

#### Factor 66: Restricciones de Hardware
**Riesgo:** 🔴 Alto (cuando aplica)

**Impacto de Limitaciones:**

| Restricción | Sin Límite | Con Límite | Overhead |
|-------------|------------|------------|----------|
| **Memoria RAM** | - | Contenedor 256MB | +40% optimización |
| **CPU** | - | 1 core limitado | +35% algoritmos eficientes |
| **Storage** | - | 5GB disco | +25% compresión/cleanup |
| **Network** | - | Bandwidth limitado | +30% caching/optimización |
| **Costo Cloud** | - | Budget estricto | +50% arquitectura costo-optimizada |

---

#### Factor 68: Compliance y Requerimientos Legales
**Riesgo:** 🟡 Medio

**Overhead por Regulación:**

```
┌────────────────────────────────────────────────────────────┐
│               IMPACTO DE COMPLIANCE                         │
├────────────────────────────────────────────────────────────┤
│ SIN REGULACIÓN                             Factor: ×1.0   │
│ - Desarrollo estándar                                      │
├────────────────────────────────────────────────────────────┤
│ GDPR (Privacidad General)                  Factor: ×1.15  │
│ - Consentimiento usuarios                                  │
│ - Right to be forgotten                                    │
│ - Data portability                                         │
│ - Privacy by design                                        │
├────────────────────────────────────────────────────────────┤
│ PCI DSS (Pagos con Tarjeta)                Factor: ×1.40  │
│ - Tokenización (no guardar PAN)                            │
│ - Cifrado E2E                                              │
│ - Logging auditable                                        │
│ - Penetration testing obligatorio                          │
│ - Documentación exhaustiva                                 │
├────────────────────────────────────────────────────────────┤
│ BCRA + CNV (Regulación Financiera ARG)     Factor: ×1.35  │
│ - Reportes regulatorios                                    │
│ - Auditoría permanente                                     │
│ - Restricciones operativas                                 │
├────────────────────────────────────────────────────────────┤
│ SOX (Sarbanes-Oxley)                       Factor: ×1.25  │
│ - Controles internos                                       │
│ - Auditoría financiera                                     │
│ - Segregación de funciones                                 │
├────────────────────────────────────────────────────────────┤
│ MÚLTIPLE (PCI + SOX + BCRA)                Factor: ×1.70  │
│ - Intersección de requerimientos                           │
│ - Documentación multiplicada                               │
│ - Auditorías múltiples                                     │
└────────────────────────────────────────────────────────────┘
```

---

#### Factor 69: Deadline Impuesto
**Riesgo:** 🔴 Alto

**Impacto de Presión Temporal:**

```
┌────────────────────────────────────────────────────────────┐
│            RELACIÓN DEADLINE vs CALIDAD                     │
└────────────────────────────────────────────────────────────┘

Calidad
   │
100├─────┐
   │     │
 80│     └────┐
   │          │
 60│          └───────┐
   │                  │          ┌── Deuda Técnica
 40│                  └──────────┤   Acumulada
   │                             │
 20│                             └─────────────
   │
  0└────┬─────┬─────┬─────┬─────┬─────┬─────┬─
      +50%  +25%  Ideal  -10%  -25%  -40%  -50%
                                              Tiempo
```

**Factores por Tipo de Deadline:**

| Situación | Factor | Consecuencias |
|-----------|--------|---------------|
| **Sin deadline fijo** | ×1.0 | Desarrollo natural, calidad óptima |
| **Deadline holgado** (+30%) | ×0.95 | Tiempo para refactoring |
| **Deadline ajustado** (justo) | ×1.1 | Presión moderada |
| **Deadline agresivo** (-20%) | ×1.3 | Overtime, calidad sufre |
| **Deadline imposible** (-40%) | ×1.6 | Deuda técnica alta, burnout |

**Ejemplo Real:**

```
Proyecto estimado: 12 meses
Deadline regulatorio: 8 meses (imposible mover)

Opciones:

A) Mantener equipo (10 devs):
   - Factor presión: ×1.35
   - Tiempo real: 12 × 1.35 = 16.2 meses
   - Resultado: NO SE CUMPLE

B) Reducir scope (MVP):
   - 60% funcionalidad
   - Tiempo: 12 × 0.6 × 1.15 = 8.3 meses
   - Resultado: AJUSTADO (con deuda técnica)

C) Aumentar equipo (15 devs):
   - Ley de Brooks: +3 meses onboarding
   - Coordinación: ×1.25
   - Tiempo: (12 / 1.5) × 1.25 + 3 = 13 meses
   - Resultado: NO MEJORA

✅ SOLUCIÓN: Opción B (MVP) + Aceptar deuda técnica
```

---

## 4. Aplicación Práctica

### 4.1 Metodología Integral de Estimación

**Proceso Completo Paso a Paso:**

```
┌─────────────────────────────────────────────────────────────┐
│           PROCESO DE ESTIMACIÓN DE SOFTWARE                 │
└─────────────────────────────────────────────────────────────┘

PASO 1: ENTENDER EL PROYECTO
├─ Requerimientos funcionales completos
├─ Arquitectura propuesta
├─ Stack tecnológico definido
├─ Restricciones conocidas
└─ Criterios de aceptación claros

PASO 2: SELECCIONAR MÉTODO DE ESTIMACIÓN
├─ ¿Hay casos de uso? → Puntos Caso de Uso
├─ ¿Requerimientos funcionales? → Puntos Función
├─ ¿Conoces LOC aproximado? → COCOMO II
├─ ¿Proyecto innovador? → Delphi
└─ ¿Proyecto pequeño? → Descomposición

PASO 3: APLICAR MÉTODO y OBTENER ESTIMACIÓN BASE
└─ Resultado: Horas o Persona-Mes base

PASO 4: IDENTIFICAR FACTORES DE RIESGO
├─ Equipo: Experiencia, tamaño, rotación, dedicación
├─ Cliente: Disponibilidad, conocimiento
├─ Aplicación: Complejidad, criticidad, tecnología, BD
└─ Contexto: Compliance, deadline, distribución

PASO 5: CALCULAR FACTOR COMPUESTO
└─ Multiplicar todos los factores aplicables

PASO 6: AJUSTAR ESTIMACIÓN
└─ Esfuerzo Real = Esfuerzo Base × Factor Compuesto

PASO 7: AGREGAR BUFFER DE CONTINGENCIA
├─ Proyecto conocido: +10-15%
├─ Proyecto con incertidumbre: +20-30%
└─ Proyecto innovador: +40-60%

PASO 8: CONVERTIR A CALENDARIO
├─ Considerar horas productivas reales (5-6h/día)
├─ Aplicar distribución Rayleigh si aplicable
└─ Calcular duración con recursos disponibles

PASO 9: VALIDAR Y AJUSTAR
├─ Comparar con proyectos históricos similares
├─ Revisión por expertos (mini-Delphi)
├─ Ajustar según feedback
└─ Documentar supuestos

PASO 10: PRESENTAR Y COMUNICAR
├─ Rango de estimación (mejor caso, esperado, peor caso)
├─ Supuestos críticos
├─ Riesgos identificados
└─ Plan de mitigación
```

---

### 4.2 Caso de Estudio Completo

**PROYECTO:** Sistema de Wallet Digital con QR Interoperable

#### Contexto del Proyecto

**Cliente:** Fintech argentina que quiere lanzar billetera digital para competir con Mercado Pago y Personal Pay.

**Funcionalidades Requeridas:**
1. Onboarding de usuarios con validación de identidad
2. Gestión de cuentas virtuales en ARS
3. Carga de saldo (transferencia bancaria, efectivo en puntos)
4. Generación de QR estático y dinámico (EMV estándar Coelsa)
5. Pago con QR escaneando en comercios
6. Transferencias P2P entre usuarios
7. Consulta de movimientos y saldos
8. Notificaciones push en tiempo real
9. Integración con Coelsa (red de pagos QR)
10. Integración con BCRA para validaciones
11. Reportes regulatorios para UIF/CNV

**Stack Tecnológico:**
- Backend: .NET Core 8, microservicios en Azure AKS
- BD: SQL Server con read replicas
- Cache: Redis
- Mensajería: RabbitMQ con MassTransit
- Frontend: React Native (iOS + Android)
- Seguridad: PCI DSS compliance requerido

**Equipo Disponible:**
- 6 developers backend (4 semi-senior .NET, 2 junior)
- 2 developers mobile (1 senior React Native, 1 junior)
- 1 QA automation
- 1 DevOps
- 1 Product Owner
- 1 Arquitecto (part-time, 50%)

**Restricciones:**
- Deadline regulatorio: 8 meses (para operar)
- Presupuesto limitado (startup seed stage)
- Compliance PCI DSS nivel 1
- Alta disponibilidad requerida (99.9%)

---

#### PASO 1: Estimación por Puntos Función

**Entradas (EI):**
1. Registro usuario - Alta (validación identidad RENAPER) = 6 PF
2. Cargar saldo - Media = 4 PF
3. Generar QR dinámico - Alta (EMV Coelsa) = 6 PF
4. Pagar con QR - Alta (integ. Coelsa, validaciones) = 6 PF
5. Transferir P2P - Alta = 6 PF
6. Configurar notificaciones - Baja = 3 PF

**Salidas (EO):**
1. Comprobante de pago - Media = 5 PF
2. Reporte de movimientos - Alta (con filtros) = 7 PF
3. Dashboard de saldo - Media = 5 PF
4. Reporte UIF - Alta (regulatorio) = 7 PF

**Consultas (EQ):**
1. Consultar saldo - Baja = 3 PF
2. Historial de transacciones - Media = 4 PF
3. Estado de QR - Baja = 3 PF
4. Buscar usuario P2P - Media = 4 PF

**Archivos Internos (ILF):**
1. Usuarios - Alta (campos identidad) = 15 PF
2. Cuentas - Media = 10 PF
3. Transacciones - Alta (volumen, relaciones) = 15 PF
4. QRs - Media = 10 PF
5. Movimientos - Alta = 15 PF
6. Notificaciones - Baja = 7 PF

**Archivos Externos (EIF):**
1. Coelsa (red QR) - Alta = 10 PF
2. BCRA (validaciones) - Media = 7 PF
3. RENAPER (identidad) - Media = 7 PF
4. Bancos (carga saldo) - Media = 7 PF

**Total PFNA:**
```
EI: 6+4+6+6+6+3 = 31 PF
EO: 5+7+5+7 = 24 PF
EQ: 3+4+3+4 = 14 PF
ILF: 15+10+15+10+15+7 = 72 PF
EIF: 10+7+7+7 = 31 PF

PFNA = 31 + 24 + 14 + 72 + 31 = 172 PF
```

**Factor de Ajuste:**
```
Sistema complejo, alta performance, múltiples integraciones,
seguridad crítica, multiplataforma

Factor: 1.20

PFA = 172 × 1.20 = 206 PF
```

**Esfuerzo Base:**
```
Sector fintech, alta complejidad: 18 h/PF

Esfuerzo Base = 206 × 18 = 3,708 horas
```

---

#### PASO 2: Identificar y Aplicar Factores de Riesgo

**Factores de Equipo:**

| Factor | Descripción | Valor | Multiplicador |
|--------|-------------|-------|---------------|
| Tamaño equipo | 10 personas (coordinación moderada) | - | ×1.20 |
| Experiencia técnica | Mix: 50% semi-senior, 30% junior | - | ×1.25 |
| Experiencia funcional | PO conoce fintech pero no QR | - | ×1.15 |
| Experiencia procesos | Equipo con SCRUM y CI/CD | - | ×0.95 |
| Dedicación | Arquitecto 50%, resto 90% | - | ×1.15 |
| Rotación | Startup, riesgo 20% anual | - | ×1.15 |
| Conocimiento tecnología | 2 developers nuevos en .NET Core | - | ×1.20 |

**Factores de Aplicación:**

| Factor | Descripción | Multiplicador |
|--------|-------------|---------------|
| Complejidad aplicación | Alta (integraciones, QR EMV, real-time) | ×2.2 |
| Criticidad | Alta (medio de pago, 99.9%) | ×1.8 |
| Complejidad BD | Media-alta (50 tablas, volumen medio) | ×1.5 |
| Complejidad pruebas | Alta (integraciones, seguridad) | ×1.4 |

**Factores de Contexto:**

| Factor | Descripción | Multiplicador |
|--------|-------------|---------------|
| Compliance | PCI DSS + BCRA + UIF | ×1.5 |
| Deadline impuesto | 8 meses (agresivo para el scope) | ×1.35 |
| Conocimiento del cliente | PO disponible 80% | ×1.05 |
| Documentación | Poca documentación Coelsa | ×1.15 |

**Factor Compuesto Total:**
```
Equipo: 1.20 × 1.25 × 1.15 × 0.95 × 1.15 × 1.15 × 1.20 = 2.28
Aplicación: 2.2 × 1.8 × 1.5 × 1.4 = 8.32
Contexto: 1.5 × 1.35 × 1.05 × 1.15 = 2.44

Factor Total = 2.28 × 8.32 × 2.44 = 46.3

⚠️ ADVERTENCIA: Factor extremadamente alto
Indica proyecto de altísima complejidad
```

Esto es irreal. Recalculemos categorizando correctamente:

**Factor Compuesto Corregido:**
```
Factor Base de Complejidad (ya incluido en 18h/PF): 
No multiplicar complejidad dos veces

Factores Adicionales:
- Equipo: 1.20 × 1.25 × 1.15 × 0.95 × 1.15 × 1.15 × 1.20 = 2.28
- Criticidad adicional: ×1.3 (alta disponibilidad)
- Compliance adicional: ×1.35 (PCI DSS overhead)
- Deadline: ×1.25 (presión)

Factor Total Ajustado = 2.28 × 1.3 × 1.35 × 1.25 = 5.18
```

---

#### PASO 3: Cálculo Final

**Esfuerzo Ajustado:**
```
Esfuerzo Real = 3,708 h × 5.18 = 19,207 horas
```

**Agregar Buffer (proyecto con incertidumbre):**
```
Buffer: 25%
Esfuerzo Total = 19,207 × 1.25 = 24,009 horas
```

**Conversión a Persona-Mes:**
```
Horas productivas/mes: 140h (7h/día × 20 días)

PM Total = 24,009 / 140 = 171.5 PM
```

**Conversión a Calendario:**
```
Equipo disponible:
- 6 backend devs × 90% = 5.4 FTE
- 2 mobile devs × 90% = 1.8 FTE
- 1 QA × 100% = 1.0 FTE
- 1 DevOps × 100% = 1.0 FTE
- 0.5 Arquitecto = 0.5 FTE

Total: 9.7 FTE

Duración = 171.5 PM / 9.7 FTE = 17.7 meses
```

---

#### PASO 4: Conclusión y Recomendaciones

**Resultado:**

```
┌────────────────────────────────────────────────────────────┐
│                    RESULTADO FINAL                          │
├────────────────────────────────────────────────────────────┤
│ Esfuerzo Total: 24,009 horas (171.5 PM)                   │
│ Duración Estimada: 17.7 meses                              │
│ Deadline Requerido: 8 meses                                │
│                                                             │
│ ❌ CONCLUSIÓN: PROYECTO INVIABLE EN PLAZO ACTUAL          │
│                                                             │
│ Gap: 17.7 - 8 = 9.7 meses de déficit                      │
└────────────────────────────────────────────────────────────┘
```

**Opciones Estratégicas:**

**OPCIÓN A: MVP Reducido** ⭐ RECOMENDADO
```
Scope: 50% funcionalidad (features core)
- Onboarding básico (sin RENAPER, validación manual)
- Carga de saldo (solo transferencia)
- QR dinámico básico
- Pago con QR
- P2P simple
- Consultas básicas
- Diferir: Reportes UIF, notificaciones push, QR estático

Esfuerzo: 24,009 × 0.5 × 1.1 (apuro) = 13,205 horas
Duración: 13,205 / (9.7 × 140) = 9.7 meses

Aún 1.7 meses sobre deadline
Plan: Launch MVP → iteraciones post-deadline
```

**OPCIÓN B: Ampliar Equipo**
```
Agregar: 4 developers semi-senior
Nuevo equipo: 13.7 FTE
Duración: 171.5 / 13.7 = 12.5 meses

Consideraciones:
- Onboarding: 2 meses
- Ley de Brooks: +overhead 20%
- Duración real: 12.5 × 1.2 + 2 = 17 meses
❌ No resuelve el problema
```

**OPCIÓN C: Reducir Calidad/Compliance**
```
❌ NO RECOMENDADO
- PCI DSS no es negociable
- Regulación BCRA obligatoria
- Alta disponibilidad esperada por usuarios
```

**OPCIÓN D: Combinación Inteligente**
```
✅ ESTRATEGIA RECOMENDADA:

1. MVP 60% funcionalidad: -40% esfuerzo
2. Aumentar 2 developers senior: -2 meses
3. Aceptar deuda técnica controlada: -1 mes
4. Negociar soft launch (beta): +2 meses flexibilidad

Esfuerzo: 24,009 × 0.6 = 14,405 horas
Equipo: 11.7 FTE (con 2 seniors más)
Duración: 14,405 / (11.7 × 140) = 8.8 meses

Con onboarding: 8.8 + 1 = 9.8 meses
Con negociación beta: Dentro de 10 meses aceptable

Roadmap:
- Mes 0-1: Onboarding + Arquitectura
- Mes 2-6: Desarrollo MVP
- Mes 7-8: Testing + Ajustes
- Mes 9: Beta privada (cumple deadline regulatorio)
- Mes 10-12: Features adicionales post-launch
```

---

### 4.3 Lecciones del Caso de Estudio

**Aprendizajes Clave:**

1. **Los factores se multiplican exponencialmente**
   - Un solo proyecto puede tener factor total >5x
   - Criticidad + Compliance + Deadline = tormenta perfecta

2. **El deadline dicta la estrategia**
   - MVP vs producto completo
   - Calidad vs velocidad
   - Scope flexible es clave

3. **La estimación es un proceso iterativo**
   - Primera estimación: Input para negociación
   - Ajustar scope, recursos, o deadline
   - Re-estimar hasta encontrar equilibrio

4. **Documentar supuestos es crítico**
   - "MVP incluye X pero excluye Y"
   - "Deuda técnica se pagará en mes 10-12"
   - "Asumimos 0 rotación de equipo"

5. **Comunicar riesgos transparentemente**
   - Presentar rangos (mejor, esperado, peor caso)
   - Explicar qué puede salir mal
   - Plan de mitigación para cada riesgo

---

## 5. Ejercicios y Casos de Estudio

### Ejercicio 1: Estimación Básica con Puntos Función

**Proyecto:** Sistema de Gestión de Turnos Médicos

**Requerimientos:**
- Pacientes pueden registrarse
- Médicos se registran con especialidades
- Pacientes reservan turnos disponibles
- Sistema envía recordatorios por email
- Médicos ven agenda del día
- Admin gestiona especialidades y horarios
- Reportes: turnos por médico, ocupación

**Consigna:**
1. Identifica y clasifica (baja/media/alta complejidad):
   - Entradas (EI)
   - Salidas (EO)
   - Consultas (EQ)
   - Archivos Internos (ILF)
   - Archivos Externos (EIF)

2. Calcula PFNA

3. Asume Factor de Ajuste = 1.1

4. Calcula PFA

5. Con productividad de 12h/PF, calcula esfuerzo total

6. Si tienes 2 developers, ¿cuántos meses toma el proyecto?

---

### Ejercicio 2: Aplicación de Factores de Riesgo

**Contexto:** El ejercicio anterior (Turnos Médicos)

**Información Adicional:**
- Equipo: 2 developers junior, recién graduados, primera vez con .NET Core
- Dedicación: 70% (también tienen soporte de sistemas legacy)
- Cliente: Médico no técnico, disponible 1 vez por semana
- Complejidad: Media (lógica de disponibilidad, validaciones de horarios)
- Tecnología: Nueva para el equipo
- Deadline: Sugerido 4 meses, pero sin penalidad

**Consigna:**
1. Identifica los factores de riesgo aplicables
2. Asigna un multiplicador a cada factor
3. Calcula el factor compuesto
4. Ajusta la estimación del Ejercicio 1
5. Recalcula la duración real del proyecto
6. Propón estrategias de mitigación

---

### Ejercicio 3: Método Delphi (Grupal)

**Proyecto:** Plataforma de Cursos Online (tipo Udemy simplificado)

**Features:**
- Instructores suben cursos (videos, PDFs)
- Estudiantes compran y acceden a cursos
- Sistema de pagos (integración con MercadoPago)
- Comentarios y ratings
- Certificados de finalización
- Panel de administración

**Consigna (Grupal 4-5 personas):**
1. Cada integrante estima independientemente el proyecto en horas (sin comunicarse)
2. Documenten sus supuestos (qué incluyen, qué excluyen, qué tecnología asumen)
3. Compartan estimaciones anónimamente
4. Discutan diferencias
5. Re-estimen (segunda ronda)
6. Lleguen a consenso final con rango (mejor caso, esperado, peor caso)

---

### Ejercicio 4: Caso Complejo - Sistema E-commerce

**Proyecto:** Marketplace Multi-Vendor (tipo MercadoLibre)

**Requerimientos:**
- Vendedores crean tiendas y publican productos
- Compradores buscan, comparan y compran
- Carrito de compras multi-vendor
- Checkout con múltiples medios de pago
- Logística (tracking de envíos)
- Sistema de reputación (ratings + reviews)
- Chat entre comprador y vendedor
- Panel de vendedor (ventas, inventario, finanzas)
- Panel admin (moderación, análisis, comisiones)
- Notificaciones en tiempo real
- App móvil (iOS + Android)

**Stack:**
- Backend: .NET Core 8, microservicios
- Frontend Web: React
- Mobile: React Native
- BD: SQL Server + MongoDB (búsqueda)
- Cache: Redis
- Mensajería: RabbitMQ
- Cloud: Azure AKS
- Pagos: Integración con 5 procesadores

**Equipo:**
- 8 developers backend (6 semi-senior, 2 junior)
- 3 developers frontend (2 senior, 1 junior)
- 2 developers mobile (1 senior, 1 junior)
- 2 QAs
- 1 DevOps
- 1 Arquitecto
- 1 Product Owner

**Restricciones:**
- Deadline: 14 meses
- Alta disponibilidad: 99.95%
- Compliance: PCI DSS (pagos)
- Escalabilidad: 10K usuarios concurrentes
- Multi-tenant

**Consigna Completa:**
1. Estima con Puntos Función o Casos de Uso
2. Identifica TODOS los factores de riesgo aplicables
3. Calcula factor compuesto total
4. Calcula esfuerzo final y duración
5. ¿Es viable en 14 meses?
6. Si no es viable, propón 3 estrategias diferentes y recalcula cada una
7. Presenta un documento ejecutivo (2 páginas) con:
   - Resumen ejecutivo
   - Estimación base y ajustada
   - Factores de riesgo críticos
   - Viabilidad del deadline
   - Recomendación estratégica
   - Riesgos y mitigaciones

---

### Ejercicio 5: Análisis Post-Mortem

**Contexto:** Proyecto real que se ejecutó

**Datos:**
- Estimación inicial: 6 meses, 4 developers
- Duración real: 11 meses, 6 developers (se sumaron 2 en el mes 4)
- Esfuerzo estimado: 960 PM
- Esfuerzo real: 1,980 PM (más del doble)

**Eventos durante el proyecto:**
- Mes 2: 1 desarrollador senior renuncia
- Mes 3: Cliente cambia 30% de requerimientos
- Mes 4: Se incorporan 2 developers junior
- Mes 5: Se descubre que debe cumplir regulación no contemplada
- Mes 6: BD requiere rediseño por performance
- Mes 7-8: Testing descubre 120 bugs críticos
- Mes 9: Cliente pide funcionalidad adicional "rápida"
- Mes 10-11: Estabilización y ajustes

**Consigna:**
1. Identifica qué factores de riesgo NO se consideraron en la estimación original
2. Asigna un multiplicador a cada evento que ocurrió
3. Calcula el factor compuesto que debió haberse aplicado
4. Compara con la realidad (¿el modelo predice bien?)
5. ¿Qué debió hacerse diferente en la estimación inicial?
6. ¿Qué mitigaciones pudieron evitar los problemas?
7. Redacta "lecciones aprendidas" (5 puntos concretos)

---

## 6. Referencias y Recursos

### 6.1 Libros Recomendados

1. **"Software Estimation: Demystifying the Black Art"** - Steve McConnell
   - El libro definitivo sobre estimación
   - Práctico y basado en evidencia
   - Incluye técnicas, herramientas y estudios de caso

2. **"The Mythical Man-Month"** - Frederick Brooks
   - Clásico sobre gestión de proyectos
   - Ley de Brooks: "Adding people to a late project makes it later"
   - Esencial para entender factores humanos

3. **"Agile Estimating and Planning"** - Mike Cohn
   - Estimación en contextos ágiles
   - Story points, planning poker
   - Velocidad y burndown charts

4. **"Software Cost Estimation with COCOMO II"** - Barry Boehm
   - El manual definitivo de COCOMO
   - Incluye dataset de miles de proyectos
   - Versión académica profunda

### 6.2 Papers Académicos

1. **"A Survey of Software Project Cost and Schedule Estimation Literature"** - Martin Shepperd (Journal of Systems and Software)

2. **"Evidence Based Guidelines for Function Point Analysis"** - Katrina Maxwell

3. **"An Empirical Validation of Software Cost Estimation Models"** - Magne Jørgensen

### 6.3 Herramientas Online

1. **COCOMO Calculator**
   - http://softwarecost.org/tools/COCOMO/
   - Calculadora gratuita para COCOMO II

2. **Function Point Calculator**
   - http://www.functionpoints.com/
   - Herramientas para contar PF

3. **Estimation Spreadsheets**
   - Plantillas Excel para diferentes métodos
   - Disponibles en GitHub y repositorios abiertos

### 6.4 Estándares Internacionales

1. **ISO/IEC 20926:2009** - Function Points
   - Estándar internacional de Puntos Función
   - Método IFPUG detallado

2. **ISO/IEC 14143** - Functional Size Measurement
   - Marco general para métricas de tamaño funcional

3. **CMMI** (Capability Maturity Model Integration)
   - Niveles de madurez de procesos
   - Impacto en estimaciones

### 6.5 Comunidades y Foros

1. **Stack Overflow** - #software-estimation
2. **Reddit** - r/projectmanagement, r/softwareengineering
3. **IFPUG** (International Function Point Users Group)
4. **PMI** (Project Management Institute)

---

## 📝 Notas Finales para Estudiantes

### Consejos Prácticos

1. **La estimación es un arte Y una ciencia**
   - Usa modelos matemáticos (ciencia)
   - Aplica juicio experto (arte)
   - Combina múltiples técnicas

2. **Siempre documenta supuestos**
   - Cada estimación tiene condiciones
   - Si los supuestos cambian, re-estima
   - Comunica claramente las bases de tu estimación

3. **Aprende de cada proyecto**
   - Guarda estimaciones vs realidad
   - Analiza las desviaciones
   - Calibra tus factores personales

4. **Sé honesto y transparente**
   - No des estimaciones optimistas bajo presión
   - Presenta rangos, no números exactos
   - Comunica riesgos claramente

5. **La incertidumbre es normal**
   - Mientras más temprano, más incertidumbre
   - Cone of Uncertainty: ±75% al inicio → ±10% al final
   - Re-estima conforme avanza el proyecto

### Rangos de Confianza

```
Fase del Proyecto        Precisión Esperada
─────────────────────────────────────────────
Idea inicial            ±100% (factor 0.5x - 2x)
Requerimientos iniciales ±75% (factor 0.7x - 1.75x)
Requerimientos completos ±50% (factor 0.75x - 1.5x)
Diseño arquitectónico    ±30% (factor 0.85x - 1.3x)
Diseño detallado         ±20% (factor 0.9x - 1.2x)
Desarrollo comenzado     ±10% (factor 0.95x - 1.1x)
```

### Errores Comunes a Evitar

1. ❌ **Olvidar factores de riesgo**
   - No aplicar multiplicadores
   - Asumir "todo saldrá perfecto"

2. ❌ **Sumar factores en lugar de multiplicarlos**
   - Factor1=1.5, Factor2=1.5 → ×2.25, no ×2.0

3. ❌ **No considerar tiempo improductivo**
   - Asumir 8h productivas por día
   - Realidad: 5-6h productivas

4. ❌ **Ignorar curva de aprendizaje**
   - Equipo nuevo en tecnología
   - Nuevos integrantes en el proyecto

5. ❌ **Presión política**
   - Dar estimaciones optimistas para "ganar el proyecto"
   - Resultado: Proyecto fallido, reputación dañada

6. ❌ **No re-estimar cuando cambian los supuestos**
   - Scope creep sin ajustar tiempos
   - Rotación de personal sin re-planificar

---

## 🎓 Conclusión

La estimación de software es una habilidad crítica que combina:
- **Conocimiento técnico** (arquitecturas, tecnologías, patrones)
- **Modelos matemáticos** (Puntos Función, COCOMO, etc.)
- **Experiencia empírica** (datos históricos, lecciones aprendidas)
- **Análisis de riesgos** (identificar y cuantificar factores)
- **Comunicación efectiva** (presentar y negociar estimaciones)

**No existe la estimación perfecta**, pero con práctica, disciplina y honestidad, puedes hacer estimaciones cada vez más precisas que ayuden a tomar mejores decisiones.

**Recuerda:** Una buena estimación no es la que acierta el número exacto, sino la que:
1. Identifica los riesgos principales
2. Comunica claramente los supuestos
3. Proporciona rangos realistas
4. Permite tomar decisiones informadas
5. Se actualiza cuando cambia el contexto

---

**¡Éxito en sus proyectos de software!**

*Este material fue creado como guía didáctica para estudiantes de Ingeniería de Software y Gestión de Proyectos.*

---

**Versión:** 1.0  
**Fecha:** Noviembre 2025  
**Licencia:** Uso educativo libre
