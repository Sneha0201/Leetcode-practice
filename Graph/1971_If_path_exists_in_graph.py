# Find if path exists in graph
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

# ====>>>> DFS
def validPath(n, edges, source, destination):
    graph = {}
    for i in range(n):
        graph[i] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei):
                    return True
        return False
    return dfs(source)
print(validPath(n, edges, source, destination))

# ====>>>> BFS
from collections import deque
def validPath(n, edges, source, destination):
    graph = {}
    for i in range(n):
        graph[i] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    q = deque([source])
    visited = {source}
    while q:
        node = q.popleft()
        if node == destination:
            return True
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return False
print(validPath(n, edges, source, destination))