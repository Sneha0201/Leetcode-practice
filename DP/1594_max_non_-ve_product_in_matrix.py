class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                candidate = []
                if i > 0:
                    candidate.append(dp_max[i - 1][j] * val)
                    candidate.append(dp_min[i - 1][j] * val)
                if j > 0:
                    candidate.append(dp_max[i][j - 1] * val)
                    candidate.append(dp_min[i][j - 1] * val)
                dp_max[i][j] = max(candidate)
                dp_min[i][j] = min(candidate)
        result = dp_max[m - 1][n - 1]
        if result < 0:
            return -1
        return result % mod