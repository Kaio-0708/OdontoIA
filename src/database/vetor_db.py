import chromadb
from chromadb.config import Settings
import uuid
   
"""
Cria e gerencia uma coleção no ChromaDB para 
armazenar textos convertidos em embeddings vetoriais.
"""

def initDB(persist_directory="db"):
    client = chromadb.Client(
        Settings(
            persist_directory=persist_directory,
            anonymized_telemetry=False
        )
    )

    collection = client.get_or_create_collection(
        name="rag_collection"
    )

    return collection


def addChunks(collection, chunks, embedding_function):
    
    embeddings = []
    ids = []

    for i, chunk in enumerate(chunks):
        emb = embedding_function(chunk)
        embeddings.append(emb)
        ids.append(str(uuid.uuid4()))

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )


def search(collection, query_text, embedding_function, k=3):
    query_embedding = embedding_function(query_text)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return {
        "documents": results["documents"][0],
        "distances": results["distances"][0],
        "ids": results["ids"][0]
    }