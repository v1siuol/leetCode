"""
1012 / 1012 test cases passed.
Status: Accepted
Runtime: 48 ms
You are here!
Your runtime beats 70.88% of python submissions.
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while (num & 1) == 0:
            num >>= 1
        while (num % 5) == 0:
            num //= 5
        while (num % 3) == 0:
            num //= 3
        return num == 1

print(Solution().isUgly(6))
print(Solution().isUgly(1))
print(Solution().isUgly(14))