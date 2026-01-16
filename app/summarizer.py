import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from app.prompts import MAP_PROMPT, REDUCE_PROMPT

# Load .env if present (project root .env expected)
env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# Initialize LLM once
llm = ChatOllama(
    model="llama3",
    temperature=0.2
)

# Create prompt templates and chains using LCEL
map_prompt = PromptTemplate.from_template(MAP_PROMPT)
reduce_prompt = PromptTemplate.from_template(REDUCE_PROMPT)

map_chain = map_prompt | llm | StrOutputParser()
reduce_chain = reduce_prompt | llm | StrOutputParser()

def summarize_text(text: str) -> str:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)
    print(f"Total chunks created: {len(chunks)}")

    if not chunks:
        return "No content to summarize."

    # MAP step
    summaries = []
    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i+1}/{len(chunks)}")
        summary = map_chain.invoke({"text": chunk})
        summaries.append(summary)

    # REDUCE step
    combined_summary = "\n".join(summaries)
    final_summary = reduce_chain.invoke({"text": combined_summary})

    return final_summary

