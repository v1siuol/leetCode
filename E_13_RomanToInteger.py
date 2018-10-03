"""
3999 / 3999 test cases passed.
Status: Accepted
Runtime: 262 ms
You are here!
Your runtime beats 5.52% of python submissions.
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        re = 0
        dic = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
               "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
               "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900,
               "M": 1000, "MM": 2000, "MMM": 3000}
        i = len(s) - 1
        while i >= 0:
            temp = s[i]
            while temp in dic:
                i -= 1
                if i < 0:
                    temp = " " + temp
                else:
                    temp = s[i] + temp
            temp = temp[1:]
            re += dic[temp]
        return re

print(Solution().romanToInt("I"))
print(Solution().romanToInt("DCXXI"))
print(Solution().romanToInt("MCMXCVI"))
