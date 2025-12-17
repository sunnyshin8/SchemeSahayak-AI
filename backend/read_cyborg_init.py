import cyborgdb
import os
import inspect

try:
    print(f"CyborgDB File: {cyborgdb.__file__}")
    
    # Try reading the file content
    with open(cyborgdb.__file__, 'r') as f:
        print("--- CONTENT START ---")
        print(f.read())
        print("--- CONTENT END ---")

    # If Client is imported in init, check where it comes from
    if hasattr(cyborgdb, 'Client'):
        print("Client found in init.")
        from cyborgdb import Client
        print(f"Client Init Signature: {inspect.signature(Client.__init__)}")
    else:
        print("Client NOT found in init.")

except Exception as e:
    print(f"Error: {e}")
