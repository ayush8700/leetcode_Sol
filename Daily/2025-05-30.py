# 2359. Find Closest Node to Given Two Nodes
# Medium

# You are given a directed graph of n nodes numbered from 0 to n - 1,
# where each node has at most one outgoing edge.
#
# The graph is represented with a given 0-indexed array 'edges' of size n,
# where edges[i] indicates a directed edge from node i to edges[i].
# If edges[i] == -1, then node i has no outgoing edge.
#
# You are also given two nodes: node1 and node2.
#
# Return the index of the node that can be reached from **both** node1 and node2,
# such that the **maximum** of the distances from node1 and node2 to that node is minimized.
#
# If there are multiple such nodes, return the one with the **smallest index**.
# If no such node exists, return -1.

# Example 1:
# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2

# Example 2:
# Input: edges = [1,2,-1], node1 = 0, node2 = 2
# Output: 2

# Constraints:
# - n == edges.length
# - 2 <= n <= 10^5
# - -1 <= edges[i] < n
# - edges[i] != i
# - 0 <= node1, node2 < n

class Solution(object):
    
    # Helper function to compute distances using DFS-like traversal
    def dfs(self, current, distance, edges, distances):
        # Traverse the path starting from current node
        while current != -1 and distances[current] == -1:
            distances[current] = distance  # Store the distance from the start node
            distance += 1
            current = edges[current]  # Move to the next node

    def closestMeetingNode(self, edges, start1, start2):
        n = len(edges)
        dist1 = [-1] * n  # Distance from node1 to each node
        dist2 = [-1] * n  # Distance from node2 to each node

        # Fill in distances from start1 and start2
        self.dfs(start1, 0, edges, dist1)
        self.dfs(start2, 0, edges, dist2)

        res = -1  # Result node
        Min_Of_Max = float('inf')  # To track the minimum of max distances

        # Iterate over all nodes to find the optimal meeting node
        for i in range(n):
            if dist1[i] >= 0 and dist2[i] >= 0:  # Reachable from both node1 and node2
                maxDist = max(dist1[i], dist2[i])
                if maxDist < Min_Of_Max:
                    Min_Of_Max = maxDist
                    res = i  # Update result to current node
        return res
