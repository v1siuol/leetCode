# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root = TreeNode(0)
        left_stack = [root]
        val_stack = []
        while left_stack:
            curr = left_stack.pop(0)
            val_stack.append(curr.val)
            if curr.left:
                left_stack.append(curr.left)
            if curr.right:
                left_stack.append(curr.right)







