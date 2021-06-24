from __future__ import annotations 
import collections 
import random 
import heapq 

"""
Success
Details 
Runtime: 64 ms, faster than 38.67% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.7 MB, less than 58.81% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Area to improve: short circuit
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recur(left_index, right_index):
            if left_index > right_index:
                return None
            mid_index = (left_index + right_index) // 2
            root = TreeNode(nums[mid_index])
            root.left = recur(left_index, mid_index-1)
            root.right = recur(mid_index+1, right_index)
            return root

        return recur(0, len(nums)-1)
