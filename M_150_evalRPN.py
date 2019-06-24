"""
Success
Details 
Runtime: 40 ms, faster than 92.57% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 13.4 MB, less than 17.19% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""
from __future__ import annotations 
import collections 


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        for token in tokens:
            if token == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        return stack.pop()



s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
