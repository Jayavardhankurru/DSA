class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
        indegree = [0] * numCourses
        for i  in range(numCourses):
            for x in adj[i]:
                indegree[x] += 1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i]  == 0:
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for x in adj[node]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        if len(topo) == numCourses:
            return topo
        else:
            return []

        