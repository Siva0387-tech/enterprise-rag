from vectorstore.pinecone_manager import PineconeManager

manager = PineconeManager()

index = manager.get_index()

print("=" * 60)
print("Connected Successfully!")
print("=" * 60)

stats = index.describe_index_stats()

print(stats)