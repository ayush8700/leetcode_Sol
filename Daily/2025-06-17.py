# 3405. Count the Number of Arrays with K Matching Adjacent Elements
# Hard
#
# Problem:
#   Given integers n, m, and k:
#     • n: length of the array
#     • m: max value each element can take (1 to m)
#     • k: exactly k adjacent equal pairs (arr[i] == arr[i-1])
#   Return the number of such "good" arrays, modulo 10^9 + 7.
#
# Example 1:
#   Input : n = 3, m = 2, k = 1
#   Output: 4
#   Explanation: [1,1,2], [1,2,2], [2,1,1], [2,2,1]
#
# Example 2:
#   Input : n = 5, m = 2, k = 0
#   Output: 2
#   Explanation: [1,2,1,2,1], [2,1,2,1,2]
#
# Constraints:
#   • 1 <= n <= 10^5
#   • 1 <= m <= 10^5
#   • 0 <= k <= n - 1
#
# Approach:
#   • Choose `k` positions for equal adjacent elements from (n - 1) places => comb(n-1, k)
#   • First element can be any of m values
#   • For the (n-1-k) non-matching positions, choose a different value than previous => (m - 1) options
#   • Result = comb(n-1, k) * m * (m-1)^(n-k-1)

MOD = 10**9 + 7
MX = 10**5 + 10

# Precompute factorials and inverse factorials
fact = [1] * MX
inv_fact = [1] * MX

for i in range(1, MX):
    fact[i] = fact[i - 1] * i % MOD
    inv_fact[i] = pow(fact[i], MOD - 2, MOD)

def comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n - 1, k) * m * pow(m - 1, n - k - 1, MOD) % MOD
