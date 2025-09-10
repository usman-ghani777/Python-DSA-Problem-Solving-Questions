# nums = [7,2,1,5,6,4,8]
# profit = 0
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[j]>nums[i]:
#             p = nums[j] - nums[i]
#             profit = max(profit,p)
# print(profit)

#*********************************************************
nums = [7,2,1,5,6,4,8]

min_price = float("inf")
max_profit = 0

for i in range(0,len(nums)):
    min_price = min(min_price,nums[i])
    max_profit = max(max_profit,nums[i]-min_price)
    
               
print(max_profit)