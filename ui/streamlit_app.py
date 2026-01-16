import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests
from app.pdf_utils import extract_text_from_pdf

API_URL = "http://127.0.0.1:8000/summarize"

st.set_page_config(
    page_title="Research Paper Summarizer",
    layout="wide"
)

st.title("📄 Research Paper Summarizer")
st.write(
    "Upload a research paper or paste text to generate a concise academic summary."
)

# ---- Input section ----
input_method = st.radio(
    "Choose input method",
    ("Paste Text", "Upload PDF")
)

text_input = ""

if input_method == "Paste Text":
    text_input = st.text_area(
        "Paste your research paper text here",
        height=300
    )

elif input_method == "Upload PDF":
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:
        try:
            first_page_text, extracted = extract_text_from_pdf(uploaded_file)
            if extracted.strip():
                st.success("Extracted text from PDF — preview below.")
                text_input = extracted
                st.text_area("Extracted text (editable)", text_input, height=300)
            else:
                st.warning("No extractable text found in PDF. Try a different file.")
        except Exception as e:
            st.error(f"PDF extraction failed: {e}")

# ---- Summarize button ----
if st.button("🔍 Generate Summary"):
    if not text_input.strip():
        st.error("Please provide text to summarize.")
    else:
        with st.spinner("Summarizing... This may take a few minutes ⏳"):
            try:
                response = requests.post(
                    API_URL,
                    json={"text": text_input},
                    timeout=None 
                )

                if response.status_code == 200:
                    data = response.json()
                    metadata = data.get("metadata", {})
                    summary = data.get("summary", "")

                    st.success("Summary generated successfully!")

                    # Display Metadata
                    if metadata and not isinstance(metadata, dict) or not metadata.get("error"):
                        st.subheader("📋 Extracted Metadata")
                        for key, value in metadata.items():
                            st.write(f"**{key.title()}:** {value}")
                    else:
                        st.warning("Metadata extraction failed or not available.")

                    # Display Summary
                    st.subheader("📄 Summary")
                    st.text_area(
                        "Summary",
                        summary,
                        height=300
                    )
                else:
                    st.error("Error from API server.")

            except requests.exceptions.RequestException as e:
                st.error(f"API error: {e}")
