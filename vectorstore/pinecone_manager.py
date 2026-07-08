from pinecone import Pinecone
from typing import List
import uuid

from langchain_core.documents import Document

from embeddings.embedding_manager import EmbeddingManager
import config


class PineconeManager:
    """
    Handles all interactions with Pinecone.
    """

    def __init__(self):

        self.pc = Pinecone(
            api_key=config.PINECONE_API_KEY
        )

        self.index = self.pc.Index(
            config.PINECONE_INDEX_NAME
        )

        self.embedding_manager = EmbeddingManager()

    def get_index(self):
        """
        Returns the Pinecone index object.
        """
        return self.index

    def describe_index(self):
        """
        Returns Pinecone index statistics.
        """
        return self.index.describe_index_stats()

    def upload_documents(self, documents: List[Document]) -> int:
        """
        Upload LangChain documents to Pinecone.
        """

        vectors = []

        for doc in documents:

            embedding = self.embedding_manager.embed_query(
                doc.page_content
            )

            vector = {

                "id": str(uuid.uuid4()),

                "values": embedding,

                "metadata": {

                    **doc.metadata,

                    "text": doc.page_content

                }

            }

            vectors.append(vector)

        self.index.upsert(
            vectors=vectors
        )

        return len(vectors)

    def similarity_search(
        self,
        query: str,
        top_k: int = config.TOP_K
    ):
        """
        Perform semantic similarity search in Pinecone.
        """

        # Generate embedding for the user's query
        query_embedding = self.embedding_manager.embed_query(query)

        # Search Pinecone
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True,
            include_values=False
        )

        # Filter results using similarity threshold
        filtered_matches = [
            match
            for match in results["matches"]
            if match["score"] >= config.SIMILARITY_THRESHOLD
        ]

        results["matches"] = filtered_matches

        return results
    
    def clear_index(self):
        """
        Deletes all vectors from the Pinecone index.
        """

        self.index.delete(delete_all=True)

        print("All vectors deleted successfully.")