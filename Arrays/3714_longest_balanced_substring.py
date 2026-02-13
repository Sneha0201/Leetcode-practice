class Solution:
    def longestBalanced(self, s: str) -> int:
        from collections import defaultdict
        n = len(s)
        ans = 0
        for i in range(n):
            count = {'a' : 0, 'b' : 0, 'c' : 0}
            for j in range(i, n):
                count[s[j]] += 1
                values = [v for v in count.values() if v > 0]
                if len(set(values)) == 1:
                    ans = max(ans, j - i + 1)
        return ans