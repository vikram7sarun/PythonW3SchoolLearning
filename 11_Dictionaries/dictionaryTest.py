# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colour": "Red"
}

print(thisdict)
print(thisdict["model"])
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict["colors"])

col = thisdict["colors"]

for i in col:
  print(i)