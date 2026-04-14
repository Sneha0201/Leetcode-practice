class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m = len(robot)
        n = len(factory)
        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return 0
            if j == n:
                return float('inf')
            res = dp(i, j + 1)
            dist = 0
            for k in range(factory[j][1]):
                if i + k >= m:
                    break
                dist += abs(robot[i + k] - factory[j][0])
                res = min(res, dist + dp(i + k + 1, j + 1))
            return res
        return dp(0, 0)