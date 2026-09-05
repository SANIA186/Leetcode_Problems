from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)

        # Reverse graph
        reverse = [[] for _ in range(n)]

        # Outdegree of each node
        outdegree = [0] * n

        for i in range(n):
            outdegree[i] = len(graph[i])

            for nei in graph[i]:
                reverse[nei].append(i)

        # Start with terminal nodes
        queue = deque()

        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)

        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True

            # Nodes that point to this safe node
            for prev in reverse[node]:
                outdegree[prev] -= 1

                if outdegree[prev] == 0:
                    queue.append(prev)

        # Return safe nodes in sorted order
        return [i for i in range(n) if safe[i]]