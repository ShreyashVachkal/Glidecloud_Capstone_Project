from langchain_core.output_parsers import JsonOutputParser
from app.prompts import METADATA_PROMPT
from app.summarizer import llm   # or wherever your llm is defined

metadata_chain = METADATA_PROMPT | llm | JsonOutputParser()

def extract_metadata(first_page_text: str) -> dict:
    return metadata_chain.invoke({"text": first_page_text})

