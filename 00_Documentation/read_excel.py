import pandas as pd
import json
import sys

def read_excel_file(file_path):
    try:
        # Read all sheets from the Excel file
        excel_file = pd.ExcelFile(file_path)
        
        print(f"Excel file has {len(excel_file.sheet_names)} sheets:")
        for i, sheet_name in enumerate(excel_file.sheet_names):
            print(f"{i+1}. {sheet_name}")
        
        all_data = {}
        
        # Read each sheet
        for sheet_name in excel_file.sheet_names:
            print(f"\n--- Reading sheet: {sheet_name} ---")
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            
            print(f"Sheet dimensions: {df.shape[0]} rows x {df.shape[1]} columns")
            print(f"Columns: {list(df.columns)}")
            
            # Store the data
            all_data[sheet_name] = {
                'columns': list(df.columns),
                'data': df.to_dict('records'),
                'shape': df.shape
            }
            
            # Show first few rows
            print("\nFirst 5 rows:")
            print(df.head().to_string())
            print("\n" + "="*80)
        
        return all_data
        
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

if __name__ == "__main__":
    file_path = "✅  Feature Map - Source of Truth - Internal use for Cx & Sales.xlsx"
    data = read_excel_file(file_path)
    
    if data:
        # Save to JSON for easier analysis
        with open("factorial_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        print("\nData saved to factorial_data.json")
