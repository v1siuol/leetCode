"""
45 / 45 test cases passed.
Status: Accepted
Runtime: 46 ms
You are here!
Your runtime beats 37.62% of python submissions.
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def jc(num):
            r = 1
            for i in range(2,num+1):
                r *= i
            return r
        i = 2
        re = 1
        while i <= n:
            re += (jc(n-i+(i>>1)) / jc(i>>1) / jc(n-i))
            i += 2
        return int(re)

print(Solution().climbStairs(6))  # 13
print(Solution().climbStairs(7))  # 21
print(Solution().climbStairs(8))  # 34
print(Solution().climbStairs(9))  # 55
print(Solution().climbStairs(1))