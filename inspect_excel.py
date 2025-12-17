import pandas as pd
import sys

try:
    df = pd.read_excel("Bank_scheme.xlsx")
    print("Columns found in Excel:")
    print(list(df.columns))
    print("\nFirst row sample:")
    print(df.iloc[0].to_dict())
except Exception as e:
    print(f"Error reading Excel: {e}")
