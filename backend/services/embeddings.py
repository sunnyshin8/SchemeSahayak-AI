from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self, model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def encode(self, text: str):
        # returns numpy array, convert to list
        params = {'normalize_embeddings': True}
        return self.model.encode(text, **params).tolist()

    def encode_batch(self, texts: list):
        params = {'normalize_embeddings': True}
        embeddings = self.model.encode(texts, **params)
        return embeddings.tolist()

# Singleton instance
embedding_service = EmbeddingService()

def get_embedding_service():
    return embedding_service
