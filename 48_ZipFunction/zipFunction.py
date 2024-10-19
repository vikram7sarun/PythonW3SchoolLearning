"""
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
"""

a = ("1", "2", "3")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(tuple(x))

l1 = ["1", "2", "3"]
l2 = ["Jenny", "Christy", "Monica","Viki"]

s = zip(l1,l2)

print(dict(s))