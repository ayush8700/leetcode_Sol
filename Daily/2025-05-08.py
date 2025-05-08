# 3342. Find Minimum Time to Reach Last Room II
#
# You are given a grid moveTime[n][m] where moveTime[i][j] is the earliest time
# you can enter cell (i, j).
#
# You start at (0, 0) at time 0. You can move to any adjacent cell, but:
# - The first move takes 1 second
# - The second move takes 2 seconds
# - The third takes 1 second again, and so on (alternating 1 and 2 seconds)
#
# Return the **minimum time** to reach the bottom-right cell (n-1, m-1).
#
# Example 1:
# Input: moveTime = [[0,4],[4,4]]
# Output: 7
#
# Example 2:
# Input: moveTime = [[0,0,0,0],[0,0,0,0]]
# Output: 6
#
# Example 3:
# Input: moveTime = [[0,1],[1,2]]
# Output: 4
#
# Constraints:
# 2 <= n, m <= 750
# 0 <= moveTime[i][j] <= 10^9

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        # Min-heap priority queue: (current_time, x, y, next_step_cost)
        # next_step_cost alternates between 1 and 2
        heap = [(0, 0, 0, 1)]  # start at (0,0), time 0, next step will cost 1
        heapq.heapify(heap)

        # Use a set to track visited (x, y) positions
        visited = set((0, 0))

        # Directions: up, down, left, right
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while heap:
            curr_time, x, y, step_cost = heapq.heappop(heap)

            # If we've reached the goal, return the time
            if (x, y) == (n - 1, m - 1):
                return curr_time

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check grid boundaries and if we've visited this cell before
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    # Time to enter the next cell must be at least moveTime[nx][ny]
                    next_time = max(curr_time, moveTime[nx][ny]) + step_cost
                    heapq.heappush(heap, (next_time, nx, ny, 3 - step_cost))  # flip step cost 1 <-> 2
                    visited.add((nx, ny))

        # If destination is unreachable (shouldn't happen as per problem constraints)
        return -1
