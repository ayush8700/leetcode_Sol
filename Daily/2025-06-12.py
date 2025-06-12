# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
# Easy
#
# Problem:
#   Given a circular array `nums`, return the maximum absolute difference
#   between any two adjacent elements. The first and last are also adjacent.
#
# Example 1:
#   Input : nums = [1, 2, 4]
#   Output: 3
#   Explanation:
#       |1 - 2| = 1
#       |2 - 4| = 2
#       |4 - 1| = 3  ← max
#
# Example 2:
#   Input : nums = [-5, -10, -5]
#   Output: 5
#
# Constraints:
#   • 2 ≤ len(nums) ≤ 100
#   • -100 ≤ nums[i] ≤ 100
#
# Approach (O(n) time, O(1) space):
#   1. Iterate through the array.
#   2. Compare each element with its next (handle circular with last vs first).
#   3. Track and return the maximum absolute difference.

from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        N = len(nums)
        maxDiff = 0

        for i in range(N):
            if i == N - 1:
                # Wrap around: compare last and first
                maxDiff = max(maxDiff, abs(nums[0] - nums[i]))
            else:
                # Normal adjacent comparison
                maxDiff = max(maxDiff, abs(nums[i] - nums[i + 1]))

        return maxDiff
