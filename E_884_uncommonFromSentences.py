"""
53 / 53 test cases passed.
Status: Accepted
Runtime: 24 ms
You are here! 
Your runtime beats 77.93 % of python submissions.
"""
import collections


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = dict()
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())
        return [i for i in count if count[i] == 1]

print(Solution().uncommonFromSentences("apple apple", "banana"))
