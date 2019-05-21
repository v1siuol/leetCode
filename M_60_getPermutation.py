"""
Success
Details 
Runtime: 36 ms, faster than 96.96% of Python3 online submissions for Permutation Sequence.
Memory Usage: 13.2 MB, less than 44.01% of Python3 online submissions for Permutation Sequence.
"""
class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        fat = [1]
        for i in range(1, n+1):
            fat.append(fat[-1]*i)

        ret = ''
        bit = n
        num = list(range(n+1))
        # while k > 0:
        while len(num)>1:
            # 迷了 k q 
            q = k // fat[bit-1]
            # print(ret, q, k, k % fat[bit-1])

            if k % fat[bit-1] > 0:
                q += 1
            ret += str(num[q])

            num.pop(q)
            k -= fat[bit-1] * (q-1)
            bit -= 1

        return ret



s = Solution()
print(s.getPermutation(3, 3))
print(s.getPermutation(4, 9))
print(s.getPermutation(1, 1))

