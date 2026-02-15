class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        up = [1]*n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up[i] = up[i-1] + 1
        down = [1]*n
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                down[i] = down[i-1] + 1
        upR = [1]*n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                upR[i] = upR[i+1] + 1
        ans = float('-inf')
        for i in range(1, n-1):
            if down[i] >= 2 and upR[i] >= 2:
                p = i - down[i] + 1
                if up[p] >= 2:
                    l = p - up[p] + 1
                    r = i + upR[i] - 1
                    total = prefix[r+1] - prefix[l]
                    ans = max(ans, total)
        return ans if ans != float('-inf') else 0