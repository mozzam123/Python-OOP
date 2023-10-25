"""
In Python, a getter is a method used to retrieve the value of an object's attribute.
Getters are often defined as instance methods within a class and are typically named with the prefix "get" followed by the attribute name they retrieve.

"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.about = f"I'm {self.name}, {self.__age} years old"

    def get_age(self):
        return self.__age


person = Person("mozzam", 22)
print(person.get_age())