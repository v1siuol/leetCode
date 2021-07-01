from __future__ import annotations
import collections
import random
import heapq

"""
Success
Details 
Runtime: 56 ms, faster than 18.10% of Python3 online submissions for Path Sum II.
Memory Usage: 19.8 MB, less than 5.52% of Python3 online submissions for Path Sum II.
Areas of improvement: Less mutable list copy operations
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
#         def recur(root, path, remain):
#             path.append(root.val)
#             if not root.left and not root.right and remain == root.val:
#                 ret.append(path)
#             if root.left:
#                 recur(root.left, path[:], remain-root.val)
#             if root.right:
#                 recur(root.right, path[:], remain-root.val)

#         if not root:
#             return []
#         ret = []
#         recur(root, [], targetSum)
#         return ret

"""
Success
Details 
Runtime: 36 ms, faster than 97.36% of Python3 online submissions for Path Sum II.
Memory Usage: 15.6 MB, less than 63.24% of Python3 online submissions for Path Sum II.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def recur(root, path, remain):
            path.append(root.val)
            if remain == root.val and not root.left and not root.right:
                ret.append(path[:])
            if root.left:
                recur(root.left, path, remain-root.val)
                path.pop()
            if root.right:
                recur(root.right, path, remain-root.val)
                path.pop()

        if not root:
            return []
        ret = []
        recur(root, [], targetSum)
        return ret
