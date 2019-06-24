"""
Success
Details 
Runtime: 84 ms, faster than 91.44% of Python3 online submissions for Basic Calculator.
Memory Usage: 13.4 MB, less than 74.81% of Python3 online submissions for Basic Calculator.
"""
from __future__ import annotations 
import collections 


class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        num = 0
        stack = collections.deque()
        for token in s:
            if token.isdigit():
                num = num * 10 + int(token)
            elif token == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif token == ')':
                res += sign * num
                num = 0
                res *= stack.pop()  # sign 
                res += stack.pop()
            elif token == '+':
                res += sign * num
                num = 0
                sign = 1
            elif token == '-':
                res += sign * num
                num = 0
                sign = -1

        res += sign * num
        return res 



s = Solution()


s1 = "1 + 1"
print(s.calculate(s1))

s1 = " 2-1 + 2 "
print(s.calculate(s1))

s1 = "(1+(4+5+2)-3)+(6+8)"
print(s.calculate(s1))