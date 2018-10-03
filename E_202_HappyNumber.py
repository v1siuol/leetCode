"""
401 / 401 test cases passed.
Status: Accepted
Runtime: 62 ms
You are here!
Your runtime beats 35.12% of python submissions.
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = abs(n)
        lst = []
        while n not in lst:
            lst.append(n)
            re = 0
            while n > 0:
                re += (n % 10) ** 2
                n //= 10
            n = re
        return n == 1

print(Solution().isHappy(49))
print(Solution().isHappy(-1))
