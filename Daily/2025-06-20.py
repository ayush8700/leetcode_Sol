# 3443. Maximum Manhattan Distance After K Changes
# Medium
#
# Problem:
#   You are given a string `s` made of directions:
#       - 'N': move +1 on y-axis
#       - 'S': move -1 on y-axis
#       - 'E': move +1 on x-axis
#       - 'W': move -1 on x-axis
#
#   You start at (0, 0). You can change at most `k` directions in the string.
#   You must follow the movements in order.
#
#   Return the **maximum Manhattan distance** (|x| + |y|) from the origin 
#   that can be achieved **at any point in the movement sequence**, allowing up to `k` direction changes.
#
# Example 1:
#   Input : s = "NWSE", k = 1
#   Output: 3
#   Explanation: Changing 'S' to 'N' gives "NWNE". At step 3, pos = (-1, 2), Manhattan distance = 3.
#
# Example 2:
#   Input : s = "NSWWEW", k = 3
#   Output: 6
#   Explanation: Changing to "NNWWWW" reaches (-3, 3) → Manhattan distance = 6.
#
# Constraints:
#   • 1 <= s.length <= 10^5
#   • 0 <= k <= s.length
#   • s consists only of 'N', 'S', 'E', 'W'
#
# Approach:
#   • Track net vertical (N - S) and horizontal (E - W) movement.
#   • Manhattan distance = |N - S| + |E - W|
#   • At each step i, we check how much we can boost distance by changing up to k moves:
#       - We add `min(2 * k, i + 1 - MD)` to account for how many moves can still be changed
#         and how much additional distance they can create (max 2 units per move).
#   • We update the answer with the max achievable distance seen so far.

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0

        for i in range(len(s)):
            c = s[i]
            if c == 'N':
                north += 1
            elif c == 'S':
                south += 1
            elif c == 'E':
                east += 1
            elif c == 'W':
                west += 1

            # Compute current Manhattan Distance (without changes)
            x = abs(north - south)
            y = abs(east - west)
            MD = x + y

            # Compute how much we can increase distance using changes
            # Each change can increase distance by at most 2 units (e.g., reversing direction)
            boost = min(2 * k, i + 1 - MD)

            # Update answer
            ans = max(ans, MD + boost)

        return ans
