from __future__ import annotations 
import collections 
import random 
import heapq 
import re


"""
Success
Details 
Runtime: 252 ms, faster than 70.55% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Subtree of Another Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return recur_s(s, t)

def recur_s(s, t):
    if s is None:
        return False
    return same_tree(s, t) or recur_s(s.left, t) or recur_s(s.right, t)

def same_tree(s, t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    if s.val != t.val:
        return False
    return same_tree(s.left, t.left) and same_tree(s.right, t.right)
