from __future__ import annotations 
import collections 
import random 
import heapq 


"""
Success
Details 
Runtime: 60 ms, faster than 94.91% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Delete Nodes And Return Forest.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        recur(root, True, res, to_delete)
        return res

def recur(root, is_root, res, to_delete):
    if not root:
        return None
    is_delete = root.val in to_delete
    if is_root and not is_delete:
        res.append(root)
    root.left = recur(root.left, is_delete, res, to_delete)
    root.right = recur(root.right, is_delete, res, to_delete)
    return None if is_delete else root
