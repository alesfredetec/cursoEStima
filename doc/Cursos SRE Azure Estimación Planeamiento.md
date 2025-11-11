

# **El Manual del SRE para la Planificación y Estimación Multi-Nube: Un Enfoque Estratégico para el Esfuerzo, la Capacidad y el Costo**

## **Sección I: El Rol del SRE y el Técnico de Nube en la Planificación Estratégica**

La disciplina de Ingeniería de Fiabilidad del Sitio (Site Reliability Engineering, SRE), aplica técnicas de ingeniería de software a problemas de infraestructura y operaciones.1 Esta definición fundamental posiciona al SRE moderno no como un operador reactivo, sino como un ingeniero proactivo cuya responsabilidad principal es la planificación estratégica. La solicitud de un "curso" que combine SRE con la estimación y la planificación no es una solicitud de habilidades adicionales, sino una validación de que la esencia misma de la SRE *es* la planificación y la estimación formalizadas.

El objetivo del SRE no es la fiabilidad máxima, sino alcanzar de manera sostenible el *nivel apropiado* de fiabilidad para sistemas, servicios y productos.2 Este "nivel apropiado" es, en sí mismo, una decisión de planificación estratégica que requiere un equilibrio calculado entre el riesgo (indisponibilidad), el costo (recursos) y la velocidad de innovación.

Para lograr este equilibrio, la SRE utiliza un conjunto de principios que son, en efecto, herramientas de planificación 4:

* **Objetivos de Nivel de Servicio (SLOs):** Los SLOs no son simplemente métricas de monitoreo; son el *objetivo de diseño* de todo el ejercicio de planificación. Un equipo de SRE planifica y aprovisiona la capacidad de la infraestructura con el fin explícito de *cumplir el SLO* acordado con el negocio.6  
* **Presupuestos de Error (Error Budgets):** Son la herramienta de planificación que gestiona el *trade-off* entre fiabilidad y velocidad de innovación.4 Un presupuesto de error es un plan formal y un acuerdo sobre cuánta falta de fiabilidad es aceptable para permitir el desarrollo y el despliegue de nuevas características.  
* **Planificación de Capacidad (Capacity Planning):** Identificada como una práctica central de SRE 5, es el proceso de estimar y aprovisionar los recursos de infraestructura necesarios para manejar la carga actual y futura, todo mientras se cumplen los SLOs.

La adopción de la SRE exige un cambio cultural hacia la responsabilidad compartida y la planificación basada en datos.8 El SRE lidera esta transición introduciendo modelos formales de estimación y planificación.

Fundamentalmente, las diversas formas de estimación solicitadas (tareas, planificación, mercado) no son silos independientes. Representan una *cadena de causalidad* que un SRE senior debe gestionar. Considere el flujo de una nueva característica:

1. **Estimación de Esfuerzo (Ágil):** El equipo debe estimar el *esfuerzo humano* necesario para diseñar, construir y desplegar la infraestructura de soporte para la nueva característica.  
2. **Estimación de Capacidad (SRE):** El equipo debe estimar el *impacto en los recursos* (CPU, memoria, red) que esta nueva característica tendrá en el sistema en producción para garantizar que los SLOs se sigan cumpliendo.  
3. **Estimación de Costos (FinOps):** Ese plan de capacidad se traduce directamente en un *pronóstico de costo financiero* que debe ser presupuestado y aprobado por el negocio.

Este informe está estructurado para guiar al técnico de nube a través de esta cadena de valor, tratando la estimación no como una habilidad secundaria, sino como el conjunto de herramientas estratégicas centrales del SRE.

## **Sección II: Prácticas de Mercado para la Estimación de Tareas y Esfuerzo (Project & Task Estimation)**

Esta sección aborda la "estimación de tareas" y se centra en las metodologías Ágiles (Agile) utilizadas para estimar el *esfuerzo humano* implicado en el desarrollo de software y la gestión de la infraestructura.

### **El Principio Básico: Estimación Relativa vs. Absoluta**

Las prácticas de mercado se han alejado en gran medida de la estimación absoluta (ej. "esta tarea tomará 16 horas") debido a su notoria propensión al error y a la falacia de la planificación.10 En su lugar, la industria favorece la **estimación relativa**, que se centra en comparar el tamaño de las tareas entre sí (ej. "la tarea A es aproximadamente el doble de grande que la tarea B").11 La estimación relativa reconoce que los equipos son mejores para juzgar el tamaño en comparación con otros elementos que en predecir el tiempo exacto.

Las dos técnicas de mercado dominantes para la estimación relativa son T-Shirt Sizing y Story Points.

### **Técnica de Mercado 1: T-Shirt Sizing (Dimensionamiento de Camisetas)**

El T-Shirt Sizing es una técnica de estimación de proyectos que asigna un "tamaño" de camiseta (ej. XS, S, M, L, XL, XXL) a cada tarea o iniciativa del proyecto.12

* **Aplicación:** Es especialmente útil en las primeras etapas de la planificación 13 y es ideal para la planificación de alto nivel, la creación de *roadmaps* y la estimación de grandes bloques de trabajo, como las *Epics*.11  
* **Beneficios:**  
  * **Rapidez e Intuición:** Es un método rápido y fácil de entender para todos los miembros del equipo, incluso aquellos nuevos en Agile.15  
  * **Multidimensional:** A diferencia de los números, que a menudo se asocian solo con el tiempo, un "tamaño" de camiseta puede representar una combinación más compleja de factores, incluyendo el alcance, el esfuerzo, la complejidad y el tiempo.12  
  * **Fomenta la Colaboración:** Promueve la discusión en equipo para llegar a un acuerdo sobre el tamaño relativo, evitando la "falsa precisión" de las estimaciones numéricas detalladas.13

### **Técnica de Mercado 2: Story Points (Puntos de Historia) y Planning Poker**

Los Story Points son la unidad de medida más común utilizada en los equipos Scrum para la estimación relativa detallada.11

* **Definición:** Un Story Point es una unidad de medida abstracta que representa una combinación de tres factores clave: la complejidad del trabajo, la cantidad de trabajo y la incertidumbre o riesgo involucrado.11  
* **Escala:** Comúnmente utiliza una versión modificada de la **secuencia de Fibonacci** (ej. 1, 2, 3, 5, 8, 13, 21...).11 Este escalado no lineal es intencional; refleja cómo la incertidumbre aumenta exponencialmente con el tamaño de la tarea. La diferencia entre una tarea de 2 y 3 puntos es pequeña, pero la diferencia entre una de 8 y 13 es significativamente mayor.  
* **Método (Planning Poker):** La técnica de mercado para asignar Story Points es el "Planning Poker". Es un método de consenso en equipo donde cada miembro "vota" por el tamaño de la *story* (historia de usuario).19 Las discrepancias en los votos conducen a discusiones que sacan a la luz suposiciones ocultas o lagunas de conocimiento.  
* **Aplicación:** Los Story Points se utilizan para la planificación de *Sprints*. Al rastrear cuántos puntos completa un equipo por sprint, se puede calcular la **Velocity (Velocidad)** del equipo.18 La velocidad es una métrica de pronóstico crucial que permite al equipo predecir cuánto trabajo pueden realizar en futuros sprints.

### **De la Práctica a la Estrategia: Un Flujo de Trabajo de Refinamiento**

Una práctica experta no consiste en elegir entre T-Shirt Sizing y Story Points. Más bien, estas herramientas se utilizan de forma complementaria en un *flujo de trabajo de refinamiento progresivo*.11

1. **Fase de Roadmap (Trimestral):** El equipo de SRE y los Product Managers estiman las grandes *Epics* (ej. "Migrar base de datos a Azure SQL") utilizando **T-Shirt Sizing** (ej. "Eso es un 'Large'"). Esto es rápido y suficiente para la planificación de alto nivel.14  
2. **Fase de Planificación de Sprint (Quincenal):** Durante el *backlog grooming* o la planificación del sprint, el equipo desglosa esa Epic "Large" en *User Stories* más pequeñas (ej. "Configurar servidor Azure SQL", "Migrar esquema", "Validar datos"). Estas *stories* más pequeñas se estiman con mayor precisión utilizando **Story Points** y **Planning Poker**.11

Otras técnicas de estimación formales, como **Wideband Delphi** (una técnica de consenso de expertos anónima) 18 y el **Juicio de Experto** (aprovechar el conocimiento de especialistas) 18, también son prácticas de mercado válidas, a menudo utilizadas para tareas de infraestructura complejas con alta incertidumbre.

---

**Tabla 1: Comparativa de Métodos de Estimación Ágil**

| Método | Escala | Nivel de Abstracción | Caso de Uso Principal | Ventaja Clave |
| :---- | :---- | :---- | :---- | :---- |
| **T-Shirt Sizing** | XS, S, M, L, XL | Alta | Planificación de Roadmap, Estimación de Epics 11 | Rápido, intuitivo, captura la complejidad multidimensional 12 |
| **Story Points (Fibonacci)** | 1, 2, 3, 5, 8, 13... | Media | Planificación de Sprints, Cálculo de Velocidad (Velocity) 11 | Precisión relativa para pronósticos, refleja la incertidumbre 11 |
| **Planning Poker** | N/A (Método) | N/A | Lograr consenso sobre Story Points 19 | Construye consenso, expone suposiciones ocultas 17 |
| **Wideband Delphi** | N/A (Método) | Media / Baja | Tareas complejas con alta incertidumbre 18 | Consenso de expertos anónimo, reduce el sesgo de grupo |
| **Horas/Días (Absoluta)** | 1h, 4h, 3d... | Baja | Tareas muy pequeñas y bien definidas | Familiaridad (aunque a menudo es engañosa 10) |

---

## **Sección III: Adaptación de Metodologías Ágiles para Equipos SRE y de Infraestructura**

La aplicación de metodologías Ágiles, diseñadas para el desarrollo de *productos* predecibles, al mundo de las *operaciones* de SRE, que es intrínsecamente impredecible, es uno de los mayores desafíos de la industria.21 Esta sección aborda el conflicto y presenta el modelo híbrido que utilizan las organizaciones maduras.

### **El Conflicto Central: Trabajo Planificado vs. No Planificado**

Los intentos de forzar a los equipos SRE/Ops a un marco de *Scrum estricto* a menudo fracasan. Las razones de este fracaso están bien documentadas 21:

* **Naturaleza Dinámica:** El trabajo de SRE es altamente dinámico, con prioridades que pueden cambiar diariamente en respuesta a las condiciones de producción.  
* **Competición de Prioridades:** El trabajo planificado (proyecto, reducción de *toil*) compite constantemente por el tiempo del ingeniero con el trabajo no planificado (incidentes, guardia, post-mortems).  
* **Interrupciones de Sprint:** El trabajo no planificado "rompe" la cadencia del sprint de dos semanas, haciendo que la planificación parezca inútil y agresiva.21  
* **Imprevisibilidad de la Guardia (On-Call):** La rotación de guardia añade una capa de imprevisibilidad que consume capacidad de formas difíciles de estimar por tarea.  
* **Estimación de Bugs:** Existe un debate en la industria sobre si los *bugs* o las tareas de soporte deben recibir Story Points. Muchos mentores desaconsejan esta práctica, ya que la estimación es casi imposible y no representa la creación de nuevo valor.22

Este fracaso no se debe a un defecto en los principios Ágiles, sino a la aplicación dogmática de una *implementación* (Scrum) que no fue diseñada para un entorno con un alto volumen de trabajo reactivo.

### **La Solución del Mercado: El Modelo Híbrido SRE**

Las organizaciones de SRE maduras, como Google, no intentan eliminar el trabajo reactivo; lo gestionan, lo miden y lo *presupuestan*.

**1\. El Principio 50/50 de Google:** La práctica de SRE de Google establece que los SREs deben dedicar un máximo del 50% de su tiempo a operaciones (trabajo reactivo, *toil*) y un mínimo del 50% a trabajo de proyecto (ingeniería de software, automatización).23 Si el trabajo de operaciones supera el 50%, el equipo detiene la incorporación de nuevas características y se enfoca en la ingeniería para reducir la carga operativa.

**2\. El Búfer de Capacidad del TPM de Google:** Una práctica de gestión de proyectos técnicos (TPM) más concreta de Google es *reservar explícitamente un búfer de capacidad* para este trabajo. Al planificar un proyecto de SRE, un TPM puede reservar el 25% del tiempo de ingeniería *solo para el trabajo de producción* y planificar el cronograma del proyecto con el 75% restante de la capacidad.23

Esto representa un cambio de mentalidad fundamental. El "trabajo no planificado" deja de ser una "interrupción" para convertirse en una *cantidad estadísticamente predecible que debe ser presupuestada*. En lugar de esperar tener cero incidentes, el equipo presupuesta un tiempo para ellos basándose en datos históricos (ej. "gastamos un promedio del 30% de nuestro tiempo en incidentes los últimos 6 meses"). Un equipo SRE maduro calcula su *capacidad real de proyecto* (Capacidad Total \- Búfer de Ops) *antes* de la planificación del sprint.

3\. Reframing de Tareas como "Stakeholder Stories":  
Para el trabajo de proyecto de SRE, las tareas de infraestructura pueden (y deben) ser estimadas. El truco consiste en enmarcarlas como "Historias de Interesados" (Stakeholder Stories).25 A menudo, el stakeholder es el propio equipo de SRE, y el beneficio es la reducción del riesgo o del toil (trabajo manual repetitivo).

* Ejemplo de Historia SRE 25: "Para minimizar el riesgo de desplegar algo roto (beneficio), Como el equipo que despliega el código (stakeholder), Queremos un sistema de despliegie automatizado (funcionalidad)".  
* Esta es ahora una *feature* clara que puede ser priorizada y estimada en Story Points, al igual que cualquier característica de producto.

### **Implementación Práctica: Scrum-ban / Kanban**

Para gestionar esta dualidad, los equipos SRE exitosos a menudo convergen en un modelo híbrido "Scrum-ban" o un sistema Kanban puro. Este modelo permite la coexistencia de ambos tipos de trabajo:

* **Carriles de Proyecto (Swimlanes):** El tablero tiene un carril para el trabajo de proyecto planificado, que se estima con Story Points y sigue un *backlog*.  
* **Carriles de Interrupción (Expedite Lanes):** El tablero tiene carriles de alta prioridad para el trabajo reactivo (Incidentes, Soporte Urgente) que *no* se estima en puntos, sino que se mide por su *cycle time* (tiempo desde el inicio hasta la finalización).

Las certificaciones modernas de SRE (SRE Foundation) 26 y las de Scrum (Scrum.org) 27 reconocen que los SREs y los Scrum Masters 28 deben colaborar para adaptar estos marcos a la realidad de las operaciones.

---

**Tabla 2: Adaptación de Prácticas Scrum/Kanban para Equipos SRE**

| Práctica Ágil Estándar | Desafío para SRE | Adaptación SRE Experta (El Modelo Híbrido) |
| :---- | :---- | :---- |
| **Planificación de Sprint** | Llenar el 100% de la capacidad con *stories* | (Desafío) Interrupciones constantes; sprints de 2 semanas son agresivos |
| **Backlog** | Un único Product Backlog priorizado | (Desafío) ¿Cómo priorizar un *bug* 22 contra una *feature*? |
| **Estimación** | Estimar todo en Story Points | (Desafío) No tiene sentido estimar *bugs* o soporte en producción 22 |
| **Métricas de Éxito** | *Velocity* (Velocidad) de puntos completados | (Desafío) La velocidad es errática e inútil debido al trabajo no planificado |

---

## **Sección IV: Planificación de Capacidad: Modelos de Estimación de Cargas de Trabajo en la Nube**

Esta sección aborda el "método de planeamiento" para los recursos de infraestructura (CPU, RAM, red, IOPS). Esta es la disciplina de estimación clásica de la SRE, que pasa del *esfuerzo humano* a la *capacidad de la máquina*.

### **El Enfoque de Google SRE (El "Por Qué")**

La gestión de capacidad de SRE se divide en dos vistas 29:

1. **Provisión de Recursos (Resource Provisioning):** La pregunta táctica: "¿Cómo mantengo el servicio funcionando *ahora mismo* con la carga actual?".  
2. **Planificación de Capacidad (Capacity Planning):** La pregunta estratégica: "¿Cómo mantengo el servicio funcionando *en el futuro previsible* con la carga esperada?".

El objetivo de esta planificación es controlar la incertidumbre y gestionar el *trade-off* fundamental entre la **eficiencia** (costo, no sobreaprovisionar) y la **fiabilidad** (no subaprovisionar y arriesgar los SLOs).29

Para crear un plan de capacidad estratégico, un SRE debe estimar basándose en factores clave 29:

* **Demanda:** Patrones de uso actuales (usuarios, tráfico).  
* **Crecimiento Orgánico:** El crecimiento predecible basado en tendencias históricas.  
* **Crecimiento Inorgánico:** Picos de crecimiento impredecibles debidos a lanzamientos de funciones, campañas de marketing o eventos externos.  
* **Redundancia:** El costo de la fiabilidad, a menudo expresado como un modelo **N+x** (ej. N+2 significa que el sistema puede tolerar 2 fallos de componentes/regiones).29

Las mejores prácticas de SRE para esta planificación incluyen la realización de pruebas de carga (load testing) adecuadas, la implementación de monitoreo y alertas exhaustivas, y el desarrollo de un plan de capacidad formal.29

### **El Enfoque de Microsoft Azure Well-Architected Framework (El "Cómo")**

Mientras que Google proporciona la filosofía SRE, Microsoft la ha *productizado* en una metodología prescriptiva para sus clientes de Azure: el **Well-Architected Framework (WAF)**.31 El pilar de "Eficiencia de Rendimiento" del WAF se alinea directamente con la planificación de capacidad de SRE.31

El WAF de Azure prescribe un proceso de 5 pasos para la planificación de la capacidad, que es esencialmente el manual de "cómo" implementar la filosofía SRE de Google 31:

1. **Recopilar datos de capacidad:** Analizar datos históricos (para cargas de trabajo existentes) utilizando herramientas como **Azure Monitor**, **Application Insights** y **Log Analytics**.31 Para cargas nuevas, usar el juicio de expertos o prototipos a pequeña escala.  
2. **Pronosticar la demanda:** Aplicar análisis estadístico, análisis de tendencias y modelado predictivo a los datos recopilados para proyectar las necesidades futuras.  
3. **Alinear las previsiones con los objetivos de la carga de trabajo:** Asegurarse de que el plan de capacidad de recursos (ej. "necesitamos 5 VMs") cumpla con los objetivos de negocio (ej. "para mantener nuestro SLO de 99.9%").  
4. **Determinar los requisitos de recursos:** Estimar los recursos informáticos (CPU, memoria, disco) y el ancho de banda de red necesarios.  
5. **Comprender las limitaciones de recursos:** Conocer los límites de los SKU de servicio de Azure, las cuotas de suscripción y los límites de escalabilidad. Esto se valida mediante **Azure Load Testing** y **Traffic Analytics**.31

Microsoft proporciona herramientas especializadas para escenarios de planificación específicos, como el **Azure Stack Hub Capacity Planner** (para nube híbrida) 32 y guías de planificación de capacidad para servicios como **Azure SQL** 34 y Microsoft Identity Manager.35

Es crucial destacar un factor que el WAF de Azure incluye explícitamente en el Paso 4 ("Determinar los requisitos de recursos"): el **Personal**.31 Un plan de capacidad completo no solo estima las máquinas, sino también los *recursos humanos* (el tiempo de SRE) necesarios para gestionar, mantener y operar la infraestructura. Esto conecta la planificación de capacidad de la máquina directamente con la estimación del esfuerzo humano (Sección II) y el modelo de búfer de capacidad (Sección III). El "50% de tiempo de operaciones" de SRE 23 *es* un requisito de capacidad que debe ser presupuestado, tan crítico como la CPU para un servidor web.

## **Sección V: FinOps: El Framework del Mercado para la Estimación y Gestión de Costos en la Nube**

Esta sección aborda los "métodos de estimación del mercado", que se refieren a la disciplina de **FinOps**, la tercera y última parte de la cadena de estimación. FinOps traduce las decisiones técnicas de capacidad en impacto financiero.

### **Introducción a FinOps**

FinOps (Cloud Financial Management) es una práctica cultural y un marco operativo que reúne a la ingeniería, las finanzas y el negocio para gestionar el gasto en la nube e impulsar el máximo valor empresarial.36 A diferencia de la gestión de costos de TI tradicional, FinOps adopta el modelo de costo variable de la nube y se centra en la toma de decisiones descentralizada y basada en datos.

### **El Framework de FinOps (FinOps Foundation)**

La industria se ha estandarizado en torno al marco de la FinOps Foundation, que se basa en un conjunto de principios, fases y dominios.40

* Principios Clave 40:  
  1. Los equipos deben colaborar.  
  2. El valor empresarial impulsa las decisiones tecnológicas (actualizado desde "valor de la nube").  
  3. Todos asumen la propiedad de su uso tecnológico (actualizado desde "uso de la nube").  
  4. Los datos de FinOps deben ser accesibles, oportunos y precisos.  
  5. Debe habilitarse de forma centralizada.  
  6. Aprovechar el modelo de costo variable de la nube.  
* Fases del Ciclo de Vida 41: FinOps es un ciclo iterativo:  
  1. **Informar (Inform):** Proporcionar visibilidad y asignación de costos.  
  2. **Optimizar (Optimize):** Reducir el desperdicio y mejorar la eficiencia (ej. usando reservas).  
  3. **Operar (Operate):** Definir y hacer cumplir políticas y gobernanza.  
* Dominios 38: Son las áreas de actividad, que incluyen "Comprender el Uso y el Costo", "Optimizar el Uso y el Costo", y "Gestionar la Práctica de FinOps".

### **Enfoque Profundo: El Dominio de "Cuantificar el Valor Empresarial"**

Para un SRE centrado en la estimación, el dominio más crítico es **"Quantify Business Value" (Cuantificar el Valor Empresarial)**. Este dominio contiene la capacidad específica de **"Planning & Estimating" (Planificación y Estimación)**.38

La estimación de FinOps es el proceso de pronosticar el costo y el uso de cargas de trabajo nuevas y existentes.43 Los métodos de estimación de FinOps recomendados por el mercado incluyen 44:

1. **Calculadoras de Costos:** Herramientas proporcionadas por los proveedores (ej. Azure Pricing Calculator).  
2. **Aplicaciones Similares (Estimación Análoga):** Usar el costo de una aplicación existente para estimar una nueva aplicación similar.  
3. **Extrapolación del Costo Pasado:** Usar tendencias históricas para pronosticar costos futuros.  
4. **Estimación de Prueba (Trial-run):** El método más preciso para la nube. Consiste en construir el entorno (a menudo con Infraestructura como Código), dejarlo funcionar durante un breve período (ej. 1-3 días) para medir el costo real, y luego destruirlo.

Este dominio también incluye el **Pronóstico (Forecasting)**, la **Presupuestación (Budgeting)** y la **Economía Unitaria (Unit Economics)** 38, que mide el costo por unidad de valor empresarial (ej. costo por usuario activo).

FinOps es el *vínculo estratégico* que traduce las decisiones técnicas de SRE (fiabilidad) al lenguaje del negocio (valor financiero). El "Presupuesto de Error" (Error Budget) del SRE 5 y el "Presupuesto" (Budget) de FinOps 38 son dos caras de la misma moneda de planificación. Un SRE utiliza la planificación de capacidad (Sección IV) para determinar que un SLO de 99.99% requiere una arquitectura N+2.29 FinOps utiliza la "Planificación y Estimación" 44 para determinar que esa arquitectura cuesta $5,000 más al mes que la arquitectura N+1 (99.9%).

Esto permite al SRE aplicar el principio de FinOps ("El valor empresarial impulsa las decisiones") 40 y preguntar al negocio: "¿Vale la pena pagar $5,000 al mes por este 'nueve' adicional de fiabilidad?".

---

Tabla 3: Framework FinOps: Fases, Dominios y Capacidades Clave 40

| Fase del Ciclo de Vida | Dominio | Capacidades Clave Relevantes |
| :---- | :---- | :---- |
| **Informar** | **Comprender el Uso y el Costo** | Ingesta de Datos, Asignación, Informes y Análisis, Gestión de Anomalías |
| **Informar / Optimizar** | **Cuantificar el Valor Empresarial** | **Planificación y Estimación**, Previsión, Presupuestación, Economía Unitaria |
| **Optimizar** | **Optimizar el Uso y el Costo** | Arquitectura para la Nube, Optimización de Cargas de Trabajo, Optimización de Tarifas (ej. Reservas 45), Sostenibilidad |
| **Operar** | **Gestionar la Práctica de FinOps** | Política y Gobernanza, Incorporación de Cargas de Trabajo, Educación de FinOps |

---

## **Sección VI: Aplicación Práctica: Herramientas de Estimación en Azure y Entornos Multi-Nube**

Esta sección unifica las tres disciplinas de estimación (Esfuerzo, Capacidad, Costo) en un flujo de trabajo práctico utilizando el conjunto de herramientas de Microsoft Azure.46

### **1\. Estimación de Esfuerzo (Agile) con Azure DevOps**

* **Plataforma:** **Azure DevOps** es la solución integral de Microsoft para implementar las prácticas de DevOps, incluyendo la planificación Ágil.46  
* **Herramienta:** **Azure Boards** es el componente de Azure DevOps para la gestión de proyectos. Permite a los equipos:  
  * Gestionar *Backlogs* de Producto y *Backlogs* de Sprint.  
  * Implementar Scrum, incluyendo la estimación de **Story Points** en los PBI (Product Backlog Items).19  
  * Realizar sesiones de **Planning Poker** durante el *backlog refinement* para llegar a un consenso de estimación.19  
* **Certificación:** La certificación **AZ-400: Designing and Implementing Microsoft DevOps Solutions** 2 valida la competencia en el uso de estas herramientas y en el desarrollo de una estrategia SRE.2

### **2\. Estimación de Capacidad (SRE) con Azure Monitor y WAF**

* **Plataforma:** **Azure Monitor** es el servicio central de Azure para la recopilación de datos de capacidad (Paso 1 del WAF).31  
* **Herramientas:**  
  * **Application Insights** y **Log Analytics:** Se utilizan para establecer líneas de base de rendimiento, recopilar métricas (CPU, memoria) y analizar patrones de uso históricos.31  
  * **Azure Load Testing:** Se utiliza para validar los modelos de capacidad (Paso 5 del WAF), simular cargas de usuarios y determinar los puntos de ruptura del sistema antes de que afecten a la producción.31  
  * **Azure Stack Hub Capacity Planner:** Una hoja de cálculo especializada para estimar los requisitos de recursos en entornos de nube híbrida.32

### **3\. Estimación de Costos (FinOps) con la Suite de Azure Cost Management**

* **Plataforma:** Microsoft proporciona un conjunto de herramientas FinOps que se alinean con las fases del ciclo de vida de la FinOps Foundation.38  
* **Herramientas para Planificación (Fase "Informar"):**  
  * **Azure Pricing Calculator:** La herramienta principal para la estimación de FinOps (método "Calculadora").44 Permite a los SREs modelar configuraciones de servicios y estimar sus costos.43 Sus características de "Guardar" y "Compartir" 50 son cruciales para la colaboración.  
  * **TCO Calculator (Total Cost of Ownership):** Se utiliza para la planificación de migraciones, proporcionando una comparación de alto nivel entre los costos locales y los de Azure.43  
  * **Azure Migrate:** Herramienta clave para la migración. Automatiza el descubrimiento y la evaluación de cargas de trabajo locales para estimar los costos de la nube y los requisitos de capacidad.43  
* **Herramientas para Gestión Continua (Fases "Informar", "Optimizar" y "Operar"):**  
  * **Azure Cost Management and Billing:** La herramienta central para la fase *Informar*. Proporciona visibilidad, asignación de costos y la capacidad de crear presupuestos.38  
  * **Azure Advisor:** La herramienta principal para la fase *Optimizar*. Analiza el uso y proporciona recomendaciones proactivas, como redimensionar VMs o comprar Reservas (Optimización de Tarifas).38  
  * **Azure Policy:** La herramienta para la fase *Operar*. Permite la gobernanza al aplicar políticas que controlan el gasto (ej. "no permitir VMs de la serie G").43  
  * **FinOps Hubs:** Una solución avanzada para la fase *Informar*, que permite análisis de datos de costos a gran escala sobre Microsoft Fabric o Azure Data Explorer.52

Estas herramientas no son independientes; forman un *flujo de trabajo de estimación de extremo a extremo*. Un SRE puede ejecutar el ciclo de vida completo (Insight 8\) dentro del ecosistema de Azure:

1. **(Agile):** Una nueva *feature* se estima en Story Points en **Azure DevOps Boards**.19  
2. **(FinOps/SRE):** El SRE modela la infraestructura necesaria en la **Azure Pricing Calculator** y adjunta la estimación de costos al PBI.43  
3. **(SRE):** Tras el despliegue, **Azure Monitor** 31 mide la capacidad real y el rendimiento.  
4. **(FinOps):** **Azure Cost Management** 38 informa sobre el costo real vs. el estimado.  
5. **(FinOps/SRE):** **Azure Advisor** 38 genera una recomendación (ej. "redimensionar VM").  
6. **(Agile):** Esta recomendación se convierte en un nuevo PBI en **Azure DevOps Boards**, reiniciando el ciclo de estimación y optimización.

---

**Tabla 4: Matriz de Herramientas de Planificación y Estimación de Azure**

| Dominio de Estimación | Tarea de Planificación Específica | Herramienta de Azure | Fuente(s) |
| :---- | :---- | :---- | :---- |
| **Esfuerzo (Agile)** | Planificación de Sprints, backlog grooming, Story Points | Azure DevOps Boards | 19 |
| **Capacidad (SRE)** | Recopilar datos de carga de trabajo existente (WAF Paso 1\) | Azure Monitor, Application Insights, Log Analytics | 31 |
| **Capacidad (SRE)** | Validar límites de rendimiento (pruebas de carga) (WAF Paso 5\) | Azure Load Testing | 31 |
| **Capacidad (SRE)** | Planificar capacidad en entorno híbrido | Azure Stack Hub Capacity Planner | 32 |
| **Costo (FinOps)** | Estimar costo de nueva carga de trabajo (Planificación) | Azure Pricing Calculator | 43 |
| **Costo (FinOps)** | Estimar costo de migración desde local (Planificación) | Azure Migrate, TCO Calculator | 43 |
| **Costo (FinOps)** | Monitorizar y analizar costo real (Fase Informar) | Azure Cost Management and Billing | 38 |
| **Costo (FinOps)** | Obtener recomendaciones de optimización (Fase Optimizar) | Azure Advisor | 38 |
| **Costo (FinOps)** | Análisis avanzado de datos de FinOps (Fase Informar) | FinOps Hubs (sobre Fabric/Data Explorer) | 52 |
| **Costo (FinOps)** | Aplicar control de costos (Fase Operar) | Azure Policy, Azure Budgets | 51 |

---

## **Sección VII: Recomendaciones Estratégicas y Próximos Pasos para el Técnico de Nube**

La estimación precisa no puede existir en el vacío. Requiere una base de **Gobernanza de la Nube (Cloud Governance)**.53 La gobernanza es el marco de políticas, roles y responsabilidades que gestionan cómo se utilizan los servicios en la nube.53 Es el pilar que sostiene tanto la planificación de SRE como la gestión de FinOps. No se puede estimar el costo sin presupuestos 51 y no se puede planificar la capacidad sin políticas de asignación de recursos. Establecer una "cultura consciente de los costos" es una mejor práctica de gobernanza fundamental.55

### **La Convergencia de Roles: El SRE Híbrido**

El análisis de las prácticas de mercado y las herramientas de Azure revela una convergencia de roles. La consulta sobre un "curso" para SRE que incluya estimación de tareas, planificación y métodos de mercado es, en efecto, la descripción de un nuevo rol híbrido y senior.

El técnico de nube o SRE exitoso del futuro es una combinación de tres roles anteriormente distintos:

1. **El Ingeniero de Software Ágil:** Que aplica la estimación relativa y la gestión del *backlog* (Sección II y III) a las tareas de infraestructura.  
2. **El Arquitecto/TPM de SRE:** Que aplica la planificación de capacidad y el diseño de fiabilidad (Sección IV) para cumplir con los SLOs.  
3. **El Practicante de FinOps:** Que aplica la estimación de costos y el análisis de valor (Sección V) para traducir las decisiones técnicas en impacto empresarial.

Los cursos de la industria reflejan esta convergencia: los cursos de gestión de proyectos ahora incluyen DevOps y Nube 57, las certificaciones SRE están dirigidas a Scrum Masters 26 y la formación en FinOps está dirigida a arquitectos de la nube.36

### **Rutas de Aprendizaje y Certificación Recomendadas**

Para dominar este rol convergente, se recomienda una *tríada de experiencia* que abarque la plataforma, la metodología y el negocio:

1. **Dominio de la Plataforma (Azure):** La certificación central es **AZ-400: Designing and Implementing Microsoft DevOps Solutions**.2 Esta certificación valida la capacidad de implementar la estrategia SRE 9, utilizar Azure DevOps para la planificación Ágil 48, y gestionar las operaciones de la nube.  
2. **Dominio de la Metodología (SRE):** La certificación **SRE Foundation** del DevOps Institute 26 proporciona los principios fundamentales de SRE, su relación con DevOps y las prácticas centrales de fiabilidad y monitoreo.  
3. **Dominio del Negocio (FinOps):** La certificación **FinOps Certified Professional** (FOCP) de la FinOps Foundation 59 es el estándar de oro de la industria para dominar el marco de gestión de costos, la estimación y la optimización.

Para la formación práctica y contextual en la región, los profesionales pueden complementar este camino con programas como el **Diplomado Universitario "DevOps Tools Engineer" de la UTN** 60 para habilidades de herramientas, o cursos especializados de proveedores como **IT College** 48 y **NobleProg** 36 para una formación intensiva en Azure o FinOps.

#### **Fuentes citadas**

1. SRE for Azure Deep Dive \- Pluralsight, acceso: noviembre 10, 2025, [https://www.pluralsight.com/courses/sre-for-azure-deep-dive](https://www.pluralsight.com/courses/sre-for-azure-deep-dive)  
2. Develop a Site Reliability Engineering (SRE) strategy \- Training ..., acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/training/paths/az-400-develop-sre-strategy/](https://learn.microsoft.com/en-us/training/paths/az-400-develop-sre-strategy/)  
3. Introduction to Site Reliability Engineering (SRE) \- Training \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/training/modules/intro-to-site-reliability-engineering/](https://learn.microsoft.com/en-us/training/modules/intro-to-site-reliability-engineering/)  
4. Site Reliability Engineering (SRE) \- Google Cloud, acceso: noviembre 10, 2025, [https://cloud.google.com/sre?hl=es](https://cloud.google.com/sre?hl=es)  
5. Production Services Best Practices \- Google SRE, acceso: noviembre 10, 2025, [https://sre.google/sre-book/service-best-practices/](https://sre.google/sre-book/service-best-practices/)  
6. SRE Best Practices: Mastering Site Reliability Engineering | by Squadcast \- Medium, acceso: noviembre 10, 2025, [https://medium.com/@squadcast/sre-best-practices-mastering-site-reliability-engineering-7e027808aafc](https://medium.com/@squadcast/sre-best-practices-mastering-site-reliability-engineering-7e027808aafc)  
7. ¿Qué es la ingeniería de fiabilidad del sitio (SRE)? \- IBM, acceso: noviembre 10, 2025, [https://www.ibm.com/es-es/think/topics/site-reliability-engineering](https://www.ibm.com/es-es/think/topics/site-reliability-engineering)  
8. Red Hat Transformational Learning: Introduction to Pragmatic Site Reliability Engineering | TL112, acceso: noviembre 10, 2025, [https://www.redhat.com/es/services/training/tl112-pragmatic-introduction-site-reliability-engineering-implementation-devops](https://www.redhat.com/es/services/training/tl112-pragmatic-introduction-site-reliability-engineering-implementation-devops)  
9. Transitional approach to implementing pragmatic Site Reliability Engineering (SRE) Technical Overview | TL012 \- Red Hat, acceso: noviembre 10, 2025, [https://www.redhat.com/es/services/training/transitional-approach-implementing-pragmatic-site-reliability-engineering-sre-technical-overview](https://www.redhat.com/es/services/training/transitional-approach-implementing-pragmatic-site-reliability-engineering-sre-technical-overview)  
10. You Should Not Estimate Using Story Points | by Martin ter Haak \- Medium, acceso: noviembre 10, 2025, [https://martinterhaak.medium.com/why-you-should-not-estimate-using-story-points-b183a5fa10d9](https://martinterhaak.medium.com/why-you-should-not-estimate-using-story-points-b183a5fa10d9)  
11. Story Points In Jira Explained | TitanApps Blog, acceso: noviembre 10, 2025, [https://titanapps.io/blog/story-points-jira/](https://titanapps.io/blog/story-points-jira/)  
12. How to Use T-Shirt Sizing to Estimate Projects \[2025\] \- Asana, acceso: noviembre 10, 2025, [https://asana.com/resources/t-shirt-sizing](https://asana.com/resources/t-shirt-sizing)  
13. T-Shirt Sizing: An Agile Estimation Guide 2025 \- KnowledgeHut, acceso: noviembre 10, 2025, [https://www.knowledgehut.com/blog/agile/t-shirt-sizing-use-to-estimate-delivery](https://www.knowledgehut.com/blog/agile/t-shirt-sizing-use-to-estimate-delivery)  
14. How to use T-Shirt Sizing to Estimate Projects \[2025\] \- Agilemania, acceso: noviembre 10, 2025, [https://agilemania.com/t-shirt-sizing-agile-estimation-technique](https://agilemania.com/t-shirt-sizing-agile-estimation-technique)  
15. How I use T-Shirt sizing as a Product Owner to estimate delivery | by Janaka Fernando | Serious Scrum | Medium, acceso: noviembre 10, 2025, [https://medium.com/serious-scrum/how-i-use-t-shirt-sizing-as-a-product-owner-to-estimate-delivery-4b24634d22a6](https://medium.com/serious-scrum/how-i-use-t-shirt-sizing-as-a-product-owner-to-estimate-delivery-4b24634d22a6)  
16. T-Shirt Sizing \- Detailed Agile Estimation Guide \- ActiveCollab, acceso: noviembre 10, 2025, [https://activecollab.com/blog/project-management/t-shirt-sizing](https://activecollab.com/blog/project-management/t-shirt-sizing)  
17. What are story points in Agile and how do you estimate them? \- Atlassian, acceso: noviembre 10, 2025, [https://www.atlassian.com/agile/project-management/estimation](https://www.atlassian.com/agile/project-management/estimation)  
18. Agile Estimation: Getting Started \- Pluralsight, acceso: noviembre 10, 2025, [https://www.pluralsight.com/courses/getting-started-agile-estimation](https://www.pluralsight.com/courses/getting-started-agile-estimation)  
19. Implementing Scrum with Azure DevOps \- Pluralsight, acceso: noviembre 10, 2025, [https://www.pluralsight.com/courses/implementing-scrum-azure-devops](https://www.pluralsight.com/courses/implementing-scrum-azure-devops)  
20. Project Estimation \[Methods & Best Practices\] | The Workstream \- Atlassian, acceso: noviembre 10, 2025, [https://www.atlassian.com/work-management/project-management/project-estimation](https://www.atlassian.com/work-management/project-management/project-estimation)  
21. process \- Is scrum or kanban really useful for SRE teams? \- DevOps ..., acceso: noviembre 10, 2025, [https://devops.stackexchange.com/questions/8758/is-scrum-or-kanban-really-useful-for-sre-teams](https://devops.stackexchange.com/questions/8758/is-scrum-or-kanban-really-useful-for-sre-teams)  
22. Should points be applied to production support tasks? : r/scrum \- Reddit, acceso: noviembre 10, 2025, [https://www.reddit.com/r/scrum/comments/10i306x/should\_points\_be\_applied\_to\_production\_support/](https://www.reddit.com/r/scrum/comments/10i306x/should_points_be_applied_to_production_support/)  
23. Project management for SREs | Google Cloud Blog, acceso: noviembre 10, 2025, [https://cloud.google.com/blog/products/devops-sre/project-management-for-sres/](https://cloud.google.com/blog/products/devops-sre/project-management-for-sres/)  
24. Project management for SREs | Google Cloud Blog, acceso: noviembre 10, 2025, [https://cloud.google.com/blog/products/devops-sre/project-management-for-sres](https://cloud.google.com/blog/products/devops-sre/project-management-for-sres)  
25. How does a Scrum team account for infrastructure tasks in the planning meeting?, acceso: noviembre 10, 2025, [https://softwareengineering.stackexchange.com/questions/61529/how-does-a-scrum-team-account-for-infrastructure-tasks-in-the-planning-meeting](https://softwareengineering.stackexchange.com/questions/61529/how-does-a-scrum-team-account-for-infrastructure-tasks-in-the-planning-meeting)  
26. Site Reliability Engineering (SRE) Foundation \- DevOps Institute, acceso: noviembre 10, 2025, [https://www.devopsinstitute.com/certifications/sre-foundation/](https://www.devopsinstitute.com/certifications/sre-foundation/)  
27. Scrum.org: Home, acceso: noviembre 10, 2025, [https://www.scrum.org/](https://www.scrum.org/)  
28. Certified Scrum Master Courses \- Xebia Academy, acceso: noviembre 10, 2025, [https://academy.xebia.com/discipline/scrum-master/](https://academy.xebia.com/discipline/scrum-master/)  
29. SRESRE Best Practices for Capacity Management \- Google SRE, acceso: noviembre 10, 2025, [https://sre.google/static/pdf/login\_winter20\_10\_torres.pdf](https://sre.google/static/pdf/login_winter20_10_torres.pdf)  
30. SRE Best Practices for Capacity Management \- Google Research, acceso: noviembre 10, 2025, [https://research.google/pubs/sre-best-practices-for-capacity-management/](https://research.google/pubs/sre-best-practices-for-capacity-management/)  
31. Architecture strategies for capacity planning \- Microsoft Azure Well ..., acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning)  
32. Azure Stack Hub Capacity Planner \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/azure-stack/operator/azure-stack-capacity-planner?view=azs-2501](https://learn.microsoft.com/en-us/azure-stack/operator/azure-stack-capacity-planner?view=azs-2501)  
33. Capacity planning for Azure Stack Hub overview \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/azure-stack/operator/azure-stack-capacity-planning-overview?view=azs-2506](https://learn.microsoft.com/en-us/azure-stack/operator/azure-stack-capacity-planning-overview?view=azs-2506)  
34. Azure SQL Capacity Planning: Overview \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/shows/data-exposed/azure-sql-capacity-planning-overview](https://learn.microsoft.com/en-us/shows/data-exposed/azure-sql-capacity-planning-overview)  
35. Capacity planning guide | Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/microsoft-identity-manager/capacity-planning-guide](https://learn.microsoft.com/en-us/microsoft-identity-manager/capacity-planning-guide)  
36. FinOps \- NobleProg Argentina, acceso: noviembre 10, 2025, [https://www.nobleprog.com.ar/cc/finops](https://www.nobleprog.com.ar/cc/finops)  
37. FinOps para Cloud \- La Guía Definitiva \- Novis, acceso: noviembre 10, 2025, [https://www.noviscorp.com/es/sap/guia-definitiva-de-finops-para-cloud/](https://www.noviscorp.com/es/sap/guia-definitiva-de-finops-para-cloud/)  
38. FinOps documentation \- Cloud Computing \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/cloud-computing/finops/](https://learn.microsoft.com/en-us/cloud-computing/finops/)  
39. ¿Qué es Cloud FinOps? \- Google Cloud, acceso: noviembre 10, 2025, [https://cloud.google.com/learn/what-is-finops?hl=es-419](https://cloud.google.com/learn/what-is-finops?hl=es-419)  
40. FinOps Framework Overview, acceso: noviembre 10, 2025, [https://www.finops.org/framework/](https://www.finops.org/framework/)  
41. FinOps Framework overview \- Cloud Computing \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/cloud-computing/finops/framework/finops-framework](https://learn.microsoft.com/en-us/cloud-computing/finops/framework/finops-framework)  
42. Framework 2025 reflects the addition of Scopes as a core element of the FinOps Framework., acceso: noviembre 10, 2025, [https://www.finops.org/insights/2025-finops-framework/](https://www.finops.org/insights/2025-finops-framework/)  
43. Planning and estimating \- Cloud Computing | Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/cloud-computing/finops/framework/quantify/planning](https://learn.microsoft.com/en-us/cloud-computing/finops/framework/quantify/planning)  
44. Planificación y estimación \- Cloud Computing | Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/es-es/cloud-computing/finops/framework/quantify/planning](https://learn.microsoft.com/es-es/cloud-computing/finops/framework/quantify/planning)  
45. 6 FinOps Principles & Best Practices – GCP, AWS, and Azure \- Economize Cloud, acceso: noviembre 10, 2025, [https://www.economize.cloud/blog/finops-principles/](https://www.economize.cloud/blog/finops-principles/)  
46. Azure DevOps, acceso: noviembre 10, 2025, [https://azure.microsoft.com/en-us/products/devops](https://azure.microsoft.com/en-us/products/devops)  
47. Introducción a la documentación de Azure DevOps \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/es-es/azure/devops/get-started/?view=azure-devops](https://learn.microsoft.com/es-es/azure/devops/get-started/?view=azure-devops)  
48. Microsoft \- It College, acceso: noviembre 10, 2025, [https://www.itcollege.com.ar/microsoft/](https://www.itcollege.com.ar/microsoft/)  
49. Overview of Cost Management \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management)  
50. Estimate costs with the Azure pricing calculator \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/pricing-calculator)  
51. Optimize your cloud investment with Cost Management \- Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices)  
52. FinOps hubs overview \- Cloud Computing | Microsoft Learn, acceso: noviembre 10, 2025, [https://learn.microsoft.com/en-us/cloud-computing/finops/toolkit/hubs/finops-hubs-overview](https://learn.microsoft.com/en-us/cloud-computing/finops/toolkit/hubs/finops-hubs-overview)  
53. Cloud Operations Best Practices and Resource Guide \- CIO Council, acceso: noviembre 10, 2025, [https://www.cio.gov/assets/resources/Cloud%20Operations%20Best%20Practices%20&%20Resources%20Guide%20-%20October%202023.pdf](https://www.cio.gov/assets/resources/Cloud%20Operations%20Best%20Practices%20&%20Resources%20Guide%20-%20October%202023.pdf)  
54. 8 Essential Cloud Governance Best Practices \- Wiz, acceso: noviembre 10, 2025, [https://www.wiz.io/academy/cloud-governance-best-practices](https://www.wiz.io/academy/cloud-governance-best-practices)  
55. Governance \- Cost Optimization Pillar \- AWS Documentation, acceso: noviembre 10, 2025, [https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/governance.html](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/governance.html)  
56. Mastering Cloud Cost Optimization? 15+ Best Practices for 2025 \- CloudZero, acceso: noviembre 10, 2025, [https://www.cloudzero.com/blog/cloud-cost-optimization/](https://www.cloudzero.com/blog/cloud-cost-optimization/)  
57. DevOps, Cloud, and Agile Foundations Professional Certificate \- edX, acceso: noviembre 10, 2025, [https://www.edx.org/certificates/professional-certificate/ibm-devops-cloud-and-agile-foundations](https://www.edx.org/certificates/professional-certificate/ibm-devops-cloud-and-agile-foundations)  
58. IBM DevOps, Cloud, and Agile Foundations | Coursera, acceso: noviembre 10, 2025, [https://www.coursera.org/specializations/devops-cloud-and-agile-foundations](https://www.coursera.org/specializations/devops-cloud-and-agile-foundations)  
59. FinOps Certification and Training, acceso: noviembre 10, 2025, [https://learn.finops.org/](https://learn.finops.org/)  
60. Diplomado Universitario "DevOps Tools Engineer" \- UTN, acceso: noviembre 10, 2025, [https://www.frd.utn.edu.ar/curso/devops-tools-engineer/](https://www.frd.utn.edu.ar/curso/devops-tools-engineer/)