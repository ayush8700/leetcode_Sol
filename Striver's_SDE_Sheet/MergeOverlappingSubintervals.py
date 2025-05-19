# 56. Merge Intervals
#
# Given a list of intervals where each interval is a pair [start, end],
# merge all overlapping intervals and return the resulting list of non-overlapping intervals.
#
# Two intervals [a, b] and [c, d] overlap if c <= b.
#
# Constraints:
# - 1 <= intervals.length <= 10^4
# - intervals[i].length == 2
# - 0 <= start <= end <= 10^4

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        res = []  # This will hold the merged intervals

        # Step 2: Iterate through the sorted intervals
        for interval in intervals:
            # If res is empty OR current interval does not overlap with the last in res
            if not res or res[-1][1] < interval[0]:
                res.append(interval)  # Add current interval as-is
            else:
                # There is overlap: merge the current interval with the last one in res
                res[-1][1] = max(res[-1][1], interval[1])

        return res
