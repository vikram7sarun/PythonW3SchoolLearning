import sqlite3


con = sqlite3.connect('users.db')


def insertData(name,age,city):
    qry = "insert into users(NAME,AGE,CITY) values (?,?,?);"
    cur = con.cursor()
    con.execute(qry, (name, age, city))
    con.commit()
    print("User Details Added")

def updateData(name,age,city,id):
    qry = "update users set NAME=?,AGE=?,CITY=? where id=?;"
    cur = con.cursor()
    con.execute(qry, (id))
    con.commit()
    print("User Details Updated")

def deleteData(id):
    qry = "delete from users where id=?;"
    cur = con.cursor()
    con.execute(qry, (id))
    con.commit()
    print("User Details Deleted")

def getData():
    qry = "select * from users;"
    cur = con.cursor()
    run = con.execute(qry)
    for i in run:
        print(i)
    # con.commit()
    print("Data fetch Successfully")

print("""
1.Create
2.Update
3.Delete
4.Select
""")

ch = 1

while ch == 1:
    c = int(input("Enter Your Choice : "))
    if (c == 1):
        print("Add New Record")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        insertData(name, age, city)
    elif (c == 2):
        print("Edit a Record")
        id = input("Enter Id : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        updateData(name, age, city, id)
    elif (c == 3):
        print("Delete a Record")
        id = input("Enter Id : ")
        deleteData(id)
    elif (c == 4):
        print("Print all Record")
        getData()
    else:
        print("Invalid Selection")
    ch = int(input("Enter 1 to Continue : "))
