from services.pdf_loader import extract_pdf_text

text = extract_pdf_text("D:/my_projects/enterprise-document-intelligence/app/documents/p1_AI.pdf")

print(text[:1000])