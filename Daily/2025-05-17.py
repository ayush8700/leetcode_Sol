# 75. Sort Colors
#
# Given an array `nums` with `n` objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
#
# Use integers 0 (red), 1 (white), and 2 (blue).
#
# Constraints:
# - Must modify the array in-place (no extra array).
# - Must not use built-in sort functions.
# - Follow-up: Can you do it in one pass with constant space?
#
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        This implementation uses a counting sort approach with two passes.
        """

        # Initialize counters for the three colors
        count0 = 0  # Count of 0s (red)
        count1 = 0  # Count of 1s (white)
        count2 = 0  # Count of 2s (blue)

        N = len(nums)

        # First pass: count the number of 0s, 1s, and 2s
        for i in range(N):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            elif nums[i] == 2:
                count2 += 1

        # Second pass: overwrite the array based on the counts
        for i in range(N):
            if count0 > 0:
                nums[i] = 0
                count0 -= 1
            elif count1 > 0:
                nums[i] = 1
                count1 -= 1
            elif count2 > 0:
                nums[i] = 2
                count2 -= 1
