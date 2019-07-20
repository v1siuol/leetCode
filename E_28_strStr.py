from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 56 ms, faster than 15.24% of Python3 online submissions for Implement strStr().
Memory Usage: 13.3 MB, less than 5.13% of Python3 online submissions for Implement strStr().
"""
# class Solution:
#     def strStr(self, haystack: 'str', needle: 'str') -> 'int':
#         h_i = 0

#         while True:
#             n_i = 0
#             while True:
#                 if n_i == len(needle):
#                     return h_i
#                 if h_i + n_i == len(haystack):
#                     return -1
#                 if needle[n_i] != haystack[h_i+n_i]:
#                     break
#                 n_i += 1
#             h_i += 1

#         return -1


# s = Solution()
# print(s.strStr("hello", "ll"))
# print(s.strStr("aaaaa", "bba"))
# print(s.strStr("ababaa", "abaa"))


"""
Success
Details 
Runtime: 48 ms, faster than 27.98% of Python3 online submissions for Implement strStr().
Memory Usage: 13.2 MB, less than 88.69% of Python3 online submissions for Implement strStr().
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i 
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i+j]:
                    break
                j += 1
            i += 1

