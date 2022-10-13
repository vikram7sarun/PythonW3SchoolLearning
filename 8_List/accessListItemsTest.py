thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

user_input = input("Please enter the fruit name :  ")

if user_input in thislist:
  print(f"Yes, {user_input} is in the fruits list")
else:
  print(f"No The {user_input} is not preseted in the list")

