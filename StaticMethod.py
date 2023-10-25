"""
In Python, a static method is a method that has nothing to do with class or class object,
we can write that def anywhere and even outside the class but as per best practices, we write
it inside the class with '@staticmethod' above the def

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def patient(cls, name, age, gender):
        person = cls(name, age)
        person.gender = gender  # Set the 'gender' attribute on the instance
        return person
    
    @staticmethod
    def make_payment(*numbers: float) -> float:
        return sum(numbers)


print(Person.make_payment(15,5))
