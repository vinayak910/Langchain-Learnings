from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

load_dotenv()


# --------------llm initializations --------------
llm = HuggingFaceEndpoint(
    repo_id= "MiniMaxAI/MiniMax-M2.1",
    temperature=0.3, 
)

model = GoogleGenerativeAI(model = "gemini-2.5-flash-lite")

parser = StrOutputParser()

# ---------------------prompttemplate

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)


parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))