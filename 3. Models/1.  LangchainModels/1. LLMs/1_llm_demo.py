# we will use open ai llm 

# LLms are outdated , so we will not use llm 

from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

llm = OpenAI(model= "gpt-3.5-turbo-instruct")

result = llm.invoke("What is the capital of India")

print(result)