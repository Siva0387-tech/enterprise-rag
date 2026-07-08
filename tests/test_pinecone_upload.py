from ingestion.document_loader import DocumentLoader
from chunking.chunker import Chunker
from vectorstore.pinecone_manager import PineconeManager

loader = DocumentLoader()
chunker = Chunker()
manager = PineconeManager()

documents = loader.load("data/uploads/resume.pdf")

chunks = chunker.split_documents(documents)

count = manager.upload_documents(chunks)

print("=" * 60)
print(f"Uploaded {count} vectors successfully.")
print("=" * 60)

stats = manager.describe_index()

print(stats)