from services.cyborg import get_cyborg_service

def verify_citizens():
    service = get_cyborg_service()
    
    # Since we are using mock DB, we can try to peek at the length if possible,
    # or just perform a search that should return results.
    # Note: Real CyborgDB might not implement 'len' on index directly via SDK.
    # We will try a meaningful search.
    
    print("Verifying citizens...")
    # Search for common Indian name part to see if we get hits
    results = service.citizen_index.query(service.embedder.encode("Kumar"), top_k=5)
    
    if results:
        print(f"Sample search for 'Kumar' found {len(results)} results:")
        for r in results:
            print(f"- {r['metadata']['name']} (Aadhaar: {r['metadata']['aadhaar']})")
            
        print("\nSUCCESS: Data appears to be present.")
    else:
        print("WARNING: No results found for query 'Kumar'.")

if __name__ == "__main__":
    verify_citizens()
