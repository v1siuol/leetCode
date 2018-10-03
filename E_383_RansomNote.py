"""
126 / 126 test cases passed.
Status: Accepted
Runtime: 159 ms
You are here!
Your runtime beats 47.04% of python submissions.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = list(magazine)
        for i in ransomNote:
            try:
                m.remove(i)
            except ValueError:
                return False
        return True

print(Solution().canConstruct("aa", "aab"))
print(Solution().canConstruct("aa", "ab"))
