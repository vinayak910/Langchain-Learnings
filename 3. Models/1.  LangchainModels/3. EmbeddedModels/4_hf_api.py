from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings

embedder = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

text = embedder.embed_query("This is a sentence to convert into embedding")

print(str(text))

