"""
60 / 60 test cases passed.
Status: Accepted
Runtime: 65 ms
You are here!
Your runtime beats 34.34% of python submissions.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

print(Solution().intersection([1,2,2,1], [2,2]))
