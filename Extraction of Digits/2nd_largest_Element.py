nums = [55, 32, -97, 23, 90, 32]

largest = float('-inf')
s_largest = float('-inf')

for num in nums:
    if num > largest:
        s_largest = largest  # shift current largest to second largest
        largest = num
    elif num > s_largest and num != largest:
        s_largest = num

print("Second largest:", s_largest)
