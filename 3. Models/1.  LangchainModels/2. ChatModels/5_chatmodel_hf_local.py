from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import torch

device = 0 if torch.cuda.is_available() else -1

llms = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task="text-generation",
    model_kwargs={"device_map": "auto"},  # ✅ model auto-placed
    pipeline_kwargs=dict(
        temperature=0.8,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llms)

result = model.invoke(
   "write a 4 lines poem on cricket"
)

print(result.content)
