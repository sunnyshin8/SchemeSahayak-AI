import pandas as pd
from services.cyborg import get_cyborg_service
import re

def slugify(text):
    text = text.lower()
    return re.sub(r'[\s]+', '-', re.sub(r'[^\w\s-]', '', text))

def ingest_excel_data():
    print("Reading Excel file...")
    try:
        df = pd.read_excel("schemes_data.xlsx")
        # Ensure columns exist
        required = ['Item', 'Explanation', 'Regulatory / Notes', 'Read More']
        for col in required:
            if col not in df.columns:
                print(f"Missing column: {col}")
                return

        service = get_cyborg_service()
        print(f"Found {len(df)} rows. Starting ingestion...")

        count = 0
        for index, row in df.iterrows():
            title = str(row['Item']).strip()
            explanation = str(row['Explanation']).strip()
            regulation = str(row['Regulatory / Notes']).strip()
            read_more = str(row['Read More']).strip()

            # ID generation
            scheme_id = slugify(title)[:50] # Truncate if too long

            # Combine explanation and regulation for description which is embedded
            description = f"{explanation}\n\nRegulatory Notes: {regulation}"

            metadata = {
                "type": "Regulation/Framework",
                "read_more": read_more,
                "regulation": regulation,
                "ministry": "RBI/Regulatory" # Fallback for UI display
            }

            try:
                service.index_scheme(scheme_id, title, description, metadata)
                print(f"Indexed: {title}")
                count += 1
            except Exception as e:
                print(f"Failed to index {title}: {e}")

        print(f"Ingestion complete. Successfully indexed {count} items.")

    except Exception as e:
        print(f"Error during ingestion: {e}")

if __name__ == "__main__":
    ingest_excel_data()
