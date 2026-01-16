from langchain_core.prompts import PromptTemplate

METADATA_PROMPT = PromptTemplate(
    input_variables=["text"],
    template="""
You are an academic document analyzer.

Extract bibliographic metadata from the given research paper text.

Extract ONLY what is explicitly mentioned.
Do NOT guess or infer.

Return the output in the following JSON format:
{
  "title": "",
  "authors": "",
  "affiliation": "",
  "publication_year": "",
  "journal_or_conference": ""
}

If a field is not found, leave it empty.

TEXT:
{text}
"""
)


MAP_PROMPT = """
You are an expert academic research assistant.

Your task is to summarize the following research text chunk.

Focus ONLY on:
1. The research problem or objective
2. The methodology or approach used
3. The key findings or contributions

Guidelines:
- Be concise and factual
- Use academic language
- Do NOT add assumptions or external information
- If a section is not present, omit it
- Write in complete sentences

RESEARCH TEXT:
{text}
"""


REDUCE_PROMPT = """
You are a senior academic editor.

Your task is to merge the following partial academic summaries into ONE
clear, coherent, and well-structured final summary.

Guidelines:
- Remove redundancy and repetition
- Preserve all important points
- Maintain logical flow
- Use formal academic tone
- Limit the final summary to 1–2 well-structured paragraphs

PARTIAL SUMMARIES:
{text}
"""

