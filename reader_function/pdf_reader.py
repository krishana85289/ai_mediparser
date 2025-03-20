import fitz  # PyMuPDF
import asyncio

# Synchronous PDF extraction function
def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts text from a PDF file (synchronous version)."""
    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)
    return text

# Async wrapper using asyncio.to_thread
async def extract_text_from_pdf_async(pdf_path: str) -> str:
    """Asynchronous wrapper for PDF text extraction."""
    return await asyncio.to_thread(extract_text_from_pdf, pdf_path)