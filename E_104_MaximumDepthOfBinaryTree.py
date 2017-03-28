"""
38 / 38 test cases passed.
Status: Accepted
Runtime: 69 ms
You are here!
Your runtime beats 53.52% of python submissions.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
