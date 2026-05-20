from fastapi import APIRouter
from pydantic import BaseModel
from app.services.vector_service import search_similar
from app.services.ai_service import summarize_text

router = APIRouter()

class Question(BaseModel):
    question: str


@router.post("/")
def ask_question(data: Question):

    relevant_chunks = search_similar(data.question)

    context = "\n".join(relevant_chunks)

    prompt = f"""
    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {data.question}
    """

    answer = summarize_text(prompt)

    return {"answer": answer}