"""
Author  => v1siuol
Date    => 2018.03.12

254 / 254 test cases passed.
Status: Accepted
Runtime: 44 ms
"""
class Solution:
	def numJewelsInStones(self, J, S):
		"""
		:type J: str
		:type S: str
		:rtype: int
		"""
		# O(n^2)
		count = 0
		for s in S:
			if s in J:
				count += 1

		return count



	# 用extra space之hash table减查询复杂度O(m+n)
	def tinghao(self, J, S):
		setJ = set(J)
		g = (s in setJ for s in S)
		# for i in g:
		# 	print (i)
		# print(sum(g))
		return sum(g)

Solution().tinghao("abA", "aaAbbc")

