from services.cyborg import get_cyborg_service

def ingest_schemes():
    service = get_cyborg_service()
    
    schemes = [
        {
            "id": "pm-kisan",
            "title": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            "description": "Financial benefit of Rs. 6000 per year to eligible farmer families.",
            "metadata": {"ministry": "Agriculture", "benefits": "6000 INR/year", "category": "Farmers"}
        },
        {
            "id": "pm-awas",
            "title": "Pradhan Mantri Awas Yojana (PMAY)",
            "description": "Housing for all. Provides financial assistance to construct pucca houses.",
            "metadata": {"ministry": "Housing & Urban Affairs", "benefits": "Housing Subsidy", "category": "Housing"}
        },
        {
            "id": "ayushman-bharat",
            "title": "Ayushman Bharat Pradhan Mantri Jan Arogya Yojana",
            "description": "Health insurance coverage up to 5 lakhs per family per year for secondary and tertiary care hospitalization.",
            "metadata": {"ministry": "Health", "benefits": "Health Insurance", "category": "Health"}
        },
        {
            "id": "kalia",
            "title": "Krushak Assistance for Livelihood and Income Augmentation (KALIA)",
            "description": "Financial assistance to cultivators and landless agricultural laborers.",
            "metadata": {"ministry": "State Gov (Odisha)", "benefits": "Financial Aid", "category": "Farmers"}
        },
        {
            "id": "mudra-loan",
            "title": "Pradhan Mantri MUDRA Yojana",
            "description": "Loans up to 10 lakhs for non-corporate, non-farm small/micro enterprises.",
            "metadata": {"ministry": "Finance", "benefits": "Business Loan", "category": "Business"}
        }
    ]

    print("Ingesting schemes...")
    for scheme in schemes:
        print(f"Indexing: {scheme['title']}")
        service.index_scheme(scheme['id'], scheme['title'], scheme['description'], scheme['metadata'])
    
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_schemes()
