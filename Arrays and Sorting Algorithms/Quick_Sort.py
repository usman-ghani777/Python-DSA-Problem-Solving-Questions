def partition(nums, low, high):
    pivot = nums[low]
    i = low + 1
    j = high

    while True:
        while i <= j and nums[i] <= pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break

    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)

nums = [2, 1, 3, 3, 4, 5, 4, 5, 4, 5, 4, 7, 6, 4, 6, 78]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
