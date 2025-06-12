# 3445. Maximum Difference Between Even and Odd Frequency II
# Hard
#
# Problem:
# Given a string `s` (digits '0' to '4') and integer `k`, return the maximum
# difference between freq[a] - freq[b] for any substring of length ≥ k
# where:
#   • freq[a] is odd,
#   • freq[b] is even.
#
# Example:
#   Input : s = "1122211", k = 3
#   Output: 1
#   Explanation:
#     Substring "11222" → '2': 3 (odd), '1': 2 (even), diff = 3 - 2 = 1
#
# Constraints:
#   • 3 ≤ |s| ≤ 3 * 10⁴
#   • Only digits '0' to '4'
#   • At least one valid substring exists (odd a and even b)
#
# Approach:
#   1. Try all (a ≠ b) character pairs.
#   2. Track count of a, b in a sliding window.
#   3. For each prefix parity status, track minimum (a-b).
#   4. Maximize: current (a-b) − previous compatible (a-b)

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(cnt_a: int, cnt_b: int) -> int:
            # Returns a unique status for (odd/even of a, b)
            return ((cnt_a & 1) << 1) | (cnt_b & 1)

        n = len(s)
        ans = float("-inf")

        for a in "01234":
            for b in "01234":
                if a == b:
                    continue

                # Initialize best values for each of the 4 parity states
                best = [float("inf")] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1

                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b

                    # Maintain sliding window of at least size k
                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b

                    right_status = getStatus(cnt_a, cnt_b)
                    # Flip a's parity to find a valid matching previous status
                    opposite_status = right_status ^ 0b10
                    if best[opposite_status] != float("inf"):
                        diff = cnt_a - cnt_b - best[opposite_status]
                        ans = max(ans, diff)

        return ans
