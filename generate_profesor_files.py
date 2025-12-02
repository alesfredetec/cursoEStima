#!/usr/bin/env python3
"""
Generate clase2_profesor.html and clase3_profesor.html
by combining original HTML slides with speech scripts
"""

import re
import json

# OpenAI API Key - Load from environment or config
OPENAI_API_KEY = "your-api-key-here"  # Replace with actual key or load from env

def extract_all_slides_html(html_path):
    """Extract entire slides section from HTML"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find complete slide-container section
    start_marker = '<div class="slide-container">'
    end_marker = '</div>\n\n    <div class="controls">'

    start_pos = content.find(start_marker)
    end_pos = content.find(end_marker)

    if start_pos == -1 or end_pos == -1:
        raise Exception("Could not find slide-container boundaries")

    # Extract including the container div but not the controls
    slides_section = content[start_pos:end_pos + 6]  # +6 for </div>

    return slides_section

def parse_speech_scripts(md_path):
    """Parse speech scripts from markdown file"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all slide sections
    slide_pattern = r'## Slide (\d+):\s*([^\(]+?)\s*\((\d+)\s*min\)(.*?)(?=## Slide \d+:|## ☕ BREAK|## 🎯|$)'
    matches = re.findall(slide_pattern, content, re.DOTALL)

    scripts = {}
    for match in matches:
        slide_num, title, duration, script = match
        slide_key = f"slide{slide_num}"

        # Clean script
        script = script.strip()
        # Remove leading/trailing quotes
        if script.startswith('"'):
            script = script[1:]
        if script.endswith('"'):
            script = script[:-1]
        # Remove extra markdown headers if present
        script = re.sub(r'^---\s*$', '', script, flags=re.MULTILINE)
        script = script.strip()

        scripts[slide_key] = {
            'title': title.strip(),
            'duration': f"{duration} min",
            'script': script
        }

    return scripts

def generate_profesor_html(clase_num, original_html_path, speech_md_path, output_path):
    """Generate profesor HTML file"""

    print(f"Generating {output_path}...")

    # Extract complete slides section from original HTML
    slides_html = extract_all_slides_html(original_html_path)
    print(f"  - Extracted slides section")

    # Parse speech scripts
    scripts = parse_speech_scripts(speech_md_path)
    print(f"  - Parsed {len(scripts)} speech scripts")

    # Read template from clase1_profesor.html
    with open('C:\\tmp\\cursoEStima\\clase1_profesor.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # Find where to replace slides in template
    slides_start = template.find('<div class="slide-container">')
    slides_end = template.find('</div>\n\n            <div class="controls">')

    if slides_start == -1 or slides_end == -1:
        raise Exception("Could not find slide boundaries in template")

    # Split template
    header_template = template[:slides_start]
    footer_template = template[slides_end + 6:]  # +6 for </div>

    # Update title
    if clase_num == 2:
        header_template = header_template.replace(
            'Clase 1: La Crisis de la Estimación (Versión Profesor)',
            'Clase 2: Métodos de Estimación (Versión Profesor)'
        )
    elif clase_num == 3:
        header_template = header_template.replace(
            'Clase 1: La Crisis de la Estimación (Versión Profesor)',
            'Clase 3: Cadena Crítica (CCPM) (Versión Profesor)'
        )

    # Build complete HTML
    html_output = header_template + slides_html + '\n\n            ' + footer_template

    # Replace speech data
    speech_data_var = f"speechDataClase{clase_num}"
    speech_json = json.dumps(scripts, ensure_ascii=False, indent=12)

    # Find and replace the speech data in the JS section
    # Need to find the complete speechDataClase1 object (handles nested braces)
    start_marker = 'const speechDataClase1 = {'
    start_pos = html_output.find(start_marker)

    if start_pos != -1:
        # Count braces to find the end of the object
        depth = 0
        pos = start_pos + len('const speechDataClase1 = ')
        in_string = False
        escape_next = False

        for i in range(pos, len(html_output)):
            char = html_output[i]

            if escape_next:
                escape_next = False
                continue

            if char == '\\':
                escape_next = True
                continue

            if char == '`' and not in_string:
                in_string = True
            elif char == '`' and in_string:
                in_string = False
            elif not in_string:
                if char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                    if depth == 0:
                        end_pos = i + 1
                        # Find the semicolon
                        while end_pos < len(html_output) and html_output[end_pos] in [' ', '\n', ';']:
                            if html_output[end_pos] == ';':
                                end_pos += 1
                                break
                            end_pos += 1

                        # Replace the entire speech data block
                        old_block = html_output[start_pos:end_pos]
                        new_block = f'const {speech_data_var} = {speech_json};'

                        html_output = html_output[:start_pos] + new_block + html_output[end_pos:]
                        break

    # Replace all references to speechDataClase1 with the correct variable
    html_output = html_output.replace('speechDataClase1', speech_data_var)

    # Update API key
    html_output = html_output.replace(
        "const OPENAI_API_KEY = 'sk-proj-",
        f"const OPENAI_API_KEY = '{OPENAI_API_KEY}';\n        // const OPENAI_API_KEY_OLD = 'sk-proj-"
    )

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"  [OK] Generated {output_path}")
    print(f"    - {len(scripts)} speech scripts embedded")
    print()

def main():
    """Generate both profesor HTML files"""
    print("=" * 60)
    print("Generating Profesor HTML Files")
    print("=" * 60)
    print()

    # Generate Clase 2
    generate_profesor_html(
        clase_num=2,
        original_html_path='C:\\tmp\\cursoEStima\\clase2.html',
        speech_md_path='C:\\tmp\\cursoEStima\\materiales_facilitador\\SPEECH_SCRIPTS_CLASE2_COMPLETO.md',
        output_path='C:\\tmp\\cursoEStima\\clase2_profesor.html'
    )

    # Generate Clase 3
    generate_profesor_html(
        clase_num=3,
        original_html_path='C:\\tmp\\cursoEStima\\clase3.html',
        speech_md_path='C:\\tmp\\cursoEStima\\materiales_facilitador\\SPEECH_SCRIPTS_CLASE3_COMPLETO.md',
        output_path='C:\\tmp\\cursoEStima\\clase3_profesor.html'
    )

    print("=" * 60)
    print("[SUCCESS] All profesor files generated successfully!")
    print("=" * 60)

if __name__ == '__main__':
    main()
