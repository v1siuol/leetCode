"""
Success
Details 
Runtime: 36 ms, faster than 87.40% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.2 MB, less than 41.91% of Python3 online submissions for Valid Perfect Square.
"""

class Solution:
    def isPerfectSquare(self, num: 'int') -> 'bool':
        r = num
        while r * r > num:
            r = (r + num//r) // 2

        return num == r * r



s = Solution()
print(s.isPerfectSquare(16))
# print(s.isPerfectSquare(14))

