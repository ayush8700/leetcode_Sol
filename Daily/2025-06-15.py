# 1432. Max Difference You Can Get From Changing an Integer
# Medium
#
# Problem:
#   You are given an integer `num`.
#   You can perform a digit remapping operation twice (independently):
#       - Pick digit x (0 <= x <= 9)
#       - Pick digit y (0 <= y <= 9)
#       - Replace all occurrences of digit x in `num` with y
#
#   Let `a` be the result of one such remapping, and `b` another result (with possibly different x and y).
#   Neither `a` nor `b` can have leading zeros or be zero.
#
#   Return the maximum difference between `a` and `b`.
#
# Example 1:
#   Input : num = 555
#   Output: 888
#   Explanation:
#       - a = 999 (replace 5 → 9)
#       - b = 111 (replace 5 → 1)
#       - max diff = 999 - 111 = 888
#
# Example 2:
#   Input : num = 9
#   Output: 8
#   Explanation:
#       - a = 9 (no change)
#       - b = 1 (replace 9 → 1)
#
# Constraints:
#   • 1 <= num <= 10^8
#
# Approach:
#   1. Convert num to string for easier manipulation.
#   2. To **maximize**:
#       - Replace first digit that is not '9' with '9'.
#   3. To **minimize**:
#       - If the first digit is not '1', replace it with '1'.
#       - Else, search from the second digit for a digit not in {'0', '1'}, and replace it with '0'.
#   4. Return the difference between the max and min numbers.

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Step 1: Maximize the number by replacing the first non-'9' digit with '9'
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # all digits are already '9'

        # Step 2: Minimize the number
        if s[0] != '1':
            # Replace the first digit with '1' (ensure no leading zero)
            min_num = int(s.replace(s[0], '1'))
        else:
            # Try to replace a non-0/1 digit (not the first digit) with '0'
            for ch in s[1:]:
                if ch not in {'0', '1'}:
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num  # nothing to replace, all digits are 0 or 1

        return max_num - min_num
