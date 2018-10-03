class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        total = sum(A) + sum(B)
        gap = sum(A) - total / 2

        for i in set(A):
            if (i - gap) in B:
                return [i, int(i-gap)]




print(Solution().fairCandySwap([1,1], [2,2]))
