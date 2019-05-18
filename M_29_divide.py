"""
Success
Details 
Runtime: 56 ms, faster than 43.94% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.2 MB, less than 60.75% of Python3 online submissions for Divide Two Integers.
"""
class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        # 可以一直从大减会快点 
        sign = (dividend > 0) ^ (divisor > 0)
        pos_dividend = abs(dividend)
        pos_divisor = abs(divisor)

        count = 0
        while pos_dividend >= pos_divisor:

            exp = 1
            div_exp = pos_divisor

            while pos_dividend >= div_exp:
                pos_dividend -= div_exp
                count += exp
                exp <<= 1
                div_exp <<= 1

        if sign:
            count = -count

        return min(max(count, -2147483648), 2147483647)



s = Solution()
# print(s.divide(10, 3), s.divide(10, 3) == 3)
# print(s.divide(7, -3) == -2)
# print(s.divide(6, 3) == 2)
# print(s.divide(6, -3) == -2)
print(s.divide(-2147483648, -1) == 2147483647)