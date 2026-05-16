# ============================================================
# Valid Sudoku
# Category : Arrays & Hashing & Matrices
# Difficulty: Medium
# NeetCode : https://neetcode.io/problems/valid-sudoku
# ============================================================
# Runtime : 28 ms   | Beats 100.00%
# Memory  : 7.9 MB  | Beats 56.75%
# Submitted: 2026-05-15
# ============================================================
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) # collections is a module; rows contains 9 sets, 1 set per row
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                   return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True
        
