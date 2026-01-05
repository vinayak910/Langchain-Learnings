import streamlit as st 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


llms = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=100
)


model = ChatHuggingFace(llm = llms)

st.header("Research tool")

user_input = st.text_area("Enter your prompt")

if st.button("submit"):



    st.write(model.invoke(user_input).content)