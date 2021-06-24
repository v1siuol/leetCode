from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
60 / 60 test cases passed.
Status: Accepted
Runtime: 65 ms
You are here!
Your runtime beats 34.34% of python submissions.
"""
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         return list(set(nums1) & set(nums2))

# print(Solution().intersection([1,2,2,1], [2,2]))


"""
Success
Details 
Runtime: 40 ms, faster than 90.28% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays.
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(n) O(n)
        return list(set(nums1) & set(nums2))
