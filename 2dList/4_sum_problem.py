# nums = [1,0,-1,0,-2,2,5,9]
# target = 0
# n = len(nums)
# s = set()
# for i in range(0,n):
#     for j in range(i+1):
#         for k in range(j+1):
#             for l in range(k+1):
#                 total = nums[i]+nums[j]+nums[k]+nums[l]
#                 if total == target:
#                     temp = [nums[i],nums[j],nums[k],nums[l]]
#                     s.add(tuple(sorted((nums[i], nums[j], nums[k],nums[l]))))
# print([list(ans) for ans in s])

#*****************************************************************************************

# nums  = [1, 0, -1, 5, -2, 2, 0, 9]
# target = 0
# n = len(nums)
# result = set()

# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             fourth = target - (nums[i] + nums[j] + nums[k])
#             if fourth in nums[k + 1:]:  # search only in remaining elements
#                 result.add(tuple(sorted((nums[i], nums[j], nums[k], fourth))))

# print([list(ans) for ans in result])

#*************************************************************************************
nums = [1,1,1,1,2,2,3,3,3,4,4,4,5,5]
target = 8
nums.sort()
n = len(nums)
ans = []

for i in range(0,n):
    if nums[i]>0 and nums[i]==nums[i-1]:
        continue

    for j in range(i+1,n):
        if j >i+1 and nums[j]==nums[j-1]:
            continue
        k =j+1
        l = n-1

        while k<l:
            total = nums[i]+nums[j]+nums[k]+nums[l]
            if total == target:
                ans.append([nums[i],nums[j],nums[k],nums[l]])
                k+=1
                l-=1
                while k <l and nums[k]==nums[k-1]:
                    k+=1
                while l > k and nums[l]==nums[l+1]:
                    l-=1
            elif total > target:
                k+=1
            else:
                l-=1
print(ans)
     





