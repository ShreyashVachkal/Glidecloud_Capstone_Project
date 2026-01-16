# 📄 GlideCloud Capstone Project – Academic Research Document Summarizer

An end-to-end **AI-powered academic document summarization system** that accepts PDF research papers or raw text, extracts metadata, and generates structured academic summaries using **Large Language Models (LLMs)**.

This project is built as a **capstone project** to demonstrate real-world skills in **FastAPI, LangChain, LLM orchestration, document processing, and Streamlit UI development**.

---

## 🚀 Project Overview

The system allows users to:
- Upload **academic research papers (PDF)**
- Automatically extract:
  - Title
  - Authors
  - Publication-related metadata (if available)
- Generate **concise, well-structured academic summaries**
- Interact through:
  - **FastAPI Swagger UI**
  - **Streamlit Web Interface**

The project follows a **learning-by-building** approach with clean architecture and modular design.

---

## 🧠 Key Features

- 📄 Supports PDF and raw text input  
- 🔍 Metadata extraction from first page of document   
- 🧩 Map–Reduce based summarization  
- 🧠 Local LLM inference using **Ollama (LLaMA 3)**  
- 🌐 REST API using **FastAPI**  
- 🖥️ User-friendly UI using **Streamlit**  

---

## 🏗️ Project Architecture (Layered Flow)
User
│
▼
Streamlit UI (Frontend)
│
▼
FastAPI Server (API Layer)
│
├── PDF Processing Layer
│ └── Text extraction using PyPDF2
│
├── Metadata Extraction Layer
│ └── LLM-based structured metadata extraction
│
├── Text Chunking Layer
│ └── RecursiveCharacterTextSplitter
│
├── Summarization Layer
│ ├── Map Step – chunk-level summaries
│ └── Reduce Step – final academic summary
│
▼
LLM Layer (Ollama – LLaMA 3)


---

## 🧩 Summarization Strategy

### 🔹 Map–Reduce Summarization
- **Map Step**: Each text chunk is summarized independently
- **Reduce Step**: All partial summaries are merged into one coherent academic summary

This approach:
- Handles large PDFs efficiently
- Preserves important context
- Reduces LLM overload

---

## 📁 Project Structure

Glidecloud_Capstone_Project/
│
├── app/
│ ├── server.py # FastAPI server
│ ├── summarizer.py # Map-Reduce summarization logic
│ ├── metadata_extractor.py # Metadata extraction using LLM
│ ├── pdf_utils.py # PDF text extraction utilities
│ ├── prompts.py # LLM prompts
│
├── ui/
│ └── streamlit_app.py # Streamlit frontend
│
├── Screenshots/ # UI screenshots
├── requirements.txt
├── .gitignore
└── README.md
📸 Screenshots

Screenshots of:

Swagger API
Streamlit Interface
Summary Output
📁 Available inside the Screenshots/ directory.

🧪 Example Workflow

Upload a research paper (PDF)
Extract first-page metadata
Chunk full document text
Generate partial summaries (Map)
Merge summaries into final output (Reduce)
Display results in UI


🔮 Future Enhancements

Vector database integration (FAISS / Pinecone)
Semantic search over documents
Multi-document summarization
Citation-aware summaries
Authentication & user history
Cloud deployment

