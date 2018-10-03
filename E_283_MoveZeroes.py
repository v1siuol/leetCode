"""
21 / 21 test cases passed.
Status: Accepted
Runtime: 69 ms
You are here!
Your runtime beats 67.57% of python submissions.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)-1):
            if nums[k] == 0:
                nums.pop(k)
                nums.append(0)
            else:
                k += 1

test = [0, 0, 1]
test2 = [1, 0, 2, 0, 3, 0]
Solution().moveZeroes(test)
print(test)
Solution().moveZeroes(test2)
print(test2)
