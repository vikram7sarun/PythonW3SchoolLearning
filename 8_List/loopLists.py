thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print(range(len(thislist)))

for i in range(len(thislist)):
  print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]