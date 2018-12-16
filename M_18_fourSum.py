class Solution:
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		return self.k_sum(nums, target, 4)

	"""
	Runtime: 1580 ms, faster than 11.96% of Python3 online submissions for 4Sum.
	reduce to 2sum, care repetition  
	"""
	def k_sum(self, nums, target, k):
		ret_lst = []

		if k == 2:
			left_index = 0 		
			right_index = len(nums) - 1
			while left_index < right_index: 
				if nums[left_index]+nums[right_index] < target:
					while left_index < right_index and nums[left_index] == nums[left_index+1]:
						left_index += 1
					left_index += 1
				elif nums[left_index]+nums[right_index] > target:
					while left_index < right_index and nums[right_index] == nums[right_index-1]:
						right_index -= 1
					right_index -= 1
				else: 
					ret_lst.append([nums[left_index], nums[right_index]])
					while left_index < right_index and nums[left_index] == nums[left_index+1]:
						left_index += 1
					while left_index < right_index and nums[right_index] == nums[right_index-1]:
						right_index -= 1
					left_index += 1
					right_index -= 1
		else:
			fix_index = 0
			while fix_index < len(nums)-k+1:
				from_lower_layer = self.k_sum(nums[fix_index+1:], target-nums[fix_index], k-1)
				for one_pos in from_lower_layer:
					ret_lst.append([nums[fix_index]] + one_pos)

				while fix_index + 1 < len(nums) and nums[fix_index] == nums[fix_index+1]:
					fix_index += 1

				fix_index += 1

		return ret_lst


sol = Solution()
# ret = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
ret = sol.fourSum([-3,-2,-1,0,0,1,1,1,2,2], 0)
print(ret)
print(len(ret))  # 7
