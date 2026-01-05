from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()

model = ChatAnthropic(mode ="claude-3-opus-20240229")


response = model.invoke("What is the capital of India")

print(response.content)

