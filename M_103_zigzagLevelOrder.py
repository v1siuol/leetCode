from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 40 ms, faster than 64.94% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 13.7 MB, less than 5.41% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs 
        res = []
        bfs(root, res, 0)
        return res

def bfs(curr, res, level):
    if curr is None:
        return 

    if len(res) <= level:
        res.append([])

    curr_layer = res[level]
    if level % 2 == 0:
        curr_layer.append(curr.val)
    else:
        curr_layer.insert(0, curr.val)

    bfs(curr.left, res, level+1)
    bfs(curr.right, res, level+1)

