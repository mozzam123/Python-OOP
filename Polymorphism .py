class Cat:
    def make_sound(self):
        return "Meow!"

class Dog:
    def make_sound(self):
        return "Woof!"

class Parrot:
    def make_sound(self):
        return "Squawk!"
    

# A function that demonstrates polymorphism
def animal_sound(animal):
    return animal.make_sound()

# Create instances of different animals
my_cat = Cat()
my_dog = Dog()
my_parrot = Parrot()

# Call the function with different animals
print(animal_sound(my_cat))  # Output: "Meow!"
print(animal_sound(my_dog))  # Output: "Woof!"
print(animal_sound(my_parrot))  # Output: "Squawk!"