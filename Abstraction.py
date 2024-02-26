"""
In Python, abstraction is achieved through the use of classes and objects.
You define classes that represent the essential properties and behaviors of a concept, and you interact with objects based on these abstractions.
The implementation details are encapsulated within the classes, providing a simplified and abstracted view for the user of the class.

"""

from abc import ABC, abstractmethod

# Abstract Base Class (ABC) representing a Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class Car inheriting from Vehicle
class Car(Vehicle):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

# Using the abstraction
my_car = Car()
my_car.start()
my_car.stop()


"""
By using this abstraction, you can create various types of vehicles (e.g., trucks, motorcycles) by inheriting
from the abstract Vehicle class and providing specific implementations for the start and stop methods.
The user of the Car class doesn't need to know the details of how the engine starts or stops;
they can interact with the car through the simplified interface provided by the abstract class.

"""
