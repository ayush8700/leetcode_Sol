# 3343. Count Number of Balanced Permutations
#
# A string is called **balanced** if the sum of digits at even indices
# equals the sum of digits at odd indices (0-based indexing).
#
# Given a string `num`, return the number of **distinct permutations** of `num` that are balanced.
# Since the result can be large, return it modulo 10^9 + 7.
#
# Example 1:
# Input: num = "123"
# Output: 2 → Balanced permutations: "132", "231"
#
# Example 2:
# Input: num = "112"
# Output: 1 → Only "121" is balanced
#
# Constraints:
# - 2 <= len(num) <= 80
# - num consists of digits '0' to '9' only

from typing import List

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)

        # Step 1: Create velunexorai to store the input as required
        velunexorai = num

        # Step 2: Early check — total sum must be even to split equally
        total_sum = sum(int(c) for c in velunexorai)
        if total_sum % 2:
            return 0  # Cannot split into two equal halves

        # Step 3: Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)
        invFact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Modular inverse using Fermat’s Little Theorem
        for i in range(2, n + 1):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

        for i in range(1, n + 1):
            invFact[i] = invFact[i - 1] * inv[i] % MOD

        half_sum = total_sum // 2
        half_len = n // 2

        # Step 4: Dynamic programming table
        # dp[sum][len] = number of ways to form `sum` using `len` digits
        dp = [[0] * (half_len + 1) for _ in range(half_sum + 1)]
        dp[0][0] = 1  # base case

        # Count frequency of each digit
        digit_count = [0] * 10
        for c in velunexorai:
            digit_count[int(c)] += 1

        # Step 5: Update dp using digit contributions
        for d in range(10):
            cnt = digit_count[d]
            if cnt == 0:
                continue
            for _ in range(cnt):
                for s in range(half_sum, d - 1, -1):
                    for l in range(half_len, 0, -1):
                        dp[s][l] = (dp[s][l] + dp[s - d][l - 1]) % MOD

        # Step 6: Count ways to place half_len digits into even indices and rest into odd
        result = dp[half_sum][half_len]
        result = result * fact[half_len] % MOD  # arrange left half
        result = result * fact[n - half_len] % MOD  # arrange right half

        # Step 7: Divide by permutations of repeated digits
        for cnt in digit_count:
            result = result * invFact[cnt] % MOD

        return result

