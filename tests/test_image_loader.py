from ingestion.image_loader import ImageLoader

loader = ImageLoader()

documents = loader.load("data/uploads/sample.png")

print("=" * 60)
print(f"Total Documents: {len(documents)}")
print("=" * 60)

doc = documents[0]

print("\nMetadata:")
print(doc.metadata)

print("\nExtracted Text:\n")
print(doc.page_content)