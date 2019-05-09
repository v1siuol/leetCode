from typing import List

"""
Success
Details 
Runtime: 68 ms, faster than 50.46% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.8 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        i = 0
        a, b = nums[0], nums[1]

        while i < len(nums):

            if a == b:
                nums.pop(i+1)
                if i + 1 >= len(nums):
                    return i+1
                b = nums[i+1]
            else:
                a = b
                if i + 2 >= len(nums):
                    return i + 2
                else:
                    b = nums[i+2]
                i += 1

        return i + 1

s = Solution()

num = [1,2,2]
print(s.removeDuplicates(num), num)

num = [1,1,2]
print(s.removeDuplicates(num), num)

num = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(num), num)
