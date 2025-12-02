#!/usr/bin/env python3
"""Update clase3_profesor.html with missing speech scripts and V3 UI"""

import re
from pathlib import Path

def add_missing_speech_scripts(html_content):
    """Add speech scripts for slides 9, 10, and 13"""

    # Speech script for slide 9
    slide9_script = '''            "slide9": {
                        "title": "Buffer de Alimentación (Detalle Visual)",
                        "duration": "2 min",
                        "script": "[VER DIAGRAMA en slide]\\n\\nEste diagrama muestra cómo funciona el Feeding Buffer.\\n\\n[SEÑALAR elementos]\\n\\nCadena NO Crítica (amarilla): Tareas D → E → FB\\nFB protege el punto donde esta cadena se une a la Cadena Crítica.\\n\\nCadena Crítica (azul): Tareas A → B → PB\\n\\n[ÉNFASIS] El FB actúa como \\"colchón\\" entre ambas cadenas. Si D o E se retrasan, el FB absorbe el retraso ANTES de que afecte a la Cadena Crítica.\\n\\n[TRANSICIÓN] Veamos ahora el tercer tipo de buffer..."
            },
            "slide10": {
                        "title": "Buffer de Recursos (Detalle Visual)",
                        "duration": "2 min",
                        "script": "[VER DIAGRAMA en slide]\\n\\nRecuerden: Resource Buffer NO es tiempo, es ALERTA.\\n\\n[LEER elementos del slide]\\n\\n'NO es tiempo adicional' - No suma días al cronograma.\\n'Es una ALERTA' - Notificación anticipada.\\n'Asegura disponibilidad' - El recurso estará listo cuando lo necesites.\\n\\n[EJEMPLO del slide] Si recurso crítico (María) necesita 2 días de aviso, colocamos RB 2 días antes de su tarea.\\n\\n[ÉNFASIS] Esto es coordinación proactiva, no padding reactivo.\\n\\n[TRANSICIÓN] Ahora veamos un diagrama que integra los 3 tipos de buffers..."
            },'''

    # Speech script for slide 13
    slide13_script = '''            "slide13": {
                        "title": "Gráfico de Fiebre (Fever Chart)",
                        "duration": "10 min",
                        "script": "El **Gráfico de Fiebre (Fever Chart)** es la herramienta visual para monitorear el consumo del buffer.\\n\\n[VER GRÁFICO SVG en slide]\\n\\nEje X: % de Progreso del Proyecto (0% a 100%)\\nEje Y: % de Buffer Consumido (0% a 100%)\\n\\n**3 Zonas de Color:**\\n\\n🟢 **VERDE (zona segura):** Buffer consumido es MENOR que progreso del proyecto.\\nEjemplo: 30% progreso, 15% buffer consumido → Todo bien, vamos adelantados.\\n\\n🟡 **AMARILLO (zona precaución):** Buffer consumido es SIMILAR al progreso.\\nEjemplo: 50% progreso, 45% buffer consumido → Ojo, monitorear de cerca.\\n\\n🔴 **ROJO (zona peligro):** Buffer consumido es MAYOR que progreso.\\nEjemplo: 40% progreso, 60% buffer consumido → ALERTA, tomar acción inmediata.\\n\\n**Línea diagonal (45°):** Consumo ideal (buffer se consume proporcionalmente al progreso).\\n\\n**Cómo leer el gráfico:**\\n- Punto DEBAJO de diagonal → Bien (sobra buffer)\\n- Punto SOBRE diagonal → Precaución\\n- Punto MUY ARRIBA de diagonal → Peligro\\n\\n[ÉNFASIS] Este gráfico se actualiza SEMANALMENTE o después de cada tarea completada.\\n\\nPM usa esto para decidir:\\n- Verde: Continuar\\n- Amarillo: Investigar causas\\n- Rojo: Replantear estrategia o avisar a stakeholders\\n\\n[TRANSICIÓN] Ahora que tenemos todas las herramientas de CCPM... hagamos un break antes del taller práctico."
            },'''

    # Find the position to insert slide9 and slide10 (after slide8, before slide11)
    pattern = r'("slide8":\s*\{[^}]+\},)\s*("slide11":)'
    match = re.search(pattern, html_content, re.DOTALL)

    if match:
        # Insert slide9 and slide10
        html_content = html_content[:match.end(1)] + '\n' + slide9_script + '\n' + html_content[match.start(2):]
        print("OK - Added speech scripts for slides 9 and 10")
    else:
        print("ERROR - Could not find insertion point for slides 9-10")

    # Find position to insert slide13 (after slide12, before slide14)
    pattern = r'("slide12":\s*\{[^}]+\},)\s*("slide14":)'
    match = re.search(pattern, html_content, re.DOTALL)

    if match:
        # Insert slide13
        html_content = html_content[:match.end(1)] + '\n' + slide13_script + '\n' + html_content[match.start(2):]
        print("OK - Added speech script for slide 13")
    else:
        print("ERROR - Could not find insertion point for slide 13")

    return html_content

def apply_v3_ui_styles(html_content):
    """Apply V3 minimalist UI styles"""

    # Update .tts-btn styles
    old_tts_btn = r'''\.tts-btn \{
            flex: 1;
            background: rgba\(102, 126, 234, 0\.2\);
            border: 1px solid rgba\(102, 126, 234, 0\.4\);
            color: #ffffff;
            padding: 8px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0\.9rem;
            transition: all 0\.3s ease;
        \}'''

    new_tts_btn = '''.tts-btn {
            flex: 1;
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            padding: 6px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }'''

    if re.search(old_tts_btn, html_content):
        html_content = re.sub(old_tts_btn, new_tts_btn, html_content)
        print("OK - Updated .tts-btn styles")

    # Update .tts-btn:hover
    old_hover = r'''\.tts-btn:hover \{
            background: rgba\(102, 126, 234, 0\.4\);
            transform: translateY\(-1px\);
        \}'''

    new_hover = '''.tts-btn:hover {
            background: rgba(255, 255, 255, 0.05);
            border-color: rgba(255, 255, 255, 0.3);
        }'''

    if re.search(old_hover, html_content):
        html_content = re.sub(old_hover, new_hover, html_content)
        print("OK - Updated .tts-btn:hover styles")

    # Update .tts-btn.active
    old_active = r'''\.tts-btn\.active \{
            background: rgba\(81, 207, 102, 0\.3\);
            border-color: #51cf66;
        \}'''

    new_active = '''.tts-btn.active {
            background: rgba(81, 207, 102, 0.15);
            border-color: #51cf66;
            color: #51cf66;
        }'''

    if re.search(old_active, html_content):
        html_content = re.sub(old_active, new_active, html_content)
        print("OK - Updated .tts-btn.active styles")

    # Update .speed-btn styles
    old_speed = r'''\.speed-btn \{
            flex: 1;
            background: rgba\(118, 75, 162, 0\.2\);
            border: 1px solid rgba\(118, 75, 162, 0\.3\);
            color: #ffffff;
            padding: 6px 8px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0\.85rem;
            transition: all 0\.3s ease;
        \}'''

    new_speed = '''.speed-btn {
            flex: 1;
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: rgba(255, 255, 255, 0.7);
            padding: 4px 6px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.8rem;
            transition: all 0.2s ease;
        }'''

    if re.search(old_speed, html_content):
        html_content = re.sub(old_speed, new_speed, html_content)
        print("OK - Updated .speed-btn styles")

    # Update .speed-btn:hover
    old_speed_hover = r'''\.speed-btn:hover \{
            background: rgba\(118, 75, 162, 0\.4\);
        \}'''

    new_speed_hover = '''.speed-btn:hover {
            background: rgba(255, 255, 255, 0.05);
            color: #ffffff;
        }'''

    if re.search(old_speed_hover, html_content):
        html_content = re.sub(old_speed_hover, new_speed_hover, html_content)
        print("OK - Updated .speed-btn:hover styles")

    # Update .speed-btn.active
    old_speed_active = r'''\.speed-btn\.active \{
            background: rgba\(118, 75, 162, 0\.5\);
            border-color: #764ba2;
            font-weight: 600;
        \}'''

    new_speed_active = '''.speed-btn.active {
            background: rgba(118, 75, 162, 0.2);
            border-color: #764ba2;
            color: #ffffff;
            font-weight: 500;
        }'''

    if re.search(old_speed_active, html_content):
        html_content = re.sub(old_speed_active, new_speed_active, html_content)
        print("OK - Updated .speed-btn.active styles")

    # Add voice selector styles (if not present)
    if '.voice-selector' not in html_content:
        voice_styles = '''
        /* Voice Selector Dropdown */
        .voice-selector {
            width: 100%;
            background: rgba(30, 30, 40, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #ffffff;
            padding: 6px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.85rem;
            margin-bottom: 10px;
            transition: all 0.2s ease;
        }

        .voice-selector:hover {
            background: rgba(30, 30, 40, 0.8);
            border-color: rgba(255, 255, 255, 0.25);
        }

        .voice-selector option {
            background: #1a1a2e;
            color: #ffffff;
            padding: 6px;
        }
'''
        # Insert before /* Toggle Sidebar Button */
        html_content = html_content.replace('        /* Toggle Sidebar Button */', voice_styles + '        /* Toggle Sidebar Button */')
        print("OK - Added .voice-selector styles")

    return html_content

def replace_mode_selector_with_voice_dropdown(html_content):
    """Replace TTS mode selector with voice dropdown"""

    # Find and replace the mode selector div
    old_mode_selector = r'''<!-- TTS Mode Selector -->
                <div class="tts-mode-selector" style="margin-bottom: 10px;">
                    <button class="mode-btn active" id="modeBrowser" onclick="setTTSMode\('browser'\)">🔊 Browser</button>
                    <button class="mode-btn" id="modeOpenAI" onclick="setTTSMode\('openai'\)">🎙️ OpenAI Pro</button>
                </div>'''

    new_voice_selector = '''<select class="voice-selector" id="voiceSelector" onchange="onVoiceChange()">
                    <optgroup label="🔊 Navegador (Gratis)">
                        <option value="browser:es-ES-female">Español España - Mujer</option>
                        <option value="browser:es-ES-male">Español España - Hombre</option>
                        <option value="browser:es-MX-female">Español México - Mujer</option>
                        <option value="browser:es-MX-male">Español México - Hombre</option>
                        <option value="browser:es-AR-female">Español Argentina - Mujer</option>
                    </optgroup>
                    <optgroup label="🎙️ OpenAI Pro (Calidad)">
                        <option value="openai:nova">Nova - Mujer clara</option>
                        <option value="openai:shimmer">Shimmer - Mujer amigable</option>
                        <option value="openai:alloy">Alloy - Neutral profesional</option>
                        <option value="openai:echo">Echo - Hombre autoritativo</option>
                        <option value="openai:fable">Fable - Británico narrativo</option>
                        <option value="openai:onyx">Onyx - Hombre profundo</option>
                    </optgroup>
                </select>'''

    if re.search(old_mode_selector, html_content):
        html_content = re.sub(old_mode_selector, new_voice_selector, html_content)
        print("OK - Replaced mode selector with voice dropdown")
    else:
        print("ERROR - Could not find mode selector to replace")

    # Update button text to icon-only
    html_content = re.sub(r'<button class="tts-btn" id="ttsPlay" onclick="toggleTTS\(\)">▶ Play</button>',
                          '<button class="tts-btn" id="ttsPlay" onclick="toggleTTS()">▶</button>',
                          html_content)

    html_content = re.sub(r'<button class="tts-btn" id="ttsStop" onclick="stopTTS\(\)" disabled>⏹ Stop</button>',
                          '<button class="tts-btn" id="ttsStop" onclick="stopTTS()" disabled>⏹</button>',
                          html_content)

    print("OK - Updated button text to icon-only")

    return html_content

def add_voice_functions(html_content):
    """Add voice selection JavaScript functions"""

    # Check if functions already exist
    if 'function onVoiceChange()' in html_content:
        print("OK - Voice functions already present")
        return html_content

    # Add after the setSpeed function
    voice_functions = '''
        // Voice Selection
        let currentVoice = 'browser:es-ES-female';
        let selectedBrowserVoice = null;
        let selectedOpenAIVoice = 'nova';

        function onVoiceChange() {
            const selector = document.getElementById('voiceSelector');
            currentVoice = selector.value;

            // Parse mode and voice
            const [mode, voice] = currentVoice.split(':');
            ttsMode = mode;

            // Stop current TTS if playing
            if (isSpeaking) {
                stopTTS();
            }

            // Update status
            const statusDiv = document.getElementById('ttsStatus');
            if (mode === 'openai') {
                selectedOpenAIVoice = voice;
                statusDiv.textContent = `✨ OpenAI: ${voice}`;
                statusDiv.style.color = '#667eea';
            } else {
                // Find best matching browser voice
                selectedBrowserVoice = findBrowserVoice(voice);
                statusDiv.textContent = selectedBrowserVoice ?
                    `🔊 ${selectedBrowserVoice.name}` :
                    '🔊 Navegador (gratis)';
                statusDiv.style.color = '#888';
            }
        }

        // Find Browser Voice by preference
        function findBrowserVoice(preference) {
            const voices = speechSynthesis.getVoices();

            // Preference map
            const preferenceMap = {
                'es-ES-female': ['es-ES', 'female', 'mujer'],
                'es-ES-male': ['es-ES', 'male', 'hombre'],
                'es-MX-female': ['es-MX', 'female', 'mujer'],
                'es-MX-male': ['es-MX', 'male', 'hombre'],
                'es-AR-female': ['es-AR', 'female', 'mujer']
            };

            const prefs = preferenceMap[preference] || ['es'];

            // Try to find best match
            for (const voice of voices) {
                const nameLower = voice.name.toLowerCase();
                const langLower = voice.lang.toLowerCase();

                if (prefs.some(p => langLower.includes(p.toLowerCase()) || nameLower.includes(p.toLowerCase()))) {
                    return voice;
                }
            }

            // Fallback to any Spanish voice
            return voices.find(v => v.lang.startsWith('es')) || voices[0];
        }

        // Initialize voices when available
        if (speechSynthesis.onvoiceschanged !== undefined) {
            speechSynthesis.onvoiceschanged = () => {
                onVoiceChange(); // Refresh voice selection
            };
        }
'''

    # Find setSpeed function and add after it
    pattern = r'(function setSpeed\(speed\) \{[^}]+\}\s*\n)'
    match = re.search(pattern, html_content)

    if match:
        html_content = html_content[:match.end()] + voice_functions + html_content[match.end():]
        print("OK - Added voice selection functions")
    else:
        print("ERROR - Could not find setSpeed function to insert voice functions")

    return html_content

def main():
    file_path = Path(r"C:\tmp\cursoEStima\clase3_profesor.html")

    print("=" * 80)
    print("CLASE 3 PROFESOR - V3 UPDATE")
    print("=" * 80)
    print()

    # Read file
    print("Reading clase3_profesor.html...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"  File size: {len(content):,} characters")
    print()

    # Apply updates
    print("Applying updates:")
    print()

    content = add_missing_speech_scripts(content)
    print()

    content = apply_v3_ui_styles(content)
    print()

    content = replace_mode_selector_with_voice_dropdown(content)
    print()

    content = add_voice_functions(content)
    print()

    # Write backup
    backup_path = file_path.with_suffix('.html.backup')
    print(f"Creating backup: {backup_path.name}")
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # Write updated file
    print(f"Writing updated file: {file_path.name}")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print()
    print("=" * 80)
    print("OK - UPDATE COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
