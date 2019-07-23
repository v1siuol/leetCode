from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 36 ms, faster than 99.89% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.7 MB, less than 5.11% of Python3 online submissions for Trapping Rain Water.
"""

# class Solution:
#     def trap(self, height: 'List[int]') -> 'int':
#         # 难啊
#         left_ptr = 0
#         right_ptr = len(height) - 1
#         left_max = 0
#         right_max = 0
#         ans = 0
#         while left_ptr < right_ptr:
#             if height[left_ptr] < height[right_ptr]:
#                 if height[left_ptr] < left_max:
#                     ans += left_max - height[left_ptr]
#                 else:
#                     left_max = height[left_ptr]
#                 left_ptr += 1
#             else:
#                 if height[right_ptr] < right_max:
#                     ans += right_max - height[right_ptr]
#                 else:
#                     right_max = height[right_ptr]
#                 right_ptr -= 1

#         return ans


# s = Solution()
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


"""
Success
Details 
Runtime: 56 ms, faster than 17.54% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.5 MB, less than 5.10% of Python3 online submissions for Trapping Rain Water.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        ret = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] <= left_max:
                    ret += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] <= right_max:
                    ret += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return ret 
