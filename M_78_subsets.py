class Solution:
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		"""
		20min
		看后面叠加
		1
		1 1,2
		1 1,3 1,2, 1,2,3
		Runtime: 60 ms, faster than 18.80% of Python3 online submissions for Subsets.
		"""
		ret_lst = [[]]
		for fix_index in range(len(nums)):
			fix_lst = [[nums[fix_index]]]
			for rest_index in range(fix_index+1, len(nums)):
				n = len(fix_lst)
				for prev in range(n):
					fix_lst.append(fix_lst[prev]+[nums[rest_index]])
			ret_lst += fix_lst
		return ret_lst



sol = Solution()
print(sol.subsets([1,2,3]))
print(sol.subsets([1,2]))
print(sol.subsets([]))
