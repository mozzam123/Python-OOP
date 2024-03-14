"""
The line @age.setter defines a setter method for the age property in your Person class. It allows you to modify the value of the __age attribute (which is "private" due to the double underscores) using the age property as if it were an attribute.

Here's how it works:

You have a age property, which you've defined with @property. This makes it possible to access the age property like an attribute, using person.age.

The @age.setter decorator is used to create a method that is called when you try to assign a new value to the age property. In your code, this method is named age.

Inside this setter method, you receive the value that is being assigned to the age property.

You use this value to set the private __age attribute to the new value, allowing you to change the age of the Person object.

So, when you write person.age = 55, it calls the age setter method, which updates the private __age attribute to 55, effectively changing the age of the Person object.
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def about(self):
        return f"My name is {self.name} and my age is {self.__age}"
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
    

person = Person("mozzam", 22)
print(person.about)
person.age = 55
print(person.about)


        