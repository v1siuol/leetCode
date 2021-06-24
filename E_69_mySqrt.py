from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 28 ms, faster than 99.92% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.2 MB, less than 52.24% of Python3 online submissions for Sqrt(x).
"""
# class Solution:
#     def mySqrt(self, x: 'int') -> 'int':
#         # newton 
#         r = x
#         while r * r > x:
#             r = (r + x//r) // 2
#             # print(r)
#         return r


# s = Solution()
# print(s.mySqrt(4))
# print(s.mySqrt(8))


"""
Success
Details 
Runtime: 32 ms, faster than 96.16% of Python3 online submissions for Sqrt(x).
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sqrt(x).
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        # math fast sqrt cheat newton
        r = x
        while r * r > x:
            r = (r + x//r) // 2
        return r
