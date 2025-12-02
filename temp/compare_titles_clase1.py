import re

# Read the HTML file
with open('C:/tmp/cursoEStima/clase1_profesor.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract HTML slide titles (slides 8-21)
html_slides = {}
html_pattern = r'<!-- Slide (\d+): ([^>]+) -->'
for match in re.finditer(html_pattern, content):
    slide_num = int(match.group(1))
    if 8 <= slide_num <= 21:
        html_slides[slide_num] = match.group(2).strip()

# Extract speech script titles (slide8-slide21)
speech_slides = {}
speech_pattern = r'slide(\d+):\s*\{[^}]*?title:\s*"([^"]+)"'
for match in re.finditer(speech_pattern, content):
    slide_num = int(match.group(1))
    if 8 <= slide_num <= 21:
        speech_slides[slide_num] = match.group(2).strip()

# Create comparison table
print("=" * 100)
print("COMPARACIÓN TÍTULOS: CLASE1_PROFESOR.HTML (Slides 8-21)")
print("=" * 100)
print(f"{'#':<4} {'Título HTML Slide':<50} {'Título Speech Script':<50}")
print("-" * 100)

mismatches = []
for slide_num in range(8, 22):
    html_title = html_slides.get(slide_num, "NO ENCONTRADO")
    speech_title = speech_slides.get(slide_num, "NO ENCONTRADO")

    match_status = "OK" if html_title.lower() == speech_title.lower() else "DESAJUSTE"

    print(f"{slide_num:<4} {html_title:<50} {speech_title:<50} {match_status}")

    if html_title.lower() != speech_title.lower():
        mismatches.append((slide_num, html_title, speech_title))

print("=" * 100)
print(f"\nRESUMEN:")
print(f"Total slides analizados: 14 (slides 8-21)")
print(f"Desajustes encontrados: {len(mismatches)}")
print(f"Coincidencias: {14 - len(mismatches)}")

if mismatches:
    print(f"\nSLIDES CON DESAJUSTE:")
    for slide_num, html_title, speech_title in mismatches:
        print(f"\n  Slide {slide_num}:")
        print(f"    HTML:   {html_title}")
        print(f"    Speech: {speech_title}")
