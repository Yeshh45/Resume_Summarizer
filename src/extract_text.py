from PyPDF2 import PdfReader
import io

def extract_resume_text(file) -> str:
    """
    Extracts text from a PDF resume file.
    """
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text
    except Exception as e:
        raise Exception(f"Error extracting text: {e}")
