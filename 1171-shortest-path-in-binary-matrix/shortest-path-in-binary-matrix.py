class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        visited = [[0] * n for _ in range(n)]
        q  = deque([(0, 0, 1)])
        visited[0][0] = 1
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        while q:
            row, col, steps = q.popleft()
            if row == n - 1 and col == n - 1:
                return steps
            for drow, dcol in directions:
                nrow = row + drow
                ncol = col + dcol
                if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol] and grid[nrow][ncol] == 0:
                    visited[nrow][ncol] = 1
                    q.append((nrow, ncol, steps + 1))
        return -1