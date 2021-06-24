from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 64 ms, faster than 99.16% of Python3 online submissions for Inorder Successor in BST.
Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Inorder Successor in BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(log n)
# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#         dump = TreeNode(float('inf'))
#         ret = [dump]
#         recur(root, p, ret)
#         if ret[-1] == dump:
#             return None
#         else:
#             return ret[-1]
    
# def recur(root, p, ret):
#     if p == root:
#         if p.right:
#             curr = p.right
#             while curr.left:
#                 curr = curr.left
#             ret[-1] = curr
#         return
#     if p.val < root.val < ret[-1].val:
#         ret[-1] = root
#     if p.val < root.val:
#         recur(root.left, p, ret)
#     else:
#         recur(root.right, p, ret)


"""
Success
Details 
Runtime: 72 ms, faster than 93.90% of Python3 online submissions for Inorder Successor in BST.
Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Inorder Successor in BST.
"""
# 简化神仙版 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root
