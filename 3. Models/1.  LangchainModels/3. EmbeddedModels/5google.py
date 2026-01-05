from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

vector = embeddings.embed_query("LangChain with Google embeddings")
print(str(vector))