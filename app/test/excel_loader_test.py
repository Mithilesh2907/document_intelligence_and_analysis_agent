from services.excel_loader import extract_excel_text

text = extract_excel_text("D:/my_projects/enterprise-document-intelligence/app/documents/Application List WHIRLPOOL2025-263 (1).xls (1).xlsx")

print(text)