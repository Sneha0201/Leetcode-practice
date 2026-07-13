# Maximize sum of array after k negations
nums = [4,2,3]
k = 1
def largestSumAfterNegation(nums, k):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
        total = sum(nums)
        if k % 2 == 1:
            total -= 2 * min(nums)
    return total
print(largestSumAfterNegation(nums, k))