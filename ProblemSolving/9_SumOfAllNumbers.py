inp1 = int(input("Enter the first Number : "))
inp2 = int(input("Enter the second Number : "))

print("The Sum of {} and {} is : {}".format(inp1, inp2, inp1 + inp2))

inp3 = int(input("Enter the Count : "))

sum = 0
for i in range(inp3):
    num = int(input())
    sum = sum+num

print("Total : ",sum)
