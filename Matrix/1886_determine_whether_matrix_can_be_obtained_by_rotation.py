class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = list(zip(*mat[::-1]))
            mat = [list(row) for row in mat]
        return False