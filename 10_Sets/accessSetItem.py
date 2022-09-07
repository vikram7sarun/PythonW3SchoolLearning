# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

