class User:

    users = 0   #Class Variable

    def __init__(self,userName,password):
        self.userName = userName #Instance Variable
        self.password = password

    def register(self):
        print("Registering.." +self.userName)
        User.users = User.users+1

    def login(self):
        print("Logging.."+self.userName)


class Student(User):  #Inheritance

     def students(self):
         print("This is Student Class")


class Faculty(User):  #Inheritance

    def factulies(self):
        print("This is faculty Class")