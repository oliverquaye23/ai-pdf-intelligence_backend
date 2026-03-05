from fastapi import FastAPI
from app.api.router import api_router
from dotenv import load_dotenv
from app.db.database import  engine
from app.db.models import Base


#Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI(title="AI-PDF-Intelligence API")
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": " AI-PDF-Intelligence API running successfully!"}