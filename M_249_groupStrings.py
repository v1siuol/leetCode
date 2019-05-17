"""
Success
Details 
Runtime: 44 ms, faster than 87.92% of Python3 online submissions for Group Shifted Strings.
Memory Usage: 13.3 MB, less than 5.88% of Python3 online submissions for Group Shifted Strings.
"""

import collections

class Solution:
    def groupStrings(self, strings: 'List[str]') -> 'List[List[str]]':
        base = ord('a')
        shift = collections.defaultdict(list)
        for word in strings:
            ids = []
            for i in range(len(word)):
                gap = ord(word[i]) - ord(word[i-1])
                if gap < 0:
                    gap += 26
                ids.append(gap)
                ids.append(ids.pop(0))

            # print(word, ids)
            shift[tuple(ids)].append(word)

        return list(shift.values())


s = Solution()
print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

