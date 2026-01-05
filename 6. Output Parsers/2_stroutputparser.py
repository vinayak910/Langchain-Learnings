# best usage of StrOutputParser is chains
# between steps there is a string output parser , which avoids giving meta data , and other trash for the next step
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation",
    temperature= 0.8
)


model = ChatHuggingFace(llm = llm)


template1 = PromptTemplate(
    template= "Write a detail report on {topic}",
    input_variables= ['topic']
)

template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)
