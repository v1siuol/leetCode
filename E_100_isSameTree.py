from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 24 ms, faster than 97.47% of Python3 online submissions for Same Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Same Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return recur(p, q)
    
def recur(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return recur(p.left, q.left) and recur(p.right, q.right)
