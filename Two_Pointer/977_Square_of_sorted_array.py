# Square of a sorted array
nums = [-4, -1, 0, 3, 10]
def sortedSquare(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result
print(sortedSquare(nums))