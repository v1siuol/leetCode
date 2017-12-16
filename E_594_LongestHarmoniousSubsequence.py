"""
201 / 201 test cases passed.
Status: Accepted
Runtime: 222 ms
You are here!
Your runtime beats 38.19 % of python submissions.
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        #print(nums)
        i = 0
        count1 = 0
        temp = nums[0]
        res = 0
        while i < len(nums):
            count2 = 0
            while i < len(nums) and nums[i] == temp:
                count1 += 1
                i += 1
            if i < len(nums) and nums[i] != temp:
                if nums[i] != temp + 1:
                    count1 = 0
                    temp = nums[i]
                else:
                    count2 += 1
                    temp = nums[i]
                    i += 1
                #print("as", nums[i])
                    while i < len(nums) and temp == nums[i]:
                        count2 += 1
                        i += 1
                #print("s", count1, count2, res)

                if count2 + count1 > res:
                    res = count2 + count1
                count1 = count2
                    #print(nums[i])

            #print(count1, count2, res)
        return res
