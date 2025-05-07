# 3341. Find Minimum Time to Reach Last Room I
# You are given an n x m dungeon grid. Each cell moveTime[i][j] represents the 
# minimum time when you can move into that room (i, j).
#
# You start at (0, 0) at time t = 0. You can move to adjacent cells (up, down, left, right),
# and each move takes exactly 1 second.
#
# Your goal is to reach the bottom-right cell (n-1, m-1) in minimum time.
#
# Return the minimum time to reach (n-1, m-1).
#
# Example 1:
# Input: moveTime = [[0,4],[4,4]]
# Output: 6
#
# Example 2:
# Input: moveTime = [[0,0,0],[0,0,0]]
# Output: 3
#
# Example 3:
# Input: moveTime = [[0,1],[1,2]]
# Output: 3
#
# Constraints:
# - 2 <= n, m <= 50
# - 0 <= moveTime[i][j] <= 10^9

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        # minTime[i][j] stores the minimum time to reach cell (i, j)
        minTime = [[float('inf')] * m for _ in range(n)]
        minTime[0][0] = 0  # start at (0, 0) at time 0

        # Min-heap priority queue: (time, x, y)
        heap = [(0, 0, 0)]

        # 4 directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, x, y = heapq.heappop(heap)

            # If we've reached the goal, return the time
            if (x, y) == (n - 1, m - 1):
                return time

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check bounds
                if 0 <= nx < n and 0 <= ny < m:
                    # You can only enter moveTime[nx][ny] at or after moveTime[nx][ny]
                    # We must wait if arriving too early
                    arrive_time = max(time + 1, moveTime[nx][ny] + 1)

                    if arrive_time < minTime[nx][ny]:
                        minTime[nx][ny] = arrive_time
                        heapq.heappush(heap, (arrive_time, nx, ny))

        # If unreachable (shouldn't happen as per problem description)
        return -1
