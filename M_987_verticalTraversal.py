from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 60 ms, faster than 5.26% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 13.9 MB, less than 5.94% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # 跟 314 相似 bfs rec idx
        # idx_map = collections.defaultdict(list)
        idx_map = collections.defaultdict(lambda: collections.defaultdict(list))
        dfs(root, 0, 0, idx_map)
        res = []
        for same_x in sorted(idx_map):
            tmp = []
            for same_y in sorted(idx_map[same_x]):
                tmp.extend(sorted(idx_map[same_x][same_y]))
            res.append(tmp)
        return res

def dfs(root, x, y, idx_map):
    if root:
        idx_map[x][y].append(root.val)
        dfs(root.left, x-1, y+1, idx_map)
        dfs(root.right, x+1, y+1, idx_map)
