from typing import List

from langchain_huggingface import HuggingFaceEmbeddings

import config


class EmbeddingManager:
    """
    Manages the embedding model used throughout the application.
    """

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=config.EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    def get_embedding_model(self):
        """
        Returns the initialized embedding model.
        """
        return self.embedding_model

    def embed_query(self, text: str) -> List[float]:
        """
        Generate an embedding for a single query/document.
        """
        return self.embedding_model.embed_query(text)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple documents.
        """
        return self.embedding_model.embed_documents(texts)