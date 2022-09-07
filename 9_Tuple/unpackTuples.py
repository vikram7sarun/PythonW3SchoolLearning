# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)