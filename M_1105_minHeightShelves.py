from __future__ import annotations 
import collections 
import random 
import heapq 
import math
import bisect


"""
Success
Details 
Runtime: 60 ms, faster than 60.56% of Python3 online submissions for Filling Bookcase Shelves.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Filling Bookcase Shelves.
"""

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [0] * (n+1)

        for i in range(1, n+1):
            width, height = books[i-1]
            dp[i] = dp[i-1] + height

            for j in range(i-1, 0, -1):
                width += books[j-1][0]
                if width > shelf_width:
                    break
                height = max(height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1]+height)
        return dp[n]
