class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        s = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in s:
                result.append(num)
        return result