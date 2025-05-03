# 1007. Minimum Domino Rotations For Equal Row
# Medium

# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
# You can rotate any domino to swap top and bottom values.

# Goal:
# Return the minimum number of rotations so that all values in either the top or bottom row are the same.
# If not possible, return -1.

# Example 1:
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: Rotate the 2nd and 4th dominoes to get all 2s on the top row.

# Example 2:
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: No single number can be made consistent across a row.

# Constraints:
# - 2 <= tops.length <= 2 * 10^4
# - tops.length == bottoms.length
# - 1 <= tops[i], bottoms[i] <= 6

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)

        # Helper function to check how many rotations needed to make all values equal to x
        def check(x):
            count_top = 0     # rotations to bring x to top row
            count_bottom = 0  # rotations to bring x to bottom row
            for i in range(N):
                # If neither side has x, it's impossible
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                # If top is not x, we need to rotate this domino to bring x to top
                elif tops[i] != x:
                    count_top += 1
                # If bottom is not x, we need to rotate to bring x to bottom
                elif bottoms[i] != x:
                    count_bottom += 1
            return min(count_top, count_bottom)

        # Try with the first value in tops or bottoms
        result = min(check(tops[0]), check(bottoms[0]))
        return result if result != float('inf') else -1
