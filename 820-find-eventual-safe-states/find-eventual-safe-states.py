class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                adj[v].append(u)
        indegree = [len(graph[i]) for i in range(n)]
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        safenodes = []
        while q:
            node = q.popleft()
            safenodes.append(node)
            for x in adj[node]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        return sorted(safenodes)