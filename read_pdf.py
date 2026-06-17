from pypdf import PdfReader

reader = PdfReader("Home LIVE CLASSES REASONING HANDOUT 14-05-2025 PDF.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

print(text[:50])