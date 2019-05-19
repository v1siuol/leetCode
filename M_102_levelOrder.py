"""
Success
Details 
Runtime: 40 ms, faster than 95.87% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.5 MB, less than 26.74% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        # BFS 
        lst = []
        curr = [root]


        while curr:
            temp = []
            _next = []
            while curr:
                node = curr.pop(0)

                if node is not None:
                    temp.append(node.val)

                    if node.left is not None:
                        _next.append(node.left)

                    if node.right is not None:
                        _next.append(node.right)

            if temp:
                lst.append(temp)
            curr = _next

        return lst



# [1,2,3,4,null,null,5]