# 2901. Longest Unequal Adjacent Groups Subsequence II
#
# Given:
# - A list of strings `words` and
# - An integer array `groups` of the same length.
#
# Task:
# Find the longest subsequence of indices such that:
# 1. Adjacent elements in the subsequence belong to different groups.
# 2. The corresponding words are the same length and have a Hamming distance of exactly 1.
#
# Return the corresponding list of words in the chosen subsequence.
# If multiple answers exist, return any one of them.
#
# Example 1:
# Input: words = ["bab","dab","cab"], groups = [1,2,2]
# Output: ["bab","cab"]
#
# Example 2:
# Input: words = ["a","b","c","d"], groups = [1,2,3,4]
# Output: ["a","b","c","d"]

from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Helper function to check if Hamming distance is exactly 1
        def hamming_distance_is_one(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        n = len(words)
        dp = [1] * n      # dp[i] stores the max length of valid subsequence ending at i
        prev = [-1] * n   # prev[i] helps reconstruct the subsequence

        # Try all pairs (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                # Check the two main constraints
                if groups[i] != groups[j] and hamming_distance_is_one(words[i], words[j]):
                    # Update if a longer subsequence ending at j is found
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        prev[j] = i

        # Find the index with the maximum subsequence length
        max_idx = max(range(n), key=lambda x: dp[x])

        # Reconstruct the path using the prev array
        result = []
        while max_idx != -1:
            result.append(words[max_idx])
            max_idx = prev[max_idx]

        # Reverse to get the correct order
        return result[::-1]
