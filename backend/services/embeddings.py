import os
import numpy as np
from sentence_transformers import SentenceTransformer

class DummyModel:
    def encode(self, texts, **kwargs):
        if isinstance(texts, list):
            return np.random.rand(len(texts), 384)
        return np.random.rand(384)

class EmbeddingService:
    def __init__(self, model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'):
        if True: # os.getenv("USE_DUMMY_EMBEDDINGS", "false").lower() == "true":
             print("Using Dummy Embedding Model (Forced)")
             self.model = DummyModel()
        else:
             print(f"Loading embedding model: {model_name}")
             self.model = SentenceTransformer(model_name)

    def encode(self, text: str):
        # returns numpy array, convert to list
        params = {'normalize_embeddings': True}
        result = self.model.encode(text, **params)
        if hasattr(result, 'tolist'):
             return result.tolist()
        return result

    def encode_batch(self, texts: list):
        params = {'normalize_embeddings': True}
        embeddings = self.model.encode(texts, **params)
        if hasattr(embeddings, 'tolist'):
             return embeddings.tolist()
        return embeddings

# Singleton instance
embedding_service = EmbeddingService()

def get_embedding_service():
    return embedding_service
