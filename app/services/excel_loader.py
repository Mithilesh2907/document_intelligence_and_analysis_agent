import pandas as pd

def extract_excel_text(file_path: str) :
    excel = pd.ExcelFile(file_path)
    
    text = ""
    
    for sheet in excel.sheet_names :
        df = pd.read_excel(file_path, sheet_name=sheet)
        
        text += f"\nSheet: {sheet}\n"
        
        text += df.to_string()
        
        text += "\n"
        
    return text