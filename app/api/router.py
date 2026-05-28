from fastapi import APIRouter
from app.api.routes import upload, analyse, ask, summary, documents


api_router = APIRouter()
api_router.include_router(upload.router, prefix="/upload", tags=["Upload"])
api_router.include_router(analyse.router, prefix="/analyse", tags=["Analyse"])
api_router.include_router(ask.router, prefix="/ask", tags=["Ask"])
api_router.include_router(summary.router, prefix="/summary", tags=["Summary"])
api_router.include_router(documents.router, prefix="/documents", tags=["Documents"])