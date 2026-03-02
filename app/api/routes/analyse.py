from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def analyse_root():
    return {"message": "Analyse endpoint is working!"}