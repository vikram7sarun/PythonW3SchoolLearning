# -----------------------Method 1-----------------------------
s = "anagram"
t = "nagaram"

a1 = sorted(s)
t1 = sorted(t)

if a1 == t1:
    print("Yes it is Anagram")
else:
    print("Not an Anagram")

# -------------------------Method 2---------------------------

a = {}
b = {}

for i in s:
    if i in a:
        a[i] = a[i] + 1
    else:
        a[i] = 1

print(a)

for j in t:
    if j in b:
        b[j] = b[j] + 1
    else:
        b[j] = 1

print(b)

if a == b:
    print(True)
else:
    print(False)

# --------------------------------------------------
String = "geekforgeeks"
print('Original String: ', String)
lst = list(String)
lst.sort()
print('Sorted String: ')
for i in lst:
    print(i, end="")
