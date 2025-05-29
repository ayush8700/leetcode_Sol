# 3373. Maximize the Number of Target Nodes After Connecting Trees II
#
# Given:
# - Two undirected trees represented as edge lists: `edges1` and `edges2`.
# - Node labels are unique within each tree: [0, n - 1] and [0, m - 1].
#
# Definitions:
# - A node `u` is target to node `v` if the number of edges on the path from `u` to `v` is even.
# - A node is always target to itself (0 edges).
#
# Task:
# - You can add one edge between a node from the first tree and a node from the second tree.
# - For each node `i` in the first tree, compute the maximum number of nodes that can be target to it
#   after optimally adding this edge.
# - Return an array `answer` where `answer[i]` is the maximum number of target nodes for node `i`.
#
# Note:
# - Queries are independent; the added edge is removed after each query.

from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(node, parent, depth, children, color):
            # Assign 0 or 1 based on even/odd depth and count nodes with even distance
            res = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                if child != parent:
                    res += dfs(child, node, depth + 1, children, color)
            return res

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            even_count = dfs(0, -1, 0, children, color)
            odd_count = n - even_count
            return [even_count, odd_count]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m

        count1 = build(edges1, color1)  # [even1, odd1]
        count2 = build(edges2, color2)  # [even2, odd2]

        res = [0] * n
        for i in range(n):
            # Connecting a node of color c to opposite parity in other tree
            # ensures the most even distances possible.
            res[i] = count1[color1[i]] + max(count2[0], count2[1])
        return res
