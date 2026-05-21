from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        rotten = deque()
        total = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        time = 0
        while rotten:
            k = len(rotten)
            count += k
            for _ in range(k):
                x, y = rotten.popleft()
                for drow, dcol in directions:
                    nrow = x  + drow
                    ncol = y + dcol
                    if (0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == 1):
                        grid[nrow][ncol] = 2
                        rotten.append((nrow, ncol))
            if rotten:
                time += 1
        return time if count == total else -1