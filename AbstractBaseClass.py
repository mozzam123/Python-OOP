"""
An abstract base class is a blueprint for classes, ensuring they have specific methods or attributes.
It enforces a common structure in related classes, making them adhere to a consistent interface or contract.
Subclasses must implement the required methods, promoting code organization and reliability.

"""


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class InvalidRectangle(Shape):
    pass

# Attempt to create an instance of the invalid subclass
invalid_rectangle = InvalidRectangle()
