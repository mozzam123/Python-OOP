# Type: Single Inheritance
" Single inheritance occurs when a class inherits from only one base class. "

class Animal():

    def __init__(self, name):
        self.name = name
        self.legs = 4


class Cat(Animal):
    def speak(self):
        print(f"Hello from {self.name} which has {self.legs} legs")


# Type: Multiple Inheritance
" Multiple inheritance occurs when a class inherits from more than one base class. "

class Mammal():
    def isType(self):
        print("type of mammal")

class Animal():

    def __init__(self, name):
        self.name = name
        self.legs = 4


class Cat(Animal, Mammal):
    def speak(self):
        print(f"Hello from {self.name} which has {self.legs} legs")


# Type: Multi-level Inheritance
" Multilevel inheritance occurs when a class is derived from a base class, and then another class is derived from that derived class. "
        
class Mammal():
        def isType(self):
            print("type of mammal")

class Animal(Mammal):

    def __init__(self, name):
        self.name = name
        self.legs = 4  

class Cat(Animal):
    def speak(self):
        print(f"Hello from {self.name} which has {self.legs} legs")



# Hierarchical Inheritance
        
" Hierarchical inheritance occurs when more than one class is derived from a single base class. "
        

class Mammal():
        def isType(self):
            print("type of mammal")

class Animal(Mammal):

    def __init__(self, name):
        self.name = name
        self.legs = 4  

class Cat(Mammal):
    def speak(self):
        print(f"Hello from {self.name} which has {self.legs} legs")