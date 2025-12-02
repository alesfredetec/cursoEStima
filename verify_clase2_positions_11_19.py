import re

# Read clase2.html (source) and clase2_profesor.html
with open('C:/tmp/cursoEStima/clase2.html', 'r', encoding='utf-8') as f:
    clase2_content = f.read()

with open('C:/tmp/cursoEStima/clase2_profesor.html', 'r', encoding='utf-8') as f:
    profesor_content = f.read()

print("=" * 120)
print("VERIFICACION DETALLADA: clase2_profesor.html POSITIONS 11-19")
print("=" * 120)

# Extract HTML slides from clase2.html (source of truth)
html_pattern = r'<!-- Slide (\d+): ([^>]+) -->(.*?)(?=<!-- Slide \d+:|<!-- NAVIGATION -->|$)'
html_matches = re.findall(html_pattern, clase2_content, re.DOTALL)

# Extract HTML slides from clase2_profesor.html
html_prof_pattern = r'<!-- Slide (\d+): ([^>]+) -->(.*?)(?=<!-- Slide \d+:|<!-- NAVIGATION -->|$)'
html_prof_matches = re.findall(html_prof_pattern, profesor_content, re.DOTALL)

# Extract speech data
speech_pattern = r'"slide(\d+)":\s*\{\s*"title":\s*"([^"]+)",\s*"duration":\s*"([^"]+)",\s*"script":\s*`([^`]+)`'
speech_matches = re.findall(speech_pattern, profesor_content, re.DOTALL)

# Create dictionaries
html_source = {int(num): (title, content[:500]) for num, title, content in html_matches}
html_prof = {int(num): (title, content[:500]) for num, title, content in html_prof_matches}
speech_dict = {int(num): (title, duration, script[:500]) for num, title, duration, script in speech_matches}

print("\nFocus: Positions 11-19 (HTML slides 12-20)")
print("=" * 120)

# Check positions 11-19 (which correspond to HTML slides 12-20)
for pos in range(11, 20):
    slide_num = pos + 1  # HTML slide number (0-indexed position + 1)
    speech_num = slide_num  # clase2 uses formula: slide${currentSlide + 1}

    print(f"\n{'='*120}")
    print(f"POSITION {pos}: HTML Slide #{slide_num} -> Speech slide{speech_num}")
    print(f"{'='*120}")

    # Get HTML title from source
    if slide_num in html_source:
        source_title, source_snippet = html_source[slide_num]
        print(f"\nHTML Source Title: '{source_title}'")
        # Remove emojis for console output
        preview = source_snippet[:200].strip().encode('ascii', 'ignore').decode('ascii')
        print(f"HTML Source Preview: {preview}")
    else:
        print(f"\nHTML Source: NOT FOUND")

    # Get HTML title from profesor
    if slide_num in html_prof:
        prof_title, prof_snippet = html_prof[slide_num]
        print(f"\nHTML Profesor Title: '{prof_title}'")

        # Check if titles match
        if slide_num in html_source and source_title != prof_title:
            print(f"WARNING: Title mismatch between source and profesor!")
    else:
        print(f"\nHTML Profesor: NOT FOUND")

    # Get speech data
    if speech_num in speech_dict:
        speech_title, duration, script_snippet = speech_dict[speech_num]
        print(f"\nSpeech Title: '{speech_title}' ({duration})")
        # Remove emojis for console output
        speech_preview = script_snippet[:300].strip().encode('ascii', 'ignore').decode('ascii')
        print(f"Speech Preview: {speech_preview}...")

        # Check if speech title matches HTML title
        if slide_num in html_prof:
            if speech_title.lower() not in prof_title.lower() and prof_title.lower() not in speech_title.lower():
                print(f"\n*** MISMATCH DETECTED ***")
                print(f"HTML shows: '{prof_title}'")
                print(f"Speech describes: '{speech_title}'")
                print(f"These appear to be DIFFERENT content!")
    else:
        print(f"\nSpeech: NOT FOUND")

print("\n" + "=" * 120)
print("SUMMARY OF ISSUES")
print("=" * 120)

issues = []
for pos in range(11, 20):
    slide_num = pos + 1
    speech_num = slide_num

    if slide_num in html_prof and speech_num in speech_dict:
        prof_title, _ = html_prof[slide_num]
        speech_title, _, _ = speech_dict[speech_num]

        # Check for obvious mismatches
        if speech_title.lower() not in prof_title.lower() and prof_title.lower() not in speech_title.lower():
            issues.append(f"Position {pos}: HTML '{prof_title}' vs Speech '{speech_title}'")

if issues:
    print(f"\nFound {len(issues)} potential mismatches:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("\nNo obvious title mismatches found.")
    print("Note: Titles may match but content could still be misaligned.")
    print("Manual review of speech content vs visual elements recommended.")
