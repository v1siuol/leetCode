"""
1000 / 1000 test cases passed.
Status: Accepted
Runtime: 63 ms
You are here!
Your runtime beats 32.41% of python submissions.
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sTod = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
                "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
        re = 0
        i = -1
        while abs(i) <= len(s):
            re += sTod[s[i]] * (26 ** (abs(i)-1))
            i -= 1
        return re

print(Solution().titleToNumber("Z"))
print(Solution().titleToNumber("AA"))
print(Solution().titleToNumber("AB"))
print(Solution().titleToNumber("BA"))
