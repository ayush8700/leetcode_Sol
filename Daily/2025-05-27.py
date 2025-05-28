# 2894. Divisible and Non-divisible Sums Difference
#
# Given:
# - Two positive integers `n` and `m`.
#
# Task:
# - Calculate:
#   - num1: The sum of all integers in the range [1, n] not divisible by m.
#   - num2: The sum of all integers in the range [1, n] divisible by m.
# - Return the result of num1 - num2.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        output = 0

        # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):
            if i % m == 0:
                output -= i  # Subtract if divisible by m (contributes to num2)
            else:
                output += i  # Add if not divisible by m (contributes to num1)

        return output
