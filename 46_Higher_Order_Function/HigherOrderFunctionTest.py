# Higher Order functions
# map
# filter
# reduce


"""
Map >>>  Return List
"""
def double_number(number):
    return number * 2

print(list(map(lambda  num: num*2, [1,2,3])))
print(list(map(lambda  num: num**2, [1,2,3])))


"""
Filter >>> Return List
"""

Number = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda number: number % 2 == 0,Number))) # return List