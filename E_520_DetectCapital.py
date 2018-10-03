"""
550 / 550 test cases passed.
Status: Accepted
Runtime: 49 ms
You are here!
Your runtime beats 82.15% of python submissions.
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        return False

print(Solution().detectCapitalUse("USA"))
print(Solution().detectCapitalUse("FlaG"))

