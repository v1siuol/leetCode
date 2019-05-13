"""
Success
Details 
Runtime: 72 ms, faster than 86.92% of Python3 online submissions for Candy.
Memory Usage: 15 MB, less than 21.28% of Python3 online submissions for Candy.
"""
class Solution:
    def candy(self, ratings: 'List[int]') -> 'int':
        if not ratings:
            return 0
        n = len(ratings)
        candys = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] + 1


        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candys[j] = max(candys[j], candys[j+1]+1)

        return sum(candys)



s = Solution()
print(s.candy([1,0,2]))
print(s.candy([1,2,2]))
