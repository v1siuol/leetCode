class Solution:
    def myPow(self, x: 'float', n: 'int') -> 'float':
        # fast pow 哈? 
        if n < 0:
            n = -n
            x = 1 / x

        i = n
        ret = 1
        prod = x
        while i > 0:
            if i % 2 == 1:
                ret *= prod

            prod *= prod
            i //= 2
            print(i, ret, prod)

        return ret


s = Solution()
print(s.myPow(2.00000, 10))
# print(s.myPow(2.10000, 3))
# print(s.myPow(2.00000, -2))
