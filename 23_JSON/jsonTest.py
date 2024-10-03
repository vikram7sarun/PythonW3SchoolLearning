import json

# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# y = json.loads(x)
#
# print(y["age"])
#
#
# x1 =  '{ "name":["Sarun","Vikram"], "age":30, "city":"New York"}'
#
# y1 = json.loads(x1)
#
# print(y1["name"])
#
#
# # a Python object (dict):
# x = {
#   "name": "Sarun",
#   "age": 28,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)
#
#
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

import json

j =  '{ "name":"John", "age":30, "city":"New York","cars":[{"model":"BMW","mpg":25},{"model":"AUDI","mpg":20}]}'

op = json.loads(j)

print(op["cars"])



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4,sort_keys=True))

print(json.dumps(x, indent=4, separators=(". ", " = ")))





















