class Solution:
    def dfs(self, i, adj_lst, visited):
        visited[i] = True
        for i in adj_lst[i]:
            if not visited[i]:
                self.dfs(i, adj_lst, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adj_lst = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_lst[i].append(j)
                    adj_lst[j].append(i)
        visited = [False] * V
        cnt = 0
        for i in range(V):
            if not visited[i]:
                cnt += 1
                self.dfs(i, adj_lst, visited)
        return cnt
