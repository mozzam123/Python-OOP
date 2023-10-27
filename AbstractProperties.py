from abc import ABCMeta, abstractmethod

class ABC_Person(metaclass=ABCMeta):
    @abstractmethod
    def greet(self):
        pass

    @property
    @abstractmethod
    def about(self):
        pass

    @property
    @abstractmethod
    def age(self):
        pass

    @age.setter
    @abstractmethod
    def age(self):
        pass 
    
class Person(ABC_Person):
    def __init__(self, name, age) :
        self.name = name
        self. age = age

    def greet(self):
        print(f"My name is {self.name}. How are you")


    @property
    def about(self):
        print(f"My name is {self.name} and Im {self.age} years old")

    @property
    def age(self):
        print(f"My age is {self.age}")
    
    def age(self, value):
        self.age = value
    


person = Person("bill", 22)
person.about
person.age = 666
person.about