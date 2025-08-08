# nums = [1,0,3,4]
# n = len(nums)
# for i in range(4):
#     if i not in nums:
#         print(i)
#***********************************************************************
# num = [9,6,4,2,3,5,7,0,1]
# dic = dict()
# n = len(num)

# # Step 1: Initialize dictionary with keys from 0 to n (inclusive), all set to 0
# for i in range(0, n+1):
#     dic[i] = 0

# print(dic)

# # Step 2: Mark which numbers are present in the list
# for n in num:
#     dic[n] = 1
# print(dic)

# for k,v in dic.items():
#     if v==0:
#         print(k)
#***************************************************************************

num = [9,6,4,2,3,5,7,0,1]
n = len(num)
sum1 = 0  
for i in num:
    sum1 += i  
print(sum1)


sum2  = 0 
for i in range(0,n+1):
    sum2+=i
print(sum2)
final = sum2-sum1
print(final)




    
