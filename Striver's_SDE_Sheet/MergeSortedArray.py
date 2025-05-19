# 88. Merge Sorted Array
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# - nums1 has a size of m + n, where the first m elements are the elements to be merged,
#   and the last n elements are set to 0 (placeholders for nums2).
# - nums2 has exactly n elements.
# - Modify nums1 in-place to be the final sorted array.
#
# Constraints:
# - nums1.length == m + n
# - nums2.length == n
# - 0 <= m, n <= 200
# - -10^9 <= nums1[i], nums2[i] <= 10^9


# FIRST SOLUTION

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place, resulting in a single sorted array.
        """
        # Step 1: Copy elements of nums2 into the tail of nums1
        for i in range(n):
            nums1[m + i] = nums2[i]
        
        # Step 2: Sort the entire nums1 array
        nums1.sort()


# SECOND SOLUTION

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        # Start merging from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Copy any remaining elements from nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
