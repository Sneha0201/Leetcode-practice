# Product of subarray should strictly less than k
nums = [10, 5, 2, 6]
k = 100
def subarrayProduct(nums, k):
    if k <= 1:
        return 0
    left = 0
    product = 1
    count = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count
print(subarrayProduct(nums, k))