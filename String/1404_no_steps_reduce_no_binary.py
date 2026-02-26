class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        steps = 0
        carry = 0
        for i in range(n - 1, 0, -1):
            bits = int(s[i]) + carry
            if bits == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry