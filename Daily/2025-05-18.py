# 1931. Painting a Grid With Three Different Colors
#
# You are given two integers `m` and `n`, representing the dimensions of an m x n grid.
# Each cell of the grid must be painted either red (0), green (1), or blue (2).
#
# The constraint is:
# - No two adjacent cells (either in the same column or in adjacent columns) may have the same color.
# - All cells must be painted.
#
# Return the number of valid ways to color the grid, modulo 10^9 + 7.
#
# Example 1:
# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are [R], [G], [B].
#
# Example 2:
# Input: m = 1, n = 2
# Output: 6
# Explanation: Valid combinations: RG, RB, GR, GB, BR, BG.
#
# Example 3:
# Input: m = 5, n = 5
# Output: 580986
#
# Constraints:
# - 1 <= m <= 5
# - 1 <= n <= 1000

MOD = 10 ** 9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product
        from collections import defaultdict

        # Helper function to check if a column configuration is valid:
        # No two adjacent cells in the same column can be the same color.
        def is_valid(col) -> bool:
            return all(col[i] != col[i + 1] for i in range(len(col) - 1))

        colors = [0, 1, 2]  # 0: Red, 1: Green, 2: Blue
        valid_cols = []

        # Step 1: Generate all valid column configurations of height `m`
        for col in product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)

        # Step 2: Assign each valid column a unique index
        col_to_index = {col: idx for idx, col in enumerate(valid_cols)}
        num_cols = len(valid_cols)

        # Step 3: Build a compatibility map
        # compatible[i] = list of column indices that can follow column i
        compatible = defaultdict(list)
        for i, c1 in enumerate(valid_cols):
            for j, c2 in enumerate(valid_cols):
                # Two columns are compatible if they differ in all corresponding rows
                if all(c1[k] != c2[k] for k in range(m)):
                    compatible[i].append(j)

        # Step 4: Initialize the DP array
        # dp[i] = number of ways to end the first column with the i-th valid configuration
        dp = [1] * num_cols

        # Step 5: Iterate through remaining columns
        for _ in range(n - 1):
            new_dp = [0] * num_cols
            for prev_col in range(num_cols):
                for next_col in compatible[prev_col]:
                    new_dp[next_col] = (new_dp[next_col] + dp[prev_col]) % MOD
            dp = new_dp

        # Step 6: Sum all ways to end the grid with any valid column configuration
        return sum(dp) % MOD
