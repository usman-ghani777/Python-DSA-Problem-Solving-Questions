nums = [55,32,-97,23,90,32]
largest = 0
for i in range(0,len(nums)):
    # largest = max(largest,nums[i])
    if nums[i] > largest:
        largest=nums[i]

print(largest)