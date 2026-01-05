from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


chatmodel = ChatOpenAI(model= 'gpt-4-turbo')

response = chatmodel.invoke("What is the capital of India?")


print(response.content)
