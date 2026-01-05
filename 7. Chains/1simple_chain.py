from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template = PromptTemplate(
    template= "Generate 5 interesting facts about {topic}",
    input_variables= ['topic'] 
)

llm = HuggingFaceEndpoint(
    repo_id = "MiniMaxAI/MiniMax-M2.1",
    temperature=0.2,
    max_new_tokens=200
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({"topic":"Black hole"})

print(result)


# graph for chain 
chain.get_graph().print_ascii()
