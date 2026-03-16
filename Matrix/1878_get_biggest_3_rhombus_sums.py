class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        for r in range(m):
            for c in range(n):
                sums.add(grid[r][c])
                size = 1
                while True:
                    if r + 2 * size >= m or c - size < 0 or c + size >= n:
                        break
                    total = 0
                    x, y = r, c
                    for i in range(size):
                        total += grid[x + i][y - i]
                    for i in range(size):
                        total += grid[x + size + i][y - size + i]
                    for i in range(size):
                        total += grid[x + 2 * size - i][y + i]
                    for i in range(size):
                        total += grid[x + size - i][y + size - i]
                    sums.add(total)
                    size += 1
        return sorted(sums, reverse = True)[: 3]