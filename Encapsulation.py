"""
Encapsulation is one of the fundamental principles of object-oriented programming (OOP) that involves
bundling the data (attributes) and the methods (functions) that operate on the data into a single unit called a class.
It allows the data to be hidden and accessed only through the defined methods, which provides a way to control access to the data and protects it from unintended modification.

"""


# Example 1

class Car:
    def __init__(self, make, model):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__speed = 0  # private attribute

    def accelerate(self, increment):
        self.__speed += increment

    def get_speed(self):
        return self.__speed

# Creating an instance of the Car class
my_car = Car(make="Toyota", model="Camry")

# Accessing attributes through methods
my_car.accelerate(20)
current_speed = my_car.get_speed()

# print(f"My {my_car._  } {my_car._Car__model}'s current speed is {current_speed} mph.")




# Example 2
class Person:
    def __init__(self):
        self.name = "mozzam"
        self.__age = 23

    def __get_age(self):
        return self.__age
    
obj = Person()
print(obj._Person__get_age())
        