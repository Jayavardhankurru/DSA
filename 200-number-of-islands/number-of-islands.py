class Solution:
    def dfs(self, r, c, directions, grid, vis):
        n = len(grid)
        m = len(grid[0])
        vis[r][c] = 1
        for drow, dcol in directions:
            nrow = r + drow
            ncol = c + dcol
            if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == "1":
                self.dfs(nrow, ncol, directions, grid, vis)


    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _  in range(n)]
        is_island = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j] == 0:
                    self.dfs(i, j, directions, grid, vis)
                    is_island += 1
        return is_island