from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.2,
)


loader = PyPDFLoader(r"D:\GEN AI (campusx pytorch)\2. Langchain\9. Document Loaders\dl-curriculum.pdf")

docs = loader.load()
print(len(docs))   # 23 document objects inside list(23 pages)

print("PAGE CONTENT -------------------")
print(docs[0].page_content)


print("META DATA ====================")

print(docs[0].metadata)





