# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         r = x[::-1]
#         return r
#
#
# ans = Solution.reverse(123)
# print(ans)


# ------------------------------------

def permute(nums, start, end):
    if start == end:
        print(nums)
    else:
        for i in range(start, end + 1):
            # Swap the current element with the start element
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse with the next element in line
            permute(nums, start + 1, end)
            # Backtrack to restore the original list
            nums[start], nums[i] = nums[i], nums[start]

# Input list
perm = [1, 2, 3, 4]
n = len(perm)

print("All possible permutations are:")
permute(perm, 0, n - 1)