# 2900. Longest Unequal Adjacent Groups Subsequence I
#
# You are given:
# - a list of strings `words`, and
# - a binary array `groups` of the same length.
#
# Your task is to select the longest *alternating* subsequence from `words`.
# A subsequence is alternating if for any two consecutive elements, 
# their corresponding group values differ (i.e., not equal).
#
# Return the selected words from the longest alternating subsequence.
# If multiple valid subsequences exist, return any one of them.
#
# Example 1:
# Input: words = ["e","a","b"], groups = [0,0,1]
# Output: ["e","b"]
#
# Example 2:
# Input: words = ["a","b","c","d"], groups = [1,0,1,1]
# Output: ["a","b","c"]

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)

        # Initialize the result with the first word
        res = [words[0]]

        # Keep track of the group of the last added word
        last_group = groups[0]

        # Iterate through the remaining elements
        for i in range(1, N):
            # Only add the word if its group differs from the last one added
            if last_group != groups[i]:
                res.append(words[i])
                last_group = groups[i]

        # Return the constructed alternating subsequence
        return res
