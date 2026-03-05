from PyPDF2 import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            text = ''
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"  # preserve page breaks
            return text.strip()
    except Exception as e:
        raise RuntimeError(f"Error extracting text from PDF '{file_path}': {e}")