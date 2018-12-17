class Solution:
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		"""
		20min
		O(n^2)
		Runtime: 108 ms, faster than 13.91% of Python3 online submissions for Minimum Path Sum.
		二维中的初行列初始 中间优化上左 
		"""
		m = len(grid)
		n = len(grid[0])

		for row_index in range(1, m):
			grid[row_index][0] = grid[row_index-1][0] + grid[row_index][0]

		for col_index in range(1, n):
			grid[0][col_index] = grid[0][col_index-1] + grid[0][col_index]

		for row_index in range(1, m):
			for col_index in range(1, n):
				grid[row_index][col_index] = min(grid[row_index-1][col_index], grid[row_index][col_index-1]) + grid[row_index][col_index]

		return grid[m-1][n-1]


sol = Solution()
print(sol.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
