# 3024. Type of Triangle
#
# You are given a 0-indexed integer array `nums` of size 3.
# Each value represents the length of one side of a potential triangle.
#
# Triangle classification rules:
# - "equilateral": All three sides are equal.
# - "isosceles": Exactly two sides are equal.
# - "scalene": All three sides are different.
# - "none": The given lengths cannot form a valid triangle.
#
# A valid triangle satisfies the triangle inequality theorem:
# Sum of any two sides must be greater than the third.
#
# Constraints:
# - nums.length == 3
# - 1 <= nums[i] <= 100

from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Sort the sides to make it easier to apply the triangle inequality
        nums.sort()

        # Check triangle inequality: sum of smaller two sides > the largest side
        if nums[0] + nums[1] > nums[2]:
            # All sides equal -> equilateral triangle
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"
            # Exactly two sides equal -> isosceles triangle
            elif nums[0] == nums[1] or nums[1] == nums[2]:
                return "isosceles"
            # All sides different -> scalene triangle
            else:
                return "scalene"
        else:
            # Fails triangle inequality -> not a triangle
            return "none"
