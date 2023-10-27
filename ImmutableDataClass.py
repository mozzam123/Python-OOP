"""
The main difference between data class and python regular class is that a data class has the methods __init__,
__eq__ and __repr__ already implemented. Frozen in dataclass means we have locked the WRITE on variables.

"""



from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

    
    def about(self):
        print(f"My name is {self.name} and my age is {self.age}")


boy = Person(name="mozzam", age=23)
boy.about()
boy.age = 33
boy.about()  # This line will give error as we cannot reassign anything in a variable