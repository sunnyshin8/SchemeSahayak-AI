from dotenv import load_dotenv
import os
import time

load_dotenv()
KEY = os.getenv("CYBORGDB_API_KEY")

try:
    from cyborgdb import Client
    print("Imported Client.")
except ImportError:
    print("Could not import Client.")
    exit()

print(f"Key: {KEY[:5]}...")

# Attempt 1: Positional Key
print("\n--- Attempt 1: Client(KEY) ---")
try:
    c = Client(KEY)
    print("Success?")
    try:
        c.get_index("test")
        print("Detailed verification: get_index working.")
    except Exception as e:
        print(f"Client created but errored on usage: {e}")
except Exception as e:
    print(f"Failed: {e}")

# Attempt 2: URL + Key
print("\n--- Attempt 2: Client('https://api.cyborgdb.co', KEY) ---")
try:
    c = Client('https://api.cyborgdb.co', KEY)
    print("Success?")
except Exception as e:
    print(f"Failed: {e}")

# Attempt 3: Key + URL
print("\n--- Attempt 3: Client(KEY, 'https://api.cyborgdb.co') ---")
try:
    c = Client(KEY, 'https://api.cyborgdb.co')
    print("Success?")
except Exception as e:
    print(f"Failed: {e}")
