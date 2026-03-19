class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        val = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    val[i][j] = 1
                elif grid[i][j] == 'Y':
                    val[i][j] = -1
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = val[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]
        count = 0
        for i in range(m):
            for j in range(n):
                total = ps[i + 1][j + 1]
                if total == 0:
                    hasX = False
                    for x in range(i + 1):
                        for y in range(j + 1):
                            if grid[x][y] == 'X':
                                hasX = True
                                break
                        if hasX:
                            break
                    if hasX:
                        count += 1
        return count