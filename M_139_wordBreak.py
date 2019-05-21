"""
Success
Details 
Runtime: 48 ms, faster than 51.99% of Python3 online submissions for Word Break.
Memory Usage: 13.2 MB, less than 57.61% of Python3 online submissions for Word Break.
"""
class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        dp = [True]
        word_set = set(wordDict)
        for end in range(1, len(s)+1):
            dp.append(any(dp[j] and s[j:end] in word_set for j in range(end)))
            # dp.append(any(dp[j] and s[j:end] in wordDict for j in range(end)))
            # print(dp)
        return dp[-1]



S = Solution()


s = "leetcode"
wordDict = ["leet", "code"]
print(S.wordBreak(s, wordDict))


s = "applepenapple"
wordDict = ["apple", "pen"]
print(S.wordBreak(s, wordDict))


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(S.wordBreak(s, wordDict))

