class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        

        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):

            # All queens are placed
            if row == n:
                result.append(1)
                return

            # Try every column in this row
            for col in range(n):

                # Check if column or diagonal is already occupied
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Undo / Backtrack
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return len(result)