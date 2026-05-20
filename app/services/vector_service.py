import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Chroma
client = chromadb.PersistentClient(path="./chromadb_store")

collection = client.get_or_create_collection(name="pdf_documents")


def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def store_document(text, document_id):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks).tolist()

    # Namespace chunk IDs with document_id to avoid collisions
    ids = [f"{document_id}_chunk_{i}" for i in range(len(chunks))]

    collection.add(
        embeddings=embeddings,
        documents=chunks,
        ids=ids
    )

def search_similar(query):

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return results["documents"][0]