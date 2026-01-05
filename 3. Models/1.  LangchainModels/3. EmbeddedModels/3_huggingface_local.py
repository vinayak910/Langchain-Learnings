from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)


document = [
    "Delhi is the capital of India",
    "Kolkata is the caoutak if West Bengal",
    "Paris is the capital of France"
]
text = "Delhi is the capital of India"

vector = embedding.embed_query(text)

doc_vector = embedding.embed_documents(document)
print(str(vector))

print(str(vector))