from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Binary Tree Vertical Order Traversal.
Memory Usage: 13.9 MB, less than 5.80% of Python3 online submissions for Binary Tree Vertical Order Traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs 遍历记录左-1 中0 右+1 
        layer = collections.defaultdict(list)

        queue = collections.deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            if node:
                layer[i].append(node.val)
                queue.append((node.left, i-1))
                queue.append((node.right, i+1))

        return [layer[i] for i in sorted(layer)]

