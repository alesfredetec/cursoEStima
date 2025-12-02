import re

# Read the HTML file
with open('C:/tmp/cursoEStima/clase1_profesor.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract slideToSpeechMap array
map_pattern = r'const slideToSpeechMap = \[(.*?)\];'
map_match = re.search(map_pattern, content, re.DOTALL)

if not map_match:
    print("ERROR: No se encontró slideToSpeechMap")
    exit(1)

map_content = map_match.group(1)
# Extract slide keys from map
map_entries = re.findall(r"'(slide\d+)'", map_content)

print("=" * 120)
print("VERIFICACION FINAL: MAPEO HTML -> SPEECH")
print("=" * 120)
print(f"{'Pos':<5} {'HTML Slide':<45} {'Speech Key':<15} {'Speech Title':<50}")
print("-" * 120)

# Extract speech data
speech_pattern = r'(slide\d+):\s*\{\s*title:\s*"([^"]+)"'
speech_matches = re.findall(speech_pattern, content)
speech_dict = {key: title for key, title in speech_matches}

# Extract HTML slide comments
html_pattern = r'<!-- Slide (\d+[a-z]*): ([^>]+) -->'
html_matches = re.findall(html_pattern, content)

# Verify mapping
errors = []
for idx, speech_key in enumerate(map_entries):
    if idx < len(html_matches):
        html_num, html_title = html_matches[idx]
        speech_title = speech_dict.get(speech_key, "NO ENCONTRADO")

        match_status = "OK" if speech_key in speech_dict else "ERROR"

        print(f"{idx:<5} {html_num + ': ' + html_title:<45} {speech_key:<15} {speech_title:<50} {match_status}")

        if speech_key not in speech_dict:
            errors.append(f"Posición {idx}: {speech_key} no existe en speechDataClase1")

print("=" * 120)
print(f"\nRESUMEN:")
print(f"Total entradas en slideToSpeechMap: {len(map_entries)}")
print(f"Total slides HTML encontrados: {len(html_matches)}")
print(f"Total speech scripts: {len(speech_dict)}")

if len(map_entries) != len(html_matches):
    print(f"\n⚠️ WARNING: Mapeo tiene {len(map_entries)} entradas pero HTML tiene {len(html_matches)} slides")
    errors.append(f"Desajuste de cantidad: {len(map_entries)} vs {len(html_matches)}")

# Count unique speech keys used
unique_keys = set(map_entries)
print(f"Speech scripts únicos usados: {len(unique_keys)}")
print(f"Speech scripts disponibles: {len(speech_dict)}")

# Find unused speeches
unused = set(speech_dict.keys()) - unique_keys
if unused:
    print(f"\n⚠️ Speech scripts NO USADOS: {sorted(unused)}")

if errors:
    print(f"\n❌ ERRORES ENCONTRADOS ({len(errors)}):")
    for err in errors:
        print(f"  - {err}")
else:
    print(f"\n✅ MAPEO CORRECTO - Todos los slides tienen speech asignado")

# Detailed breakdown by speech key
print("\n" + "=" * 120)
print("DISTRIBUCIÓN DE SPEECHES:")
print("=" * 120)
from collections import Counter
speech_usage = Counter(map_entries)
for speech_key in sorted(speech_usage.keys(), key=lambda x: int(x.replace('slide', ''))):
    count = speech_usage[speech_key]
    title = speech_dict.get(speech_key, "???")
    positions = [str(i) for i, k in enumerate(map_entries) if k == speech_key]
    positions_str = ", ".join(positions[:5]) + ("..." if len(positions) > 5 else "")
    print(f"{speech_key:<10} usado {count}x en posiciones [{positions_str}] - \"{title}\"")
