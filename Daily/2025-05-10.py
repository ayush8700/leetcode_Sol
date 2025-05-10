# 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
#
# You are given two arrays nums1 and nums2 consisting of positive integers and zeros.
# Replace all 0's in both arrays with strictly positive integers such that:
# - The total sums of both arrays become equal.
# - Return the *minimum equal sum* possible after replacement.
# - If it's impossible, return -1.
#
# Example 1:
# Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
# Output: 12
#
# Example 2:
# Input: nums1 = [2,0,2,0], nums2 = [1,4]
# Output: -1
#
# Constraints:
# - 1 <= len(nums1), len(nums2) <= 1e5
# - 0 <= nums[i] <= 1e6

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        zeroes1 = nums1.count(0)
        sum2 = sum(nums2)
        zeroes2 = nums2.count(0)

        if zeroes1 == zeroes2 == 0:
            return sum1 if sum1 == sum2 else -1
        
        elif zeroes1 == 0 and zeroes2 >0:
            if sum1 < sum2 or sum1 - sum2 < zeroes2 :
                return -1
            else:
                return sum1
        elif zeroes2 == 0 and zeroes1 >0:
            if sum2 < sum1 or sum2 - sum1 < zeroes1 :
                return -1
            else:
                return sum2
        return max(sum1 +zeroes1 , sum2 + zeroes2)
