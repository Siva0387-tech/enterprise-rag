import config

print("========== CONFIG TEST ==========")

print(f"Groq Key Loaded: {'Yes' if config.GROQ_API_KEY else 'No'}")
print(f"Pinecone Key Loaded: {'Yes' if config.PINECONE_API_KEY else 'No'}")

print("Index Name:", config.PINECONE_INDEX_NAME)
print("Cloud:", config.PINECONE_CLOUD)
print("Region:", config.PINECONE_REGION)

print("Embedding Model:", config.EMBEDDING_MODEL)

print("Chunk Size:", config.CHUNK_SIZE)
print("Chunk Overlap:", config.CHUNK_OVERLAP)

print("Top K:", config.TOP_K)
print("Similarity Threshold:", config.SIMILARITY_THRESHOLD)

print("\nConfiguration Loaded Successfully!")