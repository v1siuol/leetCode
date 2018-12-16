class Solution:
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""

		"""
		O = nlogn + n^2 = O(n^2)
		Runtime: 104 ms, faster than 86.33% of Python3 online submissions for 3Sum Closest.
		定点双指针 移动看在target左右 记录看差值  
		"""
		nums.sort()

		fix_index = 0
		ret_opt_sum = nums[0] + nums[1] + nums[2]
		curr_min_gap = abs(ret_opt_sum - target)

		while fix_index < len(nums)-2:
			curr_left = fix_index + 1
			curr_right = len(nums) - 1 
			while curr_left < curr_right:
				curr_sum = nums[fix_index] + nums[curr_left] + nums[curr_right]
				curr_gap = abs(curr_sum - target)

				if curr_gap < curr_min_gap:
					ret_opt_sum  = curr_sum
					curr_min_gap = curr_gap
					if curr_min_gap == 0:
						return target

				if curr_sum < target:
					curr_left += 1
				else:
					curr_right -= 1

			fix_index += 1
		return ret_opt_sum 


sol = Solution()
ret = sol.threeSumClosest([-1, 2, 1, -4], 1)
print(ret)

ret = sol.threeSumClosest([1,2,4,8,16,32,64,128], 82)
print(ret)
