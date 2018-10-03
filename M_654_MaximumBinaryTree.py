"""
Author  => v1siuol
Date    => 2018.06.01
107 / 107 test cases passed.
Status: Accepted
Runtime: 208 ms
You are here! 
Your runtime beats 86.35 % of python submissions.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if nums:
            pos = nums.index(max(nums))
            root = TreeNode(nums[pos])
            root.left = self.constructMaximumBinaryTree(nums[:pos])
            root.right = self.constructMaximumBinaryTree(nums[pos+1:])
            return 
