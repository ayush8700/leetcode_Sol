# 128. Longest Consecutive Sequence
# Medium

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9

# Example 3:
# Input: nums = [1, 0, 1, 2]
# Output: 3

# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # No elements, so return 0

        # Remove duplicates and sort the array
        nums = sorted(set(nums))
        
        longest = 1  # At least one number means minimum sequence length is 1
        current_streak = 1  # Track current sequence length

        # Iterate through the sorted numbers
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                # If current number is consecutive, increase streak
                current_streak += 1
                # Update longest streak if needed
                longest = max(longest, current_streak)
            else:
                # Reset current streak if sequence is broken
                current_streak = 1

        return longest
