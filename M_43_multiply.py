"""
Success
Details 
Runtime: 116 ms, faster than 54.99% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.1 MB, less than 76.42% of Python3 online submissions for Multiply Strings.
"""
class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        num1 = num1[::-1]
        num2 = num2[::-1]

        ord_0 = ord('0')
        l1 = len(num1)
        l2 = len(num2)
        mul = [0] * (l1 + l2)
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = (ord(num1[i]) - ord_0) * (ord(num2[j]) - ord_0) + mul[i+j]
                mul[i+j] = temp % 10
                mul[i+j+1] += temp // 10
                # print(num1[i], num2[j], mul)

        i = l1 + l2 - 1
        zero = 0
        while i >= 0:
            if mul[i] == 0:
                zero += 1
            else:
                break
            i -= 1

        if zero == l1 + l2:
            return '0'

        return ''.join(map(str, mul[~zero::-1]))



s = Solution()
print(s.multiply('2', '3') , s.multiply('2', '3') == '6')
print(s.multiply('123', '456'), s.multiply('123', '456') == '56088')
print(s.multiply('123', '0'))

