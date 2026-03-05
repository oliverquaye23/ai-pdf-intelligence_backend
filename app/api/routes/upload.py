from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import uuid4

from app.db.database import get_db
from app.db.models import PDFDocument as Document
from app.services.storage_service import save_uploaded_file
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter()


@router.post("/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    # create document id
    document_id = str(uuid4())

    #  save file
    file_path = await save_uploaded_file(file, document_id)

    # extract text
    extracted_text = extract_text_from_pdf(file_path)

    # save to database
    document = Document(
        id=document_id,
        file_path=file_path,
        extracted_text=extracted_text,
        summary=""
    )

    db.add(document)
    db.commit()

    return {
        "message": "File uploaded successfully",
        "document_id": document_id
    }