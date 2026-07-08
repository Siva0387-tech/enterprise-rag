from rag.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()

print("=" * 60)
print("Uploading document...")
print("=" * 60)

count = pipeline.ingest_document(
    "data/uploads/resume.pdf"
)

print(f"\nUploaded {count} chunks.")

print("\n" + "=" * 60)

question = "What Linux experience does Siva have?"

print(f"Question: {question}")

print("=" * 60)

print("\nAnswer")
print("-" * 50)
print(response["answer"])

print("\nSources")
print("-" * 50)

for i, source in enumerate(response["sources"], start=1):

    metadata = source["metadata"]

    print(f"{i}. {metadata['source']} (Page {metadata['page']})")