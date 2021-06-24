from __future__ import annotations 
import collections 
import random 
import heapq 
import re
import threading


"""
Success
Details 
Runtime: 44 ms, faster than 84.54% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return dfs(root, float('-inf'), float('inf'))

def dfs(curr, min_val, max_val):
    if not curr:
        return True
    if min_val < curr.val < max_val:
        return dfs(curr.left, min_val, curr.val) and dfs(curr.right, curr.val, max_val)
    return False
