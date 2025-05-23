# 3068. Find the Maximum Sum of Node Values
#
# You are given:
# - An undirected tree with `n` nodes (0-indexed)
# - A list `nums` where nums[i] is the value of node i
# - An integer `k`
# - A list of `edges` where each edge = [u, v] connects nodes u and v
#
# Alice can perform the following operation any number of times:
# - Choose any edge [u, v]
# - Apply XOR with `k` to both nums[u] and nums[v]
#
# Goal:
# - Maximize the total sum of all elements in `nums` after any number of operations
#
# Return the **maximum achievable sum**.
#
# Constraints:
# - 2 <= nums.length <= 2 * 10^4
# - 0 <= nums[i] <= 10^9
# - 1 <= k <= 10^9
# - edges form a valid tree
#
# Approach:
# - Consider each node independently:
#     - Compare original value vs XORed value
#     - Keep the version with the higher contribution to the total sum
# - If count of beneficial XOR operations is even, no issue
# - If odd, remove the one with the smallest gain to make the count even
#   (or consider replacing a non-beneficial one with the largest loss)
#
# Time complexity: O(n)

from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = 0         # Total sum after choosing best version of each node
        gain_count = 0        # Number of XOR operations that increase node value
        min_positive_gain = float('inf')   # Smallest positive gain (for possible removal)
        max_negative_gain = float('-inf')  # Largest negative gain (for possible swap)

        for val in nums:
            xor_val = val ^ k
            gain = xor_val - val
            total_sum += val

            if gain > 0:
                gain_count += 1
                total_sum += gain
                min_positive_gain = min(min_positive_gain, gain)
            else:
                max_negative_gain = max(max_negative_gain, gain)

        # Case 1: even number of beneficial XORs — all good
        if gain_count % 2 == 0:
            return total_sum

        # Case 2: odd — remove the least helpful XOR gain, or add back best negative
        return max(total_sum - min_positive_gain, total_sum + max_negative_gain)
