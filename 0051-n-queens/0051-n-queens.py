from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for _ in range(n)]

        # Sets to track used columns and diagonals
        cols = set()
        diag1 = set()   # r - c (constant for top-left to bottom-right)
        diag2 = set()   # r + c (constant for top-right to bottom-left)

        def backtrack(r: int):
            if r == n:
                # Convert board to list of strings and add to result
                result.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # Place queen
                board[r][c] = 'Q'
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                backtrack(r + 1)

                # Backtrack
                board[r][c] = '.'
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return result