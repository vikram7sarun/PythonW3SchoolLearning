# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

# Creating Arrays With a Defined Data Type

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)















