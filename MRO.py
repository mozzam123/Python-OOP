"""
When a class inherits from multiple classes, MRO defines the order in which Python looks for a method.
It ensures that methods are searched in a predictable and consistent manner.

MRO is essential when using the super() function to call a method in a parent class.
super() relies on the MRO to determine which class to look for the next method.

"""



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  
    pass

obj = D()
obj.show()
