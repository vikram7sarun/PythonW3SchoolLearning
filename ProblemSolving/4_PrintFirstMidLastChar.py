# -------------------------------Method 1-------------------------------------

str1 = 'SarunVikram'
print("Original String is", str1)
fl = str1[0]  # First Character
m = int(len(str1) / 2)
mid = str1[m]  # Middle Character
l = str1[-1]  # Last Character
print("Final : " + fl + mid + l)

# ---------------------------------Method  2-----------------------------------


# Get first character
res = str1[0]

# Get string size
l = len(str1)

# Get middle index number
mi = int(l / 2)

# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)
