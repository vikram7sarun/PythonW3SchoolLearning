b = "Hello, World!"

print(b[0:5])
print(b[2:5])
print(b[:5])
print(b[7:])
print(b[-5:-2])
print(b[:-2])
print(b[-5:])


print(b[0:12:2])
print(b[::-1])  # Output: '!dlroW ,olleH'


#------------

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("madam"))  # Output: True
