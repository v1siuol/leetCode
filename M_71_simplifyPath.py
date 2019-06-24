"""
Success
Details 
Runtime: 36 ms, faster than 90.77% of Python3 online submissions for Simplify Path.
Memory Usage: 13.2 MB, less than 59.43% of Python3 online submissions for Simplify Path.
"""
from __future__ import annotations 
import collections 


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = collections.deque()

        lst = path.split('/')
        for name in lst:
            if name == '..':
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)
        return '/' + '/'.join(stack) 


s = Solution()
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/a/../../b/../c//.//"))
print(s.simplifyPath("/a//b////c/d//././/.."))
