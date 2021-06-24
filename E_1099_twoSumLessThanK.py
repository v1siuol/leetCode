from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 64 ms, faster than 27.40% of Python3 online submissions for Two Sum Less Than K.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Two Sum Less Than K.
"""
# class Solution:
#     def twoSumLessThanK(self, A: List[int], K: int) -> int:
#         # brute force O(n^2) O(1)
#         curr_max = -1
#         for i in range(len(A)):
#             for j in range(i+1, len(A)):
#                 if curr_max < A[i] + A[j] < K:
#                     curr_max = A[i] + A[j]
                    
#         return curr_max


"""
Success
Details 
Runtime: 32 ms, faster than 99.36% of Python3 online submissions for Two Sum Less Than K.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Two Sum Less Than K.
"""
# sort 双指针 
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # O(n log n) O(1)
        A.sort()

        i = 0
        j = len(A)-1
        curr_max = -1

        while i < j:
            s = A[i] + A[j]
            if s >= K:
                j -= 1
            else:
                curr_max = max(curr_max, s)
                i += 1

        return curr_max
