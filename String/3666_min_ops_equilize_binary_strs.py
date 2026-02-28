class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z = s.count('0')
        n = len(s)
        if z == 0:
            return 0
        even = list(range(0, n + 1, 2))
        odd = list(range(1, n + 1, 2))
        if z % 2 == 0:
            even.remove(z)
        else:
            odd.remove(z)
        queue = deque([(z, 0)])
        while queue:
            x, ops = queue.popleft()
            low_i = max(0, k - (n - x))
            high_i = min(k, x)
            low = x + k - 2 * high_i
            high = x + k - 2 * low_i
            target = even if (low % 2 == 0) else odd
            idx = bisect.bisect_left(target, low)
            while idx < len(target) and target[idx] <= high:
                nxt = target[idx]
                if nxt == 0:
                    return ops + 1
                queue.append((nxt, ops + 1))
                target.pop(idx)
        return -1