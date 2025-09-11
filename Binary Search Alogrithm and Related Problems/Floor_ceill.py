nums = [1,2,3,3,5,6,7,8,9]
n = len(nums)
target = 4
floor = -1
ceill = -1
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] == target:
        floor = nums[mid]
        ceill = nums[mid]
        break
    
    elif nums[mid] < target:
        floor = nums[mid]        # possible floor
        low = mid + 1
    else:
        ceill = nums[mid]        # possible ceil
        high = mid - 1

print("Floor:", floor)
print("Ceil:", ceill)
