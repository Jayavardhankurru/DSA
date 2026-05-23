from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for i in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or  j == m -  1:
                    if grid[i][j] == 1 and vis[i][j] == 0:
                        vis[i][j] = 1
                        q.append((i, j))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            r, c = q.popleft()
            for drow, dcol in directions:
                nrow = r + drow
                ncol = c + dcol
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and vis[nrow][ncol] == 0:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol))
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    cnt += 1
        return cnt