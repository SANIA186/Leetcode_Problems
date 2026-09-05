import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]

        # Build graph
        for u, v, w in times:
            graph[u].append((v, w))

        # (time, node)
        pq = [(0, k)]

        # Shortest known distance to each node
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while pq:
            time, node = heapq.heappop(pq)

            # Ignore outdated entry
            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        # Check if every node was reached
        max_time = max(dist[1:])

        if max_time == float('inf'):
            return -1

        return max_time