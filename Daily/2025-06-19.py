# 2294. Partition Array Such That Maximum Difference Is K
# Medium
#
# Problem:
#   You are given an integer array `nums` and an integer `k`.
#   You may partition `nums` into one or more subsequences such that:
#     - Every number appears in exactly one subsequence.
#     - In each subsequence, the **difference between the max and min** is at most `k`.
#
#   Return the **minimum number of subsequences** needed.
#
# Example 1:
#   Input : nums = [3,6,1,2,5], k = 2
#   Output: 2
#   Explanation:
#       One possible partition is [1,2,3] and [5,6].
#
# Example 2:
#   Input : nums = [1,2,3], k = 1
#   Output: 2
#   Explanation:
#       Possible partition: [1,2], [3]
#
# Example 3:
#   Input : nums = [2,2,4,5], k = 0
#   Output: 3
#   Explanation:
#       Valid groups: [2,2], [4], [5]
#
# Constraints:
#   • 1 <= nums.length <= 10^5
#   • 0 <= nums[i] <= 10^5
#   • 0 <= k <= 10^5
#
# Approach:
#   • Sort the array so that we can form greedy groups.
#   • Iterate through the sorted list.
#   • Track the start (`min_val`) of the current group.
#   • If current number exceeds `min_val + k`, start a new group.
#   • Count how many such groups are needed.

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1               # At least one group is needed
        min_val = nums[0]     # First group's min value

        for num in nums[1:]:
            if num - min_val > k:
                ans += 1      # Start a new group
                min_val = num # Reset min_val for new group

        return ans
