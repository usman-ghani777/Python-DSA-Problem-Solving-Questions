nums = [5,2,3,4,5,6,10,7]
# n = len(nums)
# nums[:] = nums[n-1] + nums[0:n-1]
# print(nums)
n = len(nums)
temp = [n-1]
for i in range(len(nums)-2,-1,-1):
    nums[i+1] = nums[i]

nums[0] = temp

print(nums)


