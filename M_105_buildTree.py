from __future__ import annotations 
import collections 
import random 
import heapq 
import math


"""
Success
Details 
Runtime: 260 ms, faster than 15.73% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 17.7 MB, less than 85.12% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return helper(0, 0, len(inorder)-1, preorder, inorder)

def helper(pre_start, in_start, in_end, preorder, inorder):
    if pre_start >= len(preorder) or in_start > in_end:
        return None

    val = preorder[pre_start]

    # find in_idx
    in_idx = 0
    for i in range(in_start, in_end+1):
        if inorder[i] == val:
            in_idx = i
            break

    root = TreeNode(val)
    root.left = helper(pre_start+1, in_start, in_idx-1, preorder, inorder)
    root.right = helper(pre_start+in_idx-in_start+1, in_idx+1, in_end, preorder, inorder)
    return root 
