class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		"""
		15min 
		第一想法 bfs 
		最佳有 DP 
		Runtime: 64 ms, faster than 14.18% of Python3 online submissions for Unique Paths II.
		"""
		if obstacleGrid[0][0] == 1:
			return 0

		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		obstacleGrid[0][0] = 1

		for row_index in range(1, m):
			if obstacleGrid[row_index][0] == 1:
				obstacleGrid[row_index][0] = 0
			else:
				obstacleGrid[row_index][0] = obstacleGrid[row_index-1][0]

		for col_index in range(1, n):
			if obstacleGrid[0][col_index] == 1:
				obstacleGrid[0][col_index] = 0
			else:
				obstacleGrid[0][col_index] = obstacleGrid[0][col_index-1]

		# dp 
		for row_index in range(1, m):
			for col_index in range(1, n):
				if obstacleGrid[row_index][col_index] == 1:
					obstacleGrid[row_index][col_index] = 0
				else:
					obstacleGrid[row_index][col_index] = obstacleGrid[row_index-1][col_index] + obstacleGrid[row_index][col_index-1]

		return obstacleGrid[m-1][n-1]

sol = Solution()
print(sol.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))

