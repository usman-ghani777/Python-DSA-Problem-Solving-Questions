# nums = [5,9,1,2,4,15,6,3]
# result = []
# target = 13
# for i in range(0,len(nums)-1):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] == target:
            
#             result.append(i)
#             result.append(j)
# print(result)
#***********************************************************************************************
nums = [5, 9, 1, 2, 4, 15, 6, 3]
dic = dict()          # Stores number as key and its index as value
target = 13
for i in range(0, len(nums)):  # loop till second last element
    remaning = target - nums[i] # calculate the number needed to reach target
    if remaning in dic:
        print(dic[remaning], i)  # print the pair of indices
    dic[nums[i]] = i  # store current number and its index
print(dic)


