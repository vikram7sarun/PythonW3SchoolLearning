import sqlite3

con = sqlite3.connect('F:\\PYTHON_AUTOMATION\\PythonW3SchoolLearning\\43_Python_SQLite\\users.db')

def addData():
    qry = "insert into users(NAME,AGE,CITY) values (?,?,?);"
    qry = "Select * from users"
    # con.execute(qry, (name, age, city))
    con.execute(qry)
    con.commit()

    print("User Details Added")

# addData("Sarun",29,"Cbe")
addData()