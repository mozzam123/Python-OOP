class Person:

    def __init__(self, name, age) :
        self.name = name
        self.__age = age
        self.about = "I'm {}, {} years old.".format(self.name, self.__age)

        
person = Person('mozzam', 22)
print(person._Person__age + 1)