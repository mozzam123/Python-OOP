# Definition
"When a subclass provides a specific implementation for a method that is already defined in its superclass."

# Use Case
"Useful when you want a specialized version of a method in a subclass, different from the one in the superclass."



class Animal:
    def sound(self):
        print("Generic Animal Sound")


class Cat(Animal):
    def sound(self):
        print("Meow")

obj = Cat()
obj.sound()