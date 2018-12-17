class Solution:
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		"""
		20min
		O(n)
		Runtime: 40 ms, faster than 73.52% of Python3 online submissions for Plus One.
		从尾走 
		"""
		for i in range(len(digits)-1,-1,-1):
			if digits[i] < 9:
				digits[i] += 1
				return digits
			else:
				digits[i] = 0

		return [1] + digits

		
sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([1,1,9]))
print(sol.plusOne([1,9,9]))
print(sol.plusOne([9,9,9]))
print(sol.plusOne([0]))
print(sol.plusOne([9]))
