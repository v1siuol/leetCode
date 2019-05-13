"""
Success
Details 
Runtime: 68 ms, faster than 85.53% of Python3 online submissions for Flip Game II.
Memory Usage: 14.3 MB, less than 18.18% of Python3 online submissions for Flip Game II.
"""
class Solution:
    def canWin(self, s: str) -> bool:
        # 我服.. 
        memo = dict()
        def can(s):
            if s not in memo:
                memo[s] = any(s[i:i+2] == '++' and not can(s[:i]+'-'+s[i+2:]) for i in range(len(s)))
            return memo[s]
        return can(s)


s = Solution()
print(s.canWin("++++"))

