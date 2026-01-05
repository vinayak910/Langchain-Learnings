from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3,
    max_tokens= 100
)

chat_history = []

print("Welcome , Be ready to use the best chatbot")
while True: 
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break 
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(f"AI: {result.content}")

print(chat_history)