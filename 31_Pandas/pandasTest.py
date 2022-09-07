import pandas as pd
# print(pd.__version__)
#
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pd.DataFrame(mydataset)
#
# print(myvar)


path = "F:\PYTHON_AUTOMATION\PythonW3Schools\Data\data.csv"
df = pd.read_csv(path)
df = pd.DataFrame(df)

print(type(df))