# def rev(nums, left, right):
#     while left < right:

#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
#     return nums
     
# nums = [3, 3, 4, 5, 6, 78, 9]
# n = len(nums)
# z = rev(nums,3,n-1)
# x = rev(z,0,2)
# print(x)
# y = rev(x,0,6)
# print(y)
#***************************************************************8
nums = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(nums)
for i in range(n // 2):
    nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
print(nums)



