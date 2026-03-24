class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        arr = []
        for row in grid:
            arr.extend(row)
        size = m * n
        prefix = [1] * size
        suffix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % mod
        for i in range(size - 2, - 1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % mod
        result = []
        index = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append((prefix[index] * suffix[index]) % mod)
                index += 1
            result.append(row)
        return result