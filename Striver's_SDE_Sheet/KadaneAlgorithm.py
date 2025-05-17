# 53. Maximum Subarray
#
# Given an integer array `nums`, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# This solution uses Kadane's Algorithm for an efficient O(n) approach.
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
#
# Follow-up:
# Try a divide and conquer solution after understanding the O(n) approach.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize result with the first element
        res = nums[0]
        total = 0

        for n in nums:
            # If running total is negative, reset it
            if total < 0:
                total = 0
            
            # Add current number to running total
            total += n

            # Update the result if this total is a new max
            res = max(total, res)
        
        return res
