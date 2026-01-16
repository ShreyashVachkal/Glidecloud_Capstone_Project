'''from io import BytesIO
from typing import Union

try:
    from PyPDF2 import PdfReader
except Exception:
    PdfReader = None


def extract_text_from_pdf(file: Union[bytes, BytesIO, object]) -> str:
    
    if PdfReader is None:
        raise RuntimeError("PyPDF2 not available. Install pypdf2 in your environment.")

    # Read raw bytes from file-like objects
    if hasattr(file, "read"):
        data = file.read()
    elif isinstance(file, (bytes, bytearray)):
        data = bytes(file)
    else:
        # Try to use as-is
        data = file

    stream = BytesIO(data)
    reader = PdfReader(stream)
    texts = []
    for page in reader.pages:
        try:
            txt = page.extract_text()
        except Exception:
            txt = None
        if txt:
            texts.append(txt)

    return "\n".join(texts)'''

from io import BytesIO
from typing import Union, Tuple

try:
    from PyPDF2 import PdfReader
except Exception:
    PdfReader = None


def extract_text_from_pdf(
    file: Union[bytes, BytesIO, object]
) -> Tuple[str, str]:
    """
    Extracts text from a PDF.

    Returns:
    - first_page_text: Text from the first page (for metadata extraction)
    - full_text: Text from the entire document (for summarization)
    """

    if PdfReader is None:
        raise RuntimeError("PyPDF2 not available. Install pypdf2 in your environment.")

    # Read raw bytes from file-like objects
    if hasattr(file, "read"):
        data = file.read()
    elif isinstance(file, (bytes, bytearray)):
        data = bytes(file)
    else:
        raise ValueError("Unsupported file type for PDF extraction")

    stream = BytesIO(data)
    reader = PdfReader(stream)

    first_page_text = ""
    all_pages_text = []

    for idx, page in enumerate(reader.pages):
        try:
            txt = page.extract_text()
        except Exception:
            txt = None

        if not txt:
            continue

        if idx == 0:
            first_page_text = txt

        all_pages_text.append(txt)

    return first_page_text, "\n".join(all_pages_text)
