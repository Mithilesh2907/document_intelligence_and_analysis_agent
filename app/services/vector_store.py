from services.embeddings import get_embedding

# Simulates chromeDB

class InMemoryVectorStore:
    def __init__(self) :
        self.chunks = []
        self.embeddings = []
    
    def add_chunks(self, chunks) :
        for chunk in chunks :
            self.chunks.append(chunk)
            
            self.embeddings.append(
                get_embedding(chunk)
            )