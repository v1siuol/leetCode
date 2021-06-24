from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 32 ms, faster than 97.20% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return recur(root.left, root.right)

def recur(left, right):
    if left is None and right is None:
        return True
    elif left and right:
        return left.val == right.val and recur(left.left, right.right) and recur(left.right, right.left)
    else:
        return False
