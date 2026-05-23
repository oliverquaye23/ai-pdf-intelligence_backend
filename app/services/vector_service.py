import chromadb
from fastembed import TextEmbedding

# Load embedding model
embedding_model = TextEmbedding("BAAI/bge-small-en-v1.5")

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
    embeddings = list(embedding_model.embed(chunks))
    ids = [f"{document_id}_chunk_{i}" for i in range(len(chunks))]
    collection.add(
        embeddings=embeddings,
        documents=chunks,
        ids=ids
    )


def search_similar(query):
    query_embedding = list(embedding_model.embed([query]))
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )
    return results["documents"][0]