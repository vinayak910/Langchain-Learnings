from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"D:\GEN AI (campusx pytorch)\2. Langchain\9. Document Loaders\dl-curriculum.pdf")

docs = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100, 
    chunk_overlap = 0, 
)

result = splitter.split_documents(docs)


# also have split_text func , which works for normal text : ex : normal string
print(len(result))
print("\n \n \n")
print(result[0])   # each chuck itself will be a doc(ie will have page content and meta data)

print(result[0].page_content)

print(result[0].metadata)

