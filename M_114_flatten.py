from __future__ import annotations
import collections
import random
import heapq

"""
Success
Details 
Runtime: 32 ms, faster than 92.68% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.2 MB, less than 75.53% of Python3 online submissions for Flatten Binary Tree to Linked List.
Areas of improvement: Traverse the tree in the order of always finding the last one
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def recur(root):
#             if not root.left and not root.right:
#                 return root
#             elif root.left and not root.right:
#                 root.right = root.left
#                 root.left = None
#                 return recur(root.right)
#             elif not root.left and root.right:
#                 return recur(root.right)
#             else:
#                 tmp_next = root.right
#                 root.right = root.left
#                 root.left = None
#                 last = recur(root.right)
#                 last.right = tmp_next
#                 return recur(last.right)

#         if not root:
#             return None
#         recur(root)

"""
Success
Details 
Runtime: 36 ms, faster than 76.74% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.3 MB, less than 13.47% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        next_node = None
        def recur(root):
            nonlocal next_node
            if not root:
                return
            recur(root.right)            
            recur(root.left)
            root.right = next_node
            root.left = None
            next_node = root            

        recur(root)
