class Solution:


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        visited[source] = True
        q = deque([source])
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for x in adj[node]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)
        return False