from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
8 / 8 test cases passed.
Status: Accepted
Runtime: 82 ms
You are here!
Your runtime beats 54.94% of python submissions.
"""
# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         count = 1
#         result = []
#         while count <= n:
#             if count % 3 == 0:
#                 if count % 5 == 0:
#                     result.append("FizzBuzz")
#                 else:
#                     result.append("Fizz")
#             elif count % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(count))
#             count += 1
#         return result

# print(Solution().fizzBuzz(15))


"""
Success
Details 
Runtime: 40 ms, faster than 86.90% of Python3 online submissions for Fizz Buzz.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []

        for i in range(1, n+1):
            div3 = (i % 3 == 0)
            div5 = (i % 5 == 0)

            temp = ''
            if div3:
                temp += 'Fizz'
            if div5:
                temp += 'Buzz'
            if temp == '':
                temp = str(i)
            ret.append(temp)

        return ret
