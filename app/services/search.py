from services.embeddings import get_embedding
from services.retriever import retrieve

def search(query, vector_store) :
    query_embedding = get_embedding(query)
    
    results = retrieve(
        query_embedding,
        vector_store.chunks,
        vector_store.embeddings
    )
    
    return results