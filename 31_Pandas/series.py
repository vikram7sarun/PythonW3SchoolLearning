# What is a Series?
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar[0])


myvar = pd.Series(a, index = ["x", "y", "z"])


print(myvar["y"])


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)



data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data,index=["A","B","C"])

print(myvar)



















