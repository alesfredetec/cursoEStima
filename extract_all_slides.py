import re

# Read the HTML file
with open('C:/tmp/cursoEStima/clase1_profesor.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract ALL HTML slides with their h2 titles
print("=" * 120)
print("TODOS LOS SLIDES HTML EN CLASE1_PROFESOR.HTML")
print("=" * 120)
print(f"{'#':<6} {'Comentario HTML':<50} {'Titulo <h2> en Contenido':<60}")
print("-" * 120)

# Find all slide sections
slide_pattern = r'<!-- Slide (\d+[a-z]*): ([^>]+) -->.*?<div class="slide">.*?<h2>([^<]+)</h2>'
matches = re.finditer(slide_pattern, content, re.DOTALL)

slide_data = []
for match in matches:
    slide_num = match.group(1)
    comment_title = match.group(2).strip()
    h2_title = match.group(3).strip()

    # Clean h2 title from emoji and extra spaces
    h2_clean = re.sub(r'[^\w\s:,\-áéíóúÁÉÍÓÚñÑ]', '', h2_title).strip()

    slide_data.append((slide_num, comment_title, h2_clean))
    print(f"{slide_num:<6} {comment_title:<50} {h2_clean:<60}")

print("=" * 120)
print(f"\nTotal slides HTML encontrados: {len(slide_data)}")

# Now extract speech scripts
print("\n" + "=" * 120)
print("TODOS LOS SPEECH SCRIPTS EN speechDataClase1")
print("=" * 120)
print(f"{'Key':<12} {'Title':<50} {'Duration':<15}")
print("-" * 120)

speech_pattern = r'(slide\d+):\s*\{\s*title:\s*"([^"]+)",\s*duration:\s*"([^"]+)"'
speech_matches = re.finditer(speech_pattern, content)

speech_data = []
for match in speech_matches:
    key = match.group(1)
    title = match.group(2).strip()
    duration = match.group(3).strip()

    speech_data.append((key, title, duration))
    print(f"{key:<12} {title:<50} {duration:<15}")

print("=" * 120)
print(f"\nTotal speech scripts encontrados: {len(speech_data)}")

# Create mapping
print("\n" + "=" * 120)
print("MAPEO: POSICION EN NAVEGACION -> HTML SLIDE -> SPEECH SCRIPT")
print("=" * 120)
print(f"{'Pos':<5} {'HTML #':<8} {'HTML Title (h2)':<45} {'Speech':<12} {'Speech Title':<45} {'Match':<10}")
print("-" * 120)

# The navigation position should map to speechDataClase1 keys
mismatches = []
for i, (html_num, html_comment, html_h2) in enumerate(slide_data):
    nav_position = i + 1  # Navigation is 1-indexed

    # Determine which speech script should be used
    # Slides 7b, 7c, 7d should use speech slide7
    if html_num in ['7b', '7c', '7d']:
        expected_speech_key = 'slide7'
    else:
        # Convert html_num to integer for mapping
        try:
            html_int = int(html_num)
            expected_speech_key = f'slide{html_int}'
        except:
            expected_speech_key = f'slide{html_num}'

    # Find the corresponding speech
    speech_title = "NO ENCONTRADO"
    for key, title, dur in speech_data:
        if key == expected_speech_key:
            speech_title = title
            break

    # Check match
    html_h2_lower = html_h2.lower()
    speech_title_lower = speech_title.lower()

    # Fuzzy match (contains or very similar)
    if speech_title == "NO ENCONTRADO":
        match_status = "FALTA"
    elif html_h2_lower in speech_title_lower or speech_title_lower in html_h2_lower:
        match_status = "OK"
    elif len(html_h2_lower) > 10 and len(speech_title_lower) > 10:
        # Check word overlap
        html_words = set(html_h2_lower.split())
        speech_words = set(speech_title_lower.split())
        overlap = len(html_words & speech_words)
        if overlap >= 2:
            match_status = "SIMILAR"
        else:
            match_status = "DESAJUSTE"
    else:
        match_status = "DESAJUSTE"

    print(f"{nav_position:<5} {html_num:<8} {html_h2[:44]:<45} {expected_speech_key:<12} {speech_title[:44]:<45} {match_status:<10}")

    if match_status in ["DESAJUSTE", "FALTA"]:
        mismatches.append({
            'nav': nav_position,
            'html_num': html_num,
            'html_title': html_h2,
            'speech_key': expected_speech_key,
            'speech_title': speech_title,
            'status': match_status
        })

print("=" * 120)
print(f"\nRESUMEN:")
print(f"Total slides HTML: {len(slide_data)}")
print(f"Total speech scripts: {len(speech_data)}")
print(f"Desajustes/Faltantes: {len(mismatches)}")

if mismatches:
    print(f"\nDESAJUSTES ENCONTRADOS:")
    print("-" * 120)
    for m in mismatches:
        print(f"\nPosición navegación: {m['nav']} (HTML Slide {m['html_num']})")
        print(f"  HTML muestra: {m['html_title']}")
        print(f"  Speech dice:  {m['speech_title']} ({m['speech_key']})")
        print(f"  Status:       {m['status']}")
