class Solution:
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		"""
		45min
		自己位的是错的 
		diss 神仙 前置位跟之前的一样 尾位看1 
		Runtime: 164 ms, faster than 40.49% of Python3 online submissions for Counting Bits.
		"""
		ret_lst = [0] # init 
		for i in range(1, num+1):
			ret_lst.append(ret_lst[i>>1] + (i&1)) # i>>1 = i//2 i&2 check LSB 
		return ret_lst


sol = Solution()
print(sol.countBits(2))
print(sol.countBits(5))
print(sol.countBits(4))
print(sol.countBits(16))
