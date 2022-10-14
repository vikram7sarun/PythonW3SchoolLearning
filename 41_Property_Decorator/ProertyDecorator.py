

class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.msg = self.name+ " is " + str(self.age) + " years old!!"

    @property
    def msg(self):
        return self.name+ " is " + str(self.age) + " years old!!"

c = user("Vikram",28)
print(c.name)
print(c.age)
print(c.msg)
c.age = 30
print(c.msg)