class Solution:
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		"""
		Runtime: 108 ms, faster than 6.14% of Python3 online submissions for Jump Game.
		O(n)
		找最远 
		"""
		curr_loc = 0
		max_reach = 0
		while curr_loc < len(nums) and curr_loc <= max_reach:
			max_reach = max(curr_loc+nums[curr_loc], max_reach)
			curr_loc += 1 

		return curr_loc == len(nums)

sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))
print(sol.canJump([0]))
