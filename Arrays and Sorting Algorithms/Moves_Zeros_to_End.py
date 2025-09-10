# nums = [1, 0, 2, 4, 3, 0, 0, 5, 1]
# result = []   # Non-zero values
# result2 = []  # Zero values

# for i in range(len(nums)):
#     if nums[i] > 0:
#         result.append(nums[i])
#     elif nums[i] == 0:
#         result2.append(nums[i])

# print("Non-zero elements:", result)
# print("Zero elements:", result2)
# final = []
# final = result+result2
# print(final)
# **********************************************
# nums = [1,2,30,0,0,0,1,2,3,4]
# temp = []
# for i in range(0,len(nums)):
#     if nums[i] > 0:
#         temp.append(nums[i])
# n = len(temp)
# for i in range(0,n):
#     nums[i] = temp[i]
# # print(nums)
# for i in range(n,len(nums)):
#     nums[i] = 0

# print(nums)
#******************************************************

nums = [1,2,3,40,0,0,0,0,28,9,0,0,0,4,0,0,1,0,3,0]
for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]==0:
                 nums[i],nums[j] = nums[j],nums[i]            
print(nums)
    

