class Solution:
    def dfs(self, r, c, board, vis, directions):
        n = len(board)
        m = len(board[0])
        vis[r][c] = 1
        for drow, dcol in directions:
            nrow = r + drow
            ncol = c + dcol
            if 0 <= nrow < n and 0 <= ncol < m and board[nrow][ncol] == 'O' and vis[nrow][ncol] == 0:
                self.dfs(nrow, ncol, board, vis, directions)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        if n == 0 or m == 0:
            return board
        vis = [[0] * m for _ in range(n)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for j in range(m):
            if board[0][j] == 'O' and vis[0][j] == 0:
                self.dfs(0, j, board, vis, directions)
            if board[n - 1][j] == 'O' and vis[n - 1][j] == 0:
                self.dfs(n - 1, j, board, vis, directions)
        for i in range(n):
            if board[i][0] == 'O' and vis[i][0] == 0:
                self.dfs(i, 0, board, vis, directions)
            if board[i][m - 1] == 'O' and vis[i][m - 1] == 0:
                self.dfs(i, m - 1, board, vis, directions)
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
        return board