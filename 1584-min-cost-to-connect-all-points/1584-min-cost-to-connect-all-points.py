class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        visited = [False] * n
        distance = [float('inf')] * n

        distance[0] = 0
        total = 0

        for _ in range(n):

            # Find the unvisited point with minimum distance
            cur = -1

            for i in range(n):
                if not visited[i]:
                    if cur == -1 or distance[i] < distance[cur]:
                        cur = i

            # Add this point to MST
            visited[cur] = True
            total += distance[cur]

            # Update distances of remaining points
            for i in range(n):
                if not visited[i]:

                    x1, y1 = points[cur]
                    x2, y2 = points[i]

                    cost = abs(x1 - x2) + abs(y1 - y2)

                    if cost < distance[i]:
                        distance[i] = cost

        return total