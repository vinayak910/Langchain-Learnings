from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


embedding = OpenAIEmbeddings(model="text-embedding-3-large",
                 dimensions=32)


document = [
    "Delhi is the capital of India",
    "Kolkata is the caoutak if West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(document)

print(str(result))