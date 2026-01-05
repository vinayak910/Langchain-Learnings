# only difference between json and structured output parser is
# structured output parser can enforce schema , while json parser cannot

# disadvantage ? -> no data validation 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser 

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation",
    temperature= 0.8
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name = "fact_1", description = "Fact 1 about the topic"),
    ResponseSchema(name = "fact_2", description = "Fact 2 about the topic"),
    ResponseSchema(name = "fact_3", description = "Fact 3 about the topic")

]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template = "Give 3 facts about the {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({"topic":"black hole"})
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# ------chain--------

chain = template | model | parser 

result = chain.invoke({"topic":"black hole"})
print(result)