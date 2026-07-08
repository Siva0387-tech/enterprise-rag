from vectorstore.pinecone_manager import PineconeManager


manager = PineconeManager()

query = "What Linux experience does Siva have?"

results = manager.similarity_search(query)

print("=" * 70)
print(f"Query: {query}")
print("=" * 70)

for i, match in enumerate(results["matches"], start=1):

    print(f"\nResult {i}")
    print("-" * 70)

    print(f"Score : {match['score']:.4f}")

    metadata = match["metadata"]

    print(f"Source : {metadata.get('source')}")

    print(f"Page : {metadata.get('page')}")

    print("\nContent:\n")

    print(metadata.get("text"))

    print("\n")