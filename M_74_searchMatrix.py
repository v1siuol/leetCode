class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		"""
		40min
		第一感二分 
		diss 做成1维 
		O(log mn)
		Runtime: 40 ms, faster than 94.04% of Python3 online submissions for Search a 2D Matrix. 
		"""
		row_num = len(matrix)
		if row_num <= 0:
			return False 
		col_num = len(matrix[0])
		if col_num <= 0:
			return False 

		total_num = row_num * col_num

		left, right = 0, total_num
		loc = total_num // 2

		while left <= right and loc < total_num:
			if matrix[loc//col_num][loc%col_num] < target:
				left = loc + 1 
			elif matrix[loc//col_num][loc%col_num] > target:
				right = loc - 1
			else:
				return True
			loc = (left + right) // 2

		return False 


sol = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(sol.searchMatrix(matrix, target))

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
print(sol.searchMatrix(matrix, target))

matrix = [

]
target = 0
print(sol.searchMatrix(matrix, target))
matrix = [
 [ ]
]
target = 1
print(sol.searchMatrix(matrix, target))
matrix = [
 [1]
]
target = 2
print(sol.searchMatrix(matrix, target))
matrix = [
 [1,3]
]
target = 3
print(sol.searchMatrix(matrix, target))