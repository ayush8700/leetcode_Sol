# 2616. Minimize the Maximum Difference of Pairs
# Medium
#
# Problem:
#   Given an array `nums` and an integer `p`, form `p` disjoint pairs such that:
#     • No index is reused.
#     • The **maximum difference** of all selected pairs is minimized.
#
#   Return the **minimum possible value of the maximum difference**.
#
#   A pair has difference = |nums[i] - nums[j]|, and disjoint means i, j must be used only once.
#
# Example 1:
#   Input : nums = [10, 1, 2, 7, 1, 3], p = 2
#   Output: 1
#   Explanation:
#       Form pairs (1, 4) → |1-1| = 0, and (2, 5) → |2-3| = 1 → max = 1.
#
# Example 2:
#   Input : nums = [4, 2, 1, 2], p = 1
#   Output: 0
#   Explanation:
#       Pair (1, 3) → |2 - 2| = 0
#
# Constraints:
#   • 1 ≤ len(nums) ≤ 10^5
#   • 0 ≤ nums[i] ≤ 10^9
#   • 0 ≤ p ≤ len(nums) // 2
#
# Approach:
#   - Binary search on possible maximum difference [0, max(nums) - min(nums)]
#   - For each candidate value `mid`, count how many disjoint pairs can be formed with diff ≤ mid.
#   - If count ≥ p, we try smaller mid (right = mid), else we increase mid (left = mid + 1).
#   - Greedy pairing from sorted array guarantees optimal match at each step.
#
# Time Complexity: O(n log(max_diff)) where max_diff = nums[-1] - nums[0]

class Solution(object):
    def minimizeMax(self, nums, p):
        if p == 0:
            return 0

        nums.sort()  # Sort for greedy pairing
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]  # Max possible diff

        while left < right:
            mid = (left + right) // 2
            pairs = 0
            i = 1

            # Count how many disjoint pairs can be made with diff ≤ mid
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    pairs += 1
                    i += 1  # skip next since both indices used
                i += 1

            if pairs >= p:
                right = mid  # try smaller diff
            else:
                left = mid + 1  # need larger diff

        return left  # minimal maximum difference found
