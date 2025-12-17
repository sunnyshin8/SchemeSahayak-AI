import requests
import json

URL = "http://localhost:8000/api/citizen/search"

queries = ["farmer", "loan", "housing", "health"]

print(f"Testing Search API at {URL}")

for q in queries:
    print(f"\nQuery: {q}")
    try:
        response = requests.post(URL, json={"query": q})
        if response.status_code == 200:
            results = response.json().get("results", [])
            print(f"Status: 200 OK. Found {len(results)} results.")
            for r in results:
                print(f" - {r['metadata']['title']} (Score: {r['score']})")
                if 'backing_scheme_name' in r['metadata']:
                     print(f"   [Backed by: {r['metadata']['backing_scheme_name']}]")
        else:
            print(f"Status: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")
