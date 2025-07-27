def func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left + 1, right - 1)

nums = [1, 2, 3, 4, 5, 6, 7, 63, 3]
left = 2
right = 5  # Corrected this line
x = func(nums, left, right)
print(x)        # This will print None
print(nums)     # This will print the reversed list
