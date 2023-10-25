"""
In Python, a setter is a method used to update or set the value of an object's attribute.
Setters are often defined as instance methods within a class and are typically named with the prefix "set" followed by the attribute name they update.

"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.about = f"I'm {self.name}, {self.__age} years old"

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


person = Person("mozzam", 22)

print(person.about)
print(person.get_age())
print(person.about)
