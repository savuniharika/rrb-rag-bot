from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Read PDF once
reader = PdfReader("Home LIVE CLASSES REASONING HANDOUT 14-05-2025 PDF.pdf")

pdf_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        pdf_text += text

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)
def get_answer_from_pdf(question):
    try:
        prompt = f"""
        PDF Content:
        {pdf_text}

        Question:
        {question}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"