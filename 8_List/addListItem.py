thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist.insert(1, "Blueberry")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)