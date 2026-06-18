from pathlib import Path

from services.pdf_loader import extract_pdf_text
from services.docx_loader import extract_docx_text
from services.excel_loader import extract_excel_text

def load_document(file_path: str) :
    
    suffix = Path(file_path).suffix.lower()
    
    if suffix == ".pdf":
        return extract_pdf_text(file_path)
    
    if suffix == ".docx":
        return extract_docx_text(file_path)
    
    if suffix in [".xls", ".xlsx"]:
        return extract_excel_text(file_path)
    
    raise ValueError(f"Unsupported file format: {suffix}. Supported formats are: .pdf, .docx, .xls, .xlsx")