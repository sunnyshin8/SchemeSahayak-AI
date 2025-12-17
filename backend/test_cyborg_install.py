#!/usr/bin/env python
import sys

print("Testing CyborgDB installation...")
print("-" * 50)

try:
    import cyborgdb
    print(f"✓ cyborgdb package is installed")
    print(f"  Module: {cyborgdb}")
    
    from cyborgdb import Client
    print(f"✓ Can import Client class")
    
    # Test with your API key
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("CYBORGDB_API_KEY")
    if api_key:
        print(f"✓ API Key found: {api_key[:15]}...")
        
        try:
            client = Client("https://api.cyborgdb.co", api_key)
            print(f"✓ Client created successfully!")
            print(f"  Type: {type(client)}")
            
            # Try generating a key
            print("\nTesting API connection...")
            key = client.generate_key()
            print(f"✓ Connection successful! Generated key: {key[:30]}...")
            
        except Exception as e:
            print(f"✗ Error creating client or connecting: {e}")
    else:
        print("✗ No API key found in environment")
        
except ImportError as e:
    print(f"✗ cyborgdb package NOT installed")
    print(f"  Error: {e}")
    sys.exit(1)

print("-" * 50)
print("Test complete!")
