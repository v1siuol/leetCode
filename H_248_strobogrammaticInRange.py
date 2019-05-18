"""
Success
Details 
Runtime: 212 ms, faster than 47.20% of Python3 online submissions for Strobogrammatic Number III.
Memory Usage: 40 MB, less than 16.74% of Python3 online submissions for Strobogrammatic Number III.
"""
class Solution:
    def strobogrammaticInRange(self, low: 'str', high: 'str') -> 'int':
        lst = []
        i = len(low)
        while i <= len(high):
            lst += helper(i)
            i += 1
        count = len(lst)

        j = 0
        low_int = int(low)
        while j < len(lst):
            if int(lst[j]) < low_int:
                count -= 1
            else:
                break
            j += 1
        j = len(lst) - 1
        high_int = int(high)
        while j >= 0:
            if int(lst[j]) > high_int:
                count -= 1
            else:
                break
            j -= 1

        return count 


def helper(n):
    single = ['0', '1', '8']
    double = ['11', '69', '88', '96']
    double_extend = ['00', '11', '69', '88', '96']

    if n == 0:
        return []
    if n == 1:
        return single

    i = 1
    curr = double[:]
    while i < n // 2:
        _next = []
        for term in curr:
            _next += [term[:i] + ele + term[-i:] for ele in double_extend]
        curr = _next
        i += 1

    if n % 2 == 1:
        _next = []
        for term in curr:
            _next += [term[:i] + ele + term[-i:] for ele in single]
        curr = _next

    return curr


s = Solution()
print(s.strobogrammaticInRange('50', '100'))
print(s.strobogrammaticInRange('100', '1000'))
