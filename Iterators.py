"""
Iterators are objects in Python that allow you to loop through a collection of items, one item at a time.
They help you access and process elements in a sequence, such as a list or a string, without the need to load the entire collection into memory.
"""

mylist = [1,2,3,4,5]

it = mylist.__iter__()
for i in range(0, len(mylist)-1):
    print(it.__next__())