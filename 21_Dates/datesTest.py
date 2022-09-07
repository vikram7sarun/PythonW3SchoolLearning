import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)
print(x)

print(x.strftime("%a"))

# refer https://www.w3schools.com/python/python_datetime.asp