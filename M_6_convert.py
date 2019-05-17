"""
Success
Details 
Runtime: 72 ms, faster than 86.55% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.4 MB, less than 9.88% of Python3 online submissions for ZigZag Conversion.
"""


class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows == 1:
            return s
        curr_row = numRows
        ret = ''
        str_ptr = 0
        n = len(s)
        while curr_row >= 1:
            str_ptr = numRows - curr_row

            neg_row = numRows - curr_row
            while str_ptr < n:
                ret += s[str_ptr]
                str_ptr += (curr_row-1)*2

                if str_ptr < n and (curr_row != 1 and curr_row != numRows):
                    ret += s[str_ptr]
                    str_ptr += neg_row * 2
                if str_ptr < n and curr_row == 1:
                    str_ptr += neg_row * 2

            # print(ret)
            curr_row -= 1

        return ret



s = Solution()
# print(s.convert("PAYPALISHIRING", 3) == 'PAHNAPLSIIGYIR')
# print(s.convert("PAYPALISHIRING", 4) == 'PINALSIGYAHRPI')
print(s.convert("A", 1))


