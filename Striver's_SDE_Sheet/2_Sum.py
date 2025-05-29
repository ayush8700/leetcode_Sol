# 1. Two Sum
#
# Given:
# - An array of integers `nums` and an integer `target`.
#
# Task:
# - Return indices of the two numbers such that they add up to target.
#
# Constraints:
# - Each input has exactly one solution.
# - You may not use the same element twice.
# - You can return the answer in any order.
#
# Examples:
# - Input: nums = [2,7,11,15], target = 9 -> Output: [0,1]
# - Input: nums = [3,2,4], target = 6 -> Output: [1,2]
# - Input: nums = [3,3], target = 6 -> Output: [0,1]
#
# Follow-up:
# - Can you solve it in less than O(n^2) time?

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute-force approach: check every pair
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number and its index
        seen = {}

        # Iterate through the list with index
        for i, num in enumerate(nums):
            # Compute the number needed to reach the target
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in seen:
                # If found, return the index of the complement and the current index
                return [seen[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i

        # The problem guarantees a solution, so this line is never reached
        return []
