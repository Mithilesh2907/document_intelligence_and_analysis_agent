from services.embeddings import get_embedding

vector = get_embedding(
    "Warranty period is 24 months from date of purchase."
)

print(len(vector))