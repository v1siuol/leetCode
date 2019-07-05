"""
Success
Details 
Runtime: 60 ms, faster than 89.47% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 14.8 MB, less than 69.84% of Python3 online submissions for Largest Rectangle in Histogram.
"""
from __future__ import annotations 
import collections 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = collections.deque()
        stack.append(-1)
        max_area = 0

        for curr_i, curr_h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= curr_h:
                max_area = max(max_area, heights[stack.pop()] * (curr_i - stack[-1] - 1))
            stack.append(curr_i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))

        return max_area



s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))  # 10
