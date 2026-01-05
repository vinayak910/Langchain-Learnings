# topic-> llm -> report -> llm -> summary (sequence)
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id= "MiniMaxAI/MiniMax-M2.1",
    max_new_tokens=300,
    temperature=0.1
)

model = ChatHuggingFace(llm = llm)
parser = StrOutputParser()

template1 = PromptTemplate(
    template = "Generate a detailed report on {topic}",
    input_variables= ["topic"]
)
template2 = PromptTemplate(
    template = "Generate a short summary which covers the essence of this report :  {report}",
    input_variables= ["report"]

)
chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({"topic":"Black Hole"})

print(result)

chain.get_graph().print_ascii()