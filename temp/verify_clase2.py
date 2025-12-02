import re

# Read clase2_profesor.html
with open('C:/tmp/cursoEStima/clase2_profesor.html', 'r', encoding='utf-8') as f:
    profesor_content = f.read()

# Extract HTML slides
html_pattern = r'<!-- Slide (\d+): ([^>]+) -->'
html_matches = re.findall(html_pattern, profesor_content)

print("=" * 100)
print("VERIFICACION CLASE2_PROFESOR.HTML")
print("=" * 100)

print(f"\nTotal slides HTML: {len(html_matches)}")

# Extract speech data with different pattern (JSON-like format)
speech_pattern = r'"slide(\d+)":\s*\{\s*"title":\s*"([^"]+)"'
speech_matches = re.findall(speech_pattern, profesor_content)

print(f"Total speech scripts encontrados: {len(speech_matches)}")

# Create dictionaries
html_dict = {int(num): title for num, title in html_matches}
speech_dict = {int(num): title for num, title in speech_matches}

# Verify mapping
print("\n" + "=" * 100)
print("MAPEO: HTML Slide -> Speech")
print("=" * 100)
print(f"{'Pos':<5} {'HTML#':<7} {'HTML Title':<45} {'Speech':<10} {'Speech Title':<45} {'Status':<10}")
print("-" * 100)

errors = []
for i in range(1, len(html_matches) + 1):
    html_title = html_dict.get(i, "NO ENCONTRADO")
    speech_num = i  # Formula: slide${currentSlide + 1}
    speech_title = speech_dict.get(speech_num, "NO ENCONTRADO")

    status = "OK" if speech_num in speech_dict else "FALTA"

    if len(html_title) > 45:
        html_title = html_title[:42] + "..."
    if len(speech_title) > 45:
        speech_title = speech_title[:42] + "..."

    print(f"{i-1:<5} {i:<7} {html_title:<45} slide{speech_num:<5} {speech_title:<45} {status:<10}")

    if speech_num not in speech_dict:
        errors.append(f"Slide {i}: Speech slide{speech_num} no existe")

print("=" * 100)

# Check if slideToSpeechMap exists
has_map = 'slideToSpeechMap' in profesor_content
print(f"\nTiene slideToSpeechMap: {'SI' if has_map else 'NO (usa formula currentSlide + 1)'}")

# Check formula usage
formula_pattern = r'slideKey\s*=\s*`slide\$\{currentSlide \+ 1\}`'
uses_formula = bool(re.search(formula_pattern, profesor_content))
print(f"Usa formula currentSlide + 1: {'SI' if uses_formula else 'NO'}")

print("\n" + "=" * 100)
print("RESUMEN")
print("=" * 100)

if errors:
    print(f"\nERRORES ({len(errors)}):")
    for err in errors:
        print(f"  - {err}")
else:
    print("\nTODO CORRECTO - Todos los slides tienen speech")

print(f"\nTotal slides: {len(html_matches)}")
print(f"Total speeches: {len(speech_matches)}")
print(f"Desajustes: {len(errors)}")

# Verify speech durations
print("\n" + "=" * 100)
print("DURACION DE SPEECHES")
print("=" * 100)

duration_pattern = r'"slide\d+":\s*\{\s*"title":[^}]+?"duration":\s*"([^"]+)"'
durations = re.findall(duration_pattern, profesor_content)

total_min = 0
for i, dur in enumerate(durations, 1):
    # Extract number from "X min"
    match = re.search(r'(\d+)', dur)
    if match:
        mins = int(match.group(1))
        total_min += mins
        print(f"Slide {i}: {dur}")

print(f"\nDuracion total speeches: {total_min} minutos ({total_min/60:.1f} horas)")
print(f"Duracion objetivo clase 2: 180 minutos (3 horas)")

if total_min < 180:
    print(f"Margen disponible: {180 - total_min} min para interaccion")
elif total_min > 180:
    print(f"ADVERTENCIA: Excede por {total_min - 180} min")
