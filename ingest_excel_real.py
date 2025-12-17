import sys
import os

# Add backend to path so we can import from it
sys.path.append(os.path.join(os.getcwd(), 'backend'))

import pandas as pd
# Now we can import from backend packages
from services.cyborg import get_cyborg_service

def ingest_excel():
    print("Reading Excel...")
    df = pd.read_excel("Bank_scheme.xlsx")
    
    print("Initializing CyborgService (Connecting to Cloud)...")
    try:
        service = get_cyborg_service()
        print("CyborgService Initialized.")
    except Exception as e:
        print(f"Failed to initialize service: {e}")
        return
    
    print(f"Found {len(df)} rows. Starting Ingestion...")
    
    for idx, row in df.iterrows():
        try:
            # Map columns to schema
            item_name = row.get('Item', 'Unknown Scheme')
            explanation = row.get('Explanation', '')
            regulatory = row.get('Regulatory / Notes', '')
            link = row.get('Read More', '')
            
            scheme_id = f"bank-scheme-{idx}"
            title = item_name
            description = explanation
            
            metadata = {
                "regulatory_notes": str(regulatory),
                "read_more_link": str(link),
                "type": "Bank",
                "category": "Banking/Cybersecurity" # inferred from columns
            }
            
            print(f"Indexing: {title}")
            service.index_scheme(scheme_id, title, description, metadata)
            
        except Exception as e:
            print(f"Error indexing row {idx}: {e}")

    print("Excel Ingestion Complete!")

if __name__ == "__main__":
    ingest_excel()
