from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.router import api_router
from dotenv import load_dotenv
from app.db.database import engine
from app.db.models import Base
import os

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs on startup
    Base.metadata.create_all(bind=engine)
    yield
    # Runs on shutdown (nothing needed here yet)

app = FastAPI(title="AI-PDF-Intelligence API", lifespan=lifespan)
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "AI-PDF-Intelligence API running successfully!"}