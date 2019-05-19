"""
Success
Details 
Runtime: 52 ms, faster than 12.16% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.1 MB, less than 61.63% of Python3 online submissions for Binary Tree Postorder 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        stack = [root]
        ret = []

        while stack:
            node = stack.pop()
            if node is not None:
                ret.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

        return ret[::-1]

