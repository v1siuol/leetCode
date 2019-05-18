"""
Success
Details 
Runtime: 28 ms, faster than 99.92% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.2 MB, less than 52.24% of Python3 online submissions for Sqrt(x).
"""
class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        # newton 
        r = x
        while r * r > x:
            r = (r + x//r) // 2
            # print(r)
        return r



s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))

