# 1128. Number of Equivalent Domino Pairs
# Given a list of dominoes, return the number of pairs (i, j)
# such that 0 <= i < j < len(dominoes) and dominoes[i] is equivalent to dominoes[j].
#
# Two dominoes [a, b] and [c, d] are considered equivalent if:
# - (a == c and b == d) or (a == d and b == c)
# In other words, dominoes can be flipped.
#
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Explanation: [1,2] and [2,1] are equivalent.
#
# Example 2:
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
# Explanation:
# The three equivalent pairs are:
# - (0,1), (0,3), and (1,3)
#
# Constraints:
# 1 <= dominoes.length <= 4 * 10^4
# 1 <= dominoes[i][j] <= 9

from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)  # Dictionary to count how many times a normalized domino has appeared
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # Sort to handle flip equivalence, e.g., (1,2) == (2,1)
            result += count[key]         # For each prior match, add number of new valid pairs
            count[key] += 1              # Update count for the current domino

        return result
