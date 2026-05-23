import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

_client = None

def get_client():
    global _client
    if _client is None:
        _client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    return _client

def summarize_text(text: str) -> str:
    text = text[:4000]

    response = get_client().chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions and summarizes documents clearly."},
            {"role": "user", "content": text}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content