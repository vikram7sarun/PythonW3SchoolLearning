import pyodbc


server = "DESKTOP\SQLEXPRESS"
database = "master"


# conn = pyodbc.connect('driver={ODBC Driver 17 for SQL Server};'
#                       'server=server;'
#                       'database=database;'
#                       'Trusted_Connection=yes;')

conn = pyodbc.connect("driver={SQL Server};Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;")

cursor = conn.cursor()
cursor.execute('SELECT * FROM carloans')

for i in cursor:
    print(i)


conn.close()


