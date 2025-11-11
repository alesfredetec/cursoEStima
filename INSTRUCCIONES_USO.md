# Instrucciones de Uso - Curso de Estimación de Proyectos

## 📦 Material Generado

### Presentaciones HTML Interactivas

**Portal Principal:**
- `index.html` - Página de inicio con navegación a las 3 clases

**Clases:**
- `clase1.html` - La Crisis de la Estimación (21 slides, 3 horas)
- `clase2.html` - Métodos de Estimación (24 slides, 3 horas)
- `clase3.html` - Cadena Crítica CCPM (32 slides, 3 horas)

**Documentación:**
- `RESUMEN_CURSO.md` - Resumen ejecutivo completo del curso
- `CLAUDE.md` - Guía para futuras instancias de Claude Code
- `readme.md` - Documento original del curso

---

## 🚀 Cómo Usar las Presentaciones

### Opción 1: Abrir Directamente en el Navegador

1. Navega a la carpeta `C:\tmp\cursoEStima`
2. Haz doble clic en `index.html`
3. Tu navegador abrirá el portal principal
4. Haz clic en la clase que desees impartir

### Opción 2: Usar un Servidor Local (Recomendado)

Si tienes Python instalado:

```bash
cd C:\tmp\cursoEStima
python -m http.server 8000
```

Luego abre en tu navegador: `http://localhost:8000`

**Ventaja:** Evita problemas de CORS y permite mejor renderizado.

---

## ⌨️ Controles de Navegación

### Durante la Presentación:

**Teclado:**
- `→` o `Espacio` - Slide siguiente
- `←` - Slide anterior
- `Home` - Ir al inicio
- `End` - Ir al final

**Mouse:**
- Clic en botones "Anterior" / "Siguiente" en la parte inferior
- Clic en "🏠 Portal" (esquina superior derecha) para volver al inicio

**Táctil (Móviles/Tablets):**
- Desliza izquierda → Siguiente slide
- Desliza derecha → Slide anterior

**Indicadores:**
- Barra de progreso (arriba)
- Contador de slides (abajo derecha): "5 / 21"
- Información del instructor (arriba izquierda)

---

## 📚 Estructura de las Clases

### Clase 1: La Crisis de la Estimación (3 horas) - **FORMATO REMOTO**

**Contenido:**
1. Introducción al problema (30 min)
2. Cono de Incertidumbre con gráfico visual (45 min)
3. Factores de estimación y clasificación de riesgos (30 min)
4. Investigación del Desafío del Malvavisco - Análisis teórico (30 min)
5. ☕ Break (15 min)
6. Factores Psicológicos: Parkinson y Estudiante (35 min)
7. Estudios de Caso y Evidencia Empírica (25 min)

**Materiales Necesarios:**
- ✅ **Ninguno** - Completamente teórico y adaptado para entrega remota
- Includes gráficos visuales integrados:
  - Gráfico del Cono de Incertidumbre (SVG interactivo)
  - Matriz de Riesgos Probabilidad vs Impacto
  - Tablas de clasificación de factores

### Clase 2: Métodos de Estimación (3 horas) - **FORMATO REMOTO**

**Contenido:**
1. PERT y CPM (45 min)
2. Estimación Ágil (45 min)
3. ☕ Break (15 min)
4. Planning Poker: Demostración y Análisis Detallado (60 min)
5. Velocidad, Refinamiento Progresivo y Mejores Prácticas (30 min)
6. Síntesis y Cuadro Comparativo (15 min)

**Materiales Necesarios:**
- ✅ **Ninguno** - Planning Poker presentado como caso de estudio teórico
- Backlog de 5 historias de usuario (incluido en slides para análisis)
- Demostración paso a paso del proceso (no requiere participación grupal)

### Clase 3: Cadena Crítica CCPM (3 horas) - **FORMATO REMOTO**

**Contenido:**
1. Introducción a CCPM y Teoría de Restricciones (45 min)
2. Gestión de Buffers: Proyecto, Alimentación, Recursos (45 min)
3. ☕ Break (15 min)
4. Caso A-B-C-D: Walkthrough Teórico Guiado (75 min)
5. Síntesis Final y Cuadro Comparativo (15 min)

**Materiales Necesarios:**
- ✅ **Ninguno** - Caso presentado como demostración paso a paso
- Gráficos visuales integrados:
  - **Diagrama completo de los 3 tipos de Buffers** (SVG interactivo)
  - **Fever Chart (Gráfico de Fiebre)** con zonas de riesgo y ejemplo de proyecto
  - Calculadoras online (si los participantes quieren seguir los cálculos)

---

## 🎨 Diseño Visual

### Tema Oscuro Profesional

- **Fondo:** `#0a0a0a` (negro)
- **Acentos:** Gradientes púrpura/azul (`#667eea` → `#764ba2`)
- **Glass-morphism:** Efectos de vidrio esmerilado en tarjetas
- **Tipografía:** Fuentes del sistema (San Francisco, Segoe UI, Roboto)
- **Animaciones:** Transiciones suaves entre slides

### Elementos Visuales

- ✅ Boxes de colores para diferentes tipos de información
- 📊 Tablas comparativas con fondo semi-transparente
- 🎯 Workshops resaltados con bordes especiales
- 📐 Diagramas visuales para cadenas críticas
- 🔢 Fórmulas en cajas destacadas con fuente monospace

---

## 🎓 Consejos para Facilitadores - **FORMATO REMOTO**

### Antes del Curso

1. **Revisa el material:**
   - Lee `RESUMEN_CURSO.md` completamente
   - Practica con las presentaciones (navega todos los slides)
   - ✅ **NO se requieren materiales físicos** - Todo es teórico

2. **Prepara el ambiente remoto:**
   - Plataforma de videoconferencia configurada (Zoom, Teams, Meet)
   - Comparte pantalla con las presentaciones HTML
   - Micrófono y cámara funcionando
   - Conexión a internet estable

3. **Materiales digitales:**
   - ✅ Todas las presentaciones están autocontenidas
   - ✅ Gráficos visuales incluidos (SVG en slides)
   - ✅ Casos de estudio presentados teóricamente

### Durante el Curso

1. **Interactividad remota:**
   - Las slides incluyen preguntas para discusión en grupo
   - Usa chat para preguntas asíncronas
   - Habilita micrófono para participación verbal
   - Los análisis de casos reemplazan los workshops hands-on

2. **Timing:**
   - Cada slide tiene notas de duración en el resumen
   - Los breaks están marcados explícitamente (importante en remoto)
   - Ajusta según el ritmo de tu grupo
   - Considera 5 min adicionales por clase para Q&A remoto

3. **Facilitación de Contenido Teórico:**
   - **Investigación Malvavisco:** Explica los datos de Tom Wujec, pregunta si alguien tiene experiencias similares
   - **Estudios de Parkinson:** Conecta con experiencias reales de los participantes
   - **Planning Poker Demo:** Presenta el caso paso a paso, invita a que calculen mentalmente
   - **Caso A-B-C-D:** Guía paso a paso, usa pizarra virtual si es posible, asegura el momento "aha!"

### Después del Curso

1. **Seguimiento:**
   - Comparte las presentaciones HTML con participantes
   - Envía material adicional de `doc/adminpro/`
   - Programa sesión de Q&A opcional

2. **Mejora Continua:**
   - Recolecta feedback de participantes
   - Ajusta timing según experiencia
   - Adapta ejemplos a la industria del grupo

---

## 📱 Compatibilidad

### Navegadores Soportados

- ✅ Chrome/Edge (Chromium) - Recomendado
- ✅ Firefox
- ✅ Safari (macOS/iOS)
- ✅ Opera

### Dispositivos

- 💻 **Desktop:** Experiencia completa (recomendado para presentar)
- 📱 **Tablets:** Funcional con navegación táctil
- 📱 **Móviles:** Optimizado responsive (estudiantes pueden seguir)

---

## 🔧 Personalización

### Cambiar Información del Instructor

Edita en cada archivo HTML (`clase1.html`, `clase2.html`, `clase3.html`):

```html
<div class="instructor-info">
    <strong>Tu Nombre</strong> - Tu Área/Empresa
</div>
```

Y al final de cada clase:

```html
<p style="font-size: 1.4rem; margin-top: 40px;">
    <strong style="color: #667eea;">Tu Nombre</strong><br>
    Tu Área/Empresa
</p>
```

### Cambiar Colores

En la sección `<style>` de cada HTML, busca:

```css
background: linear-gradient(135deg, #667eea, #764ba2);
```

Reemplaza `#667eea` (azul) y `#764ba2` (púrpura) con tus colores.

### Agregar/Modificar Slides

Copia el bloque de una slide existente:

```html
<div class="slide">
    <div class="slide-content">
        <h2>Tu Título</h2>
        <p>Tu contenido...</p>
    </div>
</div>
```

Y modifica el contenido. El sistema de navegación se ajusta automáticamente.

---

## 📖 Documentación de Apoyo

### Para Profundizar

- **Clase 1:** `Diseño de Curso de Estimación de Proyectos.md`
- **Clase 2:** `doc/adminpro/Introduccion a SCRUM v1.pdf`
- **Clase 3:** `doc/adminpro/09_Critical_Chain.pdf`, `CCPMv6.ppt`

### Plantillas de Estimación

- `EstimacionModuloContabilidad.xls` - Ejemplo real de estimación
- `PlanillaEstimacion Workflow.xls` - Template PERT/CCPM

### Caso de Estudio

- `Analisis_Detallado_Proyecto_por_Proyecto_Fintexa.md` - 135+ microservicios
- `Analisis_Configuraciones_Ecosistema_Fintexa.md` - Infraestructura

---

## ⚠️ Solución de Problemas

### Las presentaciones no se ven correctamente

**Problema:** Estilos no cargan o layout roto
**Solución:**
- Usa un servidor local (Python HTTP server)
- Prueba en otro navegador
- Verifica que los archivos HTML no estén corruptos

### Los talleres toman más tiempo del estimado

**Problema:** Se pasa del tiempo asignado
**Solución:**
- Está OK, es normal en grupos grandes
- Prioriza el debriefing sobre terminar todos los slides
- Salta slides teóricos si es necesario (nunca saltes workshops)

### Los participantes no entienden CCPM

**Problema:** Conceptos muy abstractos
**Solución:**
- Enfatiza el caso A-B-C-D (es el momento clave)
- Usa diagramas en pizarra/papel físico
- Conecta con experiencias reales del grupo

---

## 📧 Soporte

**Para consultas sobre el contenido:**
- Revisa `RESUMEN_CURSO.md` (contiene toda la estructura)
- Consulta los PDFs en `doc/adminpro/` (teoría profunda)

**Para modificaciones técnicas:**
- Los archivos HTML son standalone (todo incluido)
- CSS está embebido en `<style>` de cada archivo
- JavaScript está embebido al final de cada archivo

---

## 📜 Licencia y Uso

Este material fue generado para fines educativos.

**Puedes:**
- ✅ Usar en cursos internos de tu empresa
- ✅ Modificar para adaptar a tu contexto
- ✅ Compartir con colegas y estudiantes

**Por favor:**
- 📌 Mantén créditos del material original
- 📌 Comparte mejoras con la comunidad
- 📌 Usa con fines educativos, no comerciales

---

## 🎯 Objetivos de Aprendizaje

Al completar este curso, los participantes podrán:

✅ Explicar por qué las estimaciones tradicionales fallan sistemáticamente
✅ Aplicar el Cono de Incertidumbre para adaptar el enfoque según la fase
✅ Identificar y mitigar factores psicológicos (Parkinson, Estudiante)
✅ Calcular estimaciones con PERT (3 puntos)
✅ Facilitar sesiones de Planning Poker
✅ Usar Story Points y calcular Velocidad
✅ Diferenciar Ruta Crítica (CPM) de Cadena Crítica (CCPM)
✅ Dimensionar y gestionar Buffers de Proyecto
✅ Monitorear proyectos con Gráfico de Fiebre
✅ Seleccionar el método apropiado según el contexto

---

## 🚀 ¡Listo para Enseñar!

1. Abre `index.html` en tu navegador
2. Navega las presentaciones
3. Prepara materiales físicos para talleres
4. Lee `RESUMEN_CURSO.md` una vez más
5. **¡A enseñar!**

---

**Instructor:** Alejandro Sfrede - Área de Arquitectura
**Versión:** 1.0 - Enero 2025
**Duración Total:** 9 horas (3 clases × 3 horas)
