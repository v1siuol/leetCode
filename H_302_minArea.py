"""
Success
Details 
Runtime: 60 ms, faster than 61.49% of Python3 online submissions for Smallest Rectangle Enclosing Black Pixels.
Memory Usage: 13.4 MB, less than 68.66% of Python3 online submissions for Smallest Rectangle Enclosing Black Pixels.
"""
from __future__ import annotations 

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def bs(lo, hi, check):
            while lo < hi:
                mid = (lo + hi) // 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo 

        top = bs(0, x, lambda x: '1' in image[x])
        bot = bs(x+1, len(image), lambda x: '1' not in image[x])
        left = bs(0, y, lambda y: any(row[y] == '1' for row in image))
        right = bs(y+1, len(image[0]), lambda y: all(row[y] == '0' for row in image))

        return (bot-top) * (right-left)


s = Solution()

lst = [
    "0010",
    "0110",
    "0100"
]

print(s.minArea(lst, 0, 2))
