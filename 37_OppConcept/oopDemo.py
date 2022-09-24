from user import User,Student,Faculty


user1 = User("Vikram","Vik@123")
user2 = User("Harry","Vik@123")

user3 = Student("Harry","Vik@123")


user1.register()
user2.register()
user2.login()
print(User.users)


user3.students()