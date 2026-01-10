from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.2,
)

prompt = PromptTemplate(
    template = "Write a summary for the following poem \n" \
    "{poem}",
    input_variables= ["poem"]
)

parser = StrOutputParser()

chain = prompt | model | parser

loader = TextLoader(r"D:\GEN AI (campusx pytorch)\2. Langchain\9. Document Loaders\black_hole_poem.txt"
                    , encoding = "utf-8")

docs = loader.load()

# print(type(docs)) # list of document objects 
# print(len(docs))
# print(docs[0])  # output -> meta data , and actual data 

# print(docs[0].page_content)
# print(docs[0].metadata)

print(chain.invoke({"poem": docs[0].page_content}))
