"""
Author  => v1siuol
Date    => 2017.03.14

482 / 482 test cases passed.
Status: Accepted
Runtime: 60 ms
You are here! 
Your runtime beats 78.33 % of python3 submissions.
"""
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        max_row = len(matrix)
        max_col = len(matrix[0])

        # check upper right matrix
        i = 0
        j = 1
        while j < max_col:
            # i = 0
            if not self.is_seq_valid(matrix, i, j, max_row, max_col):
                return False
            j += 1

        # check bottom left matrix
        i = 1
        j = 0
        while i < max_row:
            # j = 0
            if not self.is_seq_valid(matrix, i, j, max_row, max_col):
                return False
            i += 1

        # check diagonal seq
        i = 0
        j = 0
        if not self.is_seq_valid(matrix, i, j, max_row, max_col):
            return False


        return True

    def is_seq_valid(self, matrix, i, j, max_row, max_col):
        # print(i, j)
        res = matrix[i][j]
        while i < max_row and j < max_col:
            if res != matrix[i][j]:
                return False
            i += 1
            j += 1

        return True
    # 思路：挺好，了解变量作用域吧
