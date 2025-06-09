# 440. K-th Smallest in Lexicographical Order
# Hard
#
# Problem:
# Given two integers `n` and `k`, return the **k-th lexicographically smallest integer** in the range [1, n].
#
# Constraints:
# - 1 <= k <= n <= 10^9
#
# Example 1:
# Input : n = 13, k = 2
# Output: 10
# Explanation:
# Lexicographical order of numbers from 1 to 13 is:
# [1,10,11,12,13,2,3,4,5,6,7,8,9]
# The 2nd number is 10.
#
# Example 2:
# Input : n = 1, k = 1
# Output: 1

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Helper function to count how many numbers exist under a given prefix
        def count_numbers_with_prefix(prefix: int, limit: int) -> int:
            count = 0
            current = prefix
            next_prefix = prefix + 1

            # Count nodes in the lexicographical tree from prefix
            while current <= limit:
                count += min(next_prefix, limit + 1) - current
                current *= 10
                next_prefix *= 10
            return count

        current = 1
        k -= 1  # We start from number 1, so decrement k by 1

        while k > 0:
            children_count = count_numbers_with_prefix(current, n)
            
            if k >= children_count:
                # Move to next sibling in lex order
                k -= children_count
                current += 1
            else:
                # Move to next level (deeper prefix)
                current *= 10
                k -= 1

        return current
