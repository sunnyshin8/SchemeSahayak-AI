from services.cyborg import get_cyborg_service
from database import get_cyborg_client
import time

def ingest_data():
    print("Initializing CyborgService...")
    service = get_cyborg_service()
    
    # 1. Government Schemes
    gov_schemes = [
        {
            "id": "pm-kisan",
            "title": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            "description": "Financial benefit of Rs. 6000 per year to eligible landholding farmer families, payable in three equal installments of Rs. 2000 each. Funds transferred directly to bank accounts via DBT.",
            "metadata": {"ministry": "Agriculture & Farmers Welfare", "benefits": "Rs. 6000/year", "category": "Farmers", "type": "Government"}
        },
        {
            "id": "pm-awas-gramin",
            "title": "Pradhan Mantri Awas Yojana - Gramin (PMAY-G)",
            "description": "Provides financial assistance for construction of pucca house to houseless households and those living in dilapidated houses in rural areas. Assistance up to Rs. 1.2 Lakh (Plains) or Rs. 1.3 Lakh (Hilly).",
            "metadata": {"ministry": "Rural Development", "benefits": "Housing Aid up to 1.3L", "category": "Housing", "type": "Government"}
        }
    ]

    # 2. Bank Schemes (Linked)
    bank_schemes = [
        {
            "id": "sbi-kcc",
            "title": "SBI Kisan Credit Card (KCC)",
            "description": "Revolving cash credit for farmers for crop production and allied activities. Interest subvention of 2-3% available. Collateral free up to Rs. 1.60 Lakh. Linked to PM-KISAN data for ease of access.",
            "metadata": {
                "bank": "State Bank of India", 
                "benefits": "Credit Limit, Interest Subvention (4% effective)", 
                "category": "Farmers", 
                "type": "Bank",
                "backing_scheme": "pm-kisan",
                "backing_scheme_name": "PM-KISAN"
            }
        },
        {
            "id": "union-pmay-loan",
            "title": "Union Bank Home Loan (PMAY-Urban)",
            "description": "Home loan for EWS/LIG/MIG categories under PMAY-Urban 2.0. Interest subsidy up to 6.5% under CLSS. Tenure up to 30 years.",
            "metadata": {
                "bank": "Union Bank of India", 
                "benefits": "Interest Subsidy (CLSS)", 
                "category": "Housing", 
                "type": "Bank",
                "backing_scheme": "pm-awas-gramin", # Linking to housing in general for demo context
                "backing_scheme_name": "PM Awas Yojana"
            }
        }
    ]

    print("Indexing Government Schemes...")
    for s in gov_schemes:
        try:
            service.index_scheme(s['id'], s['title'], s['description'], s['metadata'])
            print(f"Indexed: {s['title']}")
        except Exception as e:
            print(f"Error indexing {s['id']}: {e}")

    print("Indexing Bank Schemes...")
    for s in bank_schemes:
        try:
            service.index_scheme(s['id'], s['title'], s['description'], s['metadata'])
            print(f"Indexed: {s['title']}")
        except Exception as e:
            print(f"Error indexing {s['id']}: {e}")

    print("Ingestion Complete!")

if __name__ == "__main__":
    ingest_data()
