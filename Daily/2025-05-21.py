# 73. Set Matrix Zeroes
#
# You are given an `m x n` integer matrix. If an element is 0:
# - Set its entire row and column to 0.
#
# You must do this **in-place** with constant space.
#
# Return nothing (modify the matrix in-place).
#
# Constraints:
# - 1 <= m, n <= 200
# - -2^31 <= matrix[i][j] <= 2^31 - 1
#
# Follow-up:
# - A naive approach uses O(m * n) space — not optimal.
# - A better one uses O(m + n), but you can do even better: O(1) space.

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        # Flags to check if first row or first column needs to be zeroed
        first_col_zero = False
        first_row_zero = False

        # Step 1: Determine if first row and first column should be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Step 2: Use first row and column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Set cells to 0 based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        # Step 5: Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
