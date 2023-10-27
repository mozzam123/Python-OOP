"""
The make_dataclass function from the dataclasses module creates a new class dynamically.
However, it doesn't automatically generate attributes for you, so you need to define the class attributes explicitly.

"""


from dataclasses import make_dataclass

Vehicle = make_dataclass('Vehicle', ['seats', 'name', 'color'])
vehicle = Vehicle(seats=14,name="wgonr", color="while")
print(vehicle.name)
print(vehicle.seats)
