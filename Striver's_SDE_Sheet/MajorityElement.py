# 169. Majority Element
#
# Given:
# - An array `nums` of size `n`.
#
# Task:
# - Return the majority element.
# - The majority element is the element that appears more than ⌊n / 2⌋ times.
# - You may assume the majority element always exists in the array.
#
# Follow-up:
# - Can you solve it in linear time and O(1) space?

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        return nums[N // 2]




class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
