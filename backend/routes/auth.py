from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.cyborg import get_cyborg_service
import hashlib

router = APIRouter()

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/register")
async def register(user: UserRegister):
    service = get_cyborg_service()
    
    # Check if user already exists
    existing = service.get_user(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password
    hashed = hash_password(user.password)
    
    try:
        # Pass email as user_id as well
        service.register_user(user.email, user.email, hashed, user.name)
        return {"message": "User registered successfully", "user": {"name": user.name, "email": user.email}}
    except Exception as e:
        print(f"Register Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login(creds: UserLogin):
    service = get_cyborg_service()
    
    user_doc = service.get_user(creds.email)
    if not user_doc:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Check password
    stored_hash = user_doc['metadata'].get('password_hash')
    if hash_password(creds.password) != stored_hash:
         raise HTTPException(status_code=401, detail="Invalid credentials")
         
    return {
        "message": "Login successful",
        "user": {
            "name": user_doc['metadata'].get('name'),
            "email": user_doc['metadata'].get('email'),
            "role": user_doc['metadata'].get('role')
        }
    }
