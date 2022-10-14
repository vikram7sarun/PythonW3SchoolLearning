
#---------Using Slicing method--------------

num = "12345"

print(num[::-1])

#---------Using Recrussion method--------------



#--------Reverse a number using while loop--------------

user_Input = int(input("Enter Number : "))

rev_Num = 0

while user_Input>0:
    remainder = user_Input % 10 #Remainder
    rev_Num = (rev_Num*10)+ remainder
    user_Input = user_Input//10

print(rev_Num)