
def lower_bound(nums, target):
    n = len(nums)
    ub = 0
    hb = n - 1
    ans = n   # default if no element >= target
    while ub <= hb:
        mid = (ub + hb) // 2
        if nums[mid] >= target:
            ans = mid
            hb = mid - 1
        else:
            ub = mid + 1
    return ans

nums = [1,2,3,4,5,6,7,8,9,10]
target = 6
x = lower_bound(nums, target)
print(x)   # prints 5
