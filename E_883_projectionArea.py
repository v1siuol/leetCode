"""
90 / 90 test cases passed.
Status: Accepted
Runtime: 32 ms
You are here! 
Your runtime beats 49.54 % of python submissions.
"""
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        col = [[] for _ in grid[0]]

        for i in grid:
            coli = 0
            for j in i:
                if j > 0:
                    # top
                    res += 1
                col[coli].append(j)
                coli += 1

            # row
            res += max(i)

        for i in col:
            res += max(i)

        return res

print(Solution().projectionArea([[1,2],[3,4]]))
