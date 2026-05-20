from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.database import get_db
from app.db.models import PDFDocument as Document
from app.services.ai_service import summarize_text

router = APIRouter()

class AnalyseRequest(BaseModel):
    document_id: str


@router.post("/")
def analyse_document(data: AnalyseRequest, db: Session = Depends(get_db)):

    # Fetch document from database
    document = db.query(Document).filter(Document.id == data.document_id).first()

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    # If summary already exists, return it without calling the LLM again
    if document.summary:
        return {
            "document_id": data.document_id,
            "summary": document.summary,
            "cached": True
        }

    # Generate summary using LLM
    summary = summarize_text(document.extracted_text)

    # Save summary back to database
    document.summary = summary
    db.commit()

    return {
        "document_id": data.document_id,
        "summary": summary,
        "cached": False
    }