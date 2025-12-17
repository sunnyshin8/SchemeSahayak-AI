import os
import sys
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("CyborgDB Connection Diagnostic")
print("=" * 50)

# Check API Key
api_key = os.getenv("CYBORGDB_API_KEY")
print(f"\n1. API Key found: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"   Key preview: {api_key[:10]}...{api_key[-5:]}")

# Check if cyborgdb package is installed
print("\n2. Checking cyborgdb package...")
try:
    import cyborgdb
    print("   ✓ cyborgdb package is installed")
    print(f"   Module location: {cyborgdb.__file__}")
except ImportError as e:
    print(f"   ✗ cyborgdb package NOT installed: {e}")

# Try to create a client
print("\n3. Attempting to create CyborgDB client...")
try:
    from cyborgdb import Client
    if api_key:
        client = Client("https://api.cyborgdb.co", api_key)
        print("   ✓ Client created successfully!")
        print(f"   Client type: {type(client)}")
        
        # Try to generate a key (this should make a request to CyborgDB)
        print("\n4. Testing connection by generating a key...")
        try:
            test_key = client.generate_key()
            print(f"   ✓ Connection successful! Generated key: {test_key[:20]}...")
        except Exception as e:
            print(f"   ✗ Key generation failed: {e}")
    else:
        print("   ✗ No API key available to create client")
except ImportError as e:
    print(f"   ✗ Cannot import Client: {e}")
except Exception as e:
    print(f"   ✗ Error creating client: {e}")

print("\n" + "=" * 50)
