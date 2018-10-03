"""
987 / 987 test cases passed.
Status: Accepted
Runtime: 260 ms
You are here! 
Your runtime beats 15.55 % of python submissions.
"""
import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head, tail = -1, 0
        hash_char = collections.OrderedDict()
        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] not in hash_char:
                hash_char[s[i]] = True
                tail = i
                if tail - head > res:
                    res = tail - head
            else:
                out = hash_char.popitem(last=False)
                head += 1
                while out[0] != s[i]:
                    out = hash_char.popitem(last=False)
                    head += 1
                hash_char[s[i]] = True
                tail = i

            i += 1
        return res

print(Solution().lengthOfLongestSubstring("au"))  # 2
print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
print(Solution().lengthOfLongestSubstring("bbb"))  # 1
print(Solution().lengthOfLongestSubstring(" "))  # 1
print(Solution().lengthOfLongestSubstring(""))  # 0
