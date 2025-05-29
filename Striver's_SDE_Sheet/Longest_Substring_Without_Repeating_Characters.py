# 3. Longest Substring Without Repeating Characters
#
# Given:
# - A string `s`.
#
# Task:
# - Find the length of the longest substring without repeating characters.
#
# Constraints:
# - 0 <= s.length <= 5 * 10^4
# - s consists of English letters, digits, symbols and spaces.
#
# Examples:
# - Input: "abcabcbb" -> Output: 3 (substring "abc")
# - Input: "bbbbb" -> Output: 1 (substring "b")
# - Input: "pwwkew" -> Output: 3 (substring "wke")

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0          # To store the maximum length found so far
        substr = ''          # Temporary substring to track unique characters

        for i in range(len(s)):
            if s[i] not in substr:
                substr += s[i]  # Append current char if not in current substring
                longest = max(longest, len(substr))  # Update max length
            else:
                # Skip characters up to the first occurrence of the repeated character
                substr = substr[substr.find(s[i]) + 1:] + s[i]

        return longest
