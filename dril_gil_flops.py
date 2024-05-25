import os
import pandas as pd

def convert_xlsx_to_csv(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter for .xlsx files
    xlsx_files = [file for file in files if file.endswith('.xlsx')]
    
    for xlsx_file in xlsx_files:
        # Define the full file path
        xlsx_path = os.path.join(folder_path, xlsx_file)
        
        try:
            # Read the Excel file using openpyxl engine
            df = pd.read_excel(xlsx_path, engine='openpyxl')
            
            # Define the new CSV file path
            csv_file = xlsx_file.replace('.xlsx', '.csv')
            csv_path = os.path.join(folder_path, csv_file)
            
            # Write the DataFrame to a CSV file
            df.to_csv(csv_path, index=False)
            
            print(f"Converted {xlsx_file} to {csv_file}")
        
        except Exception as e:
            print(f"Failed to convert {xlsx_file}: {e}")

# Example usage:
folder_path = './GIL_FLOPS/LJ_vs_BTN/LJ/UNPAIRED_TWO_TONE'  # Replace this with your folder path
convert_xlsx_to_csv(folder_path)