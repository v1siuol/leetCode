from __future__ import annotations
import collections
import random
import heapq

"""
Success
Details 
Runtime: 92 ms, faster than 54.56% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 18.5 MB, less than 91.67% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Areas of improvement: Store the index to map instead of indexing every time.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recur(left, right):
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            if left == right:
                return root
            root_idx = inorder.index(root.val)

            root.right = recur(root_idx+1, right)
            root.left = recur(left, root_idx-1)
            return root

        return recur(0, len(inorder)-1)
