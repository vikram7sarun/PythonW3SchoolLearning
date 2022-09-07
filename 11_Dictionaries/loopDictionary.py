thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "Blue"
}

for x in thisdict:
  print(thisdict[x])

for x in thisdict.keys():
  print(x)

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)