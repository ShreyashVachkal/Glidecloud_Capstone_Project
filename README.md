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

## 📸 Screenshots

The following screenshots are available inside the **`Screenshots/`** directory:

- Swagger API Interface
- Streamlit User Interface
- Generated Summary Output


## 🧪 Example Workflow

1. Upload a research paper (PDF) via the Streamlit UI
2. Extract metadata from the first page of the document
3. Process and chunk the full document text
4. Generate partial summaries using the **Map** step
5. Merge chunk-level summaries using the **Reduce** step
6. Display the final summary and metadata in the UI


## 🔮 Future Enhancements

- Vector database integration (FAISS / Pinecone)
- Semantic search over uploaded documents
- Multi-document summarization support
- Citation-aware and reference-linked summaries
- User authentication and history tracking
- Cloud deployment (AWS / GCP / Azure)


