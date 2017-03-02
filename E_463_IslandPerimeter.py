"""
5833 / 5833 test cases passed.
Status: Accepted
Runtime: 296 ms
You are here!
Your runtime beats 68.52% of python submissions.
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        para = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    para += 4
                    if i+1 < len(grid) and grid[i+1][j] == 1:  # bot
                        para -= 1
                    if i - 1 > -1 and grid[i-1][j] == 1:  # top
                        para -= 1
                    if j + 1 < len(grid[0]) and grid[i][j+1] == 1:  # right
                        para -= 1
                    if j - 1 > -1 and grid[i][j-1] == 1:  # left
                        para -= 1
        return para