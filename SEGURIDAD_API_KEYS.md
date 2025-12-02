# Seguridad de API Keys - Documentación

**Fecha:** 2025-01-02
**Tipo:** Seguridad / Git

---

## ⚠️ PROBLEMA ANTERIOR

Los archivos `*_profesor.html` contenían la API key de OpenAI **hardcodeada** directamente en el código JavaScript:

```javascript
const OPENAI_API_KEY = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
```

**Archivos afectados:**
- `clase1_profesor.html` (línea 2819)
- `clase2_profesor.html` (línea 1789)
- `clase3_profesor.html` (línea 2073)

**Riesgo:**
❌ Al hacer commit a git, la API key quedaba expuesta públicamente
❌ Cualquiera con acceso al repositorio podía usar la key
❌ Posible facturación no autorizada en OpenAI

---

## ✅ SOLUCIÓN IMPLEMENTADA

### 1. Archivo de Configuración Externo

Se crearon 2 archivos nuevos:

#### **config.js** (Contiene la API key real - NO se commitea)
```javascript
// config.js - Configuration for profesor files
// ⚠️ IMPORTANT: This file should be added to .gitignore
// Do NOT commit this file to git repository

const CONFIG = {
    OPENAI_API_KEY: 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
};
```

#### **config.example.js** (Template - SÍ se commitea)
```javascript
// config.example.js - Template for configuration
// Copy this file to config.js and add your actual API key

const CONFIG = {
    OPENAI_API_KEY: 'your-openai-api-key-here'
};
```

### 2. Actualización de .gitignore

Se agregó `config.js` al archivo `.gitignore`:

```gitignore
# Archivos de configuración local
.env
.env.local
config.local.*
config.js          ← AGREGADO
```

**Resultado:** Git ignora `config.js` y NO lo incluye en commits.

### 3. Modificación de los 3 Archivos Profesor

Se realizaron 2 cambios en cada archivo:

#### Cambio 1: Agregar script tag en <head>
```html
</style>
<!-- Load external configuration (API keys, etc.) -->
<script src="config.js"></script>
</head>
```

#### Cambio 2: Reemplazar hardcoded key
**ANTES:**
```javascript
const OPENAI_API_KEY = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
```

**DESPUÉS:**
```javascript
const OPENAI_API_KEY = CONFIG.OPENAI_API_KEY; // Loaded from config.js
```

---

## 📁 ARCHIVOS MODIFICADOS

1. ✅ **clase1_profesor.html**
   - Línea 610: Agregado `<script src="config.js"></script>`
   - Línea 2821: Cambiado a `CONFIG.OPENAI_API_KEY`

2. ✅ **clase2_profesor.html**
   - Línea 610: Agregado `<script src="config.js"></script>`
   - Línea 1791: Cambiado a `CONFIG.OPENAI_API_KEY`

3. ✅ **clase3_profesor.html**
   - Línea 639: Agregado `<script src="config.js"></script>`
   - Línea 2075: Cambiado a `CONFIG.OPENAI_API_KEY`

4. ✅ **.gitignore**
   - Línea 42: Agregado `config.js`

5. ✅ **config.js** (nuevo - NO commitear)
6. ✅ **config.example.js** (nuevo - SÍ commitear)

---

## 🔒 VERIFICACIÓN DE SEGURIDAD

### Antes del commit, verificar:

```bash
# 1. Verificar que config.js NO aparece en staged files
git status

# Debe mostrar:
# modified:   .gitignore
# modified:   clase1_profesor.html
# modified:   clase2_profesor.html
# modified:   clase3_profesor.html
# new file:   config.example.js
#
# NO debe mostrar: config.js

# 2. Verificar contenido de .gitignore
grep "config.js" .gitignore

# Debe mostrar: config.js

# 3. Buscar API keys en archivos staged
git diff --cached | grep "sk-svcacct"

# NO debe mostrar ninguna línea con la API key
```

---

## 🚀 INSTRUCCIONES PARA NUEVOS USUARIOS

Si alguien clona el repositorio:

### 1. Copiar template de configuración
```bash
cp config.example.js config.js
```

### 2. Editar config.js y agregar API key real
```bash
notepad config.js  # Windows
nano config.js     # Linux/Mac
```

Reemplazar `'your-openai-api-key-here'` con la key real de OpenAI.

### 3. Abrir archivos profesor en navegador
Los archivos ahora cargarán la configuración desde `config.js` automáticamente.

---

## ⚡ FUNCIONAMIENTO TÉCNICO

### Orden de Carga:
1. Navegador carga `clase#_profesor.html`
2. En `<head>`, carga `config.js` primero
3. `config.js` define objeto global `CONFIG`
4. Script principal usa `CONFIG.OPENAI_API_KEY`

### Compatibilidad:
✅ Funciona en todos los navegadores modernos
✅ No requiere servidor web (file:// funciona)
✅ No requiere build step ni transpilación

### Fallback (si config.js no existe):
Si un usuario abre el archivo sin crear `config.js`:
- Navegador mostrará error: `CONFIG is not defined`
- TTS con OpenAI no funcionará
- TTS del navegador (browser mode) seguirá funcionando

---

## 📝 NOTAS IMPORTANTES

### Para Desarrollo Local:
- **SIEMPRE** verificar que `config.js` existe antes de abrir archivos profesor
- **NUNCA** hacer commit de `config.js`
- **NUNCA** compartir `config.js` por email, Slack, etc.

### Para Producción / Demo:
- Si necesitas deployar a servidor web, considera usar variables de entorno server-side
- Para demos públicas, usar solo TTS del navegador (no requiere API key)

### Rotación de API Keys:
Si la key se compromete:
1. Rotar key en OpenAI dashboard
2. Actualizar `config.js` local
3. **NO** hacer commit del cambio

---

## ✅ CHECKLIST FINAL

- [x] API key removida de los 3 archivos profesor
- [x] Script tag agregado en los 3 archivos
- [x] config.js creado con key real
- [x] config.example.js creado como template
- [x] .gitignore actualizado
- [x] Verificar que config.js NO está en staged files

---

## 🔗 RECURSOS

- [OpenAI API Keys](https://platform.openai.com/api-keys)
- [Git Secrets](https://github.com/awslabs/git-secrets)
- [Pre-commit hooks](https://pre-commit.com/)

---

**Status:** ✅ **SEGURIDAD IMPLEMENTADA**

Los archivos profesor ahora están listos para commit sin exponer la API key.
