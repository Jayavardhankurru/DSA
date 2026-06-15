class Solution:
    def solve(self, col, ans, board, n, leftrow, lowerDiagnol, upperDiagnol):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
        for row in range(n):
            if leftrow[row] == 0 and lowerDiagnol[row + col] == 0 and upperDiagnol[n - 1 + col  - row] == 0:
                board[row][col] = 'Q'
                leftrow[row] = lowerDiagnol[row + col] = upperDiagnol[n - 1 + col - row] = 1
                self.solve(col + 1, ans, board, n, leftrow, lowerDiagnol, upperDiagnol)
                board[row][col] = '.'
                leftrow[row] = lowerDiagnol[row + col] = upperDiagnol[n - 1 + col - row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        leftrow = [0] * n
        lowerDiagnol = [0] * (2 * n - 1)
        upperDiagnol = [0] * (2 * n - 1)
        self.solve(0, ans, board, n, leftrow, lowerDiagnol, upperDiagnol)
        return ans