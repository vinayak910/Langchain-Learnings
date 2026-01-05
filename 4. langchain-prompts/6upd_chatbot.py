from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    temperature=0.5 , 
    max_tokens= 100
)

chat_history = [SystemMessage("You are a helpful AI assistant")]

print("Welcome to GPT-6")
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == "exit":
        break 
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print(f"AI: {result.content}")


print(chat_history)


