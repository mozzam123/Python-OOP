"""
For example, if you have a function that makes another function and gives it a number, that inner
function can still remember and use that number even after the outer function has finished its job.
This special ability is what we call a "closure." It helps you keep and use important information in your code.


In simpler terms, a closure allows a function to remember and access the variables from the outer (enclosing) function,
even after the outer function has finished executing. This helps in creating and maintaining state within a function.


"""

# First Example
def show_name(firstname, lastname):
    def concatenate(names):
        return " ".join(names)
    return concatenate(names=[firstname, lastname])

print(show_name(firstname="mozzam", lastname="inamdar"))


## Second Example
def street_name():
    def concatenate(names):
        return " ".join(names)
    return concatenate

street = street_name()
print(street(names=["high", "lane"]))


## Third Example
def name_maker(names):
    def concatenate():
        return " ".join(names)
    return concatenate

name = name_maker(names=['moz', 'tea'])
print(name())