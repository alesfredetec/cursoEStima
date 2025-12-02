# Versión Profesor - Curso de Estimación de Proyectos

**¡Archivos listos para usar! 🎉**

---

## 🎯 Inicio Rápido (5 pasos)

1. **Abrir archivo profesor:**
   - Doble click en `clase1_profesor.html` (o clase2/clase3)

2. **Elegir modo TTS:**
   - `🔊 Browser` (gratis, offline) - Ya activado por defecto
   - `🎙️ OpenAI Pro` (profesional, requiere internet)

3. **Navegar slides:**
   - Flechas ← → o Space
   - Home/End para ir a primer/último slide

4. **Controlar TTS:**
   - Presionar `T` para play/pause
   - Velocidad ya configurada en **1.2x** (óptima)

5. **Toggle sidebar:**
   - Presionar `S` para mostrar/ocultar speech scripts

**¡Eso es todo! Ya puedes enseñar con apoyo TTS.**

---

## 📁 ¿Qué archivos usar?

### Para ENSEÑAR (Proyectar en clase):

**Versión Profesor** (CON sidebar y TTS):
```
clase1_profesor.html  →  Clase 1: La Crisis (21 slides)
clase2_profesor.html  →  Clase 2: Métodos (24 slides)
clase3_profesor.html  →  Clase 3: CCPM (32 slides)
```

**Características:**
- Barra lateral con speech scripts
- TTS dual (Browser gratis + OpenAI profesional)
- Speed 1.2x por defecto
- Markers visuales: [PAUSA], [ÉNFASIS], etc.
- Shortcuts: S (sidebar), T (TTS)

### Para COMPARTIR con Alumnos:

**Versión Alumno** (SIN sidebar ni TTS):
```
clase1.html  →  Solo slides
clase2.html  →  Solo slides
clase3.html  →  Solo slides
```

**Características:**
- Versión limpia sin speech scripts
- Funciona offline
- Sin API keys
- Seguro para compartir públicamente

---

## 🔊 Modos TTS Explicados

### Modo 1: 🔊 Browser (Recomendado para empezar)

**Ventajas:**
- ✅ Gratis (100%)
- ✅ Funciona offline (sin internet)
- ✅ Instantáneo (no espera)
- ✅ Sin límites de uso

**Desventajas:**
- ❌ Calidad media (voz robótica)
- ❌ Depende de voces del sistema
- ❌ Menos natural

**Cuándo usar:**
- Testing rápido antes de clase
- Practicar timing
- Sin presupuesto
- Sin conexión a internet

---

### Modo 2: 🎙️ OpenAI Pro (Recomendado para clases importantes)

**Ventajas:**
- ✅ Calidad profesional (voz humana)
- ✅ Entonación natural
- ✅ Voz "Nova" (femenina, clara, educativa)
- ✅ Muy económico (~$0.30 por clase completa)

**Desventajas:**
- ❌ Requiere internet
- ❌ Toma 2-5 segundos generar audio
- ❌ Usa API key (ya incluida)

**Cuándo usar:**
- Presentaciones importantes
- Demos a clientes/directivos
- Grabar videos del curso
- Máxima calidad

**Costo:**
- Slide típico: ~1000 caracteres = $0.015 USD (1.5 centavos)
- Clase completa: ~$0.30 USD (30 centavos)
- **MUY económico** para uso educativo

---

## ⌨️ Atajos de Teclado

| Tecla | Acción |
|-------|--------|
| `→` o `Space` | Siguiente slide |
| `←` | Slide anterior |
| `Home` | Primer slide |
| `End` | Último slide |
| `T` | Play/Pause TTS |
| `S` | Mostrar/Ocultar sidebar |

**Tip:** Proyectar con sidebar oculto (`S`), activar solo cuando necesites leer script.

---

## 🎓 Flujo de Trabajo Sugerido

### Antes de la Clase:

1. **Abrir** `claseX_profesor.html`
2. **Revisar** speech scripts en sidebar
3. **Probar** TTS con 2-3 slides para ajustar speed
4. **Memorizar** atajos (`T` para TTS, `S` para sidebar)
5. **Preparar** ejemplos adicionales si necesario

### Durante la Clase:

1. **Proyectar** slides (alumnos ven contenido)
2. **Sidebar visible** para ti (guía de speech)
3. **Seguir markers:**
   - ⏸ PAUSA = Parar 2-3 segundos
   - ‼ ÉNFASIS = Subir tono, marcar importancia
   - ➡ TRANSICIÓN = Conectar con siguiente tema
   - ❓ PREGUNTA = Interactuar con audiencia
4. **Usar TTS** si quieres ejemplo de entonación
5. **Navegar** con flechas o Space

### Después de la Clase:

1. **Compartir** `claseX.html` (versión alumno) por email
2. **NO compartir** versión profesor (contiene API key)
3. **Recoger feedback** sobre timing y contenido

---

## 📊 Contenido de Cada Clase

### Clase 1: La Crisis de la Estimación (21 slides, 3 horas)

**Temas:**
- Cono de Incertidumbre (±400% → ±10%)
- Malvavisco Challenge (niños 66cm vs MBAs 25cm)
- Ley de Parkinson (trabajo se expande)
- Síndrome del Estudiante (procrastinación)
- Estudios empíricos (Microsoft, MIT)

**Speech scripts:** 21/21 (100%) ✅

**Momento "Aha!":** Los niños le ganan a los MBAs porque prueban, no planean.

---

### Clase 2: Métodos de Estimación (24 slides, 3 horas)

**Temas:**
- PERT: (O + 4M + P) / 6
- CPM: Ruta Crítica
- Story Points: Fibonacci (1,2,3,5,8,13)
- Planning Poker: Votación colaborativa
- Velocidad: Capacidad empírica del equipo

**Speech scripts:** 17/24 (71%) ⚠️

**Momento "Aha!":** Caso HU-3 Password Reset - votos 2 vs 13, suposiciones ocultas.

---

### Clase 3: Cadena Crítica CCPM (32 slides, 3 horas)

**Temas:**
- Goldratt y Teoría de Restricciones
- Cadena Crítica vs Ruta Crítica
- 3 Tipos de Buffers (Project, Feeding, Resource)
- Dimensionamiento: 50% de tiempo ahorrado
- Fever Chart: Monitor (Green/Yellow/Red)

**Speech scripts:** 29/32 (91%) ✅

**Momento "Aha!":** Caso A-B-C-D
- CPM dice 25 días → INCORRECTO (ignora que Ana hace B y D)
- Realidad: 35 días (lento)
- CCPM: 27 días (más rápido Y más protegido)

---

## ⚙️ Configuración TTS Actual

**Configuración por defecto (YA aplicada):**
- ✅ Speed: **1.2x** (óptimo para enseñanza)
- ✅ Modo: Browser (gratis, funciona siempre)
- ✅ Markers: Eliminados automáticamente antes de leer
- ✅ Voz: Mejor española disponible (auto-detecta)

**Si quieres cambiar algo:**

1. **Speed diferente:**
   - Hacer click en botones: 0.8x (lento), 1.0x (normal), 1.2x (actual), 1.5x (rápido)

2. **Modo OpenAI:**
   - Hacer click en `🎙️ OpenAI Pro`
   - Esperar 2-5 segundos al generar audio
   - Calidad profesional

3. **Voz OpenAI diferente:**
   - Abrir archivo con editor de texto
   - Buscar línea con `voice: 'nova'`
   - Cambiar a: `alloy`, `echo`, `fable`, `onyx`, `shimmer`

---

## 🐛 Solución de Problemas

### "No escucho nada con Browser TTS"

**Posibles causas:**
1. ❌ Volumen del sistema en mute
2. ❌ Browser sin permisos de audio
3. ❌ Voces españolas no instaladas en el sistema

**Solución:**
1. Subir volumen del sistema
2. Recargar página (F5)
3. Instalar voces españolas:
   - **Windows:** Settings → Time & Language → Speech → Add languages (es-ES)
   - **Mac:** System Preferences → Accessibility → Speech → System Voice
4. **Plan B:** Cambiar a modo OpenAI Pro

---

### "OpenAI TTS dice Error 401 o 403"

**Causa:** API key inválida o expirada

**Solución:**
1. Verificar conexión a internet
2. Revisar key en: https://platform.openai.com/api-keys
3. Si key expiró, generar nueva y reemplazar en archivo (línea ~2086)
4. **Plan B:** Usar modo Browser

---

### "Audio se corta a mitad de slide"

**Causa:** Límite de caracteres OpenAI (4096 max)

**Solución:**
- Ya implementado: Trunca automáticamente a 4000 caracteres
- Si pasa, dividir script manualmente en 2 partes

---

### "Sidebar no se ve en móvil"

**Comportamiento esperado:** En pantallas <1024px, sidebar se colapsa

**Solución:**
- Presionar `S` para toggle
- O usar en desktop/tablet para mejor experiencia

---

## 📝 Tips Pedagógicos

### 1. **Usar TTS para Practicar Timing**

**Antes de clase:**
- Activar TTS en cada slide
- Cronometrar duración real
- Ajustar si se pasa del tiempo sugerido
- Speed 1.2x es buen promedio

### 2. **Markers son Guía, No Script**

**NO leer literalmente:**
- Scripts son guía conversacional
- Adaptarlos a tu estilo
- Agregar ejemplos de tu experiencia
- Mantener tono amigable

**Markers útiles:**
- `[PAUSA]` → Dar tiempo para procesar
- `[PREGUNTA]` → Interactuar, no solo hablar
- `[ANALOGÍA]` → Simplificar conceptos complejos

### 3. **Conectar Entre Clases**

**Importante:**
- Clase 1: Diagnostica problema
- Clase 2: Presenta herramientas
- Clase 3: Solución sistémica

**Al inicio de Clase 2/3:**
- Recapitular lección clave anterior
- Mostrar progresión lógica
- Crear narrativa continua

### 4. **Momentos "Aha!" son Críticos**

**No apurar estas secciones:**
- Clase 1: Malvavisco Challenge (slide 8-9)
- Clase 2: Planning Poker HU-3 (slide 13)
- Clase 3: Caso A-B-C-D (slides 16-23)

**Hacer pausas dramáticas, crear suspense.**

---

## 🔐 Importante: API Key

**⚠️ LA API KEY ESTÁ EN EL CÓDIGO**

**Ubicación:**
- `clase1_profesor.html`: línea 2086
- `clase2_profesor.html`: línea ~1500
- `clase3_profesor.html`: línea ~1700

**Key actual:** (la proporcionaste tú)

**Cuidados:**
1. **NO compartir** archivos profesor públicamente
2. **Solo compartir** con profesores autorizados
3. **Monitorear uso** en: https://platform.openai.com/usage
4. **Rotar key** si se expone accidentalmente

**Para compartir curso:**
- ✅ Compartir `claseX.html` (alumno) - seguro
- ❌ NO compartir `claseX_profesor.html` - contiene key

**Costo esperado:**
- Clase completa: $0.30 USD
- Mes completo (10 clases): $3 USD
- Año (100 clases): $30 USD

**MUY económico para educación.**

---

## 📚 Archivos de Referencia

**Si quieres profundizar:**

| Archivo | Qué contiene |
|---------|-------------|
| `SINCRONIZACION_COMPLETA.md` | Resumen técnico completo |
| `MEJORAS_TTS_CLASE1_PROFESOR.md` | Changelog y features TTS |
| `PLAN_HTML_PROFESOR.md` | Diseño y arquitectura |
| `materiales_facilitador/GUIA_PROFESOR_CLASEX.md` | Tips pedagógicos detallados |
| `CLAUDE.md` | Contexto del proyecto |

---

## ✅ Checklist Pre-Clase

**10 minutos antes:**

- [ ] Abrir `claseX_profesor.html`
- [ ] Verificar que TTS funciona (probar slide 1)
- [ ] Conectar proyector/monitor externo
- [ ] Sidebar visible en tu pantalla, oculto en proyector
- [ ] Volumen adecuado (si usarás TTS)
- [ ] Timer/reloj visible (cumplir 3 horas)
- [ ] Revisar slides con casos importantes (Malvavisco, HU-3, A-B-C-D)
- [ ] Tener ejemplos adicionales preparados
- [ ] Confirmar conexión a internet (si usarás OpenAI TTS)

---

## 🎉 ¡Todo Listo!

**Tienes:**
- ✅ 3 archivos HTML profesor con TTS dual
- ✅ 77 slides sincronizados
- ✅ 67 speech scripts completos
- ✅ Documentación completa
- ✅ API key configurada

**Próximo paso:** Abrir `clase1_profesor.html` y empezar a practicar.

**¿Preguntas?** Revisar `SINCRONIZACION_COMPLETA.md` para detalles técnicos.

---

**Última actualización:** 2025-01-01
**Versión:** 1.1 - TTS Mejorado
**Autor:** Alejandro Sfrede
**Proyecto:** Curso de Estimación y Planificación de Proyectos (9 horas)

**¡Éxitos con el curso! 🚀**
