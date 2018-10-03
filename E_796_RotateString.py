"""
Author  => v1siuol
Date    => 2017.03.12

39 / 39 test cases passed.
Status: Accepted
Runtime: 56 ms
"""
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        b_end = 1
        a_start = 0
        a_end = 1
        is_matched = False

        while a_end <= len(A):
            # print(B[:b_end], A[a_start:a_end])
            if (B[:b_end] != A[a_start:a_end]):
                # diff: move a head pointer, reset b tail pointer
                is_matched = False
                a_start += 1
                a_end = a_start + 1
                b_end = 1
            else:
                # same: move a&b tail pointer
                is_matched = True
                b_end += 1
                a_end += 1

        if is_matched:
            # Compare left unshifted chars
            return A[:a_start] == B[b_end-1:]
        return is_matched

    # 思路：挺好，用加减可以少两变量
