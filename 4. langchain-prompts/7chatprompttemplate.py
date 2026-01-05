# THEORY 
#-----------

# for single query like research tool , where user gave the single query we had TEMPLATE (one time use)
# but for multi messages like chatbot, we were using static template where user is directly giving the query 
# how can we use dynamic template for list of messages(multi message) just like we did for single query 

# thats where chatprompttemplate comes for dynamic templates for list of messages 

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"), 
    ("human", "Explain in simple terms , what is {topic}")
])

prompt = chat_template.invoke({"domain":"cricket", "topic": "Dusra"})

print(prompt)
