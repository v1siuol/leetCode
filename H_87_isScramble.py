"""
Success
Details 
Runtime: 44 ms, faster than 99.20% of Python3 online submissions for Scramble String.
Memory Usage: 13.1 MB, less than 6.67% of Python3 online submissions for Scramble String.
"""
class Solution:
    def isScramble(self, s1: 'str', s2: 'str') -> 'bool':
        # 迷了 
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) < 4 or s1 == s2:
            return True

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False


s  = Solution()

print(s.isScramble("great", "rgeat"))
print(s.isScramble("abcde", "caebd"))

