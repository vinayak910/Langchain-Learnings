from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()


def debug_step(x):
    print(f"Here is the joke buddy : \n {x}")
    return x

# llm = HuggingFaceEndpoint(
#     repo_id= "deepseek-ai/DeepSeek-R1",
#     task= "text-translation",
#     max_new_tokens= 200
# )

# model = ChatHuggingFace(llm = llm)

model = GoogleGenerativeAI(model = "gemini-2.5-flash-lite")
parser = StrOutputParser()
prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Explain the following joke- {text}",
    input_variables=["text"]
)


chain = RunnableSequence(prompt1 , model , parser , RunnableLambda(debug_step), prompt2 , model , parser)

result = chain.invoke({"topic":"SRK"})

print(result)


