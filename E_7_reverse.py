from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 32 ms, faster than 99.26% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.3 MB, less than 32.30% of Python3 online submissions for Reverse Integer.
"""

# class Solution:
#     def reverse(self, x: 'int') -> 'int':
#         # 用数学啊 
#         s = str(x)
#         s = s[::-1]
#         if x < 0:
#             s = '-' + s[:-1]
#         i = int(s)
#         return i if -2**31 <= i <= 2**31 - 1 else 0  


# s = Solution()
# print(s.reverse(123))
# print(s.reverse(-123))
# print(s.reverse(120))
# print(s.reverse(1534236469))


"""
Success
Details 
Runtime: 36 ms, faster than 80.77% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.2 MB, less than 82.71% of Python3 online submissions for Reverse Integer.
"""

# hack 这么快？ 
class Solution:
    def reverse(self, x: 'int') -> 'int':
        ret = 0
        sign = 1 if x >= 0  else -1 
        x = max(x, -x)

        while x != 0:
            d = x % 10 
            ret = ret * 10 + d 
            x //= 10 

        r = sign * ret 
        return r if -2 ** 31 <= r <= 2 ** 31 - 1 else 0 
