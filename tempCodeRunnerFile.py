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
