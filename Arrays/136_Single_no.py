class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        for num in nums:
            if freq[num] == 1:
                return num