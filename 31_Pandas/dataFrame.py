import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)
#
#
# print(df.loc[0])
# print(df.loc[[0, 1]])
#
#
#
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
#
# print(df)
#
# print(df.loc["day3"])


path = "F:\PYTHON_AUTOMATION\PythonW3Schools\Data\data.csv"
df = pd.read_csv(path)
df = pd.DataFrame(df)
print(df)
print(pd.options.display.max_rows)
print(df.loc[0])