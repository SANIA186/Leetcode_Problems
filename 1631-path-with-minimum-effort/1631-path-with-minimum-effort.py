import heapq

class Solution:
    def minimumEffortPath(self, heights):

        rows = len(heights)
        cols = len(heights[0])

        # effort[r][c] = minimum effort needed to reach (r, c)
        effort = [[float('inf')] * cols for _ in range(rows)]

        # Starting cell has effort 0
        effort[0][0] = 0

        # Min heap: (effort, row, col)
        heap = [(0, 0, 0)]

        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1)    # left
        ]

        while heap:

            current_effort, r, c = heapq.heappop(heap)

            # If we reached the destination
            if r == rows - 1 and c == cols - 1:
                return current_effort

            # Explore all 4 directions
            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:

                    # Difference between current and next cell
                    difference = abs(
                        heights[r][c] - heights[nr][nc]
                    )

                    # Effort of the new path
                    new_effort = max(
                        current_effort,
                        difference
                    )

                    # If this is a better path
                    if new_effort < effort[nr][nc]:

                        effort[nr][nc] = new_effort

                        heapq.heappush(
                            heap,
                            (new_effort, nr, nc)
                        )

        return 0