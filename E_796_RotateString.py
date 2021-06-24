from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Author  => v1siuol
Date    => 2017.03.12

39 / 39 test cases passed.
Status: Accepted
Runtime: 56 ms
"""
# class Solution:
#     def rotateString(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: bool
#         """
#         b_end = 1
#         a_start = 0
#         a_end = 1
#         is_matched = False

#         while a_end <= len(A):
#             # print(B[:b_end], A[a_start:a_end])
#             if (B[:b_end] != A[a_start:a_end]):
#                 # diff: move a head pointer, reset b tail pointer
#                 is_matched = False
#                 a_start += 1
#                 a_end = a_start + 1
#                 b_end = 1
#             else:
#                 # same: move a&b tail pointer
#                 is_matched = True
#                 b_end += 1
#                 a_end += 1

#         if is_matched:
#             # Compare left unshifted chars
#             return A[:a_start] == B[b_end-1:]
#         return is_matched

#     # 思路：挺好，用加减可以少两变量


"""
Success
Details 
Runtime: 28 ms, faster than 94.99% of Python3 online submissions for Rotate String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rotate String.
"""
# class Solution:
#     def rotateString(self, A: str, B: str) -> bool:
#         # O(n) O(n)
#         if len(A) != len(B):
#             return False
#         rot_A = A
#         while rot_A != B:
#             rot_A = rot(rot_A)
#             if rot_A == A:
#                 return False
#         return True
        
# def rot(word):
#     return word[1:len(word)] + word[0]

"""
Success
Details 
Runtime: 32 ms, faster than 85.18% of Python3 online submissions for Rotate String.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotate String.
"""
# cv from solution 
# class Solution:
#     def rotateString(self, A: str, B: str) -> bool:
#         N = len(A)
#         if N != len(B): return False
#         if N == 0: return True

#         #Compute shift table
#         shifts = [1] * (N+1)
#         left = -1
#         for right in range(N):
#             while left >= 0 and B[left] != B[right]:
#                 left -= shifts[left]
#             shifts[right + 1] = right - left
#             left += 1

#         #Find match of B in A+A
#         match_len = 0
#         for char in A+A:
#             while match_len >= 0 and B[match_len] != char:
#                 match_len -= shifts[match_len]

#             match_len += 1
#             if match_len == N:
#                 return True

#         return False


"""
Success
Details 
Runtime: 28 ms, faster than 94.99% of Python3 online submissions for Rotate String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rotate String.
"""
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A

