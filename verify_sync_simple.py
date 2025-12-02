import re

# Read the HTML file
with open('C:/tmp/cursoEStima/clase1_profesor.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract slideToSpeechMap array
map_pattern = r'const slideToSpeechMap = \[(.*?)\];'
map_match = re.search(map_pattern, content, re.DOTALL)
map_entries = re.findall(r"'(slide\w+)'", map_match.group(1))

# Extract speech data
speech_pattern = r'(slide\w+):\s*\{\s*title:\s*"([^"]+)"'
speech_matches = re.findall(speech_pattern, content)
speech_dict = {key: title for key, title in speech_matches}

# Extract HTML slide comments
html_pattern = r'<!-- Slide (\d+[a-z]*): ([^>]+) -->'
html_matches = re.findall(html_pattern, content)

print("=" * 100)
print("VERIFICACION SIMPLIFICADA: Mapeo HTML -> Speech")
print("=" * 100)
print(f"{'Pos':<5} {'HTML':<10} {'Speech Key':<12} {'Speech Title':<50}")
print("-" * 100)

errors = []
for idx in range(min(len(map_entries), len(html_matches))):
    html_num, html_title = html_matches[idx]
    speech_key = map_entries[idx]
    speech_title = speech_dict.get(speech_key, "NO ENCONTRADO")

    status = "OK" if speech_key in speech_dict else "ERROR"

    print(f"{idx:<5} {html_num:<10} {speech_key:<12} {speech_title:<50} {status}")

    if speech_key not in speech_dict:
        errors.append(f"Posicion {idx}: {speech_key} no existe en speechDataClase1")

print("=" * 100)
print(f"\nRESUMEN:")
print(f"Total slides HTML: {len(html_matches)}")
print(f"Total entradas slideToSpeechMap: {len(map_entries)}")
print(f"Total speech scripts: {len(speech_dict)}")

if errors:
    print(f"\nERRORES ({len(errors)}):")
    for err in errors:
        print(f"  - {err}")
else:
    print(f"\nTODO CORRECTO - Todos los slides mapeados correctamente")

# Check specifically for 7b, 7c, 7d
print(f"\n" + "=" * 100)
print("VERIFICACION ESPECIFICA: Slides 7b, 7c, 7d")
print("=" * 100)
for idx in [7, 8, 9]:
    html_num, html_title = html_matches[idx]
    speech_key = map_entries[idx]
    speech_title = speech_dict.get(speech_key, "NO ENCONTRADO")
    print(f"Posicion {idx}: Slide {html_num} '{html_title[:30]}' -> {speech_key} '{speech_title[:40]}'")
