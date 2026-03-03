from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def analyse_root():
    return {"message": "Analyse endpoint is working!"}