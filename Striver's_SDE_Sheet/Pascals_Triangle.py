# 118. Pascal's Triangle
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
# Constraints:
# 1 <= numRows <= 30

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case: no rows to generate
        if numRows == 0:
            return []
        
        # Base case: first row is always [1]
        if numRows == 1:
            return [[1]]
        
        # Create a new row filled with 1's of length `numRows`
        newRow = [1] * numRows

        # Recursively get the triangle up to the previous row
        prevRow = self.generate(numRows - 1)

        # Fill the inner elements of the current row using the last row in the triangle
        for i in range(1, numRows - 1):
            newRow[i] = prevRow[-1][i - 1] + prevRow[-1][i]
        
        # Append the newly formed row to the result
        prevRow.append(newRow)

        # Return the full triangle up to numRows
        return prevRow
