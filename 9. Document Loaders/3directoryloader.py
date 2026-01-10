from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = r"D:\GEN AI (campusx pytorch)\2. Langchain\9. Document Loaders",
    glob = "*.pdf",   # load all pdf files 

    loader_cls= PyPDFLoader
)

docs = loader.load()  # normal load 
# docs = loader.lazy_load() -> lazy load solves issue of memory 

print(len(docs))  # sums up all pdf files pages into d ocs 

