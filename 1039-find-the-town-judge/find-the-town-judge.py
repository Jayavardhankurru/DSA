class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree = [0] * (n + 1)
        in_degree = [0] * (n + 1)
        for truster, trusted in trust:
            out_degree[truster] += 1
            in_degree[trusted] += 1
        for person in range(1, n+1):
            if out_degree[person] == 0 and in_degree[person] == n - 1:
                return person
        return -1 