from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id= "MiniMaxAI/MiniMax-M2.1",
    max_new_tokens=300,
    temperature=0.1
)

model1 = ChatHuggingFace(llm = llm)


model2 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.2

)
class Feedback(BaseModel):
    sentiment: Literal['postive', 'negative'] = Field(description= "give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback text into positve or negative :\n {feedback} \n {format_instruction}",
    input_variables= ["feedback"],
    partial_variables= {"format_instruction":parser2.get_format_instructions()}
)

classfier_chain = prompt1 | model1 | parser2


prompt2 = PromptTemplate(
    template = "Write an appropriate response to this positive feedback \n {feedback}",
    input_variables= ['feedback']
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to this negative feedback \n {feedback}",
    input_variables= ['feedback']
)


# for branching we need runnable branch 
branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | model2 | parser),
    (lambda x : x.sentiment == 'negative', prompt3 | model2 | parser),
    RunnableLambda(lambda x : "could not find sentiment")
)

chain = classfier_chain | branch_chain

result = chain.invoke({"feedback": "That was really the fucking terrible movie"})

print(result)