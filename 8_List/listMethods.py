fruits = ['apple', 'banana', 'cherry']

fruits.append("Orange")
print(fruits)
fruits.clear()
print(fruits)
fruits = ['cherry','apple', 'banana', 'cherry']
a = fruits.copy()
print(a)
print(fruits.count("cherry"))

fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)
print(x)

"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""