from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 40 ms, faster than 56.92% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.7 MB, less than 5.47% of Python3 online submissions for Merge Sorted Array.
"""

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # 2ptr
#         i = m-1
#         j = n-1
#         k = m+n-1
#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1
#         while j >= 0:
#             nums1[k] = nums2[j]
#             k -= 1
#             j -= 1


"""
Success
Details 
Runtime: 28 ms, faster than 99.89% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
"""
# 尾进 
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         i1 = m - 1
#         i2 = n - 1
#         i = m + n - 1

#         while i1 >= 0 and i2 >= 0:

#             if nums1[i1] <= nums2[i2]:
#                 nums1[i] = nums2[i2]
#                 i2 -= 1
#             else:
#                 nums1[i] = nums1[i1]
#                 i1 -= 1

#             i -= 1

#         if i2 >= 0:
#             nums1[:i+1] = nums2[:i2+1]


"""
Success
Details 
Runtime: 48 ms, faster than 35.41% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(m+n)
        i1 = m - 1
        i2 = n - 1 
        
        i = m + n - 1
        
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] <= nums2[i2]:
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
            i -= 1
            
        if i2 >= 0:
            nums1[:i2+1] = nums2[:i2+1]
