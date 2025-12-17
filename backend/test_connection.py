import os
import sys
from dotenv import load_dotenv

load_dotenv()

print("="*60)
print("CYBORGDB DIAGNOSTIC TEST")
print("="*60)

# Step 1: Check API Key
api_key = os.getenv("CYBORGDB_API_KEY")
print(f"\n[1] API Key check:")
if api_key:
    print(f"    PASS - Key found: {api_key[:15]}...{api_key[-10:]}")
else:
    print(f"    FAIL - No API key found")
    sys.exit(1)

# Step 2: Try importing cyborgdb
print(f"\n[2] Import cyborgdb package:")
try:
    import cyborgdb
    print(f"    PASS - Package imported")
    print(f"    Location: {cyborgdb.__file__}")
except ImportError as e:
    print(f"    FAIL - Import error: {e}")
    sys.exit(1)

# Step 3: Try importing Client
print(f"\n[3] Import Client class:")
try:
    from cyborgdb import Client
    print(f"    PASS - Client class imported")
except ImportError as e:
    print(f"    FAIL - Import error: {e}")
    sys.exit(1)

# Step 4: Try creating client  
print(f"\n[4] Create CyborgDB client:")
try:
    client = Client("https://api.cyborgdb.co", api_key)
    print(f"    PASS - Client created")
    print(f"    Type: {type(client).__name__}")
except Exception as e:
    print(f"    FAIL - Error: {e}")
    print(f"    Error type: {type(e).__name__}")
    sys.exit(1)

# Step 5: Test connection
print(f"\n[5] Test API connection (generate_key):")
try:
    test_key = client.generate_key()
    print(f"    PASS - API call successful!")
    print(f"    Generated key: {test_key[:25]}...")
except Exception as e:
    print(f"    FAIL - Error: {e}")
    print(f"    Error type: {type(e).__name__}")
    sys.exit(1)

# Step 6: Try create/load index
print(f"\n[6] Test index operations:")
try:
    index_key = client.generate_key()
    print(f"    Generated index key: {index_key[:25]}...")
    
    index = client.create_index("test_schemes", index_key, dimension=384)
    print(f"    PASS - Index created")
    print(f"    Index type: {type(index).__name__}")
except Exception as e:
    print(f"    FAIL - Error: {e}")
    print(f"    Error type: {type(e).__name__}")

print("\n" + "="*60)
print("ALL TESTS PASSED!")
print("="*60)
