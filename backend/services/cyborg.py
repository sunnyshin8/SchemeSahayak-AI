import os
import json
from database import get_cyborg_client
from services.embeddings import get_embedding_service

KEYS_FILE = "cyborg_keys.json"

def get_or_create_key(index_name: str, client):
    keys = {}
    if os.path.exists(KEYS_FILE):
        try:
            with open(KEYS_FILE, 'r') as f:
                keys = json.load(f)
        except:
             pass
    
    if index_name in keys:
        # Convert hex string back to bytes
        key_str = keys[index_name]
        try:
             return bytes.fromhex(key_str)
        except ValueError:
             # If it was a legacy string key (unlikely in this context but safe to handle), regenerate
             pass
    
    # Generate new key
    if hasattr(client, 'generate_key'):
        # Real Client - returns bytes
        new_key = client.generate_key()
    else:
        # Mock Client fallback
        # Generate a valid 32-byte key
        new_key = os.urandom(32)
        
    # Convert bytes to hex string for JSON storage
    key_to_store = new_key.hex()
        
    keys[index_name] = key_to_store
    with open(KEYS_FILE, 'w') as f:
        json.dump(keys, f)
    
    return new_key

class CyborgService:
    def __init__(self):
        self.client = get_cyborg_client()
        self.embedder = get_embedding_service()
        # Initialize indexes with keys
        self.scheme_index = self._init_index("schemes")
        self.citizen_index = self._init_index("citizens")
        self.user_index = self._init_index("users")

    def _init_index(self, name: str):
        key = get_or_create_key(name, self.client)
        
        # Try to load, if fails (or doesn't exist), create
        # Check if Real Client methods exist
        if hasattr(self.client, 'load_index') and hasattr(self.client, 'create_index'):
            try:
                # Try loading checking if it works
                return self.client.load_index(name, key)
            except Exception as e:
                print(f"Index {name} load failed/not found ({e}). Creating new...")
                return self.client.create_index(name, key)
        else:
            # Fallback for Mock Client (simplistic create/get)
            if hasattr(self.client, 'create_index'):
                 return self.client.create_index(name, key)
            return self.client.get_index(name)

    def register_user(self, user_id: str, email: str, password_hash: str, name: str):
        # We need a vector, so we embed the name/email, though we won't use it for auth search
        text_to_embed = f"{name} {email}"
        vector = self.embedder.encode(text_to_embed)
        
        item = {
            "id": email, # Use email as ID for easy lookup
            "vector": vector,
            "metadata": {
                "name": name,
                "email": email,
                "password_hash": password_hash,
                "role": "user"
            }
        }
        return self.user_index.upsert([item])

    def get_user(self, email: str):
        # Retrieve user by email (ID)
        if hasattr(self.user_index, 'get_by_id'):
            return self.user_index.get_by_id(email)
        return None

    def index_scheme(self, scheme_id: str, title: str, description: str, metadata: dict):
        text_to_embed = f"{title}. {description}"
        vector = self.embedder.encode(text_to_embed)
        
        item = {
            "id": scheme_id,
            "vector": vector,
            "metadata": {**metadata, "title": title, "description": description}
        }
        return self.scheme_index.upsert([item])

    def search_schemes(self, query: str, top_k: int = 5):
        vector = self.embedder.encode(query)
        results = self.scheme_index.query(vector, top_k=top_k)
        return results

    def get_scheme_by_id(self, scheme_id: str):
        # Using the new get_by_id method, works for Mock.
        # For Real CyborgDB, we would use fetch or similar if available, 
        # but since we are forcing mock/hybrid, this is safe.
        if hasattr(self.scheme_index, 'get_by_id'):
            return self.scheme_index.get_by_id(scheme_id)
        return None

    def index_citizen(self, citizen_id: str, profile_text: str, metadata: dict):
        # For deduplication/fraud check
        vector = self.embedder.encode(profile_text)
        item = {
            "id": citizen_id,
            "vector": vector,
            "metadata": metadata
        }
        return self.citizen_index.upsert([item])

    def verify_beneficiary(self, profile_text: str, threshold: float = 0.85):
        vector = self.embedder.encode(profile_text)
        results = self.citizen_index.query(vector, top_k=1)
        
        if not results:
            return False, None
            
        top_match = results[0]
        if top_match['score'] >= threshold:
            return True, top_match # Fraud/Duplicate detected
        return False, None

cyborg_service = CyborgService()

def get_cyborg_service():
    return cyborg_service
