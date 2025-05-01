# 2071. Maximum Number of Tasks You Can Assign
# Hard

# You have `n` tasks and `m` workers. Each task has a strength requirement stored in an array `tasks`,
# where tasks[i] is the strength needed for the ith task.
# Each worker has their strength in the `workers` array. A worker j can do task i if workers[j] >= tasks[i].

# You also have a limited number of magical pills.
# Each pill increases a worker's strength by `strength`.
# Each worker can take at most one pill.

# Goal: Return the **maximum number of tasks** that can be completed by assigning each task to a worker,
# possibly using pills to boost strength.

# --- Example 1:
# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# - Give a pill to worker 0: 0 + 1 >= 1 → assign to task 2
# - Worker 1 does task 1: 3 >= 2
# - Worker 2 does task 0: 3 >= 3

# --- Example 2:
# Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# Output: 1
# Explanation:
# - Only one worker can do task 0 using a pill

# --- Example 3:
# Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# Output: 2
# Explanation:
# - Pill to worker 0 → does task 0 (0+10)
# - Pill to worker 1 → does task 1 (10+10)
# - No one can do task 2

# --- Constraints:
# n == tasks.length
# m == workers.length
# 1 <= n, m <= 5 * 10^4
# 0 <= pills <= m
# 0 <= tasks[i], workers[j], strength <= 10^9

import bisect

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))

        while left < right:
            mid = (left + right + 1) // 2
            usedPills = 0
            avail = workers[-mid:]  # pick the strongest mid workers
            canAssign = True

            for t in reversed(tasks[:mid]):  # hardest mid tasks
                if avail[-1] >= t:
                    # Assign task without pill
                    avail.pop()
                else:
                    # Try assigning with a pill
                    idx = bisect.bisect_left(avail, t - strength)
                    if idx == len(avail) or usedPills == pills:
                        canAssign = False
                        break
                    usedPills += 1
                    avail.pop(idx)

            if canAssign:
                left = mid
            else:
                right = mid - 1

        return left
