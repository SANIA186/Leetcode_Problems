import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        # Min heap: (time, row, col)
        minHeap = [(grid[0][0], 0, 0)]

        visited = set()

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Reached bottom-right
            if r == n - 1 and c == n - 1:
                return time

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    newTime = max(time, grid[nr][nc])

                    heapq.heappush(minHeap, (newTime, nr, nc))