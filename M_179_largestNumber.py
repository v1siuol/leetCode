"""
Success
Details 
Runtime: 40 ms, faster than 98.57% of Python3 online submissions for Largest Number.
Memory Usage: 13 MB, less than 5.26% of Python3 online submissions for Largest Number.
"""

class LargeNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
# 啊？ 
class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        ret = ''.join(sorted(map(str, nums), key=LargeNumKey))
        return '0' if ret[0] == '0' else ret



s = Solution()
print(s.largestNumber([10,2]))
print(s.largestNumber([3,30,34,5,9]))

