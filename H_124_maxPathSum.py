from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 96 ms, faster than 83.81% of Python3 online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 22.2 MB, less than 6.59% of Python3 online submissions for Binary Tree Maximum Path Sum.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 妙 
        def recur(root, max_vals):
            # nonlocal max_val
            if root is None:
                return 0
            left = max(0, recur(root.left, max_vals))
            right = max(0, recur(root.right, max_vals))
            # max_val = max(max_val, left+right+root.val)
            max_vals[0] = max(max_vals[0], left+right+root.val)
            return max(left, right) + root.val

        max_vals = [float('-inf')]
        # max_val = float('-inf')
        recur(root, max_vals)
        return max_vals[0]
