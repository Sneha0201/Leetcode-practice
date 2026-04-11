class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        ans = float('inf')
        for indices in pos.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    j = indices[i + 1]
                    k = indices[i + 2]
                    dist = abs(indices[i] - j) + abs(j - k) + abs(k - indices[i])
                    ans = min(ans, dist)
        return ans if ans != float('inf') else -1