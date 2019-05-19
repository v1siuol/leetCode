"""
Success
Details 
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Subsets II.
Memory Usage: 13.2 MB, less than 67.07% of Python3 online submissions for Subsets II.
"""
class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        # nan 
        ret = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(ret)

            for j in range(len(ret)-l, len(ret)):
                ret.append(ret[j] + [nums[i]])

        return ret 


s = Solution()
print(s.subsetsWithDup([1,2,2])) 
print(s.subsetsWithDup([]))
print(s.subsetsWithDup([1]))


# [[],[1],[1,2],[1,2,2],[2],[2,2]]
