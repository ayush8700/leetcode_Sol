# 2566. Maximum Difference by Remapping a Digit
# Easy
#
# Problem:
#   Given an integer `num`, Bob can remap one digit (0-9) to another digit,
#   replacing **all occurrences** of that digit in the number.
#   He may do this **once** for max and once for min (remap may differ).
#
#   Return the **difference** between the maximum and minimum values
#   that can be created by **exactly one remap each**.
#
#   - Leading zeros **are allowed** in intermediate values.
#
# Example 1:
#   Input : num = 11891
#   Output: 99009
#   Explanation:
#       • Max: replace '1' → '9' → 99899
#       • Min: replace '1' → '0' → 890
#       • Difference: 99899 - 890 = 99009
#
# Example 2:
#   Input : num = 90
#   Output: 99
#   Explanation:
#       • Max: replace '0' → '9' → 99
#       • Min: replace '9' → '0' → 0
#
# Constraints:
#   • 1 <= num <= 10^8
#
# Approach:
#   1. Convert the number to a string.
#   2. For maximum value:
#       - Replace the **first non-9 digit** with '9' throughout.
#   3. For minimum value:
#       - Replace the **first non-0 digit** with '0' throughout.
#   4. Return max - min.

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Step 1: Maximize - replace first non-9 digit with 9
        max_s = s
        for ch in s:
            if ch != '9':
                max_s = s.replace(ch, '9')
                break

        # Step 2: Minimize - replace first non-0 digit with 0
        min_s = s
        for ch in s:
            if ch != '0':
                min_s = s.replace(ch, '0')
                break

        # Return the difference
        return int(max_s) - int(min_s)
