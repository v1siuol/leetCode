class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True

        if A[0] <= A[-1]:
            isUp = True
        else:
            isUp = False

        i = 1
        if isUp:
            while i < len(A):
                if A[i] < A[i-1]:
                    return False
                i += 1
        else:
            while i < len(A):
                if A[i] > A[i-1]:
                    return False
                i += 1

        return True
        