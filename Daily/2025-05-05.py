# 790. Domino and Tromino Tiling
# You are given a 2 x n board and tiles of size:
# - Domino (2 x 1) which can be rotated
# - Tromino (an "L" shape made by three 1x1 tiles)
#
# Return the number of ways to tile the 2 x n board using these tiles.
# Since the answer can be large, return it modulo 10^9 + 7.
#
# Example 1:
# Input: n = 3
# Output: 5
# Explanation:
# The 5 ways to tile are:
# - 3 vertical dominoes
# - 1 horizontal domino + 2 vertical
# - 2 vertical + 1 horizontal
# - 1 tromino (L-shape) + 1 vertical
# - mirrored L-shape + 1 vertical
#
# Example 2:
# Input: n = 1
# Output: 1
#
# Constraints:
# 1 <= n <= 1000

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base cases
        if n == 1:
            return 1  # Only one vertical domino
        if n == 2:
            return 2  # Two vertical or two horizontal
        if n == 3:
            return 5  # Predefined

        # Dynamic Programming table to store number of ways for each length
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty board
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        # Recurrence:
        # dp[n] = 2 * dp[n-1] + dp[n-3]
        # Explanation:
        # - 2 * dp[n-1]: Add vertical domino or tromino
        # - dp[n-3]: Handles complex shapes formed by previous trominos
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
