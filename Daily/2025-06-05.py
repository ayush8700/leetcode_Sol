# 1061. Lexicographically Smallest Equivalent String
# Medium

# Problem:
# You are given two strings `s1` and `s2` of the same length, and a string `baseStr`.
# Each pair of characters `s1[i]` and `s2[i]` is considered equivalent.
# Equivalent characters follow equivalence relation rules:
# - Reflexivity: 'a' == 'a'
# - Symmetry: 'a' == 'b' implies 'b' == 'a'
# - Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'

# Goal:
# Return the **lexicographically smallest equivalent string** of `baseStr`
# by transforming each character to its smallest equivalent using the equivalence info.

# Example 1:
# Input:
#   s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# Explanation:
#   Equivalence groups:
#     - [m,p]
#     - [a,o]
#     - [k,r,s]
#     - [e,i]
#   "parser" becomes "makkek" using the smallest equivalent characters

# Example 2:
# Input:
#   s1 = "hello", s2 = "world", baseStr = "hold"
# Output: "hdld"

# Example 3:
# Input:
#   s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
# Output: "aauaaaaada"

# Constraints:
# - 1 <= s1.length == s2.length <= 1000
# - 1 <= baseStr.length <= 1000
# - s1, s2, baseStr contain only lowercase English letters

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Step 1: Union-Find setup for characters 'a' to 'z'
        parent = list(range(26))  # each index represents a character from 'a' to 'z'

        # Step 2: Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Step 3: Union by lexicographically smaller character
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Step 4: Build equivalence classes from s1 and s2
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Step 5: Transform baseStr using smallest equivalent character
        result = []
        for ch in baseStr:
            smallest = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest)

        return ''.join(result)
