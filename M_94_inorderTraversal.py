"""
Success
Details 
Runtime: 36 ms, faster than 87.58% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.2 MB, less than 49.07% of Python3 online submissions for Binary Tree Inorder Traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, curr, lst):
        if curr is not None:
            if curr.left is not None:
                self.helper(curr.left, lst)
            lst.append(curr.val)
            if curr.right is not None:
                self.helper(curr.right, lst)

