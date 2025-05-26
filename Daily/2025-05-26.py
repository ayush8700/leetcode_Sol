# 1857. Largest Color Value in a Directed Graph
#
# Given:
# - A string `colors`, where colors[i] represents the color of node i (a lowercase letter).
# - A list of directed edges `edges`, where each edge is [u, v] (u → v).
#
# Task:
# - Find the maximum number of the same-colored nodes on any valid path.
# - If the graph has a cycle, return -1.

from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)

        # Build the graph
        for u, v in edges:
            graph[u].append(v)

        # Track visited status: 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * n
        # Count[i][c] = max count of color `c` on any path ending at node `i`
        count = [[0] * 26 for _ in range(n)]

        def dfs(node: int) -> int:
            if visited[node] == 1:
                return float('inf')  # Found a cycle
            if visited[node] == 2:
                return max(count[node])

            visited[node] = 1  # Mark as visiting

            for neighbor in graph[node]:
                result = dfs(neighbor)
                if result == float('inf'):
                    return float('inf')  # Propagate cycle detection
                # Update count of colors from child node
                for c in range(26):
                    count[node][c] = max(count[node][c], count[neighbor][c])

            # Include this node's own color
            color_index = ord(colors[node]) - ord('a')
            count[node][color_index] += 1

            visited[node] = 2  # Mark as fully processed
            return max(count[node])

        max_color_value = 0
        for node in range(n):
            result = dfs(node)
            if result == float('inf'):
                return -1  # Cycle detected
            max_color_value = max(max_color_value, result)

        return max_color_value
