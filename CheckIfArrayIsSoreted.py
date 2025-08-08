def is_sorted(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
nums = [3,4,2,3,4,3,2,4,2,2]
print(is_sorted(nums))
