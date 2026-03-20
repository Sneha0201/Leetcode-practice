class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                vals.sort()
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    if vals[t] != vals[t - 1]:
                        min_diff = min(min_diff, vals[t] - vals[t - 1])
                row.append(min_diff if min_diff != float('inf') else 0)
            ans.append(row)
        return ans