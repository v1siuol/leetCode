from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        
        def recur(root, t1, t2, t3, te1):
            nonlocal c1
            nonlocal c2
            nonlocal c3
            nonlocal e1

            if root:
                if root.val == x:
                    e1 += 1
                    recur(root.left, False, True, False, True)
                    recur(root.right, False, False, True, True)
                elif t1:
                    c1 += 1
                    recur(root.left, True, False, False, False)
                    recur(root.right, True, False, False, False)
                elif te1:
                    e1 += 1
                    if t2:
                        c2 += 1
                        recur(root.left, False, True, False, True)
                        recur(root.right, False, True, False, True)
                    elif t3:
                        c3 += 1
                        recur(root.left, False, False, True, True)
                        recur(root.right, False, False, True, True)


        c1 = 0
        c2 = 0
        c3 = 0
        e1 = 0
        recur(root, True, False, False, False)
        # print(c1, c2, c3, e1)
        if c1 > e1:
            return True
        if c2 > c3+1+c1:
            return True
        if c3 > c2+1+c1:
            return True
        return False



# [1,2,3,4,5]
# 5
# 1


# [1,2,3,4,5,6,7,8,9,10,11]
# 11
# 3

# [1,2,3,4,5]
# 5
# 2