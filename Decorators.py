"""
In Python, a decorator is like a special function that you can use to modify or enhance the behavior of another function.
It can add functionality to that function without changing its code. It's like adding extra features to a function without rewriting it.
"""


def format(names):
    return " ".join(names)


def show_name_reversed(func):
    def wrapper(names):
        res = list(func(names))
        res.reverse()
        return "".join(res)
    return wrapper


decorated = show_name_reversed(format)
result = decorated(names=["mizzam"])
print(result)