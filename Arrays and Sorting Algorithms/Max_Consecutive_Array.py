nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]
count = 0
max_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0  # Reset count when a 0 is found

print(max_count)
