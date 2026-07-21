from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.solve()

    def solve(self) -> bool:
        # 1. Find the empty cell with the fewest possibilities
        best_row = best_col = -1
        best_candidates = None   # list of digits that can be placed

        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.':
                    cand = self.get_candidates(r, c)
                    if best_candidates is None or len(cand) < len(best_candidates):
                        best_row, best_col = r, c
                        best_candidates = cand
                        # If we find a cell with only 1 candidate, we can place it immediately
                        if len(cand) == 1:
                            # We'll still let the loop finish, but we can break out
                            # Actually we can break out early for speed
                            pass

        # If no empty cell found, board is solved
        if best_row == -1:
            return True

        # 2. Try each candidate for that cell
        for d in best_candidates:
            self.board[best_row][best_col] = d
            if self.solve():
                return True
            self.board[best_row][best_col] = '.'

        return False

    def get_candidates(self, row: int, col: int) -> List[str]:
        """Return a list of digits that can be placed at (row, col)."""
        used = set()
        # Check row
        for j in range(9):
            if self.board[row][j] != '.':
                used.add(self.board[row][j])
        # Check column
        for i in range(9):
            if self.board[i][col] != '.':
                used.add(self.board[i][col])
        # Check 3x3 sub-box
        srow, scol = (row // 3) * 3, (col // 3) * 3
        for i in range(srow, srow + 3):
            for j in range(scol, scol + 3):
                if self.board[i][j] != '.':
                    used.add(self.board[i][j])
        # Return digits not used
        return [d for d in "123456789" if d not in used]