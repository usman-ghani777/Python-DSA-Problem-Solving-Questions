nums = [3,4,5,6,7,8,9]
n = len(nums)
k = 3
nums[:] = nums[n-k:] +nums [:n-k]
print(nums)