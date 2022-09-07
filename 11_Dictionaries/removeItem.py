thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "Blue"
}
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["year"]
print(thisdict)

# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

thisdict.clear()
print(thisdict)
