"""
Success
Details 
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Patching Array.
Memory Usage: 13.3 MB, less than 8.33% of Python3 online submissions for Patching Array.
"""
class Solution:
    def minPatches(self, nums: 'List[int]', n: 'int') -> 'int':
        ub_covered = 1
        ret = 0
        i = 0
        while ub_covered <= n:
            if i < len(nums) and nums[i] <= ub_covered:
                ub_covered += nums[i]
                i += 1
            else:
                ub_covered += ub_covered
                ret += 1

        return ret



s = Solution()
print(s.minPatches([1,3], 6))
print(s.minPatches([1,5,10], 20))
print(s.minPatches([1,2,2], 5))
print(s.minPatches([], 8))
