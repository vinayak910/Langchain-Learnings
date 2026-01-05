from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

llms = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llms )

result = model.invoke("write a very short poem on love")

print(result.content)