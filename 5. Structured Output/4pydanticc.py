# use pydantic for data validation, Annotation etc 


from pydantic import BaseModel, Field 
from typing import Optional


class Student(BaseModel):
    name: str = "Vinayak"
    age: Optional[int] = None 
    email:str
    cgpa:float =  Field(gt = 0 , lt = 10 , default=5, 
                     description="A decimal value representing cgpa of the student")
    

new_student = {'age': 3.4, 'email':'abc'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()
    