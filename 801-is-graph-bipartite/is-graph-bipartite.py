class Solution:
    def dfs(self, node, col, colors, graph):
        colors[node] = col
        for neigh in graph[node]:
            if colors[neigh] == -1:
                if self.dfs(neigh, not col, colors, graph) == False:
                    return False
            elif colors[neigh] == col:
                return False
        return True 

    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        colors = [-1] * v
        for i in range(v):
            if colors[i] == -1:
                if self.dfs(i, 1, colors, graph) == False:
                    return False
        return True