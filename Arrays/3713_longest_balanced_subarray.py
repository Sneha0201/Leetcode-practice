class Solution:
    def longestBalanced(self, s: str) -> int:
        from collections import defaultdict
        n = len(s)
        ans = 0
        for left in range(n):
            freq = defaultdict(int)
            for right in range(left, n):
                freq[s[right]] += 1
                values = list(freq.values())
                if len(set(values)) == 1:
                    ans = max(ans, right - left + 1)
        return ans