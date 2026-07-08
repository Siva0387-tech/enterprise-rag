from vectorstore.pinecone_manager import PineconeManager

manager = PineconeManager()

print("=" * 60)
print("Before Clearing")
print("=" * 60)

print(manager.describe_index())

manager.clear_index()

print("\n" + "=" * 60)
print("After Clearing")
print("=" * 60)

print(manager.describe_index())