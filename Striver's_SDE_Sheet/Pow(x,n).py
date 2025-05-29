# 50. Pow(x, n)
# Medium

# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/(2^2) = 1/4 = 0.25

# Constraints:
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31 - 1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= x^n <= 10^4

class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Helper function to calculate power recursively using exponentiation by squaring
        def calc_power(x, n):
            # Edge case: any number raised to 0 is 1
            if n == 0:
                return 1
            # Edge case: 0 raised to any positive number is 0
            if x == 0:
                return 0

            # Recursively compute x^(n//2)
            res = calc_power(x, n // 2)
            res = res * res  # square the result to simulate exponentiation

            # If n is odd, multiply once more by x
            if n % 2 == 1:
                return res * x

            # Return result for even n
            return res

        # Use the helper to compute power using absolute value of n
        ans = calc_power(x, abs(n))

        # If n is non-negative, return the result
        if n >= 0:
            return ans
        
        # If n is negative, return the reciprocal
        return 1 / ans
