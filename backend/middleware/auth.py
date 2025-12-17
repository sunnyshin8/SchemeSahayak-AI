from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import os

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "agency-secret-123")

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Only protect agency routes (excluding login if we had one on backend, 
        # but here we just check for token on sensitive actions)
        
        # We protect POST requests to /api/agency/*
        if request.url.path.startswith("/api/agency/") and request.method == "POST":
            token = request.headers.get("Authorization")
            if token != f"Bearer {ADMIN_TOKEN}":
                return JSONResponse(status_code=401, content={"detail": "Unauthorized: Invalid Agency Token"})
        
        return await call_next(request)
