from ingestion.document_loader import DocumentLoader
from chunking.chunker import Chunker

loader = DocumentLoader()
chunker = Chunker()

documents = loader.load("data/uploads/resume.pdf")

chunks = chunker.split_documents(documents)

print("=" * 60)
print(f"Original Documents : {len(documents)}")
print(f"Chunks Created     : {len(chunks)}")
print("=" * 60)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 60)
    print("Metadata:", chunk.metadata)
    print("Length:", len(chunk.page_content))
    print(chunk.page_content)