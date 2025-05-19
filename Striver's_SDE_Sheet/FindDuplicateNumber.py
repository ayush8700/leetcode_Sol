# 287. Find the Duplicate Number
#
# Given an array nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is exactly one repeated number in nums, which may be repeated more than once.
# Return the duplicate number.
#
# You must solve the problem without modifying the array and using only constant extra space.
#
# Constraints:
# - 1 <= n <= 10^5
# - nums.length == n + 1
# - 1 <= nums[i] <= n
# - Only one integer appears more than once

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Uses Floyd's Tortoise and Hare (Cycle Detection) algorithm to find the duplicate number.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Phase 1: Finding the intersection point of the two runners
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]          # Move by 1 step
            fast = nums[nums[fast]]    # Move by 2 steps
            if slow == fast:
                break  # Cycle detected

        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow = nums[0]  # Reset one pointer to the start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
