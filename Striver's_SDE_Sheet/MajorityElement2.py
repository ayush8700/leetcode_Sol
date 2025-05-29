
# Leetcode 229: Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Constraints:
# - 1 <= nums.length <= 5 * 10^4
# - -10^9 <= nums[i] <= 10^9
# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Approach 1: Dictionary Counting (O(n) time, O(n) space)
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        mini = N // 3         # Elements must appear more than N/3 times
        res = []              # Result list
        myDict = {}           # Frequency map

        for num in nums:
            myDict[num] = myDict.get(num, 0) + 1  # Count frequency

        for key, value in myDict.items():
            if value > mini:
                res.append(key)                  # Include if count > N//3

        return res


# Approach 2: Boyer-Moore Voting Algorithm (O(n) time, O(1) space)
# Used to find up to two elements that appear more than n/3 times
class OptimizedSolution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        count1 = count2 = 0
        candidate1 = candidate2 = None

        # First pass: Find potential candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Second pass: Verify the candidates
        res = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                res.append(candidate)

        return res
