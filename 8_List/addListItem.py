
thislist = ["apple", "banana", "cherry"]

#---------------------Append-----------------------

thislist.append("orange")
print("Append Output :",thislist)

#---------------------Insert-----------------------

thislist.insert(1, "Blueberry")
print("Insert Output :",thislist)

#---------------------Extend-----------------------

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)