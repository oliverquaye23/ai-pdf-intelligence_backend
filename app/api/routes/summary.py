from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import PDFDocument as Document

router = APIRouter()


@router.get("/{document_id}")
def get_summary(document_id: str, db: Session = Depends(get_db)):

    document = db.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    if not document.summary:
        raise HTTPException(
            status_code=400,
            detail="No summary found for this document. Call /analyse first."
        )

    return {
        "document_id": document_id,
        "summary": document.summary
    }