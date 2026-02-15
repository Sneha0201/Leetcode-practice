class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False
        dec_start = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == dec_start:
            return False
        inc2_start = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == inc2_start:
            return False
        return i == n - 1