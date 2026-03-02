from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def ask_root():
    return {"message": "Ask endpoint is working!"}