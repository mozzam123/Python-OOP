"""
Subclasses of an ABC must provide the implementation of all abstract method declared
in the abstract class in order to be instantiated. These implmentation are named concrete methods
"""



from abc import ABCMeta, abstractmethod

class ABC_Person(metaclass=ABCMeta):

    @abstractmethod
    def greet():
        pass



class Person(ABC_Person):
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    
    def greet(self):
        print(f"My name is {self.name} and my age is {self.age}")

person = Person("mozzam", 22)
person.greet()

        
