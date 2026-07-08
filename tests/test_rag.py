from vectorstore.pinecone_manager import PineconeManager
from llm.groq_manager import GroqManager


question = "What Linux experience does Siva have?"

# Retrieve relevant chunks
pinecone = PineconeManager()

results = pinecone.similarity_search(question)

context = "\n\n".join(
    match["metadata"]["text"]
    for match in results["matches"]
)

# Generate answer
groq = GroqManager()

answer = groq.generate_answer(
    question=question,
    context=context
)

print("=" * 70)
print("QUESTION")
print("=" * 70)

print(question)

print("\n" + "=" * 70)
print("ANSWER")
print("=" * 70)

print(answer)