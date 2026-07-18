# No. of islands
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

# ====>>>> DFS
def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    def dfs(r, c):
        if r < 0 or c < 0 or  r >= rows or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
    islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                islands += 1
                dfs(i, j)
    return islands
print(numIslands(grid))

# ====>>>> BFS
from collections import deque
def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    island = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                island += 1
                q = deque([(i, j)])
                grid[i][j] = "0"
                while q:
                    r, c = q.popleft()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
    return island
print(numIslands(grid))