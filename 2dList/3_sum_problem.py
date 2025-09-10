# arr = [-1,0,1,2,-1,-4]
# s = set()
# result = []
# n = len(arr)
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if arr[i]+arr[j]+arr[k]==0:
#                 temp = [arr[i],arr[j],arr[k]]
#                 temp.sort()
#                 s.add(tuple(temp))
# print(s)
# print([list(ans) for ans in s])
                
#****************************************************************
# arr = [-1, 0, 1, 2, -1, -4]
# result = set()

# for i in range(0, len(arr)):
#     for j in range(i + 1, len(arr)):
#         third = - (arr[i] + arr[j])
#         if third in arr[j + 1:]:
#             # Use tuple(sorted(...)) to avoid duplicates with different orders
#             result.add(tuple(sorted((arr[i], arr[j], third))))
# print(result)
# print([list(ans) for ans in result])

#******************************************************************************
nums = [-2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2]
n = len(nums)
ans = []
nums.sort()

for i in range(n):
    if i != 0 and nums[i] == nums[i-1]:  # skip duplicates for i
        continue

    j = i + 1  # <-- initialize j properly
    k = n - 1

    while j < k:
        total_sum = nums[i] + nums[j] + nums[k]

        if total_sum < 0:
            j += 1
        elif total_sum > 0:
            k -= 1
        else:
            ans.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1

            # Skip duplicates for j
            while j < k and nums[j] == nums[j - 1]:
                j += 1
            # Skip duplicates for k
            while j < k and nums[k] == nums[k + 1]:
                k -= 1

print(ans)








                
