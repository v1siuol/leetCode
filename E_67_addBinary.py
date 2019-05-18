"""
Success
Details 
Runtime: 40 ms, faster than 90.90% of Python3 online submissions for Add Binary.
Memory Usage: 13.3 MB, less than 9.93% of Python3 online submissions for Add Binary.
"""
class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        _sum = 0
        _carry = 0

        len_a = len(a)
        len_b = len(b)

        ret = ''
        i = 1
        while i <= max(len_a, len_b):
            _a = int(a[-i]) if i <= len_a else 0
            _b = int(b[-i]) if i <= len_b else 0

            _sum = _a ^ _b ^ _carry
            _carry = _a & _b | _carry & _b | _carry & _a

            ret = str(_sum) + ret
            i += 1

        return '1'+ret if _carry == 1 else ret


s = Solution()
print(s.addBinary('11', '1'))
print(s.addBinary('1010', '1011'))
