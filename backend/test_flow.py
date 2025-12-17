import requests
import json
import time

BASE_URL = "http://localhost:8000/api"

def test_search():
    print("\n--- Testing Citizen Search ---")
    query = "I need financial help for farming"
    print(f"Query: {query}")
    
    try:
        response = requests.post(f"{BASE_URL}/citizen/search", json={"query": query})
        if response.status_code == 200:
            results = response.json().get("results", [])
            print(f"Success! Found {len(results)} schemes.")
            for r in results:
                print(f" - {r['metadata']['title']} (Score: {r['score']:.2f})")
        else:
            print(f"Failed. Status: {response.status_code}, Msg: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def test_verification():
    print("\n--- Testing Agency Verification ---")
    
    citizen_data = {
        "citizen_id": "9999-8888-7777",
        "name": "Ramesh Gupta",
        "details": "Farmer from Uttar Pradesh seeking subsidy"
    }
    
    # 1. Register
    print("Registering citizen...")
    requests.post(f"{BASE_URL}/agency/register", json=citizen_data)
    
    # 2. Verify (Fraud Check)
    print("Verifying same citizen (should detect match)...")
    response = requests.post(f"{BASE_URL}/agency/verify", json=citizen_data)
    
    if response.status_code == 200:
        data = response.json()
        if data['is_fraud']:
            print("Success! Fraud/Duplicate detected.")
            print(f"Match Details: {data['match_details']['metadata']}")
        else:
            print("Failed. Should have detected fraud but didn't.")
    else:
        print(f"Verification call failed: {response.status_code}")

if __name__ == "__main__":
    print("Waiting for server to be ready...")
    # Health check
    try:
        requests.get("http://localhost:8000/")
        test_search()
        test_verification()
    except:
        print("Server not running. Please start backend first.")
