"""
Success
Details 
Runtime: 36 ms, faster than 73.10% of Python3 online submissions for Longest Absolute File Path.
Memory Usage: 13 MB, less than 91.30% of Python3 online submissions for Longest Absolute File Path.
"""
from __future__ import annotations 
import collections 


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        path_len = {0:0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line)-len(name)
            if '.' in name:
                res = max(res, path_len[depth] + len(name))
            else:
                path_len[depth+1] = path_len[depth] + len(name) + 1 
        return res 


s = Solution()

p = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(s.lengthLongestPath(p))
