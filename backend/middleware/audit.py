from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from models import log_audit
import json

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Only log Agency actions
        if "/api/agency/" in request.url.path and request.method == "POST":
            # We can't easily read body here without consuming it, 
            # so we'll log the path and status for now. 
            # For detailed body logging, we'd need a more complex wrapper, 
            # but for MVP this confirms usage.
            
            try:
                details = {
                    "path": request.url.path,
                    "method": request.method,
                    "status_code": response.status_code
                }
                log_audit("AGENCY_ACTION", details)
            except:
                pass
                
        return response
