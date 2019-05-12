"""
Success
Details 
Runtime: 40 ms, faster than 76.12% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 13.6 MB, less than 6.80% of Python3 online submissions for Increasing Triplet Subsequence.
"""
class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        if len(nums) < 3:
            return False
        i = float('inf') 
        j = float('inf') 
        ptr = 0
        while ptr < len(nums):
            if nums[ptr] < i:
                i = nums[ptr]
            elif i < nums[ptr] < j:
                j = nums[ptr]
            elif nums[ptr] > j:
                return True
            ptr += 1
        return False


s = Solution()
print(s.increasingTriplet([1,2,3,4,5]))
print(s.increasingTriplet([5,4,3,2,1]))
print(s.increasingTriplet([5,1,5,5,2,5,4]))
