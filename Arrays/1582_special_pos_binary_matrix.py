class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        row_count = [0] * rows
        col_count = [0] * columns
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        result = 0
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    result += 1
        return result