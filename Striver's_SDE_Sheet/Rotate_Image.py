# 48. Rotate Image
#
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You must rotate the image in-place, meaning you cannot use another 2D matrix.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
# Constraints:
# - n == matrix.length == matrix[i].length
# - 1 <= n <= 20
# - -1000 <= matrix[i][j] <= 1000

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        N = len(matrix)

        # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(N - 1):
            for j in range(i + 1, N):
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a

        # Step 2: Reverse each row
        for i in range(N):
            for j in range(N // 2):
                a = matrix[i][j]
                matrix[i][j] = matrix[i][N - j - 1]
                matrix[i][N - j - 1] = a
