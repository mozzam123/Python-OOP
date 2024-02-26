# Definition
"Having multiple methods in the same class with the same name but different parameters (number or types of parameters)."

# Use case
""" Allows a class to have multiple methods with the same name but different functionality based on the parameters.
Note: Python does not support true method overloading, but you can achieve similar effects using default parameter values or variable-length argument lists. """



class Calculator:
    def add(self,a,b):
        print(a + b)

    def add(self,a,b,c):
        print(a + b + c)



obj = Calculator()
obj.add(1,2)
obj.add(1,2,3)