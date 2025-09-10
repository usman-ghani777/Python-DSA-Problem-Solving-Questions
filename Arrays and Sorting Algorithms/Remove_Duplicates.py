# nums = [1,1,1,2,3,4,4,7,8,9,9,9,9,10]
# dic = dict()
# for i in range(0,len(nums)):
#     if nums[i] in dic:
#         dic[nums[i]]+=1
#     else:
#         dic[nums[i]] = 1
# print(dic)

# result = []

# for key,values in dic.items():
#     if values ==1:
#         result.append(key)
#     else:
#         result.append("_")
# print(result)

nums = [1,1,1,2,3,4,4,7,8,9,9,9,9,10]
dic = dict()
for i in range(0,len(nums)):
    dic[nums[i]] = 0

j = 0

for k in dic:
    nums[j] = k
    j+=1
print(nums)
    

