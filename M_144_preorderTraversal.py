"""
Success
Details 
Runtime: 36 ms, faster than 85.59% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.3 MB, less than 5.84% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        # morris? 
        stack = [root, ]
        output = []

        while stack:
            node = stack.pop()

            if node is not None:
                output.append(node.val)
                if node.right is not None:
                    stack.append(node.right)

                if node.left is not None:
                    stack.append(node.left)

        return output

