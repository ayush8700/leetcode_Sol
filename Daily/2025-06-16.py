# 2016. Maximum Difference Between Increasing Elements
# Easy
#
# Problem:
#   Given a 0-indexed array `nums` of size `n`, find the maximum difference
#   between two elements such that:
#     • i < j
#     • nums[i] < nums[j]
#     • Return nums[j] - nums[i]
#
#   If no such pair exists, return -1.
#
# Example 1:
#   Input : nums = [7, 1, 5, 4]
#   Output: 4
#   Explanation: The max diff = 5 - 1 = 4 with i = 1, j = 2
#
# Example 2:
#   Input : nums = [9, 4, 3, 2]
#   Output: -1 (no increasing pair)
#
# Example 3:
#   Input : nums = [1, 5, 2, 10]
#   Output: 9 (10 - 1)
#
# Constraints:
#   • 2 <= nums.length <= 1000
#   • 1 <= nums[i] <= 10^9
#
# Approach:
#   • Use a single pass to track the minimum seen so far (`min_val`)
#   • For each element, if it's greater than min_val, compute diff
#   • Update max_diff if the current difference is greater

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]     # Smallest value seen so far
        max_diff = -1         # Maximum difference found

        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            if nums[i] > min_val:
                # A valid increasing pair is found
                max_diff = max(max_diff, nums[i] - min_val)
            else:
                # Update the minimum value for future comparisons
                min_val = nums[i]

        return max_diff
