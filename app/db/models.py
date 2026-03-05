from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from app.db.database import Base    

class PDFDocument(Base):
    __tablename__ = "pdf_documents"

    id = Column(String, primary_key=True, index=True)
    file_path = Column(String, nullable=False)
    extracted_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False, default="")
    created_at = Column(DateTime, default=datetime.utcnow)