"""
In Python, a decorator is like a special function that you can use to modify or enhance the behavior of another function.
It can add functionality to that function without changing its code. It's like adding extra features to a function without rewriting it.
"""

# Example 1
def show_name_reversed(func):
    def wrapper(names):
        res = list(func(names))
        res.reverse()
        return "".join(res)
    return wrapper

@show_name_reversed
def format(names):
    return names


result = format(names="mozzam")
print(result)


# Example 2

def check_palindrome(func):
    def wrapper(name):
        reversed_str = list(name)
        reversed_str = reversed_str[::-1]
        reversed_str = "".join(reversed_str)
        if name == reversed_str:
            return 'Palindrome'
        return "Not Palindrome"
    return wrapper


@check_palindrome
def isPalindrome(name):
    return name

res = isPalindrome(name='madam')
print(res)