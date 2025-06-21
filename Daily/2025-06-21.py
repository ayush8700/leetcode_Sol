# 3085. Minimum Deletions to Make String K-Special
# Medium
#
# Problem:
#   A string is called k-special if for all characters x and y in the string:
#       |freq(x) - freq(y)| <= k
#
#   You are given:
#     - A string `word` of lowercase letters
#     - An integer `k`
#
#   Return the minimum number of deletions required to make the string k-special.
#
# Example 1:
#   Input : word = "aabcaba", k = 0
#   Output: 3
#   Explanation:
#       Delete 2 'a's and 1 'c' → "baba" (freqs: a=2, b=2)
#
# Example 2:
#   Input : word = "dabdcbdcdcd", k = 2
#   Output: 2
#   Explanation:
#       Delete 1 'a' and 1 'd' → "bdcbdcdcd" (freqs: b=2, c=3, d=4)
#
# Example 3:
#   Input : word = "aaabaaa", k = 2
#   Output: 1
#   Explanation:
#       Delete 'b' → "aaaaaa" (all freqs = 6)
#
# Constraints:
#   • 1 <= len(word) <= 10^5
#   • 0 <= k <= 10^5
#   • word contains only lowercase letters
#
# Approach:
#   • Count frequency of all characters
#   • Try making each frequency `a` the baseline
#     - If another frequency `b` is:
#         → less than `a`: delete all of `b`
#         → greater than `a + k`: delete excess beyond `a + k`
#   • Track the minimum deletions across all baseline choices

from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        
        res = len(word)  # Start with max possible deletions
        
        for a in cnt.values():  # Try every frequency as the baseline
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted += b  # Delete all of b
                elif b > a + k:
                    deleted += b - (a + k)  # Delete b's excess
            res = min(res, deleted)
        
        return res
