import pandas as pd
import sys

try:
    with open("inspection_output.txt", "w", encoding="utf-8") as f:
        df = pd.read_excel("schemes_data.xlsx")
        f.write(f"Columns: {list(df.columns)}\n")
        if len(df) > 0:
            f.write(f"First Row: {df.iloc[0].to_dict()}\n")
        else:
            f.write("DataFrame is empty.\n")
    print("Inspection complete. Check inspection_output.txt")
except Exception as e:
    with open("inspection_output.txt", "w", encoding="utf-8") as f:
        f.write(f"Error: {str(e)}\n")
    print(f"Error: {e}")
