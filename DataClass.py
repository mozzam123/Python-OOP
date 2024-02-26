"""
In Python, the dataclass module provides a simple way to create classes primarily used for storing data.
The main difference between data class and python regular class is that a data class has the methods __init__,
__eq__ and __repr__ already implemented.

"""


from dataclasses import dataclass

@dataclass
class Vehicle:
    name: str
    seats: int
    
    @property
    def getName(self):
        print(self.name)

    @property
    def about(self):
        print( f"My vehicle name is {self.name} and have {self.seats} seats")



car = Vehicle("toyota", 5)
car.about