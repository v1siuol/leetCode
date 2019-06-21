"""
Success
Details 
Runtime: 84 ms, faster than 51.26% of Python3 online submissions for Russian Doll Envelopes.
Memory Usage: 14.8 MB, less than 58.72% of Python3 online submissions for Russian Doll Envelopes.
"""
from __future__ import annotations 

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda a: (a[0], -a[1]))
        dp = [0] * len(envelopes)
        size = 0
        for n in envelopes:
            i = 0
            j = size
            while i < j:
                mid = (i+j) // 2
                if dp[mid] < n[1]:
                    i = mid + 1
                else:
                    j = mid

            dp[i] = n[1]
            size = max(size, i+1)

        return size



s = Solution()
print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(s.maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]))

