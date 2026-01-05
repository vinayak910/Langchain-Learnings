from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",
                               max_tokens=100,
                               temperature=0.2)

response = model.invoke("write a short poem on love?")

print(response.content)