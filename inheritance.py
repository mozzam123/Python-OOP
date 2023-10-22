# Parent class
class Animal():

    def __init__(self, name):
        self.name = name
        self.legs = 4


class Cat(Animal):
    def speak(self):
        print(f"Hello from {self.name} which has {self.legs} legs")

cat = Cat("leo")
cat.speak()