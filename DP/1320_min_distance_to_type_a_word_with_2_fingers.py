class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1 or b == -1:
                return 0
            ax, ay = divmod(a, 6)
            bx, by = divmod(b, 6)
            return abs(ax - bx) + abs(ay - by)
        n = len(word)
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == n:
                return 0
            cur = ord(word[i]) - ord('A')
            use_f1 = dist(f1, cur) + dp(i + 1, cur, f2)
            use_f2 = dist(f2, cur) + dp(i + 1, f1, cur)
            return min(use_f1, use_f2)
        return dp(0, -1, -1)