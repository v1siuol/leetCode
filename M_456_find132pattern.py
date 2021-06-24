from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 144 ms, faster than 99.10% of Python3 online submissions for 132 Pattern.
Memory Usage: 14.4 MB, less than 50.00% of Python3 online submissions for 132 Pattern.
"""
# 末尾 stack 
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # O(n) O(n)
        stack = []  # stack 存新elem 把比他小的都pop 
        s3 = float('-inf') # ak 

        for i in reversed(range(len(nums))):
            if nums[i] < s3:
                return True
            while stack and stack[-1] < nums[i]:
                s3 = stack.pop()
            stack.append(nums[i])
        return False
