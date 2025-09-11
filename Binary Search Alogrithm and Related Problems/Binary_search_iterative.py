def binary_search(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
         mid = (low+high)//2
         if nums[mid]==target:
              return mid
         elif nums[mid]<target:
              low = mid+1
         else:
              high = mid-1
    return -1               

nums = [1,1,3,4,5,7,5,8]
nums.sort()
target = 7
x = binary_search(nums,target)
print(x)



