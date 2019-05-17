"""
Success
Details 
Runtime: 100 ms, faster than 15.69% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 13.2 MB, less than 58.01% of Python3 online submissions for Remove Duplicate Letters.
"""
class Solution:
    def removeDuplicateLetters(self, s: 'str') -> 'str':
        cnt = [0] * 26
        ord_a = ord('a')
        for char in s:
            cnt[ord(char)-ord_a] += 1
        pos = 0
        for i, char in enumerate(s):
            if char < s[pos]:
                pos = i
            cnt[ord(char)-ord_a] -= 1
            if cnt[ord(char)-ord_a] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], '')) if s else ''


s = Solution()
print(s.removeDuplicateLetters("bcabc"))

