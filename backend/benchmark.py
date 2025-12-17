import time
import os
import random
import uuid
from services.cyborg import get_cyborg_service
from database import get_cyborg_client

def run_benchmarks():
    print("="*50)
    print("SchemeSahayak - CyborgDB Performance Benchmarks")
    print("="*50)

    service = get_cyborg_service()
    client = get_cyborg_client()
    
    # Check if using Mock or Real
    mode = "MOCK" if hasattr(client, 'indexes') else "REAL (CyborgDB Cloud)"
    print(f"Database Mode: {mode}")
    print("-" * 50)

    # 1. Ingestion Benchmark
    print("\n[1] Ingestion Benchmark")
    num_schemes = 20
    print(f"Ingesting {num_schemes} dummy schemes...")
    
    start_time = time.time()
    for i in range(num_schemes):
        scheme_id = f"bench-scheme-{uuid.uuid4()}"
        title = f"Benchmark Scheme {i}"
        desc = f"This is a description for benchmark scheme {i}. It provides financial aid."
        meta = {"category": "Benchmark"}
        service.index_scheme(scheme_id, title, desc, meta)
    end_time = time.time()
    
    ingest_duration = end_time - start_time
    print(f"Total Time: {ingest_duration:.4f}s")
    print(f"Avg Time per Record: {ingest_duration/num_schemes:.4f}s")

    # 2. Search Benchmark
    print("\n[2] Search Benchmark")
    query = "financial aid for farmers"
    print(f"Searching for: '{query}'")
    
    start_time = time.time()
    results = service.search_schemes(query, top_k=5)
    end_time = time.time()
    
    search_duration = end_time - start_time
    print(f"Search Time: {search_duration:.4f}s")
    print(f"Results Found: {len(results)}")

    # 3. Verification/Encrypted Search Benchmark
    print("\n[3] Verification (Encrypted Search) Benchmark")
    # First index a citizen
    citizen_id = f"citizen-{uuid.uuid4()}"
    profile_text = "Farmer with 2 acres land, income 50000, age 45."
    service.index_citizen(citizen_id, profile_text, {"name": "Test User"})
    
    print("Verifying duplicate beneficiary...")
    start_time = time.time()
    is_fraud, details = service.verify_beneficiary(profile_text)
    end_time = time.time()
    
    verify_duration = end_time - start_time
    print(f"Verification Time: {verify_duration:.4f}s")
    print(f"Match Found: {is_fraud}")
    
    print("\n" + "="*50)
    print("BENCHMARK COMPLETE")
    print("="*50)

if __name__ == "__main__":
    run_benchmarks()
