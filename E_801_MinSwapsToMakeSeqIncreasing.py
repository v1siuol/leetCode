"""
Author  => v1siuol
Date    => 2017.03.18


"""
class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # dp a
        ？
        i = 0
        count = 0
        hasSwaped = False
        while i < len(A)-1:
            
            if A[i] >= A[i+1]:
                count += 1
                hasSwaped = True
                # print(A[i], A[i+1])
            else:
                hasSwaped = False
                if B[i] >= B[i+1]:
                    count += 1

                
            if hasSwaped:
                while B[i] < A[i-1] and i>0:
                    count += 1
                    i -= 1
                
            while hasSwaped and i < len(A)-1:
                if B[i] >= A[i+1]:
                    count += 1
                    hasSwaped = True
                    # print(A[i], A[i+1])
                    i += 1
                    
                else:
                    hasSwaped = False
            i += 1


        return count