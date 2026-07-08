from ingestion.document_loader import DocumentLoader
from chunking.chunker import Chunker
from embeddings.embedding_manager import EmbeddingManager

loader = DocumentLoader()
chunker = Chunker()
embedding_manager = EmbeddingManager()

documents = loader.load("data/uploads/resume.pdf")

chunks = chunker.split_documents(documents)

embedding_model = embedding_manager.get_embedding_model()

print("=" * 60)
print("Embedding Model Loaded Successfully")
print("=" * 60)

vector = embedding_model.embed_query(
    chunks[0].page_content
)

print(f"Vector Dimension : {len(vector)}")

print("\nFirst 10 Values:\n")

print(vector[:10])