"""
In Python, a decorator is like a special function that you can use to modify or enhance the behavior of another function.
You put the decorator symbol @ above a function, and it can add functionality to that function without changing its code.
It's like adding extra features to a function without rewriting it.

"""


def reversed_name(func):
    def wrapper(names):
        res = list(func(names))
        res.reverse()
        return "".join(res)
    return wrapper

@reversed_name
def format(names):
    return "".join(names)


result = format(names="neerav")
print(result)