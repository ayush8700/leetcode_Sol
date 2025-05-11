# 1550. Three Consecutive Odds
#
# Given an integer array `arr`, return True if there are three **consecutive odd numbers** in it.
# Otherwise, return False.
#
# Example 1:
# Input: arr = [2,6,4,1]
# Output: False
#
# Example 2:
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: True (5, 7, 23 are consecutive odd numbers)
#
# Constraints:
# - 1 <= arr.length <= 1000
# - 1 <= arr[i] <= 1000

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        N = len(arr)
        for i in range(1,N-1):
            if arr[i-1] %2 != 0 and arr[i] %2 != 0 and arr[i+1] %2 != 0:
                return True
        return False        
