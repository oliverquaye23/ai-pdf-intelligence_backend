from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def summary_root():
    return {"message": "Summary endpoint is working!"}