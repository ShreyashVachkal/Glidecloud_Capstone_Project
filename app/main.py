'''from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_ollama import OllamaLLM
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langgraph.constants import Send
from langgraph.graph import START, END, StateGraph

import operator
from typing import Annotated, List,Literal,TypedDict

import requests
import warnings
from pathlib import Path'''

from pathlib import Path
from summarizer import summarize_text

def main():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "sample_text.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    summary = summarize_text(text)
    print("\nFINAL SUMMARY:\n")
    print(summary)

if __name__ == "__main__":
    main()


