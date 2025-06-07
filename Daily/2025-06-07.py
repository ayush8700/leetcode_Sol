# 3170. Lexicographically Minimum String After Removing Stars
# Medium
#
# Problem:
# You are given a string `s` that may contain any number of '*' characters.
#
# While there is a '*', perform the following operation:
#   - Delete the **leftmost `*`** and the **smallest non-'*' character to its left**.
#     If there are multiple smallest characters, **you may choose any one** of them.
#
# Return the **lexicographically smallest** resulting string after all '*' characters are removed.
#
# Example 1:
#   Input : s = "aaba*"
#   Output: "aab"
#   Explanation: Remove '*' and one of the 'a' characters (choose the one that gives smallest result).
#
# Example 2:
#   Input : s = "abc"
#   Output: "abc"
#   Explanation: No '*' to process, return original.
#
# Constraints:
# - 1 ≤ |s| ≤ 10^5
# - s contains lowercase English letters and '*'
# - It's guaranteed that it’s possible to delete all '*' characters.

import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        """
        Strategy:
        - Use a min-heap to track all characters and their positions.
        - When a '*' is found, pop the smallest character from the heap and mark its index as deleted.
        - Finally, build a result string with all characters that aren't deleted or '*'.
        """
        heap = []              # Min-heap to store (char, -index)
        deleted = set()        # Track indices to be deleted

        for i, c in enumerate(s):
            if c == '*':
                ch, neg_idx = heapq.heappop(heap)  # Get smallest char (earliest due to -index)
                deleted.add(-neg_idx)              # Mark that index for deletion
            else:
                heapq.heappush(heap, (c, -i))       # Push char with -index to break ties by leftmost

        # Construct result excluding deleted characters and '*'
        res = []
        for i, c in enumerate(s):
            if i in deleted or c == '*':
                continue
            res.append(c)

        return ''.join(res)
