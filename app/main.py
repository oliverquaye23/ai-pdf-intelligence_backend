from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="AI-PDF-Intelligence API")
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": " AI-PDF-Intelligence API running successfully!"}