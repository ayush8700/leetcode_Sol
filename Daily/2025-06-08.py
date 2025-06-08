# 386. Lexicographical Numbers
# Medium
#
# Problem:
# Given an integer `n`, return all the numbers in the range [1, n] **sorted in lexicographical order**.
#
# Constraints:
# - 1 <= n <= 5 * 10^4
# - You must write an algorithm that runs in O(n) time and uses O(1) extra space.
#
# Example 1:
#   Input : n = 13
#   Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
#
# Example 2:
#   Input : n = 2
#   Output: [1,2]

class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        """
        Strategy:
        - Use a DFS-like traversal (iterative).
        - At each step, try to go deeper by multiplying by 10.
        - If you can't go deeper (exceeds n), try to move to the next sibling by adding 1.
        - If not possible, backtrack by dividing by 10 until you can move forward.
        - This avoids using extra space (stack) and runs in O(n) time.
        """
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            if current * 10 <= n:
                # Dive deeper (e.g., 1 → 10)
                current *= 10
            else:
                # Go to the next sibling (e.g., 10 → 11), or backtrack
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                current += 1

        return result
