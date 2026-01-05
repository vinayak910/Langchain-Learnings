from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 


embedder = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = ['Virat Kohli is Indian cricketer known for his aggressive batting and leadership', 
            'Sachin Tendulkar is an Indian cricketer revered for his masterful technique and record-breaking achievements.', 
            'Mahendra Singh Dhoni is an Indian cricketer celebrated for his calm demeanor and exceptional finishing skills.', 
            'Rohit Sharma is an Indian cricketer recognized for his effortless timing and ability to score big hundreds.', 
            'Jasprit Bumrah is an Indian cricketer admired for his unique bowling action and precise yorkers.'
            ]

query = "tell me about Bumrah"

doc_embeddings = embedder.embed_documents(documents)

query_embedding = embedder.embed_query(query)


# semantic search 

# tip : stored document embeddings in vector database
# as it will cost too much , 


scores = (cosine_similarity([query_embedding],doc_embeddings))[0]
index,score = (sorted(list(enumerate(scores)) , key = lambda x:x[1])[-1])

print(query)
print(documents[index])
print("Similarity score is :", score)





