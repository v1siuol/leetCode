"""
186 / 186 test cases passed.
Status: Accepted
Runtime: 106 ms
You are here!
Your runtime beats 59.07% of python submissions.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def v(here, r=[]):
            if here is not None:
                v(here.left)
                r.append(here.val)
                v(here.right)
                return r

        lst = v(root)
        i = 1
        min = lst[1] - lst[0]
        while i < len(lst) - 1:
            if lst[i + 1] - lst[i] < min:
                min = lst[i + 1] - lst[i]
            i += 1
        return min

        """
        re = []
        if root is None:
            return -1
        if root.val is None:
            return -1
        a = -1
        b = -1
        if root.left is not None and root.left.val is not None:
            a = root.val - root.left.val
        if root.right is not None and root.right.val is not None:
            b = root.right.val - root.val

        c = self.getMinimumDifference(root.left)
        d = self.getMinimumDifference(root.right)
        re = [a, b, c, d]
        while re.count(-1) > 0:
            re.remove(-1)
        if len(re) == 0:
            re.append(-1)
        return min(re)

        #return min(a,b, self.getMinimumDifference(root.left), self.getMinimumDifference(root.right)), key=lambda x: x==-1)
        """