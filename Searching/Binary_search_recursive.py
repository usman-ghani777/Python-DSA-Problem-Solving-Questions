
def binary_searc(target, nums, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_searc(target, nums, mid + 1, high)
    else:
        return binary_searc(target, nums, low, mid - 1)


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5
result = binary_searc(target, nums, 0, len(nums) - 1)
print(result)
