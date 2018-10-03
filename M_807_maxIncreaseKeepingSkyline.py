"""
133 / 133 test cases passed.
Status: Accepted
Runtime: 128 ms
You are here! 
Your runtime beats 4.21 % of python submissions.
"""
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = [[] for _ in grid]
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                col[j].append(grid[i][j])
                j += 1
            i += 1

        res = 0
        m = 0
        while m < len(grid):
            n = 0
            while n < len(grid[m]):
                res += min(max(grid[m]), max(col[n])) - grid[m][n]
                n += 1
            m += 1

        return res

print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

