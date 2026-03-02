from fastapi import APIRouter
from app.api.routes import upload, analyse, ask, summary

api_router = APIRouter()
api_router.include_router(upload.router, prefix="/upload", tags=["Upload"])
api_router.include_router(analyse.router, prefix="/analyse", tags=["Analyse"])