"""
Success
Details 
Runtime: 48 ms, faster than 99.41% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.3 MB, less than 51.66% of Python3 online submissions for Integer to Roman.
"""
from math import floor
class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        M = ['', 'M', 'MM', 'MMM']

        # print(floor(num/1000), M[floor(num/1000)])
        # print(floor((num%1000) / 100), C[floor((num%1000) / 100)])
        # print(floor((num%100) / 10), X[floor((num%100) / 10)])
        # print((num%10), I[(num%10)])

        return M[floor(num/1000)]+ C[floor((num%1000) / 100)]+X[floor((num%100) / 10)]+I[(num%10)] 



s = Solution()
# print(s.intToRoman(3))
# print(s.intToRoman(4))
# print(s.intToRoman(9))
# print(s.intToRoman(58))
# print(s.intToRoman(1994))
print(s.intToRoman(30))

