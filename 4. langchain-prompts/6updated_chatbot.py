# this is the updated chatbot with messages labeled 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import re

def clean_response(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

llm = HuggingFaceEndpoint(
    repo_id= "HuggingFaceTB/SmolLM3-3B",
    task= "text-generation",
    temperature= 0.7,
    max_new_tokens= 100
)

model = ChatHuggingFace(llm = llm, verbose = False)


chat_history = [
    SystemMessage(content = "You are a helpful AI assistant")
]

while True: 
    user_input = input("You: ")
    chat_history.append(HumanMessage(content =  user_input))
    if user_input == "exit":
        break 

    result = model.invoke(chat_history)
    result = clean_response(result.content)
    chat_history.append(AIMessage(result))

    print("AI: ",result )

print(chat_history)    

    