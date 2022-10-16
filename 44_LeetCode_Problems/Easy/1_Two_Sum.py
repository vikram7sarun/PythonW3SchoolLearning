
class Solution:
    count = 0
    def twoSum(nums, target):
        i = 0
        while nums is not None:
            count = nums[i] + nums[i + 1]
            if count == target:
                return [i, i + 1]
                break
            else:
                i = i + 1





nums = [2,7,11,15]
target = 9
a = Solution
ans = a.twoSum(nums, target)
print(ans)

nums = [3,2,4]
target = 6
a = Solution
ans = a.twoSum(nums, target)
print(ans)

nums = [3,3,4,5,7,5,8,9]
target = 17
a = Solution
ans = a.twoSum(nums, target)
print(ans)