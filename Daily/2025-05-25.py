# 2131. Longest Palindrome by Concatenating Two Letter Words
#
# Given:
# - A list of strings `words`, where each string is two lowercase letters.
#
# Goal:
# - Construct the longest possible palindrome by concatenating selected words (each used at most once).
# - Return the length of this longest palindrome.
#
# Example:
# Input: words = ["lc", "cl", "gg"]
# Output: 6
# Explanation: "lc" + "gg" + "cl" -> "lcggcl" (a palindrome of length 6)
#
# Constraints:
# - 1 <= words.length <= 10^5
# - Each word is exactly two lowercase English letters

from typing import List
import collections

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = collections.Counter(words)  # Count occurrences of each word
        total = 0                         # Total palindrome length
        has_center = 0                    # Flag for a word like "gg" used in center

        for word in freq:
            if word[0] == word[1]:  # Case: word is symmetric like "gg"
                # Use pairs of such symmetric words
                total += (freq[word] // 2) * 4
                # Check if one can be placed in the middle (only once)
                if freq[word] % 2 == 1:
                    has_center = 1
            else:
                reversed_word = word[::-1]
                if reversed_word in freq:
                    # Use as many mirror-pairs as possible
                    pair_count = min(freq[word], freq[reversed_word])
                    total += pair_count * 4
                    # Avoid double counting
                    freq[reversed_word] = 0

        return total + has_center * 2
