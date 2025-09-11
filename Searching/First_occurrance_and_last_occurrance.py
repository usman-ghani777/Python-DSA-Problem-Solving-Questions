def occurance(nums,target):
    n = len(nums)
    first = -1
    last = -1
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            low = mid+1
            if first is -1:
                first = mid
            last = mid


        
