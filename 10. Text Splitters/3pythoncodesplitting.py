from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        # We leave this generic because different animals make different sounds
        return "Some generic animal sound"

    def describe(self):
        return f"I am {self.name}, and I am a {self.species}."


class Dog(Animal):
    def __init__(self, name, breed):
        # Use super() to call the parent __init__ method
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,  ## can also use markdown or any other languages 
    chunk_size = 400,
    chunk_overlap = 0
)

results = splitter.split_text(text)

for result in results:
    print(result)
    print("\n \n ")
