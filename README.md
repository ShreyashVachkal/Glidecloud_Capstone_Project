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

1. **User Interaction**
   - Uploads PDF or text via UI

2. **Streamlit UI (Frontend)**
   - Accepts input
   - Displays summaries and metadata

3. **FastAPI Server (API Layer)**
   - Handles requests
   - Orchestrates processing pipeline

4. **PDF Processing Layer**
   - Extracts text using **PyPDF2**

5. **Metadata Extraction Layer**
   - Extracts title, authors, and key details using **LLM**

6. **Text Chunking Layer**
   - Splits text using **RecursiveCharacterTextSplitter**

7. **Summarization Layer**
   - **Map Step**: Chunk-level summaries
   - **Reduce Step**: Final academic summary

8. **LLM Layer**
   - Local inference via **Ollama (LLaMA 3)**


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

**Screenshots of**:

-Swagger API
-Streamlit Interface
-Summary Output
📁 Available inside the Screenshots/ directory.

**🧪 Example Workflow**

Upload a research paper (PDF)
Extract first-page metadata
Chunk full document text
Generate partial summaries (Map)
Merge summaries into final output (Reduce)
Display results in UI


**🔮 Future Enhancements**

Vector database integration (FAISS / Pinecone)
Semantic search over documents
Multi-document summarization
Citation-aware summaries
Authentication & user history
Cloud deployment

