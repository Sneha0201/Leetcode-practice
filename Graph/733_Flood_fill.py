# Flood Fill
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
color = 2

# ====>>>> DFS
def floodFill(image, sr, sc, color):
    old = image[sr][sc]
    if old == color:
        return image
    rows = len(image)
    cols = len(image[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != old:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    dfs(sr, sc)
    return image
print(floodFill(image, sr, sc, color))

# ====>>>> BFS
from collections import deque
def floodFill(image, sr, sc, color):
    old = image[sr][sc]
    if old == color:
        return image
    rows = len(image)
    cols = len(image[0])
    q = deque()
    q.append((sr, sc))
    while q:
        r, c = q.popleft()
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue
        if image[r][c] != old:
            continue
        image[r][c] = color
        q.append((r + 1, c))
        q.append((r - 1, c))
        q.append((r, c + 1))
        q.append((r, c - 1))
    return image
print(floodFill(image, sr, sc, color))