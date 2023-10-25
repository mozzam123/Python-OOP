"""
Single inheritance in Python refers to a situation where a class inherits attributes and
methods from only one parent class. It means that a subclass is derived from a single base or parent class.
In simpler terms, a class can have only one immediate ancestor class, and it inherits the properties and behaviors of that parent class.

"""


class Parent:
    def func1(self):
        print("This function is in parent class")

    
class Child(Parent):
    def func2(self):
        print("This function is in child class")


obj = Child()
obj.func1()
obj.func2()