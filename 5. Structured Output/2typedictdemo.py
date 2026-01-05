# we will use this for llm to give structured output 
# NOTE : it doesnt include validation , only annotation 


from typing import TypedDict

class Person(TypedDict):

    name: str 
    age: int 

new_person : Person = {"name":"Vinayak"
                       , "age":22}

print(new_person)
print(new_person['name'])