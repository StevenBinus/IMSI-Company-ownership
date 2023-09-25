from fastapi import Request
from src.configs.database import SessionLocal
from starlette.middleware.base import BaseHTTPMiddleware

class DBTransactionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request, call_next):
        request.state.db = SessionLocal()
        response = await call_next(request)
        request.state.db.close()
        return response
        