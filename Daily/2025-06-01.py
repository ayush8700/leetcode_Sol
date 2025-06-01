# 2929. Distribute Candies Among Children II
# Medium

# You are given two positive integers n and limit.
# Return the total number of ways to distribute n candies among 3 children 
# such that no child gets more than 'limit' candies.

# Constraints:
# - Each child can receive between 0 and 'limit' candies.
# - Total candies distributed must equal 'n'.

# Example 1:
# Input: n = 5, limit = 2
# Output: 3
# Explanation: Valid combinations are: (1, 2, 2), (2, 1, 2), and (2, 2, 1)

# Example 2:
# Input: n = 3, limit = 3
# Output: 10
# Explanation: All combinations of 3 numbers (x, y, z) with x+y+z=3 and x, y, z ≤ 3

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0  # Total valid ways to distribute candies
        
        # Fix the number of candies for the first child: i
        for i in range(min(limit, n) + 1):
            # Remaining candies to distribute to 2 other children
            remaining = n - i
            
            # If remaining candies are more than what 2 kids can hold, skip
            if remaining > 2 * limit:
                continue
            
            # Minimum and maximum values the second child can take
            min_val = max(0, remaining - limit)
            max_val = min(remaining, limit)

            # Number of valid (j, k) pairs where j + k = remaining and both ≤ limit
            ans += max_val - min_val + 1

        return ans
