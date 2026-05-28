from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import PDFDocument as Document

router = APIRouter()

@router.get("/")
def get_documents(db: Session = Depends(get_db)):
    documents = db.query(Document).order_by(Document.created_at.desc()).all()
    
    return [
        {
            "id": doc.id,
            "file_path": doc.file_path,
            "summary": doc.summary,
            "created_at": doc.created_at
        }
        for doc in documents
    ]