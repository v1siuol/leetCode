class Solution:
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""

		"""
		35min 
		O(n^2)
		模拟方向走 
		Runtime: 68 ms, faster than 10.38% of Python3 online submissions for Spiral Matrix II.
		discuss 有神仙写法 
		"""
		curr_row = 0
		curr_col = 0
		curr_val = 1
		ret_lst = [[1 for _ in range(n)] for _ in range(n)]
		right_bound = n
		bot_bound = n 
		top_bound = 1
		left_bound = 0

		iter_count = 0

		while iter_count < n-1: #i < n

			# go right 
			while curr_col < right_bound:
				ret_lst[curr_row][curr_col] = curr_val
				curr_col += 1 
				curr_val += 1
			curr_col -= 1 
			right_bound -= 1

			# go down 
			curr_row += 1 
			while curr_row < bot_bound:
				ret_lst[curr_row][curr_col] = curr_val
				curr_row += 1 
				curr_val += 1
			curr_row -= 1 
			bot_bound -= 1

			# go left 
			curr_col -= 1
			while curr_col >= left_bound:
				ret_lst[curr_row][curr_col] = curr_val
				curr_col -= 1
				curr_val += 1
			curr_col += 1
			left_bound += 1

			# go up
			curr_row -= 1
			while curr_row >= top_bound:
				ret_lst[curr_row][curr_col] = curr_val
				curr_row -= 1
				curr_val += 1
			curr_row += 1
			top_bound += 1

			curr_col += 1
			iter_count += 1 

		return ret_lst 

		
sol = Solution()
print(sol.generateMatrix(1))
print(sol.generateMatrix(2))
print(sol.generateMatrix(3))
print(sol.generateMatrix(4))
