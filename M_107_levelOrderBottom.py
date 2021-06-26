from __future__ import annotations
import collections
import random
import heapq

"""
Success
Details
Runtime: 32 ms, faster than 84.23% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.4 MB, less than 86.16% of Python3 online submissions for Binary Tree Level Order Traversal II.
Areas of improvement: deque appendleft instead of list reverse
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # BFS iterative
        if not root:
            return []
        levels = []
        curr_nodes = [root]
        while curr_nodes:
            level = []
            next_nodes = []
            while curr_nodes:
                node = curr_nodes.pop(0)
                level.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            levels.append(level)
            curr_nodes = next_nodes
        levels.reverse()
        return levels
