from __future__ import annotations
import collections
import random
import heapq

"""
Success
Details
Runtime: 32 ms, faster than 64.10% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 14 MB, less than 98.94% of Python3 online submissions for Sum Root to Leaf Numbers.
Areas of improvement:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total = 0
        def recur(root, curr_sum):
            curr_sum = 10 * curr_sum + root.val
            if not root.left and not root.right:
                nonlocal total
                total += curr_sum
                return
            if root.left:
                recur(root.left, curr_sum)
            if root.right:
                recur(root.right, curr_sum)

        recur(root, 0)
        return total
