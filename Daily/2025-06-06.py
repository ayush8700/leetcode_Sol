# 2434. Using a Robot to Print the Lexicographically Smallest String
# Medium
#
# Problem:
# You are given a string `s` and a robot that builds a string `t` (initially empty)
# and finally writes characters on paper (string `p`, initially empty).
#
# Repeat the following until both `s` and `t` are empty:
#   1. **Take from `s`** –  Remove the first character of `s` and append it to the end of `t`.
#   2. **Write from `t`** –  Remove the last character of `t` and append it to the end of `p`.
#
# You may perform these two operations in any order, as long as they are valid
# (i.e., operation 1 needs a non-empty `s`, operation 2 needs a non-empty `t`).
#
# Return the **lexicographically smallest string** `p` that can be produced.
#
# Example 1:
#   Input : s = "zza"
#   Output: "azz"
#
# Example 2:
#   Input : s = "bac"
#   Output: "abc"
#
# Example 3:
#   Input : s = "bdda"
#   Output: "addb"
#
# Constraints:
#   1 ≤ |s| ≤ 10^5
#   s consists only of lowercase English letters.

from collections import Counter
from typing import List

class Solution:
    def robotWithString(self, s: str) -> str:
        """
        Simulate the robot with a greedy rule:
        - Maintain a stack `st` for the robot’s current string `t`.
        - Maintain a frequency map `freq` of remaining characters in `s`.
        - While the top of `st` is ≤ the *smallest* unused character left in `s`,
          pop from `st` and append to answer (`p`).  This guarantees lexicographic minimality.
        """
        freq = Counter(s)  # Remaining char counts in `s`
        st: List[str] = []  # Acts as `t` (stack)
        res: List[str] = []  # Acts as `p` (answer)

        # Helper to get the smallest character that is still available in `s`
        def smallest_remaining() -> str:
            for i in range(26):
                ch = chr(ord('a') + i)
                if freq[ch] > 0:
                    return ch
            return 'a'  # Default (should not hit if handled correctly)

        # Process each character of `s`
        for ch in s:
            st.append(ch)      # Operation 1: push char to `t`
            freq[ch] -= 1      # Update remaining count in `s`

            # Greedily pop from `t` while it is safe to write
            while st and st[-1] <= smallest_remaining():
                res.append(st.pop())  # Operation 2

        # Empty any remaining chars in `t`
        while st:
            res.append(st.pop())

        return ''.join(res)
