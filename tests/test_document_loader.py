from ingestion.document_loader import DocumentLoader

loader = DocumentLoader()

files = [
    "data/uploads/resume.pdf",
    "data/uploads/resume.docx",
    "data/uploads/sample.xlsx",
    "data/uploads/sample.png",
]

for file in files:

    print("\n" + "=" * 70)
    print(f"Testing: {file}")
    print("=" * 70)

    documents = loader.load(file)

    print(f"Documents Created: {len(documents)}")

    for i, doc in enumerate(documents, start=1):
        print(f"\nDocument {i}")
        print("Metadata:", doc.metadata)
        print("Content Preview:")
        print(doc.page_content[:200])