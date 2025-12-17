import os
from dotenv import load_dotenv

load_dotenv()

CYBORGDB_API_KEY = os.getenv("CYBORGDB_API_KEY")
print(f"Testing CyborgDB Connection with Key: {CYBORGDB_API_KEY[:10]}...")

try:
    from cyborgdb import Client
    client = Client(api_key=CYBORGDB_API_KEY)
    print("Client initialized successfully.")
    
    # Try to verify auth by listing indexes (if method exists) or creating one
    # Assuming list_indexes() exists or similar. Checking dir(client)
    print("Client attributes:", dir(client))
    
    # Just creating a dummy index to test connectivity
    # index = client.create_index("test_connectivity", 4)
    # print("Index created/accessed.")
    
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Connection Failed: {e}")
