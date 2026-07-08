from ingestion.pdf_loader import PDFLoader

loader = PDFLoader()

documents = loader.load("data/uploads/resume.pdf")

print("=" * 60)
print(f"Total Documents: {len(documents)}")
print("=" * 60)

doc = documents[0]

print("\nMetadata:")
print(doc.metadata)

print("\nContent Preview:\n")
print(doc.page_content[:500])