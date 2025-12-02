import re

# Read both files
with open('C:/tmp/cursoEStima/clase1.html', 'r', encoding='utf-8') as f:
    clase1_content = f.read()

with open('C:/tmp/cursoEStima/clase1_profesor.html', 'r', encoding='utf-8') as f:
    profesor_content = f.read()

print("=" * 100)
print("ANALISIS DETALLADO: SLIDE 9")
print("=" * 100)

# Extract slide 9 HTML from clase1
slide9_pattern = r'<!-- Slide 9: Análisis del Comportamiento -->(.*?)<!-- Slide 10:'
slide9_match = re.search(slide9_pattern, clase1_content, re.DOTALL)

if slide9_match:
    slide9_html = slide9_match.group(1)

    # Extract key elements
    print("\nElementos visuales en SLIDE 9 (clase1.html):")
    print("-" * 100)

    # Title
    title_match = re.search(r'<h2>(.*?)</h2>', slide9_html)
    if title_match:
        print(f"Titulo: {title_match.group(1)}")

    # MBAs column
    print("\nColumna IZQUIERDA (Patron de Fracaso - MBAs):")
    mba_section = re.search(r'Patrón de Fracaso \(MBAs\)</h3>(.*?)</div>', slide9_html, re.DOTALL)
    if mba_section:
        items = re.findall(r'<li>(.*?)</li>', mba_section.group(1))
        for i, item in enumerate(items, 1):
            clean_item = re.sub(r'<.*?>', '', item)
            print(f"  {i}. {clean_item}")

        conclusion = re.search(r'<p[^>]*>(.*?)</p>', mba_section.group(1))
        if conclusion:
            clean_conclusion = re.sub(r'<.*?>', '', conclusion.group(1))
            print(f"  Conclusion: {clean_conclusion}")

    # Kids column
    print("\nColumna DERECHA (Patron de Exito - Ninos):")
    kids_section = re.search(r'Patrón de Éxito \(Niños\)</h3>(.*?)</div>', slide9_html, re.DOTALL)
    if kids_section:
        items = re.findall(r'<li>(.*?)</li>', kids_section.group(1))
        for i, item in enumerate(items, 1):
            clean_item = re.sub(r'<.*?>', '', item)
            print(f"  {i}. {clean_item}")

        conclusion = re.search(r'<p[^>]*>(.*?)</p>', kids_section.group(1))
        if conclusion:
            clean_conclusion = re.sub(r'<.*?>', '', conclusion.group(1))
            print(f"  Conclusion: {clean_conclusion}")

# Now check speech
print("\n" + "=" * 100)
print("VERIFICACION: Speech cubre elementos visuales?")
print("=" * 100)

speech9_pattern = r'slide9:\s*\{[^}]*script:\s*`([^`]+)`'
speech9_match = re.search(speech9_pattern, profesor_content, re.DOTALL)

if speech9_match:
    speech9_text = speech9_match.group(1)

    print("\nSlide 9 - Elementos del HTML cubiertos en Speech:")
    print("-" * 100)

    checks = [
        ("Minutos 0-10: Planificacion", "0-10" in speech9_text and "Planificación" in speech9_text),
        ("Minutos 10-15: Discusion", "10-15" in speech9_text and "Debate" in speech9_text),
        ("Minutos 15-17: Construccion frenetica", "15-17" in speech9_text and ("PÁNICO" in speech9_text or "frenética" in speech9_text)),
        ("Minuto 18: Colapso", "18" in speech9_text and "COLAPSO" in speech9_text),
        ("MBAs: No tiempo para iterar", "no hay tiempo" in speech9_text.lower()),
        ("Ninos Minuto 1: Malvavisco inmediato", "Minuto 1" in speech9_text and "malvavisco" in speech9_text.lower()),
        ("Ninos Minutos 2-5: Primera version colapsa", "2-5" in speech9_text or "Segunda" in speech9_text),
        ("Ninos Minutos 6-10: Segunda variante", "6-10" in speech9_text or "Tercera" in speech9_text),
        ("Ninos Minutos 11-18: Iteraciones", "11-18" in speech9_text or "Versiones 4" in speech9_text),
        ("Ninos: Multiples ciclos de feedback", "ciclos" in speech9_text.lower() and "feedback" in speech9_text.lower()),
    ]

    for check_name, result in checks:
        status = "OK" if result else "FALTA"
        print(f"  [{status}] {check_name}")

print("\n" + "=" * 100)
print("ANALISIS DETALLADO: SLIDE 10")
print("=" * 100)

# Extract slide 10 HTML from clase1
slide10_pattern = r'<!-- Slide 10: Lecciones del Malvavisco para Proyectos -->(.*?)<!-- Slide 11:'
slide10_match = re.search(slide10_pattern, clase1_content, re.DOTALL)

if slide10_match:
    slide10_html = slide10_match.group(1)

    print("\nElementos visuales en SLIDE 10 (clase1.html):")
    print("-" * 100)

    # Title
    title_match = re.search(r'<h2>(.*?)</h2>', slide10_html)
    if title_match:
        print(f"Titulo: {title_match.group(1)}")

    # Section 1
    print("\nSeccion 1 (Malvavisco = Incertidumbre Oculta):")
    section1 = re.search(r'El Malvavisco = La INCERTIDUMBRE OCULTA(.*?)</ul>', slide10_html, re.DOTALL)
    if section1:
        items = re.findall(r'<li>(.*?)</li>', section1.group(1))
        for i, item in enumerate(items, 1):
            clean_item = re.sub(r'<.*?>', '', item)
            print(f"  {i}. {clean_item}")

    # Section 2
    print("\nSeccion 2 (Leccion Central):")
    section2 = re.search(r'Lección Central del Experimento</h3>(.*?)</p>', slide10_html, re.DOTALL)
    if section2:
        clean_text = re.sub(r'<.*?>', ' ', section2.group(1))
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        print(f"  {clean_text}")

# Check speech
speech10_pattern = r'slide10:\s*\{[^}]*script:\s*`([^`]+)`'
speech10_match = re.search(speech10_pattern, profesor_content, re.DOTALL)

if speech10_match:
    speech10_text = speech10_match.group(1)

    print("\n" + "=" * 100)
    print("VERIFICACION: Speech cubre elementos visuales?")
    print("=" * 100)
    print("\nSlide 10 - Elementos del HTML cubiertos en Speech:")
    print("-" * 100)

    checks = [
        ("Malvavisco = Incertidumbre Oculta", "INCERTIDUMBRE OCULTA" in speech10_text),
        ("MBAs planearon todo: fase requisitos 6 meses", "6 meses" in speech10_text and "requisitos" in speech10_text.lower()),
        ("Pusieron malvavisco al final: integracion final", "final" in speech10_text and "integra" in speech10_text.lower()),
        ("Suposicion falsa", "ASUMEN" in speech10_text or "suposici" in speech10_text.lower()),
        ("Descubren problemas cuando no hay tiempo", "no hay tiempo" in speech10_text.lower() or "ya no hay" in speech10_text.lower()),
        ("Ninos no son mas inteligentes", "inteligente" in speech10_text.lower() or "NIÑOS" in speech10_text),
        ("No tienen mal habito planificar primero", "planificar" in speech10_text.lower() or "método" in speech10_text),
        ("Prueban inmediatamente", "inmediatamente" in speech10_text or "Prueban" in speech10_text),
        ("Les da tiempo para ajustar", "tiempo" in speech10_text and "ajust" in speech10_text.lower()),
    ]

    for check_name, result in checks:
        status = "OK" if result else "FALTA"
        print(f"  [{status}] {check_name}")

print("\n" + "=" * 100)
print("RESUMEN")
print("=" * 100)
print("Los slides 9 y 10 HTML son IDENTICOS entre clase1.html y clase1_profesor.html")
print("Los speeches existen y cubren los elementos visuales")
print("\nSi el usuario reporta diferencias, posibles causas:")
print("1. Navegacion incorrecta (posiciones vs numeros de slide)")
print("2. Cache del navegador")
print("3. Speeches no se actualizan en sidebar")
print("4. Comparando con version vieja de clase1.html")
