import re

# Read both files
with open('C:/tmp/cursoEStima/clase1.html', 'r', encoding='utf-8') as f:
    clase1_content = f.read()

with open('C:/tmp/cursoEStima/clase1_profesor.html', 'r', encoding='utf-8') as f:
    profesor_content = f.read()

# Extract slide 9 from both files
def extract_slide(content, slide_num):
    pattern = rf'<!-- Slide {slide_num}:.*?-->(.*?)(?=<!-- Slide \d+[a-z]*:|</div>\s*</div>\s*<script>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

print("=" * 100)
print("COMPARACION SLIDE 9")
print("=" * 100)

slide9_clase1 = extract_slide(clase1_content, 9)
slide9_profesor = extract_slide(profesor_content, 9)

if slide9_clase1 and slide9_profesor:
    # Clean whitespace for comparison
    clean1 = re.sub(r'\s+', ' ', slide9_clase1)
    clean2 = re.sub(r'\s+', ' ', slide9_profesor)

    if clean1 == clean2:
        print("Slide 9: IDENTICO")
    else:
        print("Slide 9: DIFERENTE")
        print(f"\nClase1 length: {len(slide9_clase1)}")
        print(f"Profesor length: {len(slide9_profesor)}")

        # Show differences
        lines1 = slide9_clase1.split('\n')
        lines2 = slide9_profesor.split('\n')

        print(f"\nLineas en clase1: {len(lines1)}")
        print(f"Lineas en profesor: {len(lines2)}")

print("\n" + "=" * 100)
print("COMPARACION SLIDE 10")
print("=" * 100)

slide10_clase1 = extract_slide(clase1_content, 10)
slide10_profesor = extract_slide(profesor_content, 10)

if slide10_clase1 and slide10_profesor:
    clean1 = re.sub(r'\s+', ' ', slide10_clase1)
    clean2 = re.sub(r'\s+', ' ', slide10_profesor)

    if clean1 == clean2:
        print("Slide 10: IDENTICO")
    else:
        print("Slide 10: DIFERENTE")
        print(f"\nClase1 length: {len(slide10_clase1)}")
        print(f"Profesor length: {len(slide10_profesor)}")

        lines1 = slide10_clase1.split('\n')
        lines2 = slide10_profesor.split('\n')

        print(f"\nLineas en clase1: {len(lines1)}")
        print(f"Lineas en profesor: {len(lines2)}")

# Now check the speech scripts
print("\n" + "=" * 100)
print("VERIFICACION SPEECHES")
print("=" * 100)

# Extract speech for slide 9
speech_pattern = r'slide9:\s*\{[^}]*title:\s*"([^"]+)"[^}]*duration:\s*"([^"]+)"[^}]*script:\s*`([^`]+)`'
match9 = re.search(speech_pattern, profesor_content, re.DOTALL)

if match9:
    print(f"\nSlide 9 Speech:")
    print(f"  Title: {match9.group(1)}")
    print(f"  Duration: {match9.group(2)}")
    print(f"  Script length: {len(match9.group(3))} chars")
    print(f"  First 100 chars: {match9.group(3)[:100]}...")
else:
    print("\nSlide 9 Speech: NO ENCONTRADO")

# Extract speech for slide 10
speech_pattern = r'slide10:\s*\{[^}]*title:\s*"([^"]+)"[^}]*duration:\s*"([^"]+)"[^}]*script:\s*`([^`]+)`'
match10 = re.search(speech_pattern, profesor_content, re.DOTALL)

if match10:
    print(f"\nSlide 10 Speech:")
    print(f"  Title: {match10.group(1)}")
    print(f"  Duration: {match10.group(2)}")
    print(f"  Script length: {len(match10.group(3))} chars")
    print(f"  First 100 chars: {match10.group(3)[:100]}...")
else:
    print("\nSlide 10 Speech: NO ENCONTRADO")
