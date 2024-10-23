from operator import index

nums = [2,7,11,15]
target = 9

#return [0,1]

a = 0
l = len(nums)

d = []

for i in range(l-1):
    a = nums[i] + nums[i+1]
    if a == 9:
        print(True)
        index(nums[i])
    else:
        print(False)