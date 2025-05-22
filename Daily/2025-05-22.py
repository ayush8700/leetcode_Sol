# 3362. Zero Array Transformation III
#
# You are given:
# - An integer array `nums` of length `n`
# - A list of `queries[i] = [li, ri]` indicating that:
#     - You can decrement **each index** in range `[li, ri]` by **at most 1**
#     - The decrement amount can be chosen independently per index per query
#
# Goal:
# - Return the **maximum number of queries you can remove**
#   such that `nums` can still be converted to a Zero Array.
# - If it’s impossible to make all elements 0 even with all queries, return -1.
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - 0 <= nums[i] <= 10^5
# - 1 <= queries.length <= 10^5
# - 0 <= li <= ri < nums.length

from typing import List
import collections
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Step 1: Sort queries by left boundary (li)
        queries.sort(key=lambda x: x[0])
        q = collections.deque(queries)

        # Priority queues (heaps)
        available = []   # Max-heap for right boundaries of usable queries
        active = []      # Min-heap for queries currently used at index

        used_queries = 0
        n = len(nums)

        # Step 2: Process each index in nums
        for i in range(n):
            # Push all queries starting at or before index `i` into available heap
            while q and q[0][0] <= i:
                li, ri = q.popleft()
                heapq.heappush(available, -ri)  # Use max-heap via negative values

            # Remove queries from active heap that no longer cover current index
            while active and active[0] < i:
                heapq.heappop(active)

            # Need at least nums[i] queries to decrement index i to zero
            while len(active) < nums[i]:
                if not available:
                    return -1  # Not enough queries to meet requirement

                r = -heapq.heappop(available)
                if r < i:
                    continue  # This query can't help anymore

                heapq.heappush(active, r)
                used_queries += 1

        # Step 3: Return how many queries we can remove
        return len(queries) - used_queries
