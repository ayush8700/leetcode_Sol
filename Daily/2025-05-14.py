# 3337. Total Characters in String After Transformations II
#
# You are given:
# - A string `s` consisting of lowercase letters
# - An integer `t` representing the number of transformations
# - An array `nums` of size 26, where nums[i] determines how many next characters
#   each character transforms into (with alphabet wrap-around)
#
# In one transformation:
# - Each character `ch` becomes the next `nums[ord(ch) - ord('a')]` characters
#   in the alphabet, wrapping around after 'z'
#
# Return the length of the string after `t` transformations, modulo 10^9 + 7.
#
# Example:
# Input: s = "abcyy", t = 2, nums = [1,...,1,2]  # only nums[25] = 2 for 'z'
# Output: 7
#
# Explanation:
#   After t=1: "a"→"b", "b"→"c", ..., "y"→"z" → string: "bcdzz"
#   After t=2: "b"→"c", ..., "z"→"ab" → string: "cdeabab" (length = 7)

from typing import List

MOD = 10**9 + 7
L = 26  # number of lowercase English letters

# Matrix representation of character transitions
class Mat:
    def __init__(self, copy_from: "Mat" = None) -> None:
        self.a = [[0] * L for _ in range(L)]
        if copy_from:
            for i in range(L):
                for j in range(L):
                    self.a[i][j] = copy_from.a[i][j]

    def __mul__(self, other: "Mat") -> "Mat":
        result = Mat()
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    result.a[i][j] = (result.a[i][j] + self.a[i][k] * other.a[k][j]) % MOD
        return result

# Create an identity matrix
def identity_matrix() -> Mat:
    m = Mat()
    for i in range(L):
        m.a[i][i] = 1
    return m

# Fast exponentiation of matrices using binary exponentiation
def matrix_power(matrix: Mat, exponent: int) -> Mat:
    result = identity_matrix()
    base = matrix
    while exponent:
        if exponent % 2:
            result = result * base
        base = base * base
        exponent //= 2
    return result

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Build the transformation matrix T
        T = Mat()
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T.a[(i + j) % 26][i] = 1  # character i maps to (i+1)%26, ..., (i+nums[i])%26

        # Compute T^t using matrix exponentiation
        T_powered = matrix_power(T, t)

        # Count initial frequencies of each character in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Compute final total length after all transformations
        total = 0
        for i in range(26):
            for j in range(26):
                total = (total + T_powered.a[i][j] * freq[j]) % MOD

        return total
