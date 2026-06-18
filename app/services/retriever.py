from sklearn.metrics.pairwise import cosine_similarity
from services.embeddings import get_embedding

def retrieve(
    query_embedding,
    chunks,
    chunks_embeddings,
    top_k=3
) :
   # query_vector = get_embedding(query)
    
    scores = []
    
    for chunk, embedding in zip(
        chunks,
        chunks_embeddings
    ):
        similarity = cosine_similarity(
            [query_embedding],
            [embedding]
        )[0][0]
        
        scores.append((chunk, similarity))
        
    
    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )
    
    return scores[:top_k]