"""
Success
Details 
Runtime: 16 ms, faster than 100.00% of Python online submissions for H-Index.
Memory Usage: 11.7 MB, less than 8.51% of Python online submissions for H-Index.
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # bucket sort 
        n = len(citations)
        bucket = {i:0 for i in range(n+1)}
        for i in citations:
            if i >= n:
                bucket[n] += 1
            else:
                bucket[i] += 1

        over_h = 0
        for j in range(n, -1, -1):
            over_h += bucket[j]
            if over_h >= j:
                return j

        return -1 


s = Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([1, 2, 10, 10]))

