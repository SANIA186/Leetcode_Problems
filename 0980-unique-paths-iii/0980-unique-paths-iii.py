class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
       
        rows = len(grid)
        cols = len(grid[0])

        # Find start position and count empty cells
        empty = 0
        start_r = 0
        start_c = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    start_r = r
                    start_c = c

        def backtrack(r, c, remaining):
            # Out of bounds or obstacle/already visited
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == -1:
                return 0

            # Reached the ending cell
            if grid[r][c] == 2:
                if remaining == 0:
                    return 1
                return 0

            # Mark current cell as visited
            grid[r][c] = -1

            paths = 0

            # Move up
            paths += backtrack(r - 1, c, remaining - 1)

            # Move down
            paths += backtrack(r + 1, c, remaining - 1)

            # Move left
            paths += backtrack(r, c - 1, remaining - 1)

            # Move right
            paths += backtrack(r, c + 1, remaining - 1)

            # Undo the visit (backtracking)
            grid[r][c] = 0

            return paths

        return backtrack(start_r, start_c, empty + 1)
