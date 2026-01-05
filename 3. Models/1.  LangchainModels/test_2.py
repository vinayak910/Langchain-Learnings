from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-rw-1b",  # ✅ Small model, has HF inference
    task="text-generation",
    temperature=0.7,
    max_new_tokens=50
)

response = llm.invoke("Why do rivers always know where to go?")
print(response)
