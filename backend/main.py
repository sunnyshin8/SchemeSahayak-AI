from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import citizen, agency, auth
import uvicorn

app = FastAPI(title="SchemeSahayak API", description="AI-Powered Government Scheme Intelligence Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(citizen.router, prefix="/api/citizen", tags=["Citizen"])
app.include_router(agency.router, prefix="/api/agency", tags=["Agency"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "SchemeSahayak Backend is Running with CyborgDB Integration"}

@app.on_event("startup")
async def startup_event():
    from database import get_cyborg_client
    from services.cyborg import get_cyborg_service
    
    client = get_cyborg_client()
    # Ingest if Mock OR Real (to ensure data exists for demo)
    print("Startup: Ingesting Dummy Data into CyborgDB (Real/Mock)...")
    try:
        service = get_cyborg_service()
        # 1. Government Schemes
        gov_schemes = [
            {
                "id": "pm-kisan",
                "title": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
                "description": "Financial benefit of Rs. 6000 per year to eligible landholding farmer families, payable in three equal installments of Rs. 2000 each. Funds transferred directly to bank accounts via DBT.",
                "metadata": {"ministry": "Agriculture & Farmers Welfare", "benefits": "Rs. 6000/year", "category": "Farmers", "type": "Government", "link": "https://pmkisan.gov.in/"}
            },
            {
                "id": "pm-awas-gramin",
                "title": "Pradhan Mantri Awas Yojana - Gramin (PMAY-G)",
                "description": "Provides financial assistance for construction of pucca house to houseless households and those living in dilapidated houses in rural areas. Assistance up to Rs. 1.2 Lakh (Plains) or Rs. 1.3 Lakh (Hilly).",
                "metadata": {"ministry": "Rural Development", "benefits": "Housing Aid up to 1.3L", "category": "Housing", "type": "Government", "link": "https://pmayg.nic.in/"}
            },
             {
                "id": "ayushman-bharat",
                "title": "Ayushman Bharat Pradhan Mantri Jan Arogya Yojana",
                "description": "Health insurance coverage up to 5 lakhs per family per year for secondary and tertiary care hospitalization.",
                "metadata": {"ministry": "Health", "benefits": "Health Insurance", "category": "Health", "type": "Government", "link": "https://pmjay.gov.in/"}
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
                    "backing_scheme_name": "PM-KISAN",
                    "link": "https://sbi.co.in/web/agri-rural/agriculture-banking/crop-loan/kisan-credit-card"
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
                    "backing_scheme": "pm-awas-gramin",
                    "backing_scheme_name": "PM Awas Yojana",
                    "link": "https://www.unionbankofindia.co.in/english/home-loan-pmay.aspx"
                }
            }
        ]
        
        
        # Load Excel Schemes if available
        import os
        import pandas as pd
        excel_path = "../Bank_scheme.xlsx"
        if os.path.exists(excel_path):
            try:
                print("Reading Real Data from Bank_scheme.xlsx...")
                df = pd.read_excel(excel_path)
                for idx, row in df.iterrows():
                    item_name = str(row.get('Item', 'Unknown'))
                    bank_schemes.append({
                        "id": f"bank-real-{idx}",
                        "title": item_name,
                        "description": str(row.get('Explanation', '')),
                        "metadata": {
                            "regulatory_notes": str(row.get('Regulatory / Notes', '')),
                            "link": str(row.get('Read More', '')),
                            "type": "Bank",
                            "backing_scheme_name": "General Banking" # Default
                        }
                    })
                print(f"Loaded {len(df)} schemes from Excel.")
            except Exception as e:
                print(f"Failed to load Excel data: {e}")

        schemes = gov_schemes + bank_schemes

        for s in schemes:
            service.index_scheme(s['id'], s['title'], s['description'], s['metadata'])
        print("Startup Ingestion Complete.")
    except Exception as e:
        print(f"Startup Ingestion Failed: {e}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
