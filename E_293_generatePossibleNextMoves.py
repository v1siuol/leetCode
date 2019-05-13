"""
Success
Details 
Runtime: 44 ms, faster than 22.69% of Python3 online submissions for Flip Game.
Memory Usage: 13.3 MB, less than 6.67% of Python3 online submissions for Flip Game.
"""
class Solution:
    def generatePossibleNextMoves(self, s: 'str') -> 'List[str]':
        # 可以不用 list 
        ret = []
        lst_s = list(s)
        for i in range(1, len(s)):
            if s[i] == s[i-1] == '+':
                ret.append(''.join(lst_s[:i-1] + ['--'] + lst_s[i+1:]))
        return ret


s = Solution()
print(s.generatePossibleNextMoves("++++"))


