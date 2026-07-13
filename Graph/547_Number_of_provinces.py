# Number of provinces
isConnected = [[1,1,0],
               [1,1,0],
               [0,0,1]]
def findCircleNum(isConnected):
    n = len(isConnected)
    visited = set()
    def dfs(city):
        visited.add(city)
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)
    provinces = 0
    for city in range(n):
        if city not in visited:
            dfs(city)
            provinces += 1
    return provinces
print(findCircleNum(isConnected))