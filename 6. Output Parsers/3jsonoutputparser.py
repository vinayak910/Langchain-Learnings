# used json parser , but problem , structure of json is not decided by us
# its decided by model output , which may vary model to model
# biggest limitation : cannot enforce schema 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation",
    temperature= 0.8
)

parser = JsonOutputParser()
model = ChatHuggingFace(llm = llm)

template = PromptTemplate(
    template = "Give me the name , age , city of fictional person \n {format_instruction}", 
    input_variables= [],
    partial_variables= {'format_instruction':parser.get_format_instructions()}
)

#-----------------------------------
# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)
# print(final_result)
# #-----------------------------------

# OR WE CAN USE CHAINS 
chain = template | model | parser 
result = chain.invoke({}) #pass input , if not any , pass empty dict
print(result)