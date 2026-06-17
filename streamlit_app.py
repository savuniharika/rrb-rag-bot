import streamlit as st
from pdf_chat import get_answer_from_pdf

st.set_page_config(page_title="RRB RAG Bot", layout="wide")

st.title("📚 RRB RAG Study Assistant")

question = st.text_input("Ask your question from the PDF")

if st.button("Get Answer"):
    if question:
        with st.spinner("Thinking..."):
            answer = get_answer_from_pdf(question)

        st.write(answer)
    else:
        st.warning("Please enter a question")