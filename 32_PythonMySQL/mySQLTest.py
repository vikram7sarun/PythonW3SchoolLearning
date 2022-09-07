import mysql.connector as con


mydb = con.connect(host="",user="",password="")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")


mydb = con.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)