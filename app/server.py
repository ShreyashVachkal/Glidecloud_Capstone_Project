'''from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import PyPDF2
import io
from app.summarizer import summarize_text

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent


@app.post("/summarize")
async def summarize(request: Request, file: UploadFile = File(None)):
   
    text = None

    # If a file was uploaded, extract text from the PDF
    if file is not None:
        if file.content_type != "application/pdf":
            return JSONResponse({"error": "Only PDF files are supported."}, status_code=400)
        content = await file.read()
        try:
            reader = PyPDF2.PdfReader(io.BytesIO(content))
            text_pages = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_pages.append(page_text)
            text = "\n".join(text_pages)
        except Exception as e:
            return JSONResponse({"error": f"Failed to read PDF: {e}"}, status_code=500)

        if not text or not text.strip():
            return JSONResponse({"error": "No extractable text found in PDF."}, status_code=400)

    else:
        # Try to parse JSON body with `text` field
        try:
            body = await request.json()
        except Exception:
            body = None

        if body and isinstance(body, dict) and body.get("text"):
            text = body.get("text")
        else:
            return JSONResponse({"error": "No input provided. Send a PDF file or JSON with a `text` field."}, status_code=422)

    # At this point we have `text` to summarize
    summary = summarize_text(text)
    return {"summary": summary}
'''
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import JSONResponse
from typing import Optional

from app.pdf_utils import extract_text_from_pdf
from app.summarizer import summarize_text
from app.metadata_extractor import extract_metadata

app = FastAPI()


@app.post("/summarize")
async def summarize(
    request: Request,
    file: Optional[UploadFile] = File(None)
):
    first_page_text: Optional[str] = None
    full_text: Optional[str] = None

    # ---------- Case 1: PDF upload ----------
    if file is not None:
        if file.content_type != "application/pdf":
            return JSONResponse(
                {"error": "Only PDF files are supported."},
                status_code=400
            )

        try:
            pdf_bytes = await file.read()
            result = extract_text_from_pdf(pdf_bytes)

            # 🔐 SAFETY: ensure correct unpacking
            if not isinstance(result, tuple) or len(result) != 2:
                return JSONResponse(
                    {"error": "PDF extraction returned invalid data."},
                    status_code=500
                )

            first_page_text, full_text = result

        except Exception as e:
            return JSONResponse(
                {"error": f"Failed to process PDF: {str(e)}"},
                status_code=500
            )

        # 🔐 SAFETY: ensure full_text is a valid string
        if not isinstance(full_text, str) or not full_text.strip():
            return JSONResponse(
                {"error": "No extractable text found in PDF."},
                status_code=400
            )

    # ---------- Case 2: Raw text input ----------
    else:
        try:
            body = await request.json()
        except Exception:
            body = None

        if body and isinstance(body, dict) and isinstance(body.get("text"), str):
            full_text = body["text"]
            first_page_text = full_text[:2000]  # Safe slice for metadata
        else:
            return JSONResponse(
                {"error": "No input provided. Send a PDF file or JSON with a `text` field."},
                status_code=422
            )

    # ---------- Metadata Extraction ----------
    try:
        metadata = extract_metadata(first_page_text)
    except Exception as e:
        metadata = {"error": f"Metadata extraction failed: {str(e)}"}

    # ---------- Summarization ----------
    try:
        summary = summarize_text(full_text)
    except Exception as e:
        return JSONResponse(
            {"error": f"Summarization failed: {str(e)}"},
            status_code=500
        )

    return {
        "metadata": metadata,
        "summary": summary
    }

