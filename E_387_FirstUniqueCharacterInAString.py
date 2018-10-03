"""
104 / 104 test cases passed.
Status: Accepted
Runtime: 762 ms
You are here!
Your runtime beats 4.81% of python submissions.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        while i < len(s):
            if s[i] not in s[0:i] and s[i] not in s[i+1:]:
                return i
            else:
                i += 1
        return -1

print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("cc"))
print(Solution().firstUniqChar("aabbcc"))

