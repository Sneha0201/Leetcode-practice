class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False
        half = total // 2
        curr = 0
        for i in range(m - 1):
            curr += sum(grid[i])
            if curr == half:
                return True
        curr = 0
        for j in range(n - 1):
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            curr += col_sum
            if curr == half:
                return True
        return False