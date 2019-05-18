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


    def helper(curr, lst):

        if curr is not None:

            if curr.left is not None:
                self.helper(curr.left, lst)

            lst.append(curr.val)

            if curr.right is not None:
                self.helper(curr.right, lst)

