from ingestion.document_loader import DocumentLoader
from chunking.chunker import Chunker
from vectorstore.pinecone_manager import PineconeManager
from llm.groq_manager import GroqManager


class RAGPipeline:
    """
    End-to-end Retrieval Augmented Generation pipeline.
    """

    def __init__(self):

        self.loader = DocumentLoader()
        self.chunker = Chunker()
        self.vectorstore = PineconeManager()
        self.llm = GroqManager()

    def ingest_document(self, file_path: str):
        """
        Loads, chunks, and uploads a document to Pinecone.
        """

        # Clear previous vectors
        self.vectorstore.clear_index()

        # Load document
        documents = self.loader.load(file_path)

        # Chunk document
        chunks = self.chunker.split_documents(documents)

        # Upload chunks
        uploaded = self.vectorstore.upload_documents(chunks)

        return uploaded

    def ask(
        self,
        question: str,
        chat_history: str = ""
    ):
        """
        Ask a question against the uploaded document.
        """

        # Retrieve relevant chunks
        results = self.vectorstore.similarity_search(question)

        if not results["matches"]:
            return {
                "answer": "No relevant information was found in the uploaded document.",
                "sources": []
            }

        # Build context
        context = "\n\n".join(
            match["metadata"]["text"]
            for match in results["matches"]
        )

        # Generate answer
        answer = self.llm.generate_answer(
            question=question,
            context=context,
            chat_history=chat_history
        )

        return {
        "answer": answer,
        "sources": results["matches"]
        }   