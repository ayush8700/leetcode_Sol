# 3442. Maximum Difference Between Even and Odd Frequency I
# Easy
#
# Problem:
# Given a string `s` of lowercase English letters, find the maximum difference
#     diff = a1 - a2
# where:
#   • a1 is the frequency of a character that occurs an **odd** number of times,
#   • a2 is the frequency of a character that occurs an **even** number of times.
#
# Return this maximum difference.
#
# Example 1
#   Input : s = "aaaaabbc"
#   Output: 3
#   Explanation:
#       'a' occurs 5 times  (odd)
#       'b' occurs 2 times  (even)
#       diff = 5 - 2 = 3
#
# Example 2
#   Input : s = "abcabcab"
#   Output: 1
#   Explanation:
#       'a' occurs 3 times  (odd)
#       'c' occurs 2 times  (even)
#       diff = 3 - 2 = 1
#
# Constraints
#   • 3 ≤ |s| ≤ 100
#   • s contains at least one letter with odd frequency and one with even frequency
#   • Only lowercase English letters appear in s
#
# Approach (O(26) ≈ O(1) time, O(1) space):
#   1. Count the frequency of every character.
#   2. Among odd frequencies, take the maximum (max_odd).
#   3. Among even frequencies, take the minimum (min_even).
#   4. The desired maximum difference is max_odd − min_even.

from collections import Counter

class Solution:
    def maximumDifference(self, s: str) -> int:
        freq = Counter(s)
        
        max_odd  = -1   # highest odd frequency
        min_even = 101  # lowest even frequency (|s| ≤ 100)
        
        for f in freq.values():
            if f % 2 == 1:                # odd frequency
                max_odd = max(max_odd, f)
            else:                         # even frequency
                min_even = min(min_even, f)
        
        # According to constraints, both must exist
        return max_odd - min_even
