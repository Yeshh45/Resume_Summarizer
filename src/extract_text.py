from pdfminer.high_level import extract_text
from docx import Document
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        text = extract_text(pdf_path)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file."""
    try:
        doc = Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {docx_path}: {e}")
        return None

def extract_resume_text(file_path):
    """Determine file type and extract text accordingly."""
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        print("Unsupported file format. Please use PDF or DOCX.")
        return None

# Test the function with a sample file
if __name__ == "__main__":
    sample_file = "C:/Users/bargav/Desktop/Resume_Summarizer/Resume_Summarizer/data/YeshwanthGovindu_.pdf"  # Change this to your actual file path
    extracted_text = extract_resume_text(sample_file)
    if extracted_text:
        print("Extracted Text:\n", extracted_text[:1000])  # Print first 1000 characters for preview
 
