# 3355. Zero Array Transformation I
#
# You are given:
# - an integer array `nums` of size `n`
# - a list of queries `queries[i] = [li, ri]`, where each query allows you to:
#   - choose *any subset* of indices in range [li, ri]
#   - decrement their values by 1
#
# You must apply all queries in order. At the end, check:
# - Can `nums` become a zero array (i.e., all elements become 0)?
#
# Return True if possible, otherwise False.
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - 0 <= nums[i] <= 10^5
# - 1 <= queries.length <= 10^5
# - 0 <= li <= ri < nums.length

from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        
        # Step 1: Create a difference array to represent range update counts
        # diff[i] represents the net increment at index i
        diff = [0] * (n + 1)  # Extra space for handling range boundaries
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        # Step 2: Apply the difference array and validate if each index
        # received enough decrements to bring nums[i] to zero
        curr_decrement = 0
        for i in range(n):
            curr_decrement += diff[i]
            # If nums[i] needs more decrements than available, impossible
            if nums[i] > curr_decrement:
                return False

        # If we never exceeded the available decrements, it's possible
        return True
