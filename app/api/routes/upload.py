from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.storage_service import save_uploaded_file
from app.services.pdf_service import extract_text_from_pdf
from uuid import uuid4
import os

router = APIRouter()

ALLOWED_TYPES = ['application/pdf']

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    #File type validation
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400,detail="PDF files only")
    
    #Generate unique document id
    document_id = str(uuid4())

    #Save file
    try:
        file_path = await save_uploaded_file(file,document_id)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

    return {
        "message": "Upload endpoint is working!",
        "document_id": document_id,
        "file_path": file_path
        }

