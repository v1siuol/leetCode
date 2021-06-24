from __future__ import annotations 
import collections 
import random 
import heapq 
import math


# """
# 401 / 401 test cases passed.
# Status: Accepted
# Runtime: 62 ms
# You are here!
# Your runtime beats 35.12% of python submissions.
# """
# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         n = abs(n)
#         lst = []
#         while n not in lst:
#             lst.append(n)
#             re = 0
#             while n > 0:
#                 re += (n % 10) ** 2
#                 n //= 10
#             n = re
#         return n == 1

# print(Solution().isHappy(49))
# print(Solution().isHappy(-1))

"""
Success
Details 
Runtime: 44 ms, faster than 47.32% of Python3 online submissions for Happy Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Happy Number.
"""
# set 
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()
#         while n not in seen:
#             seen.add(n)

#             temp = 0
#             while n != 0:
#                 temp += (n % 10) ** 2
#                 n //= 10
#             n = temp

#         return n == 1


"""
Success
Details 
Runtime: 32 ms, faster than 95.22% of Python3 online submissions for Happy Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Happy Number.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        # brute force O(n) space 
        visited = set()
        n = abs(n)
        while n not in visited:
            visited.add(n)
            new_n = 0
            while n != 0:
                new_n += (n % 10) ** 2
                n //= 10
            n = new_n
            
        return n == 1
