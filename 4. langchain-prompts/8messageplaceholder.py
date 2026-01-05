# THEORY : 
# ---------------

# used inside chatprompttemplate 
# to dynamically insert chathistory or a list of messages as runtime 

# EXAMPLE : 

# IN amazon chatbots are there, I asked for refund 
# chatbot : will be refunded in 3 days 
# i didnt recieve i go back and asked for it 
#  so we should also keep the track of that prev chats 
# so when i asked for what about my refund , the chathistory should be inserted before that query 

# so make a placeholder for that whole chathistory 


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template 

chat_template = ChatPromptTemplate([
    ("system", "You are helpful customer support agent"), 
    MessagesPlaceholder(variable_name="chat_history"), 
    ("human", "{query}")
])



# load chat history 
chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

# inserting the history in template 

prompt = chat_template.invoke({'chat_history':chat_history, 'query':"Where is my refund?"})

print(prompt)
