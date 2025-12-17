from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.cyborg import get_cyborg_service

router = APIRouter()
cyborg_service = get_cyborg_service()

class VerifyRequest(BaseModel):
    citizen_id: str
    name: str
    details: str 

@router.post("/verify")
async def verify_beneficiary(req: VerifyRequest):
    # Construct a profile string to check similarity
    profile_text = f"{req.name} {req.details}"
    is_fraud, match = cyborg_service.verify_beneficiary(profile_text)
    
    return {
        "is_fraud": is_fraud,
        "match_details": match if is_fraud else None
    }

@router.post("/register")
async def register_beneficiary(req: VerifyRequest):
    profile_text = f"{req.name} {req.details}"
    cyborg_service.index_citizen(req.citizen_id, profile_text, {"name": req.name})
    return {"status": "success", "message": "Beneficiary registered securely in CyborgDB"}
