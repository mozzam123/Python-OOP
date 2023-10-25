"""
Multiple inheritance in Python refers to a situation where a class inherits attributes and
methods from more than one parent class. It means that a subclass is derived from more than one base or parent class.

"""



class Parent1:
    def func1(self):
        print("This function is in Parent1 class")


class Parent2:
    def func2(self):
        print("This function is in Parent2 class")


class Child(Parent1, Parent2):
    def func3(self):
        print("This function is in Child class")


obj = Child()
obj.func1()
obj.func2()
obj.func3()