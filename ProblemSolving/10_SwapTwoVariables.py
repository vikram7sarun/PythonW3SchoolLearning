#with Temporary Variable

x=10
y=20

print("the value of x and y before swapping : {}, {}".format(x,y))

temp = x
x = y
y = temp

print("the value of x and y after swapping : {}, {}".format(x,y))

#---------------Without Using Temporary Variable

x=10
y=20

print("the value of x and y before swapping : {}, {}".format(x,y))

x, y = y,x

print("the value of x and y after swapping : {}, {}".format(x,y))