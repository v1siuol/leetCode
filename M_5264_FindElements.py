from __future__ import annotations 
import collections 
import random 
import heapq 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = set()
        recur(root, 0, self.vals)

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


def recur(root, root_val, store):
    if not root:
        return
    root.val = root_val
    store.add(root_val)
    recur(root.left, root_val * 2 + 1, store)
    recur(root.right, root_val * 2 + 2, store)
