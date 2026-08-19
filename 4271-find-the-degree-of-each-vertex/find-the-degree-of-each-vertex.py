class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = [0] * n
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    ans[j] += 1
        return ans