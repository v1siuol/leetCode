"""
Success
Details 
Runtime: 128 ms, faster than 49.63% of Python online submissions for H-Index II.
Memory Usage: 16.4 MB, less than 10.34% of Python online submissions for H-Index II.
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """
        看的边界 
        """

        size = len(citations)

        left = 0
        right = size - 1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == size - mid:
                return citations[mid]
            elif citations[mid] > size - mid:
                right = mid - 1
            else:
                left = mid + 1

        return size - (right + 1)




s = Solution()
print(s.hIndex([0,1,3,5,6]))
print(s.hIndex([1, 2, 10, 10]))
print(s.hIndex([1, 2, 10, 10, 10]))
print(s.hIndex([0,1,5,5,6]))



