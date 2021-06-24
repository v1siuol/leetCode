from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 36 ms, faster than 99.40% of Python3 online submissions for Next Permutation.
Memory Usage: 13.3 MB, less than 20.98% of Python3 online submissions for Next Permutation.
"""

# class Solution:
#     def nextPermutation(self, nums: 'List[int]') -> 'None':
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # nums 不为空
#         j = len(nums) - 1
#         while j > 0:
#             if nums[j] > nums[j-1]:
#                 # find
#                 break
#             j -= 1

#         if j > 0:
#             l_min_pos = j - 1 
#             swap_next_pos = j + 1 
#             # curr is smaller than l_min
#             while swap_next_pos < len(nums):
#                 if nums[swap_next_pos] <= nums[l_min_pos]:
#                     break
#                 swap_next_pos += 1
#             swap_next_pos -= 1
#             nums[l_min_pos], nums[swap_next_pos] = nums[swap_next_pos], nums[l_min_pos]
#             # print(l_min_pos, j, swap_next_pos, nums)

#         # all reverse 
#         if j == 0:
#             l_min_pos = -1


#         left = l_min_pos + 1
#         right = len(nums) - 1

#         # reverse
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1



# s = Solution()
# lst = [1, 2, 3]
# s.nextPermutation(lst)
# print(lst)


# lst = [3, 2, 1]
# s.nextPermutation(lst)
# print(lst)

# lst = [1, 1, 5]
# s.nextPermutation(lst)
# print(lst)

# lst = [1]
# s.nextPermutation(lst)
# print(lst)


# lst = [1, 5, 1]
# s.nextPermutation(lst)
# print(lst)


"""
Success
Details 
Runtime: 40 ms, faster than 84.13% of Python3 online submissions for Next Permutation.
Memory Usage: 13.2 MB, less than 48.01% of Python3 online submissions for Next Permutation.
"""

# 奇妙的做法 
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         j = n - 1
#         while j > 0:
#             if nums[j] > nums[j-1]:
#                 # find
#                 break
#             j -= 1
#         # 123
#         #   j
#         #   i

#         if j == 0:
#             reverse(nums, 0, n-1)
#         else:
#             val = nums[j-1]
#             i = n-1
#             while i >= j:
#                 if nums[i] > val:
#                     break
#                 i -= 1
#             swap(nums, i, j-1)
#             reverse(nums, j, n-1)

# def swap(nums, i, j):
#     nums[i], nums[j] = nums[j], nums[i]

# def reverse(nums, start, end):
#     if start > end:
#         return 
#     for i in range(start, (start+end)//2+1):
#         swap(nums, i, start+end-i)


"""
Success
Details 
Runtime: 36 ms, faster than 99.43% of Python3 online submissions for Next Permutation.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Next Permutation.
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n - 1

        while j > 0 and nums[j] <= nums[j-1]:
            j -= 1

        if j == 0:
            reverse(nums, 0, n-1)
        else:
            # find next big 
            small_val = nums[j-1]
            reverse_start = j
            while j <= n-1:
                if nums[j] <= small_val:
                    break
                j += 1

            swap(nums, reverse_start-1, j-1)
            reverse(nums, reverse_start, n-1)


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def reverse(nums, i, j):
    for k in range(i, ((i+j)//2) + 1):
        swap(nums, k, i+j-k)
