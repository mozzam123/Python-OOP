"""
In Python, a class method is a method that is bound to the class and not the instance. It's defined using
the @classmethod decorator and takes the class itself as its first argument (usually named cls). Class methods are often
used for operations related to the class itself rather than individual instances.

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

person = Person.patient("Bill", 23, "M")
print(person.__dict__)
