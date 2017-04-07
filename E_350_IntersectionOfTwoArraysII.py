"""
61 / 61 test cases passed.
Status: Accepted
Runtime: 96 ms
You are here!
Your runtime beats 12.75% of python submissions.
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        re = []
        for i in nums1:
            try:
                nums2.remove(i)
                re.append(i)
            except Exception:
                pass
        return re
