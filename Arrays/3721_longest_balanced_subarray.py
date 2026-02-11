class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        ans = 0
        for i in range(n):
            even_freq = defaultdict(int)
            odd_freq = defaultdict(int)
            distinct_even = 0
            distinct_odd = 0
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    if even_freq[nums[j]] == 0:
                        distinct_even += 1
                    even_freq[nums[j]] += 1
                else:
                    if odd_freq[nums[j]] == 0:
                        distinct_odd += 1
                    odd_freq[nums[j]] += 1
                if distinct_even == distinct_odd:
                    ans = max(ans, j - i + 1)
        return ans