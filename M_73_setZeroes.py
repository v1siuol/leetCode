class Solution:
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		"""
		20min
		第一感 O(2mn) 先记录行列 后改 
		discuss 有要求 space 
		Runtime: 176 ms, faster than 15.98% of Python3 online submissions for Set Matrix Zeroes.
		"""
		row_0 = False
		col_0 = False
		m = len(matrix)
		n = len(matrix[0])

		# record to head, first line exception 
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					if i == 0:
						row_0 = True
					if j == 0:
						col_0 = True
					matrix[i][0] = 0
					matrix[0][j] = 0

		# set row 0 
		for i in range(1, m):
			if matrix[i][0] == 0:
				for j in range(1, n):
					matrix[i][j] = 0

		# set col 0 
		for j in range(1, n):
			if matrix[0][j] == 0:
				for i in range(1, m):
					matrix[i][j] = 0

		# set first line 
		if row_0:
			for j in range(n):
				matrix[0][j] = 0
		if col_0:
			for i in range(m):
				matrix[i][0] = 0


sol = Solution()
m = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
sol.setZeroes(m)
print(m)

m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
sol.setZeroes(m)
print(m)
