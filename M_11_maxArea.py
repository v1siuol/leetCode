from __future__ import annotations 
import collections 
import random 
import heapq 

# class Solution:
#   def maxArea(self, height):
#       """
#       :type height: List[int]
#       :rtype: int
#       """

#       """ 
#       O(n^2)
#       TLE 
#       """
#       """
#       length = len(height) 
#       step = 1
#       container_dict = dict()

#       while step < length: 
#           for i in range(length-step):
#               prev_left_area = 0 
#               if (i, i+step-1) in container_dict:
#                   prev_left_area = container_dict[(i, i+step-1)]

#               prev_right_area = 0 
#               if (i+1, i+step) in container_dict:
#                   prev_right_area = container_dict[(i+1, i+step)]


#               container_dict[(i, i+step)] = max(min(height[i], height[i+step]) * step, prev_left_area, prev_right_area) # curr, left, right
#           step += 1

#       # print(container_dict)
#       return container_dict[(0, length-1)]
#       """

#       """
#       O(n) tips: improve current bars, so focus on curr short bar 
#       Runtime: 136 ms, faster than 8.19% of Python3 online submissions for Container With Most Water.
#       """
#       curr_max_area = 0
#       left_ptr = 0
#       right_ptr = len(height) - 1
#       while left_ptr < right_ptr:
#           curr_max_area = max(curr_max_area, min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr))

#           if height[left_ptr] < height[right_ptr]:
#               left_ptr += 1
#           else:
#               right_ptr -= 1

#       return curr_max_area

# sol = Solution()
# ret = sol.maxArea([1,8,6,2,5,4,8,3,7])  # 49 
# print(ret)


"""
Success
Details 
Runtime: 68 ms, faster than 44.93% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.3 MB, less than 95.28% of Python3 online submissions for Container With Most Water.
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0 
        left = 0
        right = len(height)-1
        while left < right:
            ret = max(ret, min(height[left], height[right]) * (right-left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1  

        return ret
