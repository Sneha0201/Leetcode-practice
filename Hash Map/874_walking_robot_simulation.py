class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))
        x = 0
        y = 0
        d = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        max_dist = 0
        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d - 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + directions[d][0]
                    ny = y + directions[d][1]
                    if (nx, ny) in obstacles_set:
                        break
                    x, y = nx, ny
                    max_dist = max(max_dist, x * x + y * y)
        return max_dist