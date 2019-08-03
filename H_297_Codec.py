from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 192 ms, faster than 9.96% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 24.5 MB, less than 5.98% of Python3 online submissions for Serialize and Deserialize Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recur(root, ret):
            if root:
                ret += str(root.val)+','
                ret = recur(root.left, ret)
                ret = recur(root.right, ret)
            else:
                ret += 'null,'
            return ret

        return '['+recur(root, '')[:-1]+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recur(data_lst):
            if data_lst[0] == 'null':
                data_lst.pop(0)
                return
            root = TreeNode(int(data_lst[0]))
            data_lst.pop(0)
            root.left = recur(data_lst)
            root.right = recur(data_lst)
            return root

        return recur(data[1:-1].split(','))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))