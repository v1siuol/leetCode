class Solution:
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		"""
		15min
		?? laji
		Runtime: 40 ms, faster than 50.47% of Python3 online submissions for House Robber.
		diss 有个很巧妙的ab 
		"""
		dp_dict = dict()
		n = len(nums)
		if n > 0:
			dp_dict[0] = nums[0]
			if n > 1:
				dp_dict[1] = nums[1]
				if n > 2:
					dp_dict[2] = max(dp_dict[0]+nums[2], dp_dict[1])
			else:
				return nums[0]
		else:
			return 0 

		for i in range(3, n):
			dp_dict[i] = max(dp_dict[i-3]+nums[i], dp_dict[i-2]+nums[i], dp_dict[i-1])

		return max(dp_dict[n-2], dp_dict[n-1])

		
sol = Solution()
print(sol.rob([1,2,3,1]))  # 4 
print(sol.rob([2,7,9,3,1]))  # 12 
print(sol.rob([1]))  # 1
print(sol.rob([]))  # 0
print(sol.rob([2,1]))  # 2
print(sol.rob([2,1,1,2]))  # 4 
