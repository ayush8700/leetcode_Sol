# 3372. Maximize the Number of Target Nodes After Connecting Trees I
#
# Given:
# - Two undirected trees represented as edge lists: `edges1` for the first tree and `edges2` for the second.
# - An integer `k` indicating the max number of allowed edges between two nodes to consider one as target of the other.
#
# Definitions:
# - Node `u` is target to node `v` if the number of edges from `u` to `v` is ≤ `k`. A node is always target to itself.
# - We can add **one** extra edge between any node in the first tree and any node in the second tree.
#
# Task:
# - For each node `i` in the first tree, find the max number of nodes target to `i` after optimally adding one such edge.
# - Return a list `answer` where `answer[i]` corresponds to node `i` in the first tree.

class Solution(object):
    def buildList(self, edges):
        # Build adjacency list from edge list
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfs(self, adj, u, p, k):
        # Depth-limited DFS to count reachable nodes within distance k
        if k < 0:
            return 0
        cnt = 1  # Count this node
        for v in adj[u]:
            if v != p:
                cnt += self.dfs(adj, v, u, k - 1)
        return cnt

    def maxTargetNodes(self, edges1, edges2, k):
        adj1 = self.buildList(edges1)
        adj2 = self.buildList(edges2)

        # Precompute the best connection (max reachable nodes in tree2 within k-1 steps)
        maxiB = 0
        for i in range(len(adj2)):
            maxiB = max(maxiB, self.dfs(adj2, i, -1, k - 1))

        # For each node in tree1, compute reachable nodes in tree1 + best possible gain from tree2
        res = []
        for i in range(len(adj1)):
            res.append(self.dfs(adj1, i, -1, k) + maxiB)

        return res
