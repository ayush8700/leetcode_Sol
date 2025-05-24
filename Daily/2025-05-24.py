# 2942. Find Words Containing Character
#
# You are given:
# - A list of lowercase strings `words`
# - A character `x`
#
# Task:
# - Return a list of indices `i` such that `x` occurs in `words[i]`
# - The order of indices in the output does not matter
#
# Example:
# Input: words = ["leet", "code"], x = "e"
# Output: [0, 1]  # Both "leet" and "code" contain 'e'
#
# Constraints:
# - 1 <= words.length <= 50
# - 1 <= words[i].length <= 50
# - Each word and `x` are lowercase English letters

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result
