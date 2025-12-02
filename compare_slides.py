#!/usr/bin/env python3
"""Compare slide content between clase3.html and clase3_profesor.html"""

import re
from pathlib import Path

def extract_slides(html_path):
    """Extract all slide content from HTML file"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all slides - more robust pattern
    slides = []
    slide_starts = [m.start() for m in re.finditer(r'<div class="slide"', content)]

    for i, start in enumerate(slide_starts):
        if i < len(slide_starts) - 1:
            end = slide_starts[i + 1]
        else:
            # Last slide - find end before script tag or closing body
            script_pos = content.find('<script>', start)
            body_pos = content.find('</body>', start)
            end = min(p for p in [script_pos, body_pos] if p > start)

        slide_html = content[start:end]
        slides.append(slide_html)

    parsed_slides = []
    for i, slide in enumerate(slides, 1):
        # Extract title (h1, h2, or h3)
        title_match = re.search(r'<h[123]>(.*?)</h[123]>', slide)
        title = title_match.group(1) if title_match else f"Slide {i} (no title)"

        # Clean HTML tags for comparison
        clean_content = re.sub(r'<[^>]+>', '', slide)
        clean_content = re.sub(r'\s+', ' ', clean_content).strip()

        parsed_slides.append({
            'num': i,
            'title': title,
            'html': slide,
            'clean': clean_content[:500]  # First 500 chars for preview
        })

    return parsed_slides

def compare_slides(slides1, slides2):
    """Compare two sets of slides"""
    differences = []

    max_slides = max(len(slides1), len(slides2))

    for i in range(max_slides):
        if i >= len(slides1):
            differences.append({
                'slide_num': i + 1,
                'status': 'MISSING in clase3.html',
                'title2': slides2[i]['title']
            })
        elif i >= len(slides2):
            differences.append({
                'slide_num': i + 1,
                'status': 'MISSING in clase3_profesor.html',
                'title1': slides1[i]['title']
            })
        else:
            s1, s2 = slides1[i], slides2[i]

            # Compare titles (removing HTML entities for comparison)
            title1 = re.sub(r'<[^>]+>', '', s1['title'])
            title2 = re.sub(r'<[^>]+>', '', s2['title'])

            # Normalize for comparison
            title1_norm = re.sub(r'\s+', ' ', title1).strip()
            title2_norm = re.sub(r'\s+', ' ', title2).strip()

            if title1_norm != title2_norm:
                differences.append({
                    'slide_num': i + 1,
                    'status': 'TITLE MISMATCH',
                    'title1': title1_norm,
                    'title2': title2_norm
                })

            # Compare content length (rough check)
            len_diff = abs(len(s1['html']) - len(s2['html']))
            if len_diff > 100:  # Allow 100 char difference for minor variations
                differences.append({
                    'slide_num': i + 1,
                    'status': 'CONTENT LENGTH DIFFERS',
                    'title': title1_norm,
                    'len1': len(s1['html']),
                    'len2': len(s2['html']),
                    'diff': len_diff
                })

    return differences

def main():
    base_path = Path(r"C:\tmp\cursoEStima")

    print("=" * 80)
    print("CLASE 3 SLIDE COMPARISON REPORT")
    print("=" * 80)
    print()

    # Extract slides
    print("Extracting slides from clase3.html...")
    slides1 = extract_slides(base_path / "clase3.html")
    print(f"  Found {len(slides1)} slides")

    print("Extracting slides from clase3_profesor.html...")
    slides2 = extract_slides(base_path / "clase3_profesor.html")
    print(f"  Found {len(slides2)} slides")
    print()

    # Compare
    print("Comparing slide content...")
    differences = compare_slides(slides1, slides2)
    print()

    if not differences:
        print("OK - All slides match perfectly!")
    else:
        print(f"WARNING - Found {len(differences)} differences:")
        print()

        for diff in differences:
            print(f"Slide {diff['slide_num']}: {diff['status']}")

            if 'title1' in diff and 'title2' in diff:
                print(f"  clase3.html:          {diff['title1']}")
                print(f"  clase3_profesor.html: {diff['title2']}")
            elif 'title1' in diff:
                print(f"  Title: {diff['title1']}")
            elif 'title2' in diff:
                print(f"  Title: {diff['title2']}")

            if 'len1' in diff:
                print(f"  Length difference: {diff['diff']} chars (clase3: {diff['len1']}, profesor: {diff['len2']})")
                print(f"  Title: {diff['title']}")

            print()

    # List all slide titles
    print("=" * 80)
    print("ALL SLIDE TITLES (clase3.html)")
    print("=" * 80)
    for slide in slides1:
        title = re.sub(r'<[^>]+>', '', slide['title'])
        # Remove emojis and special chars that cause encoding issues
        title = title.encode('ascii', 'ignore').decode('ascii')
        print(f"{slide['num']:2d}. {title}")

if __name__ == "__main__":
    main()
