from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.cyborg import get_cyborg_service

from services.llm import get_llm_service

router = APIRouter()
cyborg_service = get_cyborg_service()
llm_service = get_llm_service()

class SearchQuery(BaseModel):
    query: str

class ChatRequest(BaseModel):
    question: str

@router.post("/search")
async def search_schemes(search: SearchQuery):
    try:
        results = cyborg_service.search_schemes(search.query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/scheme/{scheme_id}")
async def get_scheme_details(scheme_id: str):
    scheme = cyborg_service.get_scheme_by_id(scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    return scheme

@router.post("/scheme/{scheme_id}/chat")
async def chat_scheme(scheme_id: str, req: ChatRequest):
    scheme = cyborg_service.get_scheme_by_id(scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    
    # Construct context from scheme details
    meta = scheme.get('metadata', {})
    context = f"Title: {meta.get('title', 'Unknown')}\n"
    context += f"Description: {meta.get('description', '')}\n"
    context += f"Full Metadata: {meta}"
    
    answer = llm_service.chat_about_scheme(context, req.question)
    return {"answer": answer}
