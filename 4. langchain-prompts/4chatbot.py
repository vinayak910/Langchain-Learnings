from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "HuggingFaceTB/SmolLM3-3B",
    task= "text-generation",
    temperature= 0.7,
    max_new_tokens= 100
)

model = ChatHuggingFace(llm = llm, verbose = False)
chat_history = []
while True:

    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)
