from ingestion.excel_loader import ExcelLoader

loader = ExcelLoader()

documents = loader.load("data/uploads/sample.xlsx")

print("=" * 60)
print(f"Total Documents: {len(documents)}")
print("=" * 60)

for i, doc in enumerate(documents, start=1):
    print(f"\nDocument {i}")
    print("Metadata:", doc.metadata)
    print("Content Preview:")
    print(doc.page_content[:300])