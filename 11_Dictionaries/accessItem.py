thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

for i in car.values():
  if i == 1984:
    print("Values are equal")
print("Values are Not equal")


x = thisdict.items()
print(x)