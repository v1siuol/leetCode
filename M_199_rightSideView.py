from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 40 ms, faster than 58.62% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.6 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        right_tree(root, res, 0)
        return res

def right_tree(curr, res, level):
    if curr is None:
        return 

    if level == len(res):
        res.append(curr.val)

    right_tree(curr.right, res, level+1)
    right_tree(curr.left, res, level+1)
