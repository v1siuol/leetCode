"""
Success
Details 
Runtime: 240 ms, faster than 49.41% of Python3 online submissions for Word Pattern II.
Memory Usage: 13.2 MB, less than 35.51% of Python3 online submissions for Word Pattern II.
"""
class Solution:
    def wordPatternMatch(self, pattern: 'str', str: 'str') -> 'bool':
        mapping = dict()
        exist_set = set()
        return backtrack(pattern, 0, str, 0, mapping, exist_set)

def backtrack(pattern, i, str, j, mapping, exist_set):
    if i == len(pattern) or j == len(str):
        if i == len(pattern) and j == len(str):
            return True
        return False

    # part 
    p = pattern[i]
    if p in mapping:
        s = mapping[p]

        if str[j:j+len(s)] == s:
            return backtrack(pattern, i+1, str, j+len(s), mapping, exist_set)
        else:
            return False

    for k in range(j, len(str)):

        word = str[j:k+1]
        # print(pattern[i], word, mapping)
        if word in exist_set:
            continue

        mapping[pattern[i]] = word
        exist_set.add(word)

        if backtrack(pattern, i+1, str, k+1, mapping, exist_set):
            return True 

        mapping.pop(pattern[i])
        # del mapping[pattern[i]]
        exist_set.remove(word)

    return False



s = Solution()
print(s.wordPatternMatch("abab", "redblueredblue") == True)
print(s.wordPatternMatch("aaaa", "asdasdasdasd") == True)
print(s.wordPatternMatch("aabb", "xyzabcxzyabc") == False)
print(s.wordPatternMatch("itwasthebestoftimes", "ittwaastthhebesttoofttimes") == True)


