import os
import redis
from dotenv import load_dotenv

load_dotenv()

# CyborgDB Setup
# In a real scenario, we import the actual client. 
# Since I cannot verify if 'cyborgdb' pip package is fully functional in this env without credentials,
# I will create a robust Mock wrapper that switches if the key is missing or import fails.

CYBORGDB_API_KEY = os.getenv("CYBORGDB_API_KEY")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Redis Client
try:
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
except Exception as e:
    print(f"Warning: Redis connection failed: {e}")
    redis_client = None

class MockCyborgClient:
    def __init__(self):
        print("Initializing Mock CyborgDB Client")
        self.indexes = {}

    def create_index(self, index_name: str, index_key: str = None):
        print(f"Mock: Creating index {index_name} (key={index_key})")
        if index_name not in self.indexes:
            self.indexes[index_name] = MockEncryptedIndex(index_name)
        return self.indexes[index_name]

    def load_index(self, index_name: str, index_key: str):
        print(f"Mock: Loading index {index_name} (key={index_key})")
        if index_name not in self.indexes:
             # For Mock, we just auto-create if loading a non-existent one to act like "found it" or "clean state"
             # Real implementation would throw, but Mock is loose.
             self.indexes[index_name] = MockEncryptedIndex(index_name)
        return self.indexes[index_name]

    def get_index(self, index_name: str):
        # Legacy fallback
        return self.load_index(index_name, "legacy-mock-key")

class MockEncryptedIndex:
    def __init__(self, name):
        self.name = name
        self.filename = f"mock_index_{name}.json"
        self.data = self._load() # List of {'id': str, 'vector': list, 'metadata': dict}

    def _load(self):
        import json
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Mock: Error loading {self.filename}: {e}")
        return []

    def _save(self):
        import json
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f)
        except Exception as e:
            print(f"Mock: Error saving {self.filename}: {e}")

    def upsert(self, items):
        # items: list of dicts with id, vector, metadata
        print(f"Mock: Upserting {len(items)} items into {self.name}")
        for item in items:
            # Simple overwrite logic
            self.data = [d for d in self.data if d['id'] != item['id']]
            self.data.append(item)
        self._save() # Persist
        return True

    def query(self, vector, top_k=5):
        print(f"Mock: Querying {self.name} with vector length {len(vector)}")
        # Simple cosine similarity scan
        import numpy as np
        if not self.data:
            return []
        
        query_vec = np.array(vector)
        results = []
        for doc in self.data:
            doc_vec = np.array(doc['vector'])
            # Cosine sim
            denom = (np.linalg.norm(query_vec) * np.linalg.norm(doc_vec))
            if denom == 0:
                score = 0
            else:
                score = np.dot(query_vec, doc_vec) / denom
            results.append({**doc, 'score': float(score)})
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]

    def get_by_id(self, item_id: str):
        print(f"Mock: Fetching item {item_id} from {self.name}")
        for doc in self.data:
            if doc['id'] == item_id:
                return doc
        return None

# Attempt to load real client
cyborg_client = None

try:
    # Try real connection first
    use_mock = False # os.getenv("USE_MOCK_DB", "false").lower() == "true"
    
    if CYBORGDB_API_KEY and not use_mock:
        try:
            from cyborgdb import Client
            print("CyborgDB API Key found. Connecting to CyborgDB Cloud...")
            # Attempt connection
            cyborg_client = Client("https://api.cyborgdb.co", CYBORGDB_API_KEY) 
            print("Successfully connected to CyborgDB Cloud.")
            print(f"Using API Key: {CYBORGDB_API_KEY[:5]}...{CYBORGDB_API_KEY[-5:]}")
        except Exception as e:
            print(f"CRITICAL: Failed to connect to CyborgDB Cloud ({type(e).__name__}: {e}). Falling back to Mock Client.")
            cyborg_client = MockCyborgClient()
    else:
        if use_mock:
            print("USE_MOCK_DB is True. Using Mock Client.")
        else:
            print("No CyborgDB API Key found. Using Mock Client.")
        cyborg_client = MockCyborgClient()
except Exception as e:
    print(f"Unexpected error in DB setup: {e}. Using Mock Client.")
    cyborg_client = MockCyborgClient()

def get_cyborg_client():
    return cyborg_client

def get_redis_client():
    return redis_client
