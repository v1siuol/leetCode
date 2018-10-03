"""
69 / 69 test cases passed.
Status: Accepted
Runtime: 46 ms
You are here!
Your runtime beats 72.20 % of python submissions.
"""
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        #if ops:
        if ops[0]:
            minX = ops[0][0]
            minY = ops[0][1]
            index = 1
            while index < len(ops):
                if ops[index][0] < minX:
                    minX = ops[index][0]
                if ops[index][1] < minY:
                    minY = ops[index][1]
                index += 1
            return minX * minY
        else:
            return m * n




print(Solution().maxCount(3, 3, [[2,2],[3,3]]))
print(Solution().maxCount(3, 3, [[]]))