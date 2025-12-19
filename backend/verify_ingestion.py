from services.cyborg import get_cyborg_service

def verify_ingestion():
    service = get_cyborg_service()
    print("Searching for 'Aadhaar'...")
    results = service.search_schemes("Aadhaar", top_k=5)
    
    if results:
        print(f"Found {len(results)} results:")
        for r in results:
            print(f"- {r['metadata']['title']}")
    else:
        print("No results found.")

if __name__ == "__main__":
    verify_ingestion()
