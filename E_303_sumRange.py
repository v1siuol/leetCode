class NumArray:

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""

		"""
		20min
		全部cache法 TLE
		diss 用总和真的牛逼 
		Runtime: 80 ms, faster than 39.88% of Python3 online submissions for Range Sum Query - Immutable.
		"""
		# self.cache_dict = dict()
		# n = len(nums)
		# for i in range(n):
		# 	self.cache_dict[(i, i)] = nums[i]

		# for step in range(1, n):
		# 	for left in range(0, n-step):
		# 		right = left+step
		# 		self.cache_dict[(left, right)] = self.cache_dict[(left, right-1)] + self.cache_dict[(right, right)]
		for i in range(1, len(nums)):
			nums[i] += nums[i-1]
		self.nums = nums

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		# return self.cache_dict[(i, j)]
		"""
		1 2 3 4 
		1 3 6 10 
		"""
		if i == 0:
			return self.nums[j]
		return self.nums[j] - self.nums[i-1]		


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
print(param_1)
param_1 = obj.sumRange(2,5)
print(param_1)
param_1 = obj.sumRange(0,5)
print(param_1)
param_1 = obj.sumRange(0,0)
print(param_1)
