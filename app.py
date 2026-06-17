import os
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai

load_dotenv()

# Load Gemini
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.title("📚 RRB Study Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text

    question = st.text_input(
        "Ask a question from the PDF"
    )

    if st.button("Get Answer") and question:

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

        st.write(response.text)