class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        return self.countPaths(m - 1, n - 1, dp)

    def countPaths(self, m, n, dp):
        if m == 0 or n == 0:
            return 1
        if dp[m][n] != 0:
            return dp[m][n]
        dp[m][n] = self.countPaths(m - 1, n, dp) + self.countPaths(m, n - 1, dp)
        return dp[m][n]