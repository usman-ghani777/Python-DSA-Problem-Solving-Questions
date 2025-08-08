def bubble_sort(nums):
   n = len(nums)
   for i in range(n-2,-1,-1):
      for j in range(0,i+1):
         if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]

nums = [3,45,46,45,645,6,4]
bubble_sort(nums)
print(nums)