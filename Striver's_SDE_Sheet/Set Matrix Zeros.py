# 73. Set Matrix Zeroes
#
# Given an m x n matrix, if an element is 0, set its entire row and column to 0s.
# Must be done *in place* with constant extra space.
#
# Strategy:
# - Use the first row and first column as markers for which rows/columns need to be zeroed.
# - Track separately whether the first row and first column originally contained any zero.
#
# Time: O(m * n)
# Space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Flags to track if the first row or first column originally had any zero
        Row1_0 = False
        Col1_0 = False

        Rows = len(matrix)
        Cols = len(matrix[0])

        # Check if any element in the first column is zero
        for i in range(Rows):
            if matrix[i][0] == 0:
                Col1_0 = True

        # Check if any element in the first row is zero
        for j in range(Cols):
            if matrix[0][j] == 0:
                Row1_0 = True

        # Use the first row and first column as markers
        # If matrix[i][j] == 0, mark matrix[i][0] and matrix[0][j] as 0
        for i in range(1, Rows):
            for j in range(1, Cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Set matrix[i][j] to 0 if either its row or column is marked
        for i in range(1, Rows):
            for j in range(1, Cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # If the first row originally had a zero, set the entire row to 0
        if Row1_0:
            for j in range(Cols):
                matrix[0][j] = 0

        # If the first column originally had a zero, set the entire column to 0
        if Col1_0:
            for i in range(Rows):
                matrix[i][0] = 0
