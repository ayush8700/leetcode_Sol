# 74. Search a 2D Matrix
#
# Given:
# - An m x n matrix with the following properties:
#   1. Each row is sorted in non-decreasing order.
#   2. The first integer of each row is greater than the last integer of the previous row.
# - An integer target.
#
# Task:
# - Return True if target exists in the matrix, otherwise False.
# - Must be done in O(log(m * n)) time complexity.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])

        Row = 0
        for i in range(N):
            if target <= matrix[i][M - 1]:
                Row = i
                break 
            else:
                Row += 1

        if Row >= N:
            return False

        for j in range(M):
            if matrix[Row][j] == target:
                return True
        return False



# Binary search as if the matrix is a 1D array

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
