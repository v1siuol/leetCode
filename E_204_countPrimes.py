"""
Success
Details 
Runtime: 356 ms, faster than 75.29% of Python3 online submissions for Count Primes.
Memory Usage: 24.9 MB, less than 57.88% of Python3 online submissions for Count Primes.
"""
class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        # 惊叹 
        if n < 2:
            return 0

        is_prime = [1] * n
        is_prime[0] = 0
        is_prime[1] = 0

        i = 2
        while i <= n ** 0.5:
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = 0
            i += 1

        return sum(is_prime)



s = Solution()
print(s.countPrimes(10))

