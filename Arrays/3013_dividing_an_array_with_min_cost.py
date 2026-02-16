class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 1
        small = []
        large = []
        curr_sum = 0
        for i in range(1, dist + 2):
            heapq.heappush(small, -nums[i])
            curr_sum += nums[i]
            if len(small) > need:
                val = -heapq.heappop(small)
                curr_sum -= val
                heapq.heappush(large, val)
            ans = nums[0] + curr_sum
            left = 1
        for right in range(dist + 2, n):
            val = nums[right]
            if small and val < -small[0]:
                heapq.heappush(small, -val)
                curr_sum += val
            else:
                heapq.heappush(large, val)
            if len(small) > need:
                moved = -heapq.heappop(small)
                curr_sum -= moved
                heapq.heappush(large, moved)
            out = nums[left]
            left += 1
            if out <= -small[0]:
                curr_sum -= out
                small.remove(-out)
                heapq.heapify(small)
            else:
                large.remove(out)
                heapq.heapify(large)
            while len(small) < need:
                moved = heapq.heappop(large)
                heapq.heappush(small, -moved)
                curr_sum += moved
            ans = min(ans, nums[0] + curr_sum)
        return ans