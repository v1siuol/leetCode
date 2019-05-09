"""
Success
Details 
Runtime: 96 ms, faster than 52.74% of Python online submissions for Majority Element II.
Memory Usage: 12.7 MB, less than 5.00% of Python online submissions for Majority Element II.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Boyer-Moore Algorithm

        num1 = None
        num2 = None
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0: 
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # print(num1, cnt1, num2, cnt2)

        count1 = 0
        count2 = 0
        for num in nums:
            if num1 == num:
                count1 += 1
            elif num2 == num:
                count2 += 1

        res = []
        if count1 > (len(nums) // 3):
            res.append(num1)
        if count2 > (len(nums) // 3):
            res.append(num2)
        return res


s = Solution()
print(s.majorityElement([3,2,3]))


print(s.majorityElement([1, 1, 1]))

print(s.majorityElement([1, 2, 3]))
print(s.majorityElement([1,1,1,3,3,2,2,2]))

