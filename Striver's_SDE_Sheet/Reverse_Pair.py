# 493. Reverse Pairs
#
# Given:
# - An integer array `nums`.
#
# Task:
# - Return the number of reverse pairs in the array.
# - A reverse pair is defined as a pair (i, j) where:
#     0 <= i < j < len(nums) and nums[i] > 2 * nums[j]
#
# Constraints:
# - 1 <= nums.length <= 5 * 10^4
# - -2^31 <= nums[i] <= 2^31 - 1
#
# Examples:
# - Input: [1,3,2,3,1] -> Output: 2 (Pairs: (1,4), (3,4))
# - Input: [2,4,3,5,1] -> Output: 3 (Pairs: (1,4), (2,4), (3,4))

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start, end):
            # Base case: if the array has one or no element, no reverse pair
            if start >= end:
                return 0

            mid = (start + end) // 2

            # Count reverse pairs in left and right halves
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)

            # Count the important reverse pairs that span across the halves
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge the two halves in sorted order
            temp = []
            left, right = start, mid + 1
            while left <= mid and right <= end:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= end:
                temp.append(nums[right])
                right += 1

            # Copy the sorted values back into the original array
            for i in range(len(temp)):
                nums[start + i] = temp[i]

            return count

        return merge_sort(0, len(nums) - 1)
