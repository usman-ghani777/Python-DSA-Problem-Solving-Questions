nums = [-2,1,-3,4,-1,2,1,-5,4]
maxi = nums[0]
total = 0

for i in range(len(nums)):
    total += nums[i]
    if total > maxi:
        maxi = total
    if total < 0:
        total = 0

print(maxi)
