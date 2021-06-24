from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 44 ms, faster than 99.47% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 13.3 MB, less than 70.00% of Python3 online submissions for Median of Two Sorted Arrays.
"""

"""
      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
"""

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         # 无敌二分 
#         m = len(nums1)
#         n = len(nums2)
#         if m > n:
#             nums1, nums2 = nums2, nums1
#             m, n = n, m

#         if n == 0:
#             return None

#         i_min = 0
#         i_max = m
#         half_len = (m + n + 1) // 2 
#         max_of_left = None 
#         min_of_right = None 
#         while i_min <= i_max:
#             i = (i_max + i_min) // 2 

#             j = half_len - i

#             if i < m and nums2[j-1] > nums1[i]:
#                 # i is too small, must increase it 
#                 i_min = i + 1 
#             elif i > 0 and nums1[i-1] > nums2[j]:
#                 # i is too big, must decrease it 
#                 i_max = i - 1
#             else:
#                 # i is perfect 
#                 if i == 0:
#                     max_of_left = nums2[j-1]
#                 elif j == 0:
#                     max_of_left = nums1[i-1]
#                 else:
#                     max_of_left = max(nums1[i-1], nums2[j-1])

#                 if (m + n) % 2 == 1:
#                     return max_of_left

#                 if i == m:
#                     min_of_right = nums2[j]
#                 elif j == n:
#                     min_of_right = nums1[i]
#                 else:
#                     min_of_right = min(nums1[i], nums2[j])

#                 return (max_of_left + min_of_right) / 2


"""
Success
Details 
Runtime: 112 ms, faster than 49.68% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.
"""

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m = len(nums1)
#         n = len(nums2)
#         if m > n:
#             nums1, nums2 = nums2, nums1
#             m, n = n, m

#         # nums1 shorter than nums2
#         imax = m 
#         imin = 0

#         half = (m + n + 1) // 2

#         while imin <= imax:
#             i = (imax + imin) // 2
#             j = half - i

#             if i > 0 and nums1[i-1] > nums2[j]:
#                 imax = i - 1
#             elif i < m and nums1[i] < nums2[j-1]:
#                 imin = i + 1
#             else:
#                 # perfect 

#                 if i == 0:
#                     max_of_left = nums2[j-1]
#                 elif j == 0:
#                     max_of_left = nums1[i-1]
#                 else:
#                     max_of_left = max(nums1[i-1], nums2[j-1])

#                 if (m + n) % 2 == 1:
#                     # one median 
#                     return max_of_left

#                 if i == m:
#                     min_of_right = nums2[j]
#                 elif j == n:
#                     min_of_right = nums1[i]
#                 else: 
#                     min_of_right = min(nums1[i], nums2[j])

#                 return (max_of_left+min_of_right)/2



"""
Success
Details 
Runtime: 92 ms, faster than 81.70% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        imin = 0
        imax = m
        half = (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i

            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            elif i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            else:
                # perfect

                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2
