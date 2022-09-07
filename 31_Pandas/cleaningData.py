import pandas as pd

# Remove Rows
# df.dropna()

path = "F:\PYTHON_AUTOMATION\PythonW3Schools\Data\TestData.csv"
df = pd.read_csv(path)
x = df["Name"] == "Sarun Vikram"
print(x)


# df = pd.DataFrame(df)
# print(df)
# new_df = df.dropna()
#
# print(new_df.to_string())
#
# # Replace Empty Values
#
# df.fillna(130, inplace = True)
# newdf = df["Name"].fillna("Duce",inplace=True)
# print(newdf)


# x = df["Name"].mean()
# print(x)