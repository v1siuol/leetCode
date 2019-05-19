"""
Success
Details 
Runtime: 632 ms, faster than 48.18% of Python3 online submissions for Combinations.
Memory Usage: 15.2 MB, less than 19.20% of Python3 online submissions for Combinations.
"""
class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        # 噩梦 
        ret = []
        def backtrack(first=1, lst=[]):
            if len(lst) == k:
                ret.append(lst[:])
            else:
                for i in range(first, n+1):
                    lst.append(i)
                    backtrack(i+1, lst)
                    lst.pop()

        backtrack()
        return ret


s = Solution()
# print(s.combine(4, 2))
print(s.combine(4, 3))

