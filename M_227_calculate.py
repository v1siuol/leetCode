"""
Success
Details 
Runtime: 116 ms, faster than 53.82% of Python3 online submissions for Basic Calculator II.
Memory Usage: 14.8 MB, less than 70.77% of Python3 online submissions for Basic Calculator II.
"""
from __future__ import annotations 
import collections 


class Solution:
    def calculate(self, s: str) -> int:
        stack = collections.deque()
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            if not s[i].isdigit() and s[i] != ' ' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                sign = s[i]
                num = 0
        return sum(stack)


s = Solution()


s1 = "3+2*2"
print(s.calculate(s1))

s1 = " 3/2 "
print(s.calculate(s1))

s1 = " 3+5 / 2 "
print(s.calculate(s1))