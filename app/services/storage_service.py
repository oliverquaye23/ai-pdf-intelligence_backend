import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

async def save_uploaded_file(file: UploadFile, document_id: str) -> str:
    # Ensure upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Create a unique file path
    file_path = os.path.join(UPLOAD_DIR, f"{document_id}.pdf")

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)   

    return file_path