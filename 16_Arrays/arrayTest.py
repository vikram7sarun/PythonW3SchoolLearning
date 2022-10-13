# Python does not have built-in support for Arrays, but Python Lists can be used instead.


cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(type(cars))
print(x)

for x in cars:
  print(x)

cars.append("Honda")
print(cars)
print(cars.pop(1))
# print(cars.remove("Volvo"))