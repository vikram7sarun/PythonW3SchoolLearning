class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x[::-1]
        return r


ans = Solution.reverse(123)
print(ans)