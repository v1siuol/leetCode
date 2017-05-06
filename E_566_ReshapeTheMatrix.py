"""
56 / 56 test cases passed.
Status: Accepted
Runtime: 176 ms
You are here!
Your runtime beats 39.94 % of python submissions.
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        else:
            re = []

            count = 0
            k = 0
            i = 0
            j = 0
            temp = []
            #for i in nums:
            while i < len(nums):
                j = 0
                #for j in i:
                while j < len(nums[i]):
                    if count < c:
                        #temp.append(j)
                        temp.append(nums[i][j])
                        count += 1
                    if count >= c:
                        re.append(temp)
                        temp = []
                        count = 0
                    j += 1
                    #print(re, i, j)

                i += 1
                #print(re, i, j)
        return re
