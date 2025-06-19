# 2966. Divide Array Into Arrays With Max Difference
# Medium
#
# Problem:
#   Given an array `nums` of length `n` (a multiple of 3) and an integer `k`,
#   divide `nums` into n/3 subarrays of size 3 such that:
#       - In each subarray, the maximum difference between any two elements is ≤ k.
#
#   Return any valid 2D list of subarrays if possible.
#   If not possible, return an empty list.
#
# Example 1:
#   Input : nums = [1,3,4,8,7,9,3,5,1], k = 2
#   Output: [[1,1,3], [3,4,5], [7,8,9]]
#
# Example 2:
#   Input : nums = [2,4,2,2,5,2], k = 2
#   Output: []
#
# Constraints:
#   • 1 <= n <= 10^5
#   • n is a multiple of 3
#   • 1 <= nums[i] <= 10^5
#   • 1 <= k <= 10^5
#
# Approach:
#   • Sort the array.
#   • Process in chunks of 3 elements.
#   • For each triplet, check that max - min <= k.
#   • If not, return [].
#   • Otherwise, collect all valid groups and return.

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(0, len(nums), 3):
            # Group of 3 consecutive numbers
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])

        return ans
