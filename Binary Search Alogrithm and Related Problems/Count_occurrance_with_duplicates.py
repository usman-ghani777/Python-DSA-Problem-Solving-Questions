nums =  [1,2,3,3,3,3,3,5,6,7,8,9,10]
target =  3
count = 0
n = len(nums)
for i in range(n):
    if nums[i]==target:
        count+=1
# print(count)
# another solution
first = -1
last = -1
for i in range(0,n):
    if nums[i]== target:
        if first ==-1:
            first = i
        last = i
print(last-first+1)

