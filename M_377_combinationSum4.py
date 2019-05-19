"""
Success
Details 
Runtime: 44 ms, faster than 96.97% of Python3 online submissions for Combination Sum IV.
Memory Usage: 16.8 MB, less than 23.77% of Python3 online submissions for Combination Sum IV.
"""
class Solution:
    def combinationSum4(self, nums: 'List[int]', target: 'int') -> 'int':
        # 哈？ 
        dp = [-1] * (target+1)
        dp[0] = 1
        return backtrack(dp, nums, target)

def backtrack(dp, nums, target):
    if dp[target] != -1:
        return dp[target]
    res = 0
    for num in nums:
        if num <= target:
            res += backtrack(dp, nums, target-num)
    dp[target] = res
    return res


s = Solution()
# print(s.combinationSum4([1,2,3], 4))
print(s.combinationSum4([4, 2, 1], 32))

