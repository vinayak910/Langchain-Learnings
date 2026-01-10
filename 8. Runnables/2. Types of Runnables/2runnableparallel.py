from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda
from langchain_google_genai import GoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

load_dotenv()


# --------------llm initializations --------------
llm = HuggingFaceEndpoint(
    repo_id= "zai-org/GLM-4.7",
    temperature=0.3, 
)

model1 = ChatHuggingFace(llm = llm)


parser = StrOutputParser()


# ------------Prompttemplate --------------------

prompt1 = PromptTemplate(
    template="Write a small joke about {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template= "Generate a single linkedin post about Trending topic of {topic}",
    input_variables= ["topic"]
)



parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model1 ,RunnableLambda(debug), parser), 
    "linkedin_post":RunnableSequence(prompt2 , model2 , parser)
})

result = parallel_chain.invoke({"topic":"AI"})  # result is a dictionary 

print(result['tweet'])  
print("\n \n \n \n")
print(result['linkedin_post'])
